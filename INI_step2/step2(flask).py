from flask import Flask
from flask import request
from apistar import App, Route
from pathlib import Path
from flask import session
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def upload_file():
 if request.method == 'POST':

   file = request.files['file1']
   filename = file.filename
   fileDes = '/var/www/html/wp-content/file/'+filename
   P_fileDes = Path(fileDes)
   app.config[fileDes] = fileDes

   if P_fileDes.is_dir(): 
      print( str(fileDes)+'/'+filename )
      if os.path.isfile( str(fileDes)+'/'+filename ):  
        return (filename + ' already exists. Change your file name')

      else:  
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config[fileDes],filename))
        return 'Success file upload'

   else: 
     os.makedirs(str(fileDes))  
     filename = secure_filename(file.filename)  
     file.save(os.path.join(app.config[fileDes],filename))
     return 'Make your new Directory and Success file upload'



if __name__ == '__main__':
    app.serve('127.0.0.1', 5000 ,debug=True)



