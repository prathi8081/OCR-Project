from flask import *
from PIL import Image
import pytesseract
import sys,os

app = Flask(__name__)  
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
						f = request.files['file']  
						f.save(f.filename)
						text = pytesseract.image_to_string(Image.open(f), lang = 'eng')
						print(text)
						f = open("templates/output.txt", "w")
						f.write(text+'\n')
						f.close()
						f=open('templates/output.txt','r')
						g= f.read()
						return render_template('index.html',n=g)
					





if __name__=="__main__":
    app.run(debug=True)



