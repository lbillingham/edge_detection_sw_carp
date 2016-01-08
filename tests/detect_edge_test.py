import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

#input correct module name here
from detect_edge import * 


def generate_image(st_dev_gauss=0, noise_param=0):
    
    img = np.zeros((200, 200))
    rr, cc = circle(100, 100, 50)
    img[rr, cc] = 1

    img = ndi.gaussian_filter(im, st_dev_gauss)
    img += noise_param * np.random.random(im.shape)
    return img
    

def test_clean_img():
    im = generate_image()
    edge_test = detect_edge(im, sigma=2) 
    
    assert (count_rings == 1)


def test_medium_noise_img():
    im = generate_image(2, 0.2)
    edge_test = detect_edge(im, sigma=3)    

    assert (count_rings == 1)
    
        
def test_high_noise_img():
    im = generate_image(4, 0.5)
    edge_test = detect_edge(im, sigma=6)
                                           
    assert (count_rings == 1)

