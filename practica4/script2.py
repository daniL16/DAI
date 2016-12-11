from lxml import etree
import urllib2
import sys

tree = etree.parse('meneame.xml')
rss = tree.getroot()
channel = rss[0]

cont_art=0
cont_img=0
q = sys.argv[1]

for e in channel:
		if (e.tag == 'item'):
				cont_art = cont_art + 1 
		for item in e:
			if(item.tag == '{http://search.yahoo.com/mrss/}thumbnail'):
				cont_img = cont_img + 1
				url = item.get('url')
				f = urllib2.urlopen(url)
				name = url.split('/')[-1]
				imagen = open("imagenes/"+name, "wb")
				imagen.write(f.read())
				imagen.close()
			if item.tag=='title' and q in item.text:
				print item.text
		
print "Numero de noticias: %s" % cont_art
print "Numero de imagenes: %s" % cont_img
