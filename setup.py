import os

import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()

setuptools.setup(
    name="COCO_merger",
    version="0.0.2",
    author="Mohamad Mansour & Tristan Cotte",
    author_email="moemansour03@gmail.com",
    description="Python package which aims to merge 2 COCO .json files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohamadmansourX/Merge_COCO_FILES",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
