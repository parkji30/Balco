import os, shutil

## Change this to where your balco is located.

balco_home = "/Users/a16472/Desktop/Balco/dev/"
comp_folder = "/Users/a16472/Desktop/Balco/dev/comp_images/"
og_folder = "/Users/a16472/Desktop/Balco/dev/images/"

# Change directory to Balco.
os.chdir(balco_home)

def empty_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

## Delete the compression folder each time we run.
empty_folder(comp_folder)

## Load Packages
from Compression import Compression
from Model import Model
from astropy.io import fits

original_images = './images/'
comp_images = './comp_images/'

# c_list = ['RICE_1', 'GZIP_1', 'GZIP_2', 'PLIO_1', 'HCOMPRESS_1']
# try:
#     algorithm = sys.argv[-2]
#     q_factor = float(sys.argv[-1])
# except:
#     print("Something went wrong...")
#     exit()

# if not algorithm in c_list:
#     print("Could not comprehend command, system exiting...")
#     exit()

original_image = fits.open(og_folder + 'dwb_image_ifc_1568792972_1459_target_150.fits')[0].data
file_size = os.path.getsize(og_folder + 'dwb_image_ifc_1568792972_1459_target_150.fits')

## Compress
# Compression List -> ['RICE_1', 'GZIP_1', 'GZIP_2', 'PLIO_1', 'HCOMPRESS_1']
# algorithm = 'RICE_1'

compressor = Compression(data=original_image, image_name="dwb_image_ifc_1568792972_1459_target_150.fits", file_size=file_size)
compressor.update_save_directory(comp_folder)
# compressor.compress(algorithm='RICE_1')
selected_image = compressor.optimize(algorithm="HCOMPRESS_1", compression_range=(0, 1), iterations=10)

## Model Analysis
selected_image.Im_show()
selected_image.Im_show(version="Compressed")

## Empties the compression(analysis) folder.
empty_folder(comp_folder)

## Save the image now.
selected_image.save_image("/Users/a16472/Desktop/Balco/dev/")