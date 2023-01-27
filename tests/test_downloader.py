import unittest
import os
from PIL import Image
from image_tools import ImageDownloader


class TestImageDownloader(unittest.TestCase):
    def setUp(self):
        # Create an instance of the ImageDownloader class
        self.test_image_url = 'https://i.ytimg.com/vi/4vn40Wdcsmc/maxresdefault.jpg'
        self.image_downloader = ImageDownloader(self.test_image_url)
        self.test_image_name = self.test_image_url.split("/")[-1]
        self.test_image_path = os.path.join(self.image_downloader.current_directory, self.test_image_name)

    def test_download_image(self):
        # Test if the image is downloaded successfully
        self.image_downloader.download_image()
        self.assertTrue(os.path.exists(self.test_image_path))

    def test_resize_image(self):
        # Test if the image is resized successfully
        width = 200
        height = 300
        self.image_downloader.download_image()
        self.image_downloader.resize_image(width, height)
        with Image.open(self.test_image_path) as im:
            self.assertEqual(im.size, (width, height))

    def test_resize_image_by_percent(self):
        # Download the image
        self.image_downloader.download_image()

        # Open the image and save old size
        with Image.open(self.image_downloader.save_path) as im:
            # Check if the image size is equal to the expected size
            old_size = im.size

        # Resize the image
        percent = 50
        self.image_downloader.resize_image_by_percent(percent)
        with Image.open(self.image_downloader.save_path) as im:
            # Check if the image size is equal to the expected size
            self.assertEqual(im.size, (old_size[0] * (percent / 100), old_size[1] * (percent / 100)))

    def test_resize_image_by_filesize(self):
        # Download the image
        self.image_downloader.download_image()
        old_size = os.path.getsize(self.image_downloader.save_path)
        # Resize the image
        new_size = 30
        self.image_downloader.reduce_image_filesize(new_size)

        # Open the image
        with Image.open(self.image_downloader.save_path) as im:
            # Check if the image size is equal to the expected size
            self.assertTrue(old_size > new_size)

    def test_change_image_format(self):
        # Test if the image format is changed successfully
        format = "PNG"
        self.image_downloader.download_image()
        self.image_downloader.change_image_format(format)
        with Image.open(self.test_image_path) as im:
            self.assertEqual(im.format, format)


    def tearDown(self):
        # Delete the tests image
        os.remove(self.test_image_path)


if __name__ == "__main__":
    unittest.main()
