"""Render brand covers (1600x900 JPG) from the OSM extracts saved by fetch.py.
PROJ maps each slug to a color scheme (the theme group) and an accent layer.
Copy the result to content/<lang>/projects/<slug>/feature.jpg for both languages.

Usage: python scripts/covers/render.py <out_dir> [slug ...]   (needs Pillow)
"""
import json,os,sys,math
from PIL import Image,ImageDraw
D=os.path.dirname(os.path.abspath(__file__))
OUT=sys.argv[1]
W,H=1600,900; K=2
C=dict(olive=(56,60,47),dark=(31,35,24),rust=(123,36,5),orange=(217,68,0),sage=(147,169,126),
       sagel=(205,215,197),peach=(254,210,191),cream=(255,248,242),yellow=(253,211,74),grey=(218,210,204))
SCHEMES={ # bg, line, accent
 'climate':('olive','sagel','orange'),
 'form':('sage','olive','rust'),
 'housing':('rust','peach','yellow'),
 'regional':('cream','olive','orange'),
}
PROJ={
 'urban-suitability-index-post-disasters':('climate','river'),
 'floods-in-small-cities':('climate','river'),
 'coastal':('form','coast'),
 'small-cities-dynamics':('form','river'),
 'housing-porto-alegre':('housing','arterial'),
 'sociospatial-fragmentation':('housing','arterial'),
 'territorial-management-role-of-medium-sized-cities':('regional','arterial'),
 'territorial-division-of-labor-and-urban-network':('regional','places'),
 'polycentrism-and-regional-development':('regional','places'),
 'dispersion-of-covid-19':('regional','corridor'),
}
MINOR={'residential','living_street','service','track','unclassified'}
MID={'tertiary','secondary','secondary_link','tertiary_link'}
MAJOR={'primary','primary_link','trunk','trunk_link','motorway','motorway_link'}
def render(slug):
    scheme,acc=PROJ[slug]; bg,ln,ac=[C[x] for x in SCHEMES[scheme]]
    s,w,n,e=json.load(open(f'{D}/{slug}.bbox.json'))['bbox']
    data=json.load(open(f'{D}/{slug}.json'))['elements']
    regional=any(el['type']=='node' for el in data)
    def P(lat,lon): return ((lon-w)/(e-w)*W*K,(n-lat)/(n-s)*H*K)
    img=Image.new('RGB',(W*K,H*K),bg)
    layers={k:Image.new('RGBA',img.size,(0,0,0,0)) for k in ['minor','mid','major','acc']}
    dr={k:ImageDraw.Draw(v) for k,v in layers.items()}
    def line(layer,pts,col,a,wd):
        if len(pts)>1: dr[layer].line(pts,fill=col+(a,),width=max(1,int(wd*K)),joint='curve')
    places=[]
    for el in data:
        t=el.get('tags',{})
        if el['type']=='node':
            places.append((P(el['lat'],el['lon']),t.get('place'))); continue
        pts=[P(g['lat'],g['lon']) for g in el.get('geometry',[])]
        hw=t.get('highway'); ww=t.get('waterway')
        if ww:
            if acc=='river': line('acc',pts,ac,255,5 if ww=='river' else 1.6)
            elif not regional: line('mid',pts,ln,110,2 if ww=='river' else 0.8)
        elif t.get('natural')=='coastline':
            line('acc' if acc=='coast' else 'major',pts,ac if acc=='coast' else ln,255,4)
        elif t.get('railway'):
            if acc=='corridor': line('acc',pts,ac,255,3.5)
            else: line('mid',pts,ln,140,1.2)
        elif hw:
            if regional:
                if acc=='corridor' and hw in ('trunk','motorway','trunk_link','motorway_link'): line('acc',pts,ac,230,3)
                elif hw in MAJOR: line('major',pts,ln,200,1.6)
                else: line('mid',pts,ln,120,0.9)
            elif hw in MINOR: line('minor',pts,ln,200 if scheme=='form' else 150,0.8 if hw!='track' else 0.6)
            elif hw in MID:
                if acc=='arterial' and hw.startswith('secondary'): line('acc',pts,ac,220,2.4)
                else: line('mid',pts,ln,210,1.5)
            else:
                if acc=='arterial': line('acc',pts,ac,255,3.2)
                else: line('major',pts,ln,240,2.6)
    for (x,y),p in places:
        r=(11 if p=='city' else 4.5)*K
        dr['acc'].ellipse([x-r,y-r,x+r,y+r],fill=ac+(255,))
    for k in ['minor','mid','major','acc']: img.paste(layers[k],(0,0),layers[k])
    img=img.resize((W,H),Image.LANCZOS)
    img.save(f'{OUT}/{slug}.jpg',quality=85,optimize=True,progressive=True)
    print(slug,os.path.getsize(f'{OUT}/{slug}.jpg')//1024,'KB')
for slug in (sys.argv[2:] or PROJ): render(slug)
