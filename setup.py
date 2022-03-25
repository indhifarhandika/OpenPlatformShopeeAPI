from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Open Platform Shopee API'
LONG_DESCRIPTION = 'This API has been provided by Shopee, this project was created to make it easier to use the API features on the Shopee Open Platform.'

# Setting up
setup(
    name="OpenPlatformShopeeAPI",
    version=VERSION,
    author="indhifarhandika",
    author_email="indhifarhandika@gmail.com",
    url="https://github.com/indhifarhandika/OpenPlatformShopeeAPI",
    license="MIT",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api', 'shopee', 'open platform', 'open platform shopee', 'shopee api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)