import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage.measure import label
from skimage.morphology import disk, binary_closing, binary_opening
from skimage.color import label2rgb

plt.rcParams["font.size"] = 16

def labeling_2d(input_img):

    # Threshold
    output_img = np.where(input_img>100, 1, 0)

    # closing
    output_img = binary_closing( output_img, disk(3) )

    # opening
    output_img = binary_opening( output_img, disk(2) )
    morph_img = output_img

    # labeling
    output_img = label( output_img )
    output_rgb = label2rgb( output_img, bg_label=0 )

    # Plot the input and output images.
    plt.figure(figsize=(12, 4), dpi=50)
    plt.subplot(1,3,1),plt.title("original"),plt.imshow(input_img, cmap="gray")
    plt.subplot(1,3,2),plt.title("remove small regions"),plt.imshow(morph_img)
    plt.subplot(1,3,3),plt.title("labeled result"),plt.imshow(output_rgb)
    plt.show()

def main() :
    print("This is an example of labeling usiong scikit-image.")

if __name__ == "__main__":
    main()