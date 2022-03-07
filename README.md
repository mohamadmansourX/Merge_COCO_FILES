# Merge_COCO_FILES

Simple yet fully working tool

## Requirments
`python==3.x`

## Installation
```
Simply:
1- git clone https://github.com/mohamadmansourX/Merge_COCO_FILES.git
2- cd Merge_COCO_FILES
```

## COCO Files Merge Usage
```
python merge.py Json1.json Json2.json OUTPU_JSON.json
```

Json1 and Json2 are the two COCO files to be merged.

OUTPU_JSON is the output file for the combined results

<br>

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

## COCO File Class Edit Usage

```
python INPUT_JSON.json OUTPU_JSON.json Label1 Label2...
```

*Note: the script will do the necessary checks as well (duplicate filenames, ....)*
