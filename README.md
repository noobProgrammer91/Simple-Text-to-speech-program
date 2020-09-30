Text-to-speech program in Python

This is a simple program that will read your pdf files as well as any words or sentences you want.

## Installation

We need to install two modules for this program to work.

1.pyttsx3

2.pypdf2

```bash
pip install pyttsx3==2.7
pip install pypdf2
```

## Usage

```python
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
page = pdf_reader.getPage(1) 

#This is going to extract all the text from your pdf file
text = page.extractText() 

#Setting up the engine for the speaker

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License & Copyright
[MIT] Swastik Sarkar
