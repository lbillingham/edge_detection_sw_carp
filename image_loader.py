# -*- coding: utf-8 -*-
"""
Load an image to a numpy array
Created on Fri Jan  8 11:23:56 2016

@author: laurence
"""
import matplotlib.pyplot as plt


def load_image(filename):
    """
    Load an image from `filename` and return a `numpy.array`
    Parameters
    ----------
    filename:
        path to an image file

    Returns
    -------
    image as a numpy array

    *   for grayscale images, the return array is MxN.
    *   for RGB images, the return value is MxNx3.
    *   for RGBA images the return value is MxNx4.

    Side Effects
    ------------
    None
    """
    image = plt.imread(filename)
    return image
