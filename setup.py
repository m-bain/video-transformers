import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="video-transformers",
    version="0.0.1",
    author="m-bain",
    author_email="maxbain@robots.ox.ac.uk",
    description="pytorch implementations of video transformers",
    long_description=long_description,
    url="https://github.com/m-bain/video-transformers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)