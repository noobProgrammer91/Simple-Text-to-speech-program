
#We need two modules for this program -pyttsx3 and pyPDF2


#Importing the modules

import pyttsx3
import PyPDF2

#Setting up the pdf reader

#opening the file in read binary mode
pdf_file = open('C://Users//KharabNaHona//Desktop//test2.pdf','rb') 
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

#Get all the pages from your pdf file
pages = pdf_reader.numPages 

#This is going to locate a single page in your file
page =pdf_reader.getPage(1) 

#This is going to extract all the text from your pdf file
text = page.extractText() 

#Setting up the engine for the speaker

engine = pyttsx3.init()
engine.say(text)
engine.setProperty('volume',10)
engine.runAndWait()



