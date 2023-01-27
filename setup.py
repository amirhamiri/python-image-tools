from setuptools import find_packages, setup

import os, sys

exec(open("image_tools/version.py").read())

github_url = "https://github.com/amirhamiri"
package_name = "python-image-tools"
package_url = "{}/{}".format(github_url, package_name)
package_path = os.path.abspath(os.path.dirname(__file__))
long_description_file_path = os.path.join(package_path, "README.md")
long_description_content_type = "text/markdown"
long_description = ""
try:
    long_description_file_options = (
        {} if sys.version_info[0] < 3 else {"encoding": "utf-8"}
    )
    with open(long_description_file_path, "r", **long_description_file_options) as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name=package_name,
    include_package_data=True,
    version=__version__,
    description="python-image-tools is a python package for working with images",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author="Amirhossein Amiri",
    author_email="amirhamiri74@gmail.com",
    url=package_url,
    packages=find_packages(),
    download_url="{}/archive/{}.tar.gz".format(package_url, __version__),
    project_urls={
        "Documentation": "{}#readme".format(package_url),
        "Issues": "{}/issues".format(package_url),
    },
    keywords=[
        "image",
        "download",
        "python",
        "resize"
    ],
    install_requires=[
        "Pillow==9.4.0", "requests==2.28.2"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Build Tools",
    ],
    license="MIT",
    test_suite="runtests.runtests",
)
