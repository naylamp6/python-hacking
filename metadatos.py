# Python
# -*- encoding: utf-8 -*-
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

path = ""
rb = ""
def printMeta():
	for dirpath, dirnames, files in os.walk("docs"):
		for name in files:
			ext = name.lower().rsplit('.', 1)[-1]
		if ext in ['pdf']:
			print ("[ + ] Metadata for file: %s") %(dirpath+os.path.sep+name)
			pdffile = PdfFileReader(open(dirpath+os.path.sep+name, 'rb'))
			docInfo = pdffile.getDocumentInfo()
			for metaItem in docInfo:
				print ('[+] ' + metaItem + ':' + docInfo[metaItem])
	print ("\n")
print ("\n")
print (printMeta)
print ("\n")
def contenidoPDF(path):
	contenido = ""
	p = open(path, rb)
	pdf = pyPdf.PdfFileReader(p)
	num_pages = pdf.getNumberPages()
	for i in range(0, num_pages):
		contenido += pdf.getPage(i).extractText() + "\n"
	contenido = "".join(contenido.replace(u"\xa0", " ").strip().split())
	return contenido
print (contenidoPDF)
print ("\n")
print ("\t"+"Finalizado")
