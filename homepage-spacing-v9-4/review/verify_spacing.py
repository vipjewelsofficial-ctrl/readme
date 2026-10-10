import asyncio,json,sys
from pathlib import Path
sys.path.insert(0,'/workspace/theme-analysis/tools')
from playwright.async_api import async_playwright
root=Path('/workspace/theme-homepage-spacing-v9-4/theme')
source=Path('/workspace/theme-product-template-repair-v9-2/review/verify_all.py').read_text().split('checks=[]')[0]
source=source.replace("/workspace/theme-product-template-repair-v9-2/theme",str(root))
ns={};exec(compile(source,'fixture_helpers','exec'),ns)
after=ns['saved'];before=json.loads(Path('/workspace/theme-product-template-repair-v9-2/theme/templates/index.json').read_text())
results=[]
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  for width in [320,360,390,430,768,989,990,1440,1920]:
   measurements={}
   page=await browser.new_page(viewport={'width':width,'height':900})
   async def route(r):
    url=r.request.url
    if '/assets/' in url:
     path=root/'assets'/url.split('/assets/')[-1].split('?')[0]
     if path.is_file():await r.fulfill(path=str(path))
     else:await r.fulfill(status=404,body='')
    elif '/cart.js' in url:await r.fulfill(content_type='application/json',body='{"item_count":0}')
    else:await r.fulfill(body='')
   await page.route('**/*',route)
   for label,data in [('before',before),('after',after)]:
    ns['saved']=data
    await page.set_content(ns['home_html'](),wait_until='load')
    # Absolute base lets the fixture load only local theme assets.
    await page.evaluate("document.head.insertAdjacentHTML('afterbegin','<base href=\"http://spacing.test/\">')")
    # Reinsert section asset links after base is set so their styles are available.
    await page.evaluate("document.querySelectorAll('link[rel=stylesheet]').forEach(e=>{const href=e.getAttribute('href');e.href=href;})")
    await page.wait_for_timeout(150)
    measurements[label]=await page.evaluate('''() => {
      const sections=[...document.querySelectorAll('#MainContent .section[style*="--section-bg"]')];
      const paddings=sections.map(e=>{const c=getComputedStyle(e),inner=e.querySelector(':scope > .container');return {className:e.className,top:parseFloat(c.paddingTop),bottom:parseFloat(c.paddingBottom),innerTop:inner?parseFloat(getComputedStyle(inner).paddingTop):null,innerBottom:inner?parseFloat(getComputedStyle(inner).paddingBottom):null};});
      const gap=(a,b)=>{a=document.querySelector(a+' > .container');b=document.querySelector(b+' > .container');return b.getBoundingClientRect().top-a.getBoundingClientRect().bottom;};
      return {paddings,headings:sections.map(e=>e.querySelector('h2')?.textContent.trim()),gaps:{arrivals_styles:gap('.new-arrivals-section','.collection-card-section'),styles_confidence:gap('.collection-card-section','.benefits'),confidence_trending:gap('.benefits','#trending-picks')},overflow:document.documentElement.scrollWidth>innerWidth};
    }''')
   b=measurements['before'];a=measurements['after'];assert a['headings']==b['headings'];assert len(a['paddings'])==len(b['paddings'])==7,a
   expected=12 if width<=768 else 20
   for item in a['paddings']:
    if width<990 and 'category-directory' in item['className']:
     assert item['top']==0 and item['bottom']==0,item
     assert item['innerTop']==12 and item['innerBottom']==12,item
    elif 768<width<990 and 'new-arrivals-section' in item['className']:
     assert item['top']==12 and item['bottom']==20,(width,item)
    else:assert item['top']==expected and item['bottom']==expected,(width,item)
   for name,gap in a['gaps'].items():
    assert abs(gap-expected*2)<1,(width,name,gap)
    assert gap < b['gaps'][name],(width,name,b,a)
   assert not a['overflow'],width
   if width in [390,1440]:await page.screenshot(path=str(root.parent/'review'/f'home-spacing-{width}.png'),full_page=True)
   results.append({'width':width,'before_gap_px':b['gaps'],'after_gap_px':a['gaps'],'all_visible_sections_retained':True,'page_overflow':False})
   print('PASS',width,'gaps',b['gaps'],'->',a['gaps'],flush=True)
   await page.close()
  await browser.close()
 (root.parent/'review'/'spacing-checks.json').write_text(json.dumps({'live_shopify_tested':False,'checks':results},indent=2))
asyncio.run(main())
