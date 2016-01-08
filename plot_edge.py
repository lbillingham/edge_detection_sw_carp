import matplotlib.pyplot as plt
from edge_detection import detect_edge

def plot_edge(im,sigma=1,high_threshold,low_threshold):
    '''
    Plots original image and edge image next to each other.
    
    Arguments
    im = 2D array describing image
    sigma
    high_threshold
    low_threshold

    Function which will be made interactive.
    '''

    edges = detect_edge(im,sigma,high_threshold,low_threshold)
    

    fig, axes = plt.subplots(nrows=1, ncols=2)
    ax_orig = axes[0]
    ax_edges = axes[1]
    ax_orig.imshow(image_in)
    ax_edges.imshow(edges)
    fig.show()

#    fig = plt.figure(figsize=(10,3))
#    ax1 = fig.add_subplot(1,2,1)
#    ax2 = fig.add_subplot(1,2,2)
    
#    ax1.imshow(im)
#    ax2.imshow(edges)
    
#    fig.tight_layout()
#    fig, axes = plt.subplots(nrows=1, ncols=2)
