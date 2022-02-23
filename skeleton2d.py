import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage.measure import label
from skimage.morphology import disk, binary_closing, binary_opening, convex_hull_image, skeletonize, dilation
from skimage.color import label2rgb

plt.rcParams["font.size"] = 16

def skeleton_2d(input_img):

    im_row = 2
    im_col = 3

    plt.figure(figsize=(12, 9), dpi=50),plt.subplots_adjust(hspace=0.5)
    plt.subplot(im_row,im_col,1),plt.title("original"),plt.imshow(input_img, cmap="gray")

    # Threshold
    output_img = np.where(input_img>100, 1, 0)
    plt.subplot(im_row,im_col,2),plt.title("CT>100HU"),plt.imshow(output_img)

    # closing
    output_img = binary_closing( output_img, disk(3) )

    # opening
    output_img = binary_opening( output_img, disk(2) )
    plt.subplot(im_row,im_col,3),plt.title("remove small regions"),plt.imshow(output_img)

    # labeling
    output_img = label( output_img )
    max_label = np.max( output_img )
    print("max_label:", max_label)
    plt.subplot(im_row,im_col,4),plt.title("labeled regions"),plt.imshow(label2rgb( output_img, bg_label=0 ))

    # convex hull
    for i in range(1,max_label+1):
        label_img = np.where( output_img==i, 1, 0 )
        label_img = convex_hull_image( label_img )
        output_img = np.where( label_img==1, i, output_img )
    plt.subplot(im_row,im_col,5),plt.title("convex hull"),plt.imshow(label2rgb( output_img, bg_label=0 ))

    # copy
    labeled_result_img = output_img

    # skeletonize
    output_img = np.where( output_img>0, 1, 0)
    output_img = skeletonize( output_img )
    output_img = np.where( output_img>0, labeled_result_img, 0 )

    # dilation
    output_img = dilation( output_img, disk(3) )

    # Plot
    plt.subplot(im_row,im_col,6),plt.title("skeletonized result"),plt.imshow(label2rgb( output_img, bg_label=0 ))
    plt.show()

def main() :
    print("This is an example of convex hull usiong scikit-image.")

if __name__ == "__main__":
    main()