"""Local browser verification with Shopify fixture data; no live orders or accounts."""
import sys,json,copy,re,asyncio
from pathlib import Path
sys.path.insert(0,'/workspace/theme-customizable-v7/review')
import fixtures as v
from liquid import DictLoader
from playwright.async_api import async_playwright
ROOT=Path('/workspace/theme-product-restored-v9-1/theme');OUT=ROOT.parent/'review'
v.ROOT=ROOT;v.OUT=OUT
v.sources={p.stem:v.adapt(p.read_text()) for p in list((ROOT/'sections').glob('*.liquid'))+list((ROOT/'snippets').glob('*.liquid'))};v.env.loader=DictLoader(v.sources)
v.routes['account_login_url']='/account/login';v.routes['cart_change_url']='/cart/change'
v.globals={f['id']:f.get('default','') for g in json.loads((ROOT/'config/settings_schema.json').read_text()) for f in g.get('settings',[]) if 'id' in f}
v.globals.update(json.loads((ROOT/'config/settings_data.json').read_text())['current'])
v.globals.update(body_font={'family':'Inter','fallback_families':'sans-serif'},heading_font={'family':'Cormorant Garamond','fallback_families':'Georgia, serif'})
v.base['settings']=v.globals
v.inline=v.env.from_string(v.rootstyle).render(settings=v.globals)

styles=''.join('<style>'+(ROOT/'assets'/n).read_text()+'</style>' for n in ['theme.css','homepage.css','simple-theme.css','wishlist.css','hero-slider.css','product-mobile-details.css','footer-brand.css'])
saved=json.loads((ROOT/'templates/index.json').read_text())
def section_data(sid,data):
 d=copy.deepcopy(data);d['id']=sid;d['blocks']=[{**d['blocks'][k],'id':k} for k in d.get('block_order',[])] if isinstance(d.get('blocks'),dict) else d.get('blocks',[])
 for b in d['blocks']:
  if b['type']=='slide':b['settings']['desktop_image']=v.image('demo-hero-desktop.jpg');b['settings'].pop('mobile_image',None)
  if b['type']=='category_group':
   asset={'Earrings':'category-earrings.jpg','Necklaces':'category-necklaces.jpg','Bangles & Bracelets':'category-bangles.jpg','Rings':'category-rings.jpg','Jewellery Sets':'category-sets.jpg','Hair Accessories':'category-hair.jpg'}.get(b['settings'].get('title'),'demo-category-1.jpg')
   b['settings']['image']=v.image(asset)
 return d
def nav(changes={},**extra):return v.render_changes('mobile-bottom-bar',changes,**extra)
def home_html(nav_changes={}):
 parts=[]
 for sid in saved['order']:
  d=section_data(sid,saved['sections'][sid]);parts.append(v.render(d['type'],d,request={'page_type':'index','path':'/','design_mode':False}))
 return doc('index',''.join(parts),nav_changes)
def doc(kind,content,nav_changes={},extra='',cart=None):
 cart=cart or {'item_count':0}
 header_data=json.loads((ROOT/'sections/header-group.json').read_text())['sections']
 announcement=v.render('announcement-bar',section_data('announcement-bar',header_data['announcement-bar']))
 header=v.render('header',section_data('header',header_data['header']),cart=cart)
 footer=v.render('footer',section_data('footer',json.loads((ROOT/'sections/footer-group.json').read_text())['sections']['footer']))
 return '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+styles+v.inline+'</head><body class="template-'+kind+'">'+announcement+'<div class="header-section">'+header+'</div><main id="MainContent">'+content+'</main>'+footer+nav(nav_changes,cart=cart,request={'page_type':kind,'path':'/','design_mode':False})+v.env.get_template('wishlist-drawer').render(**v.base)+v.js_globals+'<script src="/assets/theme.js"></script>'+extra+'<script src="/assets/wishlist.js"></script></body></html>'
