
from PIL import Image
from io import BytesIO
import re, base64

import cv2
import face_recognition

def getI420FromBase64(codec, image_name):
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    img.save(image_name + '.png', "PNG")

def match_faces():
    licface=face_recognition.load_image_file('lpic.png')
    licface=cv2.cvtColor(licface,cv2.COLOR_BGR2RGB)
    realface=face_recognition.load_image_file('vpic.png')
    realface=cv2.cvtColor(realface,cv2.COLOR_BGR2RGB)
    encodelic=face_recognition.face_encodings(licface)[0]
    encodereal=face_recognition.face_encodings(realface)[0]
    results=face_recognition.compare_faces([encodelic],encodereal)
    facedis=face_recognition.face_distance([encodelic],encodereal)
    status='Verification successful' if results[0] else 'Verification Failed'
    return {'results':results[0],'face_distances':(1-facedis[0])*100, 'status': status}
