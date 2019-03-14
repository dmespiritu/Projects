#Script to make a pdf document into a text file and pull then have a number count of how many times a word appears in the text

import PyPDF2

pdfName = '/Users/dmespiritu/git/Projects/Python/31-reasons.pdf'
rdPdf = PyPDF2.PdfFileReader(pdfName)

for i in xrange(rdPdf.getNumPages()):
	page = rdPdf.getPage(i)
    	print 'Page No - ' + str(1+rdPdf.getPageNumber(page))
    	page_content = page.extractText()
    	print page_content

