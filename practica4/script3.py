import feedparser
import urllib2
import sys

feed = feedparser.parse('meneame.xml')
items = feed[ "items" ]
cont_img = 0
q = sys.argv[1]

for item in items:
	if 'media_thumbnail' in item:
		cont_img = cont_img +1
		url = item['media_thumbnail'][0]['url']
		f = urllib2.urlopen(url)
		name = url.split('/')[-1]
		imagen = open("imagenes/"+name, "wb")
		imagen.write(f.read())
		imagen.close()
	if q in item['title']:
		print item['title']

print "Numero de noticias: %s" % len(items)
print "Numero de imagenes: %s" % cont_img
