import numpy as np

scalar = np.array(42)
one_d = np.array([1, 2, 3])
two_d = np.array([[1, 2, 3], [4, 5, 6]])
three_d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(
    'scalar tensor (axes: {scalar.ndim}; shape: {scalar.shape}; type: {scalar.dtype}): \n{scalar}\n\n',
    '1D tensor (axes: {one_d.ndim}; shape: {one_d.shape}; type: {scalar.dtype}): \n{one_d}\n\n',
    '2D tensor (axes: {two_d.ndim}; shape: {two_d.shape}; type: {scalar.dtype}): \n{two_d}\n\n',
    '3D tensor (axes: {three_d.ndim}; shape: {three_d.shape}; type: {scalar.dtype}): \n{three_d}\n\n'
)


from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

def print_structures():
    print(
        'training images \
            \n\tcount: {len(train_images)} \
            \n\tdimensions: {train_images.ndim} \
            \n\tshape: {train_images.shape} \
            \n\tdata type: {train_images.dtype}\n\n',
        'testing images \
            \n\tcount: {len(test_labels)} \
            \n\tdimensions: {train_labels.ndim} \
            \n\tshape: {test_labels.shape} \
            \n\tdata type: {test_labels.dtype} \
            \n\tvalues: {test_labels}\n',
    )
print_structures()