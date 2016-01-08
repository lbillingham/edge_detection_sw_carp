# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:14:47 2016

@author: laurence
"""

from image_loader import load_image
from edge_detection import detect_edge

import os.path as pth
import matplotlib.pyplot as plt


def plot_test_image_and_edges():
    """
    example to plot an image and the detected edges
    """
    test_file = pth.join('.', 'tests', 'test_data', '10_circles_colour.gif')
    image_in = load_image(test_file)
    edges = detect_edge(image_in)
    fig, axes = plt.subplots(nrows=1, ncols=2)
    ax_orig = axes[0]
    ax_edges = axes[1]
    ax_orig.imshow(image_in)
    ax_edges.imshow(edges)
    fig.show()

if '__main__' == __name__:
    plot_test_image_and_edges()
