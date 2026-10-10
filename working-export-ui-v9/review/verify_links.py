"""Product navigation regression checks on controlled HTTP routes, not the live store."""
import asyncio, json
from pathlib import Path
from urllib.parse import urlsplit
from playwright.async_api import async_playwright

ROOT = Path('/workspace/theme-working-export-v9/theme')
OUT = ROOT.parent / 'review'
KEY = 'gujju-jewels:wishlist:v1'
checks = []

def item(url='/products/old-handle', title='Old product', id='123'):
    return dict(id=id, url=url, title=title, image='')

BUTTON = '''<button data-wishlist-product data-product-id="123"
 data-product-url="/products/current-handle" data-product-title="Current product"
 data-add-label="Save" data-remove-label="Remove" hidden>Heart</button>'''
HTML = '''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="/assets/wishlist.css"></head><body>
<button data-wishlist-open hidden>Wishlist<span data-wishlist-count hidden></span></button>
<div id="products">BUTTON</div>
<dialog data-wishlist-dialog data-view-label="View product" data-remove-label="Remove"
 data-count-label="Wishlist ([count])" data-saved-text="Saved" data-add-text="Save"
 data-error-message="Storage unavailable" data-saved-message="Saved" data-removed-message="Removed">
<button data-wishlist-close>Close</button><p data-wishlist-empty>Empty</p>
<ul data-wishlist-list></ul><span data-wishlist-message></span></dialog>
<script src="/assets/wishlist.js"></script></body></html>'''

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        async def setup(saved, button=BUTTON, width=390, original=False):
            page = await browser.new_page(viewport=dict(width=width, height=850))
            errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            await page.add_init_script('if(location.pathname==="/")localStorage.setItem('+json.dumps(KEY)+','+json.dumps(json.dumps(saved))+');')
            async def route(r):
                u = urlsplit(r.request.url)
                if u.path == '/':
                    await r.fulfill(content_type='text/html', body=HTML.replace('BUTTON', button))
                elif u.path == '/assets/wishlist.js':
                    source = Path('/workspace/theme-centered-header-v8-1/theme') if original else ROOT
                    await r.fulfill(path=str(source / 'assets/wishlist.js'))
                elif u.path == '/assets/wishlist.css':
                    await r.fulfill(path=str(ROOT / 'assets/wishlist.css'))
                elif u.path in ['/products/current-handle', '/hi/products/current-handle']:
                    await r.fulfill(content_type='text/html', body='<h1>Current product page</h1>')
                else:
                    await r.fulfill(status=404, content_type='text/html', body='<h1>404</h1>')
            await page.route('**/*', route)
            await page.goto('http://wishlist.test/', wait_until='networkidle')
            return page, errors
        def passed(name, **details):
            checks.append(dict(check=name, passed=True, **details))
            print('PASS', name, details, flush=True)
        page, errors = await setup([item()], original=True)
        await page.locator('[data-wishlist-open]').click()
        await page.locator('.wishlist-dialog__actions a').click()
        await page.wait_for_url('**/products/old-handle')
        assert await page.locator('h1').text_content() == '404'
        assert not errors
        baseline = dict(original_script=True, stale_saved_url='/products/old-handle', result='404 reproduced on controlled route')
        print('BASELINE', baseline, flush=True)
        await page.close()
        for width in [390, 1440]:
            for kind in ['fresh', 'old handle', 'old collection']:
                saved = [] if kind == 'fresh' else [item('/collections/deleted/products/old-handle' if kind == 'old collection' else '/products/old-handle')]
                page, errors = await setup(saved, width=width)
                if kind == 'fresh':
                    await page.locator('[data-wishlist-product]').click()
                await page.locator('[data-wishlist-open]').click()
                assert await page.locator('[data-wishlist-count]').text_content() == '1'
                assert await page.locator('.wishlist-dialog__title').text_content() == 'Current product'
                stored = await page.evaluate('JSON.parse(localStorage.getItem('+json.dumps(KEY)+'))')
                assert len(stored) == 1 and stored[0]['id'] == '123' and stored[0]['url'] == '/products/current-handle'
                response = await page.locator('.wishlist-dialog__actions a').click()
                await page.wait_for_url('**/products/current-handle')
                assert await page.locator('h1').text_content() == 'Current product page'
                assert not errors, errors
                passed('View product navigates to an existing product route', width=width, saved_link=kind)
                await page.close()
        for path in ['/collections/deleted/products/current-handle?variant=12', '/hi/collections/deleted/products/current-handle?variant=12']:
            page, errors = await setup([item(path)], button='')
            await page.locator('[data-wishlist-open]').click()
            links = page.locator('.wishlist-dialog__item a')
            expected = path.replace('/collections/deleted', '')
            assert await links.evaluate_all('(es)=>es.map(e=>e.getAttribute("href"))') == [expected] * 3
            await links.nth(2).click()
            await page.wait_for_url('**'+expected)
            assert await page.locator('h1').text_content() == 'Current product page'
            assert not errors, errors
            passed('Collection-independent link retains locale and variant query', path=expected)
            await page.close()
        for selector in ['.wishlist-dialog__title', '.wishlist-dialog__item > a']:
            page, errors = await setup([item()])
            await page.locator('[data-wishlist-open]').click()
            await page.locator(selector).click(force=True)
            await page.wait_for_url('**/products/current-handle')
            assert await page.locator('h1').text_content() == 'Current product page'
            assert not errors
            passed('Product title and image also use the updated link', selector=selector)
            await page.close()
        page, errors = await setup([item()], button='')
        await page.locator('[data-wishlist-open]').click()
        await page.evaluate('(markup)=>document.querySelector("#products").innerHTML=markup', BUTTON)
        await page.wait_for_function('document.querySelector(".wishlist-dialog__title").getAttribute("href")==="/products/current-handle"')
        await page.locator('[data-wishlist-remove]').click()
        assert await page.locator('[data-wishlist-empty]').is_visible()
        await page.locator('[data-wishlist-close]').click()
        assert await page.locator('[data-wishlist-open]').evaluate('e=>e===document.activeElement')
        assert not errors
        passed('New Shopify sections refresh an open drawer; removal and focus still work')
        await page.close()
        page, errors = await setup([item()])
        await page.evaluate('(key)=>{localStorage.setItem(key,JSON.stringify([{id:"123",url:"/products/old-handle",title:"Old product",image:""}]));window.dispatchEvent(new StorageEvent("storage",{key}));}', KEY)
        await page.locator('[data-wishlist-open]').click()
        assert await page.locator('.wishlist-dialog__title').get_attribute('href') == '/products/current-handle'
        assert not errors
        passed('Cross-tab storage updates refresh stale links without losing product IDs')
        await page.close()
        for saved in ['invalid', [item(), item(id='123'), item('https://other.test/products/current-handle', id='999'), item('/cart', id='888')]]:
            page, errors = await setup(saved)
            await page.locator('[data-wishlist-open]').click()
            assert await page.locator('[data-wishlist-remove]').count() == (1 if isinstance(saved, list) else 0)
            assert not errors
            passed('Malformed, duplicate and external stored entries remain guarded', input_type=type(saved).__name__)
            await page.close()
        await browser.close()
    (OUT/'link-checks.json').write_text(json.dumps(dict(live_store_tested=False, baseline=baseline, checks=checks), indent=2))

asyncio.run(main())
