import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from skimage.feature import hessian_matrix, hessian_matrix_eigvals
plt.rcParams["font.size"] = 16

def hessian_2d(input_img):

    H_elems = hessian_matrix(input_img, sigma=1.0, order='rc')
    e0, e1 = hessian_matrix_eigvals(H_elems)

    # Plot the input and output images.
    plt.figure(figsize=(12, 4), dpi=50)
    plt.subplot(1,3,1),plt.title("original"),plt.imshow(input_img, cmap="gray")
    plt.subplot(1,3,2),plt.title("eigen 1"),plt.imshow(e0)
    plt.subplot(1,3,3),plt.title("eigen 2"),plt.imshow(e1)
    plt.show()

def main() :
    print("This is a hessian matrix and its eigen values computation usiong scikit-image.")

if __name__ == "__main__":
    main()