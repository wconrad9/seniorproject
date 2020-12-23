from skimage.io import imsave, imread
from skimage.util import img_as_ubyte
import glob
from skimage.color import rgb2hsv, hsv2rgb
import numpy as np
import os

imageset = glob.glob("../vid/images/*.jpg")

def generate_moodmap():
    """Creates hsv color map for video clip"""

    hsv_set = []

    i = 1
    for im in imageset:
        rgb_im = imread(im)
        hsv_im = rgb2hsv(rgb_im)
        hm = np.mean(hsv_im[:,:,0])
        sm = np.mean(hsv_im[:,:,1])
        vm = np.mean(hsv_im[:,:,2])
        
        frame = [hm, sm, vm]
        #rgb2 = hsv2rgb(frame)

        #scaler = np.ones((500,500,3), dtype=np.uint8)

        #square = scaler * frame
        
        #square_uint8 = img_as_ubyte(square)
        
        #if not os.path.exists("../Vid/moodmap/"):
                #os.mkdir("../Vid/moodmap/")
                
        #imsave(f"../Vid/moodmap/{i}.jpg", square)
        
        hsv_set.append(frame)

        i+=1
        print(i/len(imageset)*100)

    return hsv_set