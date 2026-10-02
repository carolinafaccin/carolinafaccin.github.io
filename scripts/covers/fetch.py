"""Download OpenStreetMap linework (streets, rivers, coastline, rail, towns) for each
project cover via the Overpass API. Edit SPECS (center lat/lon, height in degrees)
to add a project. Output: <slug>.json + <slug>.bbox.json next to this script.

Usage: python scripts/covers/fetch.py   (needs network; Pillow not required)
"""
import json,subprocess,os,sys,time
D=os.path.dirname(__file__)
# slug: (lat, lon, dlat, query-body)
def bb(lat,lon,dlat):
    dlon=dlat*16/9/0.874*1.0
    return (lat-dlat/2,lon-dlon/2,lat+dlat/2,lon+dlon/2)
CITY='way["highway"~"^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|living_street|service|track|motorway_link|trunk_link|primary_link|secondary_link)$"]{b};way["waterway"~"^(river|stream)$"]{b};way["natural"="coastline"]{b};way["railway"="rail"]{b};'
REG='way["highway"~"^(motorway|trunk|primary|secondary)$"]{b};way["waterway"="river"]{b};way["natural"="coastline"]{b};way["railway"="rail"]{b};node["place"~"^(city|town)$"]{b};'
SPECS={
 'urban-suitability-index-post-disasters':(-29.168,-51.880,0.02,CITY),
 'floods-rs-2024':(-29.475,-51.955,0.10,CITY),
 'coastal':(-29.982,-50.138,0.05,CITY),
 'mikripoli':(-29.238,-51.874,0.028,CITY),
 'housing-poa':(-30.085,-51.225,0.09,CITY),
 'urb-frag':(-29.715,-52.43,0.075,CITY),
 'territorial-management-role-of-medium-sized-cities':(-29.69,-53.81,0.08,CITY),
 'territorial-division-of-labor-and-urban-network':(-29.55,-52.15,1.1,REG),
 'polycentrism-and-regional-development':(-28.6,-52.9,2.6,REG.replace('secondary','secondary_DISABLED')),
 'dispersion-of-covid-19':(-29.85,-51.05,0.55,REG),
}
for slug,(lat,lon,dlat,q) in SPECS.items():
    out=f'{D}/{slug}.json'
    if os.path.exists(out) and os.path.getsize(out)>5000: continue
    s,w,n,e=bb(lat,lon,dlat); b=f'({s},{w},{n},{e})'
    body='[out:json][timeout:170];('+q.replace('{b}',b)+');out geom;'
    for k in range(3):
        r=subprocess.run(['curl','-s','-m','200','-A','carolinafaccin-site-covers/1.0','-H','Accept: application/json','https://overpass-api.de/api/interpreter','--data-urlencode','data='+body,'-o',out])
        sz=os.path.getsize(out) if os.path.exists(out) else 0
        ok=sz>5000 and open(out).read(1)=='{'
        print(slug,sz,ok,flush=True)
        if ok: break
        time.sleep(20)
    json.dump({'bbox':[s,w,n,e]},open(f'{D}/{slug}.bbox.json','w'))
