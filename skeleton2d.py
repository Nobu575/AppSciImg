import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage.measure import label
from skimage.morphology import disk, binary_closing, binary_opening, convex_hull_image, skeletonize, binary_dilation
from skimage.color import label2rgb

plt.rcParams["font.size"] = 16

def skeleton_2d(input_img):

    # Threshold
    output_img = np.where(input_img>100, 1, 0)

    # closing
    output_img = binary_closing( output_img, disk(3) )

    # opening
    output_img = binary_opening( output_img, disk(2) )

    # labeling
    output_img = label( output_img )
    max_label = np.max( output_img )
    print("max_label:", max_label)

    # convex hull
    for i in range(1,max_label+1):
        label_img = np.where( output_img==i, 1, 0 )
        label_img = convex_hull_image( label_img )
        output_img = np.where( label_img==1, i, output_img )
    labeled_result_img = output_img

    # skeletonize
    output_img = np.where( output_img>0, 1, 0)
    output_img = skeletonize( output_img )

    # dilation
    output_img = binary_dilation( output_img, disk(1) )
    output_img = np.where( output_img>0, labeled_result_img, 0 )

    output_labeled_rgb = label2rgb( labeled_result_img, bg_label=0 )
    output_rgb = label2rgb( output_img, bg_label=0 )

    # Plot the input and output images.
    plt.figure(figsize=(12, 4), dpi=50)
    plt.subplot(1,3,1),plt.title("original"),plt.imshow(input_img, cmap="gray")
    plt.subplot(1,3,2),plt.title("convex hull result"),plt.imshow(output_labeled_rgb)
    plt.subplot(1,3,3),plt.title("skeletonized result"),plt.imshow(output_rgb)
    plt.show()

def main() :
    print("This is an example of convex hull usiong scikit-image.")

if __name__ == "__main__":
    main()