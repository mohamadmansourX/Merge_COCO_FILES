import sys
import os
import json
from tqdm import tqdm

def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same

def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated
def testt(A):
    aa=[]
    for i in A:
      aa.append(i['id'])
    print("MAX {}".format(max(aa)))
    print("MIN {}".format(min(aa)))
    return Repeat(aa)


def combine(tt1,tt2,output_file):
    """ Combine two COCO annoatated files and save them into new file
    :param tt1: 1st COCO file path
    :param tt2: 2nd COCO file path
    :param output_file: output file path
    """
    with open(tt1) as json_file:
        d1 = json.load(json_file)
    with open(tt2) as json_file:
        d2 = json.load(json_file)
    b1={}
    for i,j in enumerate(d1['images']):
        b1[d1['images'][i]['id']]=i

    temp=[cc['file_name'] for cc in d1['images']]
    temp2=[cc['file_name'] for cc in d2['images']]
    for i in temp:
        assert not(i in temp2), "Duplicate filenames detected between the two files! @" + i
        
    files_check_classes={}
    for i,j in enumerate(d1['images']):
        for ii,jj in enumerate(d1['annotations']):
            if jj['image_id']==j['id']:
                try:
                    files_check_classes[j['file_name']].append(jj['category_id'])
                except:
                    files_check_classes[j['file_name']]=[jj['category_id']]

    for i,j in enumerate(d2['images']):
        for ii,jj in enumerate(d2['annotations']):
            if jj['image_id']==j['id']:
                try:
                    files_check_classes[j['file_name']].append(jj['category_id'])
                except:
                    files_check_classes[j['file_name']]=[jj['category_id']]

    b2={}
    for i,j in enumerate(d2['images']):
        b2[d2['images'][i]['id']]=i+max(b1)+1
        
    #Reset File 1 and 2 images ids
    for i,j in enumerate(d1['images']):
        d1['images'][i]['id']= b1[d1['images'][i]['id']]
    for i,j in enumerate(d2['images']):
        d2['images'][i]['id']= b2[d2['images'][i]['id']]
        
    #Reset File 1 and 2 annotations ids
    b3={}
    for i,j in enumerate(d1['annotations']):
        b3[d1['annotations'][i]['id']]=i
    b4={}
    for i,j in enumerate(d2['annotations']):
        b4[d2['annotations'][i]['id']]=max(b3)+i+1




    for i,j in enumerate(d1['annotations']):
        d1['annotations'][i]['id']= b3[d1['annotations'][i]['id']]
        d1['annotations'][i]['image_id']=b1[d1['annotations'][i]['image_id']]
    for i,j in enumerate(d2['annotations']):
        d2['annotations'][i]['id']= b4[d2['annotations'][i]['id']]
        d2['annotations'][i]['image_id']=b2[d2['annotations'][i]['image_id']]

    files_check_classes_temp={}
    pbar = tqdm(total=len(d1['images'])+len(d2['images']))
    for i,j in enumerate(d1['images']):
        for ii,jj in enumerate(d1['annotations']):
            if jj['image_id']==j['id']:
                try:
                    files_check_classes_temp[j['file_name']].append(jj['category_id'])
                except:
                    pbar.update(1)
                    files_check_classes_temp[j['file_name']]=[jj['category_id']]


    for i,j in enumerate(d2['images']):
        for ii,jj in enumerate(d2['annotations']):
            if jj['image_id']==j['id']:
                try:
                    files_check_classes_temp[j['file_name']].append(jj['category_id'])
                except:
                    pbar.update(1)
                    files_check_classes_temp[j['file_name']]=[jj['category_id']]
    pbar.close()
    added, removed, modified, same = dict_compare(files_check_classes, files_check_classes_temp)
    assert (len(added)==0 and len(removed)==0 and len(modified)==0),"filenames detected before merging error: "+len(added)+" filenames added "+ len(removed)+" filenames removed "+len(modified)+" filenames' classes modified "+ len(same)+ " filenames entries reserved"

    test=d1.copy()
    for i in d2['images']:
        test['images'].append(i)
    for i in d2['annotations']:
        test['annotations'].append(i)
    for curr_cat in d2['categories'] :
            if curr_cat not in test['categories'] :
                test['categories'].append(curr_cat)
    files_check_classes_temp={}
    pbar = tqdm(total=len(test['images']))
    for i,j in enumerate(test['images']):
        for ii,jj in enumerate(test['annotations']):
            if jj['image_id']==j['id']:
                try:
                    files_check_classes_temp[j['file_name']].append(jj['category_id'])
                except:
                    pbar.update(1)
                    files_check_classes_temp[j['file_name']]=[jj['category_id']]

    pbar.close()
    added, removed, modified, same = dict_compare(files_check_classes, files_check_classes_temp)
    assert (len(added)==0 and len(removed)==0 and len(modified)==0),"filenames detected after merging error: "+len(added)+" filenames added "+ len(removed)+" filenames removed "+len(modified)+" filenames' classes modified "+ len(same)+ " filenames entries reserved"

    with open(output_file, 'w') as f:
        json.dump(test,f)


if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print('3 arguments are need.')
        print('Usage: %s json1.json json2.json OUTPU_JSON.json'%(sys.argv[0]))
        exit(1)
    combine(sys.argv[1],sys.argv[2],sys.argv[3])
    print("\n\nThanks for using our service :p !!")
