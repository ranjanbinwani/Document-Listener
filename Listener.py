import PyPDF2
import os
import docx
from gtts import gTTS
import re
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)


def getText(file_path):
    if(os.path.exists(file_path)):
        pass
    else:
        print("File does not exist")
        exit()

    doc = docx.Document(file_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ('/n'.join(fullText))

def docs(file_path):
    string_words = getText(file_path)
    print(string_words)
    tts = gTTS(text=string_words, lang='en', slow=True)
    tts.save("C:/Users/ranjan/Desktop/listen_pdf.mp3")
    os.system("mpg321 C:/Users/ranjan/Desktop/listen_pdf.mp3")

def my_function(file_path):
   
  if(os.path.exists(file_path)):
      pass
  else:
      print("File does not exist")
      exit()
   
  f = open(file_path, 'rb')
  pdffile = PyPDF2.PdfFileReader(f)

  if(pdffile.isEncrypted):
    pdfReader.decrypt('your_password')

  no_of_pages = pdffile.getNumPages()
   
   
  string_words = ''
  for pageno in range(no_of_pages):
      pi = pdffile.getPage(pageno)
      page = pdffile.getPage(pageno)
      content = page.extractText()
      textonly = re.findall(r'[a-zA-Z0-9]+', content)
      for word in textonly:
          string_words = string_words + ' ' + word
   
  print(string_words)
  tts = gTTS(text=string_words, lang='en')
  tts.save("C:/Users/ranjan/Desktop/listen_pdf.mp3")
  os.system("mpg321 C:/Users/ranjan/Desktop/listen_pdf.mp3")

def getTextTxt(file_path):
    if(os.path.exists(file_path)):
        pass
    else:
        print("File does not exist")
        exit()

    f = open(file_path,"r")
    return(f.read())

def docsTxt(file_path):
    string_words = getTextTxt(file_path)
    print(string_words)
    tts = gTTS(text=string_words, lang='en')
    tts.save("C:/Users/ranjan/Desktop/listen_pdf.mp3")
    os.system("mpg321 C:/Users/ranjan/Desktop/listen_pdf.mp3")


@app.route('/')
def upload_file():
  return '<html><body> <form action = "http://localhost:5000/upload" method = "POST" enctype = "multipart/form-data"><input type = "file" name = "file" /><input type = "submit"/></form></body></html>'
  
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      ext = f.filename.split('.')
      if ext[1] == "pdf":
        my_function(request.files['file'].filename)
      elif ext[1] == "docx":
        docs(f.filename)
      elif ext[1] == "txt":
        docsTxt(f.filename)
      else:
        print('Invalid File')
      return ('file generated successfully')
    
if __name__ == '__main__':
   app.run(debug = True)
