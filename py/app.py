import base64
from flask import Flask
from flask import request
from get_image_label import chekcImage
import os
import uuid
import shutil
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/img/upload2',methods=['POST'])
@cross_origin(origin='*')
def saveImage2():
	file_path = createFolder()
	names = request.json["names"]
	i = 1
	for name in names:
		print(name)
		print()
		print()
		name = base64.b64decode(name)
		fh = open(file_path + "imageToSave"+str(i)+".jpg", "wb")
		fh.write(name)
		fh.close()
		i = i + 1
		
	return chekcImage(file_path)
	
def createFolder():
	file_path = "archives/" + str(uuid.uuid4())+"/"
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
		os.makedirs(directory)
	return file_path

def cleanUp():
	shutil.rmtree("7042df97-2955-4631-83af-1ca468d55c06")
	return "aaaa"
	
if __name__ == '__main__':    
	app.run(port=5000)  