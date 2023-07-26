from PIL import Image
import numpy as np


def png_to_numpy(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Convert the image to grayscale if it's not already
    if image.mode != 'L':
        image = image.convert('L')

    # Convert the PIL image to a NumPy array
    numpy_array = np.array(image)

    # Replace black values with 0 and white values with 255
    numpy_array = np.where(numpy_array == 0, 255, 0)

    return numpy_array


# Replace 'path/to/your/image.png' with the actual path to your black and white PNG image

def file_to_array():
    image_path = '/home/ale/project/hackmeeting2023/test.png'
    numpy_array = png_to_numpy(image_path)
    numpy_array = np.rot90(numpy_array, k=1, axes=(0, 1))
    numpy_array = np.flip(numpy_array, axis=0)
    x, y = numpy_array.shape
    print("------------> ", x, y)
    print(numpy_array)

    return numpy_array
