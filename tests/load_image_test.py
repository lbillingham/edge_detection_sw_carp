import os.path as pth
import image_loader as il


def test_load():
    filename = pth.join('.', 'test_data', 'blurry_ring.png')
    test_on_image = il.load_image(filename)
    obs_size = (200, 200)
    #obs_max = 
    #obs_min =

    exp_size = test_on_image.shape
    #exp_max =
    #exp_min =

    assert ((obs_size == exp_size))# and (obs_max == exp_max) and (obs_min == exp_min))
