from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np

test_model = load_model('models/model2.h5')

def catdogclassifier(imgpath):
    img = load_img(imgpath,False,target_size=(150,150))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = test_model.predict_classes(x)
    return preds

 #catdogclassifier('data/mini_validation/cat.1008.jpg')