import sys
import os
import json
import pickle
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated
def testt(A, qqqq=True, sss=True):
    aa=[]
    for i in A:
        aa.append(i['id'])
    if qqqq:
        print("MAX {}".format(max(aa)))
        print("MIN {}".format(min(aa)))
    if sss:
        return Repeat(aa)
    return aa
def mm_red(a1,aa):
    with open(a1) as json_file:
        d1 = json.load(json_file)
    ind=[]
    res=[]
    k=[]
    ann=[]
    a=d1['categories'].copy()
    print("Initial checks:")
    l1=[i['name'] for i in d1['categories']]
    def chch(aac):
        res=[]
        [res.append(i) for i in aac if i not in res]
        return res
    print("\tPrevious labels: {}".format(l1))
    if any(x not in l1 for x in aa):
        print("\tLabels not found: {}".format([i for i in aa if i not in l1]))
        return {}
    print("\tChecking Images...")
    if len(testt(d1['images'],qqqq=False))!=0:
        print("\t\tImages section error: {} duplicate ids".format(len(testt(d1['images'],qqqq=False))))
        print("\t\t\tChecking for solution...")
        d1['images']=chch(d1['images'])
        if len(testt(d1['images'],qqqq=False))!=0:
            print("\t\t\tImages couldn't fix: {} duplicate id are still present".format(len(testt(d1['images'],qqqq=False))))
            return {}
        print("\t\t\tImages duplicates fixed succesfully!")
    print("\tChecking Annotations...")
    if len(testt(d1['annotations'],qqqq=False))!=0:
        print("\t\tAnnotations section error: {} duplicate ids".format(len(testt(d1['annotations'],qqqq=False))))
        print("\t\t\tChecking for solution...")
        d1['annotations']=chch(d1['annotations'])
        if len(testt(d1['annotations'],qqqq=False))!=0:
            print("\t\t\tAnnotations couldn't fix: {} duplicate id are still present".format(len(testt(d1['annotations'],qqqq=False))))
            return {}
        print("\t\t\tAnnotations duplicates fixed succesfully!")
    print("Stage 1...")
    [ind.append(i) for i, elem in enumerate(a) if any(x in elem.values() for x in aa)]
    ind.sort(reverse=True)
    [k.append(d1['categories'][i]['id']) for i in ind]
    for i in ind: del a[i]
    [ann.append(j) for i, j in enumerate(d1['annotations']) if d1['annotations'][i]['category_id'] not in k]
    print("Stage 2...")
    d1['categories']=a
    res2=[]
    res3=[]
    [res2.append(i['image_id']) for i in ann if i not in res]
    [res3.append(i['file_name']) for i in d1['images'] if i['id'] in res2]
    asd=input('Please enter images filepath to clean or "NA" to return deleted images files as text file ("temp_mm_delete.txt"):')
    if asd!="NA":
        [os.remove[os.path.join(asd,i)] for i in res3]
    else:
        with open("temp_mm_delete.txt", "wb") as fp:
            pickle.dump(res3, fp)
    res3=[]
    [res3.append(i) for i in d1['images'] if i['id'] in res2]
    d1['images']=res3
    print("Annotations Summary: Initial {}  Final {} Removed {}".format(len(d1['annotations']),len(ann),len(d1['annotations']) - len(ann)))
    d1['annotations']=ann
    return d1
if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('2 auguments are need.')
        print('__________________________________________________________________________')
        print('Usage: %s INPUT_JSON.json OUTPU_JSON.json Label1 Label2...'%(sys.argv[0]))
        print('__________________________________________________________________________')
        exit(1)
    jsona = json.dumps(mm_red(sys.argv[1], sys.argv[3:]))
    assert json.dumps({})!='{}'
    print("Saving..")
    with open(sys.argv[2],"w") as f:
        f.write(jsona)
    print("\n\nThanks for using our service :) !!")
