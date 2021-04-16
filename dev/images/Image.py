import numpy as np
import matplotlib.pyplot as plt

class Image:
    def __init__(self, data, compressed_data=0, image_name, compressed_image_name, info):
        """
        @type self: Image
        
        @type data: Numpy Array(2d) 
            Image represented by its 2D pixel values

        @type info:
            Information of the image containing it's header.
        """

        self.data = data
        self.data_modified = np.copy(self.data)
        self.compressed_data = compressed_data

        self.image_name = image_name
        self.compressed_image_name = compressed_image_name
        self.info = info

    def median_reduction(self):
        """
        Median reduction of image. 

        Typically used in situations where a major portion of the image
        is dark empty space.
            e.g. Super/Giga BIT images.

        @type self: Image
        @rtype: Numpy Array(2d) 
            Image represented by its 2D pixel values
        """
        return self.data - np.median(self.data)

    def flat_field_reduction(self):
        """
        Flat field reduction of image to account for faulty light measurement
        across camera

        @type self: Image
        @rtype: Numpy Array(2d) 
            Image represented by its 2D pixel values
        """
        pass

    def get_mms(self, version='original'):
        """
        Returns the mean, median, standard deviation of the input image.

        @type self: Model
        @type original_view: Boolean (Display the original or compressed Image)
        """
        original = self.data
        compressed = self.compressed_data

        if version.lower()=='original':
            return [np.mean(original), np.median(original), np.std(original)]
        else:
            return [np.mean(compressed), np.median(compressed), np.std(compressed)]

    def update_compressed_name(self, name):
        """
        Updates the compressed image name and stores in into the variable.

        @type self: Image
        @type name: String
            Name of the compressed image file.
        @rtype: None
        """
        self.compressed_image_name = name