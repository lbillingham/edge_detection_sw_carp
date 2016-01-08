# -*- coding: utf-8 -*-
"""
Wrapper for scikit-image Canny edge detector

Created on Fri Jan  8 11:16:40 2016

@author: laurence
"""
from skimage.feature import canny
from skimage.color import rgb2gray


def detect_edge(image_array, sigma=1.0,
                low_threshold=None, high_threshold=None):
    """
    Detect the edges in an image using the Canny filter

    Parameters
    ----------
    image_array

    Returns
    -------
    array with edges identified

    Side Effects
    ------------
    None
    """
    gscale = rgb2gray(image_array)
    edges = canny(gscale)
    return edges

