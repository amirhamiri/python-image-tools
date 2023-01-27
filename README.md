#python-image-tools
The python-image-tools is a python package that allows you to easily download an image from a given URL and manipulate it.

## Installation
- Run `pip install python-image-tools`

### Usage
To use the class, you first need to import it:

```python
from image_tools import ImageDownloader

img = ImageDownloader("https://www.example.com/image.jpg")
```
###Download an Image
To download an image, you can use the `download_image` method:
```python
img.download_image()
```

###Resize an Image
To resize an image, you can use the `resize_image` method, passing in the desired width and height of the image:
```python
img.resize_image(500, 500)
```

###Resize an Image by Percent
To resize an image by a certain percent, you can use the `resize_image_by_percent` method, passing in the desired percent:
```python
img.resize_image_by_percent(50)
```

###Change Image format
To change image format, you can use the `change_image_format` method, passing in the desired format:
```python
img.change_image_format("png")
```

###Reduce Image size
To reduce image size, you can use the `reduce_image_size` method, passing in the desired size in kilobytes:
```python
img.reduce_image_size(50)
```

###Rename Image
To rename image, you can use the `rename_image` method, passing in the desired name:
```python
img.rename_image('test')
```
###Note
- If you want to resize the image to a specific file size, you should first reduce the image file size to your desired file size and then change the image format to a format that supports compression such as JPEG.

- The class will overwrite the original image file, so make sure to save a copy of the original image before using the class.

###Support
If you have any issues or questions, please don't hesitate to reach out to us at amirhamiri74@gmail.com.