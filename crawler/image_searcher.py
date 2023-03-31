from google_images_search import GoogleImagesSearch
from io import BytesIO
from PIL import Image
import os
os.environ['HTTP_PROXY'] = '127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = '127.0.0.1:7890'
def google_image_search(text):
    # create a GoogleImagesSearch object with your API key and project ID
    gis = GoogleImagesSearch('AIzaSyCJCbdICq04XHRT2RkcW_WlXTTly9JJ0c4', 'map-2021-335109')

    # define a callback function to handle each image object
    def my_callback(image_object):
        # do something with image object, such as displaying it or saving it
        image = Image.open(BytesIO(image_object))
        image.show()

    # define the search parameters with your text to search for images
    search_params = {
        'q': text,
        'num': 10,
        'safe': 'high',
        'fileType': 'jpg',
    }

    # perform the search and call the callback function for each image object
    gis.search(search_params=search_params, path_to_dir=None, custom_image_name=None)

# test the function with some text
google_image_search('puppies')