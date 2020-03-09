
import tensorflow as tf
import pandas as pd 
import numpy as np
import skimage 
import matplotlib.pyplot as plt
import seaborn as sns
from os import listdir
from skimage.io import imread_collection, imread
from skimage.io.collection import ImageCollection
import random
sns.set_style("whitegrid")


from tensorflow.keras.layers import Input, Conv2D, UpSampling2D, MaxPool2D, AveragePooling2D, Conv2DTranspose
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam




def list_files1(directory, extension):
    """
    list_files1: Find files with a certain extension in the directory and return the names in a list
            Args:
                directory: Directory to be searched
                extension: the extension of the files
            Returns:
                List of files with the extension within the directory
    """
    return list(( (directory + f) for f in listdir(directory) if f.endswith('.' + extension)))

def imread_grayscale(img_path):
    """
    imread_grayscale: Read images in lab
               Args:
                    img_path: Get the path of the image
               Returns:
                    Matrix with the image as a gray-scale
                
    """
    img = (1.0/255)*imread(img_path)
    return skimage.color.rgb2lab(img)

def load_from_dir(directory, extension):
    """
    load_from_dir: Takes in the directory path and extension of images to be read, and reads them in.
            Args:
                (String) directroy: path to directory
                (String) extension: extension of the files to be read
            Returns:
                (Numpy Array)data: The normal data w the 3 channels
                (Numpy Array) data_gray: the data converted to gray scale format 
    """
    data = np.array(ImageCollection('{a}/*.{b}'.format(a = directory, b = extension), load_func=imread))
    data_gray = np.array(ImageCollection('{a}/*.{b}'.format(a = directory, b = extension), load_func = imread_grayscale))
    return (data,data_gray)

### Plot a few points
def plt_predict(idx,X_HE,Y_HE, myModel, mode = 0):
    """
    plt_predict_HE: Plot the gray scale image, expected output and the color prediction by model
                Args:
                    (int) idx: index within X_HE that needs to be plotted
            (Numpy Array) X_HE: Data containing the colored image. Shape = (example_no, img_size, img_size,1)
            (Numpy Array) Y_HE: Data containg the color image. Shape = (example_no, img_size, img_size, 3)
            (keras Model) myModel: Model that is used for prediction
            (int) mode: 0 for H&E, 1 for MUSE
                Returns:
                        None
                    
    """
    img = X_HE[idx,:,:]
    
    pred = myModel.predict(img.reshape(1,512,512,1)).reshape(512,512,2)
    pred = (pred * 256)- 128
    pred = skimage.color.lab2rgb( np.concatenate((img,pred), axis =2 ))
    
    sns.set_style('whitegrid')
    plt.figure(figsize = (10,10))
    plt.subplot(1,3,1)
    plt.imshow(img.reshape(512,512), cmap = "gray")
    plt.title("Gray Scale Image(Input)")
    plt.subplot(1,3,2)
    plt.imshow(Y_HE[idx,:,:,:])
    if(mode==0):
        plt.title("Actual Color mapping for H&E(output)")
    if(mode ==1):
        plt.title("MUSE Image")
    plt.subplot(1,3,3)
    plt.imshow(pred)
    plt.title("Color prediction by model") 
    
    
# directory = "../datasets/MUSE/trainB"
# extension = "png"
# data, data_gray = load_from_dir(directory, extension)


directory = "trainA"
extension = "jpg"
data_MUSE, data_gray_MUSE = load_from_dir(directory, extension)
# print("Shape of data_gray is {}".format(data_gray.shape))
# print("Shape of data is {}".format(data.shape))

