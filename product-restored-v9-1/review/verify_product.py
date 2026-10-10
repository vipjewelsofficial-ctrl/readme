"""Render the restored product template and test interactions on controlled Shopify fixture routes."""
from pathlib import Path
exec(Path('/workspace/theme-product-restored-v9-1/review/verify_all.py').read_text().split('async def main():')[0])
from urllib.parse import urlsplit
original_product=copy.deepcopy(v.product)
second_image=v.image('category-necklaces.jpg')
second_media={'id':12,'alt':'Second sample image','preview_image':second_image}
v.product['media'].append(second_media);v.product['images'].append(second_image)
v.product['variants'][1]['featured_media']=second_media
checks=[]
async def run():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  async def setup(width,path='/products/sample-1',card=False):
   page=await browser.new_page(viewport={'width':width,'height':900});page.errors=[];page.on('pageerror',lambda e:page.errors.append(str(e)))
   async def route(r):
    u=urlsplit(r.request.url)
    if u.path.startswith('/assets/'):
     f=ROOT/'assets'/u.path.split('/assets/')[1]
     await r.fulfill(path=str(f)) if f.is_file() else await r.fulfill(status=404,body='missing asset')
    elif u.path=='/products/sample-1':await r.fulfill(content_type='text/html',body=product_html())
    elif u.path=='/':
     content=v.env.get_template('product-card').render(**v.base)
     await r.fulfill(content_type='text/html',body=doc('index',content))
    elif u.path.startswith('/recommendations/products'):await r.fulfill(status=503,body='')
    else:await r.fulfill(status=404,body='<h1>404</h1>')
   await page.route('**/*',route);await page.goto('http://product.test'+path,wait_until='networkidle');return page
  for width in [320,390,768,989,1440]:
   page=await setup(width)
   assert await page.locator('.product-info__title').text_content()==v.product['title']
   assert await page.locator('.product-gallery__thumb').count()==2
   await page.locator('.product-gallery__thumb').nth(1).click()
   assert await page.locator('#ProductMainImage').get_attribute('src')==second_image['src']
   assert await page.locator('.product-gallery__thumb').nth(1).get_attribute('aria-pressed')=='true'
   await page.locator('[data-variant-select]').select_option('101')
   assert await page.locator('[data-product-submit]').is_disabled()
   assert '649' in await page.locator('[data-product-price]').text_content()
   assert '?variant=101' in page.url
   await page.locator('[data-variant-select]').select_option('100')
   assert not await page.locator('[data-product-submit]').is_disabled()
   assert await page.locator('#ProductMainImage').get_attribute('src')==v.product['featured_image']['src']
   await page.locator('.product-form input[name=quantity]').fill('3')
   await page.locator('[data-product-submit]').click()
   assert await page.evaluate('submissions')==[{'id':'100','quantity':'3'}]
   await page.locator('.product-info-wrap [data-wishlist-product]').click()
   assert await page.locator('[data-wishlist-count]').evaluate_all("es=>es.every(e=>e.textContent==='1')")
   assert not page.errors,page.errors
   assert not await page.evaluate('document.documentElement.scrollWidth>innerWidth')
   passed('Restored template renders title, gallery, variants, quantity and wishlist without overflow or JS errors',width=width)
   await page.close()
  for width in [390,1440]:
   for selector in ['.product-card__image-link','.product-card__title-link','.wishlist-dialog__actions a']:
    page=await setup(width,path='/')
    if selector.startswith('.wishlist'):
     await page.locator('[data-wishlist-product]').click()
     await page.locator('[data-wishlist-open]:visible').first.click()
    await page.locator(selector).click()
    await page.wait_for_url('**/products/sample-1')
    assert await page.locator('.product-info__title').text_content()==v.product['title']
    assert await page.locator('.product-form').get_attribute('action')=='/cart/add'
    assert not page.errors,page.errors
    passed('Product card and wishlist navigate to the restored rendered product template',width=width,selector=selector)
    await page.close()
  v.product.clear();v.product.update(copy.deepcopy(original_product));v.product['variants']=v.product['variants'][:1]
  page=await setup(390)
  assert await page.locator('[data-variant-select]').count()==0
  assert await page.locator('.product-form input[name=id]').get_attribute('value')=='100'
  await page.locator('[data-product-submit]').click()
  assert await page.evaluate('submissions')==[{'id':'100','quantity':'1'}]
  passed('Single variant uses native hidden variant ID and quantity submission');await page.close()
  v.product['available']=False;v.product['variants'][0]['available']=False
  page=await setup(390)
  assert await page.locator('[data-product-submit]').is_disabled()
  passed('Unavailable product cannot be added through the native product button');await page.close()
  await browser.close()
 (OUT/'product-checks.json').write_text(json.dumps({'live_shopify_tested':False,'product_template_rendered':True,'checks':checks},indent=2))
asyncio.run(run())