def product_html(nav_changes={}):
 p=json.loads((ROOT/'templates/product.json').read_text());parts=[v.render(d['type'],section_data(sid,d)) for sid,d in p['sections'].items()]
 observer='<script>window.submissions=[];document.addEventListener("submit",e=>{if(e.target.matches(".product-form")){e.preventDefault();window.submissions.push(Object.fromEntries(new FormData(e.target)));}});</script>'
 return doc('product',''.join(parts),nav_changes,observer)
def initial_items():return [dict(id=n*100,variant_id=n*100,key=str(n*100)+':key',properties={},quantity=1,price=price,final_price=price,final_line_price=price,product={'title':title},variant={'title':'Default Title'},url='/products/sample-'+str(n),url_to_remove='/cart/change?id='+str(n*100)+':key&quantity=0',image=v.image(asset)) for n,price,title,asset in [(2,24900,'Traditional Gold-Tone Choker Necklace Set','category-necklaces.jpg'),(3,19900,'Navrang Tree-of-Life Oxidised Long Necklace Set','category-sets.jpg')]]
def cart_data(items):return {'items':items,'item_count':sum(i['quantity'] for i in items),'total_price':sum(i['final_line_price'] for i in items)}
def cart_section(items):return v.render('main-cart',{'id':'test-cart','settings':{},'blocks':[]},cart=cart_data(items))
checks=[]
def passed(name,**details):checks.append({'check':name,'passed':True,**details});print('PASS',name,details,flush=True)
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'],env={'XDG_CACHE_HOME':'/tmp/theme-browser-cache','XDG_CONFIG_HOME':'/tmp/theme-browser-config'})
  async def setup(width,html,items=None):
   page=await browser.new_page(viewport={'width':width,'height':900});page.errors=[];page.on('pageerror',lambda e:page.errors.append(str(e)));page.cart_adds=[]
   async def route(r):
    url=r.request.url
    if url.rstrip('/')=='http://v8.test':await r.fulfill(content_type='text/html',body=html)
    elif '/assets/' in url:
     path=ROOT/'assets'/url.split('/assets/')[-1].split('?')[0]
     await r.fulfill(path=str(path)) if path.is_file() else await r.fulfill(status=404,body='')
    elif '/cart/change.js' in url:
     body=r.request.post_data_json;item=next(i for i in items if i['key']==body['id']);qty=body['quantity']
     if not qty:items.remove(item)
     else:item.update(quantity=qty,final_line_price=item['final_price']*qty)
     payload=cart_data(items);payload['sections']={'test-cart':cart_section(items)};await r.fulfill(content_type='application/json',body=json.dumps(payload))
    elif '/cart/add.js' in url:page.cart_adds.append(r.request.post_data);await r.fulfill(content_type='application/json',body='{"id":200}')
    elif '/cart.js' in url:await r.fulfill(content_type='application/json',body='{"item_count":2}')
    elif '/recommendations/products' in url:await r.fulfill(status=503,body='')
    else:await r.fulfill(body='')
   await page.route('**/*',route);await page.goto('http://v8.test/',wait_until='networkidle');return page
  async def no_errors(page):assert not page.errors,page.errors;assert not await page.evaluate('document.documentElement.scrollWidth>innerWidth')
  for width in [320,360,390,430,768,989,990,1440,1920]:
   page=await setup(width,home_html());mobile=width<990;bar=page.locator('[data-mobile-bottom-bar]');assert await bar.is_visible()==mobile
   heart=page.locator('.product-card .wishlist-toggle--compact').first;b=await heart.bounding_box();assert b['width']==(32 if mobile else 44)
   svg=await heart.locator('svg').bounding_box();assert svg['width']==(18 if mobile else 22)
   grid=await page.locator('.category-directory__grid').bounding_box();heading=await page.locator('#new-arrivals .section-header').bounding_box();gap=heading['y']-grid['y']-grid['height'];assert abs(gap-(24 if mobile else 120))<1,(width,gap)
   assert await bar.locator('.mobile-bottom-bar__item').count()==5
   assert await bar.locator('a').nth(0).get_attribute('href')=='/'
   assert await bar.locator('a').nth(1).get_attribute('href')=='/account/login'
   assert await bar.locator('a').nth(2).get_attribute('href')=='/collections/all'
   assert await bar.locator('a').nth(3).get_attribute('href')=='/cart'
   if mobile:
    bb=await bar.bounding_box();assert abs(bb['y']+bb['height']-900)<1
    for item in await bar.locator('.mobile-bottom-bar__item').all():
     ib=await item.bounding_box();assert ib['width']>=44 and ib['height']>=44
    assert abs((await page.locator('.mobile-bottom-bar-spacer').bounding_box())['height']-bb['height'])<1
    await heart.click(position={'x':-4,'y':16},force=True)
   else:await heart.click()
   assert await page.locator('[data-wishlist-count]').evaluate_all("es=>es.every(e=>e.textContent==='1')")
   if mobile:
    await bar.locator('[data-wishlist-open]').click();assert await page.locator('[data-wishlist-dialog]').is_visible()
    await page.locator('[data-wishlist-remove]').click();assert await page.locator('[data-wishlist-empty]').is_visible();await page.locator('[data-wishlist-close]').click();assert await bar.locator('[data-wishlist-open]').evaluate('e=>e===document.activeElement')
   await page.locator('#new-arrivals [data-quick-add]').first.click();await page.wait_for_function("[...document.querySelectorAll('.header-cart-count')].every(e=>e.textContent==='2')");assert len(page.cart_adds)==1
   await page.evaluate("window.changes=0;new MutationObserver(rs=>window.changes+=rs.length).observe(document.querySelector('[data-hero-slider]'),{attributes:true,subtree:true,attributeFilter:['hidden']});document.querySelector('[data-hero-slider]').dataset.interval='150';document.activeElement.blur();document.dispatchEvent(new Event('visibilitychange'))")
   await page.wait_for_function('window.changes>0');assert not await page.locator('[data-slider-pause]').is_visible();assert not await page.locator('[data-slider-next]').is_visible()
   await no_errors(page)
   await page.locator('.category-directory__image').evaluate_all("es=>es.forEach(e=>e.loading='eager')")
   await page.wait_for_function("[...document.querySelectorAll('.category-directory__image')].every(e=>e.complete&&e.naturalWidth>0)")
   if width in [390,1440]:await page.evaluate('window.scrollTo(0,0)');await page.screenshot(path=str(OUT/f'home-{width}.png'))
   passed('Responsive homepage, fixed navigation, smaller hearts, spacing, shared counts and autoplay',width=width,heart_px=b['width'],gap_px=round(gap,2));await page.close()
  for width in [320,390,768,989,1440]:
   page=await setup(width,product_html());primary=page.locator('[data-product-submit]');sticky=page.locator('[data-mobile-sticky-cart]');bar=page.locator('[data-mobile-bottom-bar]')
   await primary.evaluate('e=>window.scrollTo(0,scrollY+e.getBoundingClientRect().bottom+30)');await page.wait_for_function("document.querySelector('[data-mobile-sticky-cart]').hidden==="+('false' if width<990 else 'true'))
   await page.locator('[data-variant-select]').select_option('101');assert await primary.is_disabled();await page.wait_for_function("document.querySelector('[data-mobile-sticky-cart] button').disabled")
   await page.locator('[data-variant-select]').select_option('100');await page.wait_for_function("!document.querySelector('[data-mobile-sticky-cart] button').disabled")
   if width<990:
    sb=await sticky.bounding_box();nb=await bar.bounding_box();assert abs(sb['y']+sb['height']-nb['y'])<1,(width,sb,nb)
    await sticky.locator('button').click();assert len(await page.evaluate('submissions'))==1
    await bar.locator('[data-wishlist-open]').click();assert await page.locator('[data-wishlist-dialog]').is_visible();await page.locator('[data-wishlist-close]').click()
   await no_errors(page)
   if width==390:await page.screenshot(path=str(OUT/'product-two-bars-390.png'))
   passed('Product sticky button stays above navigation; variant and native form behaviour preserved',width=width);await page.close()
  for width in [390,1440]:
   items=initial_items();observer='<script>window.checkoutSubmissions=[];document.addEventListener("submit",e=>{if(e.target.matches(".cart-form")&&!e.defaultPrevented){e.preventDefault();window.checkoutSubmissions.push(e.submitter.name);}});</script>'
   page=await setup(width,doc('cart',cart_section(items),extra=observer,cart=cart_data(items)),items)
   await page.locator('[data-cart-delta="1"]').nth(1).click();await page.wait_for_function("document.querySelector('.cart-summary__subtotal').textContent.includes('647')")
   assert await page.locator('.header-cart-count').evaluate_all("es=>es.every(e=>e.textContent==='3')")
   await page.locator('[data-cart-delta="-1"]').nth(1).click();await page.wait_for_function("document.querySelector('.cart-summary__subtotal').textContent.includes('448')")
   await page.locator('[data-cart-quantity]').first.fill('0');await page.locator('[data-cart-quantity]').first.dispatch_event('change');await page.wait_for_function("document.querySelectorAll('[data-cart-quantity]').length===1")
   assert await page.locator('.header-cart-count').evaluate_all("es=>es.every(e=>e.textContent==='1')")
   await page.locator('[name="checkout"]').click();await page.wait_for_function('checkoutSubmissions.length===1');assert await page.get_by_role('button',name='Update Cart',exact=True).count()==0
   await no_errors(page);passed('Cart quantity autosave, remove, totals, both counts and native checkout submit',width=width);await page.close()
  for changes,count in [({'enabled':False},0),({'show_account':False},4),({'show_wishlist':False},4)]:
   page=await setup(390,home_html(changes));assert await page.locator('[data-mobile-bottom-bar] .mobile-bottom-bar__item').count()==count
   await no_errors(page);passed('Editable bar visibility and optional items',settings=changes);await page.close()
  page=await setup(390,home_html({'use_theme_colours':False,'background_color':'#FFFFFF','text_color':'#222222','accent_color':'#820022','collections_link':'/collections/oxidised-jewellery','home_label':'A much longer navigation label'}))
  assert await page.locator('[data-mobile-bottom-bar]').evaluate("e=>getComputedStyle(e).backgroundColor")=='rgb(255, 255, 255)'
  assert await page.locator('[data-mobile-bottom-bar] a').nth(2).get_attribute('href')=='/collections/oxidised-jewellery'
  nb=await page.locator('[data-mobile-bottom-bar]').bounding_box();assert abs(nb['height']-(await page.locator('.mobile-bottom-bar-spacer').bounding_box())['height'])<1
  await page.set_viewport_size({'width':1440,'height':900});assert not await page.locator('[data-mobile-bottom-bar]').is_visible();await page.set_viewport_size({'width':390,'height':900});assert await page.locator('[data-mobile-bottom-bar]').is_visible();await no_errors(page)
  await page.evaluate("const b=document.querySelector('[data-mobile-bottom-bar]');b.parentNode.dispatchEvent(new CustomEvent('shopify:section:unload',{bubbles:true}));b.remove();document.querySelector('.mobile-bottom-bar-spacer').remove()")
  assert not await page.locator('body').evaluate("e=>e.classList.contains('has-mobile-bottom-bar')")
  passed('Custom labels, colour and URL controls, resized height and editor unload cleanup');await page.close()
  signed=nav(customer={'id':123});assert '>Account</span>' in signed and 'href="/account"' in signed
  passed('Signed-in account label and Shopify account route')
  await browser.close()
 (OUT/'browser-checks.json').write_text(json.dumps({'live_shopify_tested':False,'mock_cart_and_accounts':True,'checks':checks},indent=2))
asyncio.run(main())
