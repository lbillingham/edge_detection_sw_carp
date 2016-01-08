def plot_edge(sigma=1,high_threshold,low_threshold):
    im = plt.imread('image.jpeg')
    edges = detect_edge(im,sigma,high_threshold,low_threshold)
    
    fig = plt.figure(figsize=(10,3))
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    
    ax1.imshow(im)
    ax2,imshow(edge)
    
    fig.tight_layout()
    plt.show()
