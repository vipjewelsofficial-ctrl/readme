from pathlib import Path
prefix=Path('/workspace/theme-product-template-repair-v9-2/review/verify_all.py').read_text().split('async def main():')[0]
exec(prefix)
ORIGINAL=Path('/workspace/theme-working-export-v9/original')
NEW_HEADER=v.sources['header'];NEW_STYLES=styles
header_group=json.loads((ROOT/'sections/header-group.json').read_text())['sections']['header']
def header_html(changes={},globals_changes={}):
 config={**v.globals,**globals_changes};h=section_data('header',header_group);h['settings'].update(changes)
 return '<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">'+styles+v.inline+'</head><body><div class="header-section">'+v.render('header',h,settings=config)+'</div><main style="height:1500px"><h1>Local header check</h1>'+v.render_changes('featured-products',{'collection':v.collection,'products_to_show':4},settings=config)+'</main>'+nav(settings=config)+v.env.get_template('wishlist-drawer').render(**{**v.base,'settings':config})+v.js_globals+'<script src="/assets/theme.js"></script><script src="/assets/wishlist.js"></script></body></html>'
async def run():
 global styles
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'],env={'XDG_CACHE_HOME':'/tmp/theme-browser-cache','XDG_CONFIG_HOME':'/tmp/theme-browser-config'})
  async def setup(width,changes={},globals_changes={}):
   page=await browser.new_page(viewport={'width':width,'height':850});page.errors=[];page.on('pageerror',lambda e:page.errors.append(str(e)))
   html=header_html(changes,globals_changes)
   async def route(r):
    u=r.request.url
    if u.rstrip('/')=='http://header.test':await r.fulfill(content_type='text/html',body=html)
    elif '/assets/' in u:
     path=ROOT/'assets'/u.split('/assets/')[-1].split('?')[0]
     if path.exists():await r.fulfill(path=str(path))
     else:await r.fulfill(status=404,body='')
    elif '/cart/add.js' in u:await r.fulfill(content_type='application/json',body='{"id":200}')
    elif '/cart.js' in u:await r.fulfill(content_type='application/json',body='{"item_count":2}')
    else:await r.fulfill(body='')
   await page.route('**/*',route);await page.goto('http://header.test/',wait_until='networkidle');return page
  async def rects(page):
   return await page.locator('.site-header,.header-inner,.header-logo,.header-logo__image--desktop,.header-actions,.header-action-btn,.header-nav').evaluate_all('es=>es.map(e=>{const r=e.getBoundingClientRect();return [r.x,r.y,r.width,r.height,getComputedStyle(e).display]})')
  for width in [280,320,360,390,430,768,989,990,1440,1920]:
   page=await setup(width)
   if width<990:
    logo=await page.locator('.header-logo__image--mobile').bounding_box();assert abs(logo['x']+logo['width']/2-width/2)<.6,(width,logo)
    assert logo['height']<=56.1
    visible=await page.locator('.header-actions .header-action-btn:visible').count();assert visible==2
    assert await page.locator('#search-toggle-btn').is_visible()
    assert not await page.locator('.header-wishlist-btn').is_visible();assert not await page.locator('.header-account-btn').is_visible()
    button=await page.locator('#mobile-menu-toggle').bounding_box();assert button['width']==44 and button['height']==44
    lines=await page.locator('.header-hamburger__line').evaluate_all('es=>es.map(e=>{let r=e.getBoundingClientRect();return [r.width,r.height]})');assert lines==[[22,2]]*3
    hb=await page.locator('.header-inner').bounding_box();assert hb['height']==64,(width,hb)
    for sel in ['#mobile-menu-toggle','#search-toggle-btn','.header-actions a[href="/cart"]']:
     b=await page.locator(sel).bounding_box();assert b['width']==44 and b['height']==44;assert abs(b['y']+22-(logo['y']+logo['height']/2))<1
    actions=await page.locator('.header-actions').bounding_box();assert logo['x']>=button['x']+button['width'] and logo['x']+logo['width']<=actions['x']
    await page.locator('#mobile-menu-toggle').click();assert await page.locator('#mobile-menu').is_visible();assert await page.locator('#mobile-menu-toggle').get_attribute('aria-expanded')=='true'
    await page.keyboard.press('Escape');assert not await page.locator('#mobile-menu').is_visible();assert await page.locator('#mobile-menu-toggle').evaluate('e=>e===document.activeElement')
    await page.locator('#search-toggle-btn').click();assert await page.locator('#search-drawer').is_visible();await page.keyboard.press('Escape');assert not await page.locator('#search-drawer').is_visible()
    await page.locator('.product-card .wishlist-toggle--compact').first.click();assert await page.locator('.mobile-bottom-bar [data-wishlist-count]').text_content()=='1'
    await page.locator('.mobile-bottom-bar [data-wishlist-open]').click();assert await page.locator('[data-wishlist-dialog]').is_visible();await page.locator('[data-wishlist-close]').click()
    await page.locator('[data-quick-add]').first.click();await page.wait_for_function("[...document.querySelectorAll('.header-cart-count')].every(e=>e.textContent==='2')")
   else:
    assert await page.locator('.header-actions .header-action-btn:visible').count()==4
    new_rects=await rects(page)
    v.sources['header']=v.adapt((ORIGINAL/'sections/header.liquid').read_text());v.env.loader=DictLoader(v.sources)
    styles=NEW_STYLES.replace((ROOT/'assets/wishlist.css').read_text(),(ORIGINAL/'assets/wishlist.css').read_text())
    old=await setup(width);assert new_rects==await rects(old),(width,new_rects,await rects(old));await old.close()
    v.sources['header']=NEW_HEADER;v.env.loader=DictLoader(v.sources);styles=NEW_STYLES
   assert not page.errors,page.errors;assert not await page.evaluate('document.documentElement.scrollWidth>innerWidth')
   if width in [390,1440]:
    await page.screenshot(path=str(OUT/f'header-{width}.png'))
    await page.locator('.site-header').screenshot(path=str(OUT/f'header-only-{width}.png'))
   passed('Centered compact mobile header; menu/search, wishlist and shared cart counts; original desktop geometry',width=width);await page.close()
  for width in [280,320,390,768,989]:
   for changes,globals_changes in [({'show_account_mobile':True,'logo_alignment':'left'},{}),({'logo_mode':'text','logo_text':'Gujju Jewels'},{}),({'logo':v.image('demo-hero-desktop.jpg'),'mobile_logo':v.image('demo-hero-desktop.jpg')},{}),({}, {'enable_wishlist':False})]:
    page=await setup(width,changes,globals_changes)
    logo=await page.locator('.header-logo__wordmark:visible' if changes.get('logo_mode')=='text' else '.header-logo__image--mobile').bounding_box();assert abs(logo['x']+logo['width']/2-width/2)<.6,(width,changes,logo)
    assert await page.locator('.header-actions .header-action-btn:visible').count()==2
    assert not await page.evaluate('document.documentElement.scrollWidth>innerWidth');assert not page.errors
    passed('Native logo options, left desktop alignment, optional account and wishlist settings remain responsive',width=width,options=changes,globals=globals_changes);await page.close()
  page=await setup(390);await page.set_viewport_size({'width':1440,'height':850});assert await page.locator('.header-wishlist-btn').is_visible();await page.set_viewport_size({'width':320,'height':850});assert not await page.locator('.header-wishlist-btn').is_visible();assert await page.locator('.header-actions .header-action-btn:visible').count()==2
  passed('Resize switches desktop icons to the two-icon mobile header');await page.close()
  await browser.close()
 (OUT/'header-checks.json').write_text(json.dumps({'live_shopify_tested':False,'checks':checks},indent=2))
asyncio.run(run())
