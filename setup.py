import setuptools #library, which helps in packaging Python projects so they can be easily distributed.
#It's commonly used to build and install Python packages.

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

""" 
with open(...) as f:: This opens the README.md file in read mode ("r"), specifying the encoding as UTF-8.
The with statement ensures the file is closed properly after reading.
f.read(): Reads the entire content of the file and stores it in the long_description variable.
This will be used later to provide a detailed description of the project for the package.
"""

__version__ = "0.0.0" #This defines the version of the package.

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "Vijay Sonavane"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "vijaysonawane0001@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)