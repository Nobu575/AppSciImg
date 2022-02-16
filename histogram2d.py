import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage import data, img_as_float
from skimage import exposure


matplotlib.rcParams['font.size'] = 8

''' This file contains tutorial code of scikit-image.
https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_equalize.html#sphx-glr-auto-examples-color-exposure-plot-equalize-py
'''

def plot_img_and_hist_original(image, axes, bins=256):
    """Plot an image along with its histogram and cumulative histogram.

    """
    # image = img_as_float(image)
    ax_img, ax_hist = axes

    # Display image
    ax_img.imshow(image, cmap=plt.cm.gray)
    ax_img.set_axis_off()

    # Display histogram
    ax_hist.hist(image.ravel(), range=(-200,200), bins=bins, histtype='step', color='black')
    ax_hist.set_xlabel('Pixel intensity')

    return ax_img, ax_hist

def plot_img_and_hist(image, axes, bins=256):
    """Plot an image along with its histogram and cumulative histogram.

    """
    image = img_as_float(image)
    ax_img, ax_hist = axes
    ax_cdf = ax_hist.twinx()

    # Display image
    ax_img.imshow(image, cmap=plt.cm.gray)
    ax_img.set_axis_off()

    # Display histogram
    ax_hist.hist(image.ravel(), bins=bins, histtype='step', color='black')
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')
    ax_hist.set_xlim(0, 1)
    ax_hist.set_yticks([])

    # Display cumulative distribution
    img_cdf, bins = exposure.cumulative_distribution(image, bins)
    ax_cdf.plot(bins, img_cdf, 'r')
    ax_cdf.set_yticks([])

    return ax_img, ax_hist, ax_cdf

def histogram_2d(input_img):
    # Load an example image
    img = input_img

    # Contrast stretching
    p2, p98 = np.percentile(img, (2, 98))
    img_rescale = exposure.rescale_intensity(img, in_range=(p2, p98))

    # Equalization
    # img_eq = exposure.equalize_hist(img)

    # Adaptive Equalization
    # img_adapteq = exposure.equalize_adapthist(img, clip_limit=0.03)

    # Display results
    fig = plt.figure(figsize=(6, 3))
    axes = np.zeros((2, 2), dtype=np.object)
    axes[0, 0] = fig.add_subplot(2, 2, 1)
    axes[0, 1] = fig.add_subplot(2, 2, 2)
    axes[1, 0] = fig.add_subplot(2, 2, 3)
    axes[1, 1] = fig.add_subplot(2, 2, 4)

    ax_img, ax_hist = plot_img_and_hist_original(img, axes[:, 0],bins=20)
    ax_img.set_title('Original image')

    y_min, y_max = ax_hist.get_ylim()
    ax_hist.set_ylabel('Number of pixels')
    ax_hist.set_yticks(np.linspace(0, y_max, 5))

    ax_img, ax_hist, ax_cdf = plot_img_and_hist(img_rescale, axes[:, 1])
    ax_img.set_title('Contrast stretching')

    ax_cdf.set_ylabel('Fraction of total intensity')
    ax_cdf.set_yticks(np.linspace(0, 1, 5))

    # prevent overlap of y-axis labels
    fig.tight_layout()
    plt.show()

def main() :
    print("This is a histogram computation usiong scikit-image.")

if __name__ == "__main__":
    main()