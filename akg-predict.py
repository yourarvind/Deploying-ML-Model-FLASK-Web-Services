# ------------------------------------------------ 
# Accessing pre-trained deep learning (ML) model
#    through FLASK based web services
# Author: Arvind Kumar
# Email: arvind.cse@gmail.com
#-------------------------------------------------
import numpy as np
import sys
import io
import base64
import numpy as np

from flask import Flask
from flask import request
from flask import jsonify

from PIL import Image

import keras.backend
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
#.......................................

app = Flask(__name__)

#.......................................
def preprocessImage(image, target_size):
    if image.mode != "RGB" :
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image
#.......................................
    
@app.route('/akg-predict',methods=['POST'])
def predict():
    print('model predict is called.  ', file=sys.stderr)
    #create instance of VGG16 model
    model = VGG16()

    # read client request
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded)) 

    image = preprocessImage(image, target_size=(224, 224))
    #print(image.shape  , file=sys.stderr)

    # predict the probability across all output classes
    yhat = model.predict(image)

    # convert the probabilities to class labels
    label1 = decode_predictions(yhat)
    
    # retrieve the most likely result, e.g. highest probability
    label = label1[0][0]
    objName = label[1]
    objConfidence = label[2]*100

    # print the classification
    #print('%s (%.2f%%)' % (label[1], label[2]*100), file=sys.stderr)
    
    #prepare return response
    response = {
            'prediction':{
                    'name': objName,
                    'confidence': objConfidence                    
            }
    }
            
    # clear this session before returning to client
    keras.backend.clear_session() 
    return jsonify(response)
#.......................................


