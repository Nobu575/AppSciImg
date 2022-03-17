import matplotlib.pyplot as plt

from skimage.filters import meijering, sato, frangi, hessian

def identity(image, **kwargs):
    """Return the original image, ignoring any kwargs."""
    return image

def ridge_2d(input_img):

    cmap = plt.cm.gray
    kwargs = {'sigmas': [1.5], 'mode': 'reflect'}

    fig, axes = plt.subplots(2, 5)
    for i, black_ridges in enumerate([1, 0]):
        for j, func in enumerate([identity, meijering, sato, frangi, hessian]):
            kwargs['black_ridges'] = black_ridges
            result = func(input_img, **kwargs)
            axes[i, j].imshow(result, cmap=cmap, aspect='auto')
            if i == 0:
                axes[i, j].set_title(['Original\nMIP image', 'Meijering\nneuriteness',
                                    'Sato\ntubeness', 'Frangi\nvesselness',
                                    'Hessian\nvesselness'][j])
            if j == 0:
                axes[i, j].set_ylabel('black_ridges = ' + str(bool(black_ridges)))
            axes[i, j].set_xticks([])
            axes[i, j].set_yticks([])

    plt.tight_layout()
    plt.show()

def main() :
    print("This is an example of ridge operation usiong scikit-image.")

if __name__ == "__main__":
    main()