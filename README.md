# Merge .json COCO files
This package is intended for data scientist who wants to merge several COCO datasets before 
training a new model.

## Requirements
`python==3.x`

## Installation

Simply set up a Python environment and type :
```
pip install COCO_merger
```

## COCO Files Merge Usage
```
python -m COCO_merger.merge --src Json1.json Json2.json --out OUTPUT_JSON.json
```

### Argument parser
```
usage: merge.py [-h] --src SRC SRC --out OUT

Merge two annotation files to one file

optional arguments:
  -h, --help     show this help message and exit
  --src SRC SRC  Path of two annotation files to merge
  --out OUT      Path of the output annotation file
```

**Note:**

The script will do the following checks as well:
1. Duplicate filenames checks (to count if the same image has two annotations)
2. Categories checks (Both files should have same categegories (name, id))

The reason I didn't mix categories, incase they are different, is to help annotators identifying any change in there categories. 
I believe this will be helpful incase of annotating a dataset as batches or splitting the annotation on members. Any change in ids caused by software being used or human mistake will be directly identified.
  

Example of Dog category existing in file 2 but not file 1
  
<code>AssertionError: Category name: Dog in file 2 does not exist in file 1</code>


Example of Cat category existing in both files but with different ids:

<code>AssertionError: Category name: Cat, id: 1 in file 1 and 2 in file 2</code>
<br>

<hr>

*Note: the script will do the necessary checks as well (duplicate filenames, ....)*
