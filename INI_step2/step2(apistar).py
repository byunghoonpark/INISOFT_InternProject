from apistar import App, Route
from apistar import http
import os
from werkzeug.utils import secure_filename
from pathlib import Path
import requests
from werkzeug.datastructures import FileStorage

def upload_file2(request: http.Request) -> http.Response:
 if request.method == 'OPTIONS':
   return 200

def upload_file(request: http.Request, request_data:http.RequestData) -> http.Response:

 if request.method == 'POST':

   file = request_data.get('file1')
   filename = file.filename

   print(filename)

   fileDes = '/var/www/html/wp-content/file/'+filename

   if os.path.isdir(fileDes):
      if os.path.isfile( str(fileDes)+'/'+filename ):
        content = filename + ' already exists. Change your file.name'
        headers = {'Content-Type':'text/plain'}
        return http.Response(content, headers=headers)
      else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(fileDes,filename))
        content =  'Success file upload'
        headers = {'Content-Type' : 'text/plain'}
        return http.Response(content, headers=headers)

   else:
     os.makedirs(str(fileDes))
     filename = secure_filename(file.filename)
     file.save(os.path.join(fileDes,filename))
     content = 'Make your new Directory and Success file upload'
     headers = {'Content-Type':'text/plain'}
     return http.Response(content, headers=headers)

routes = [
 Route('/upload', method='POST', handler=upload_file),
 Route('/upload', method='OPTIONS', handler=upload_file2)
]

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000 ,debug=True)


