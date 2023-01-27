import math
import os
import requests
from PIL import Image


class ImageDownloader:
    def __init__(self, image_url):
        self.current_directory = os.getcwd()
        self.image_url = image_url

    def download_image(self):
        image_name = self.image_url.split("/")[-1]

        # Combine the current working directory and image name to get the full path to save the image
        self.save_path = os.path.join(self.current_directory, image_name)

        # Make a request to download the image
        try:
            response = requests.get(self.image_url)
        except ConnectionError:
            raise Exception('Check your internet connection')

        # Open the file and write the content
        with open(self.save_path, "wb") as f:
            f.write(response.content)

        print(f"Image downloaded successfully and saved in {self.current_directory}")

    def resize_image(self, width, height):
        # Open the image file
        with Image.open(self.save_path) as im:
            # Resize the image
            im = im.resize((width, height))
            # Save the resized image
            im.save(self.save_path)
        print(f"Image resized successfully to {width}x{height}")

    def resize_image_by_percent(self, percent):
        # Open the image file
        with Image.open(self.save_path) as im:
            original_width, original_height = im.size
            # Calculate the new width and height based on the percent
            new_width = int(original_width * percent / 100)
            new_height = int(original_height * percent / 100)
            # Resize the image
            im = im.resize((new_width, new_height))
            # Save the resized image
            im.save(self.save_path)
        print(f"Image resized successfully to {percent}% of original size")

    def reduce_image_filesize(self, target_filesize):
        with Image.open(self.save_path) as im:
            original_filesize = os.path.getsize(self.save_path)
            current_filesize = original_filesize
            quality = 100
            while current_filesize > target_filesize * 1000:
                im.save(self.save_path, quality=quality)
                current_filesize = os.path.getsize(self.save_path)
                quality -= 1
        print(f"Image filesize reduced successfully to {target_filesize} KB")

    def change_image_format(self, format):
        with Image.open(self.save_path) as im:
            # get format of current image
            original_format = im.format
            # check if current format is same as desired format
            if original_format != format:
                im.save(self.save_path, format=format)
                print(f"Image format changed successfully to {format}")

    def rename_image(self, new_name):
        # Get the current format of the image
        current_format = os.path.splitext(self.save_path)[1]
        # Combine the new name and the current format to get the new full path
        new_path = os.path.join(self.current_directory, new_name + current_format)
        # Rename the file
        os.rename(self.save_path, new_path)
        self.save_path = new_path
        print(f"Image renamed successfully to {new_name}{current_format}")

