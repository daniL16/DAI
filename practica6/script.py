from lxml import etree
import urllib2
import sys

class ParseRssNews ():
	def __init__ (self):
		print ("inicio archivo")
		self.cont_art = 0
		self.cont_img = 0
		self.q = sys.argv[1]

	def start (self, tag, attrib):
		if (tag == "item"):
			self.cont_art = self.cont_art+1
		if (tag == "{http://search.yahoo.com/mrss/}thumbnail"):
			self.cont_img = self.cont_img+1
		
		#if (tag == "title" and self.q in tag ):
	def data(self,data):
		if (self.q in title):
			print title
	def close (self):
		print "Numero de noticias: %s" % self.cont_art
		print "Numero de imagenes: %s" % self.cont_img
		print ("---- Fin del archivo")

parser = etree.XMLParser (target=ParseRssNews ())
etree.parse ('meneame.xml', parser)

