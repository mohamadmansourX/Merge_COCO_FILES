import sys
import os
import json


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
def mm_combo(tt1,tt2):
  with open(tt1) as json_file:
      d1 = json.load(json_file)

  with open(tt2) as json_file:
      d2 = json.load(json_file)
  b1={}
  for i,j in enumerate(d1['images']):
    b1[d1['images'][i]['id']]=i
  print('\n\n_________________STEP1_________________________')
  print("b1:")
  print(min(list(b1.values())))
  print(max(list(b1.values())))
  print(Repeat(list(b1.values())))
  print(Repeat(list(b1.keys())))
  b2={}
  for i,j in enumerate(d2['images']):
    b2[d2['images'][i]['id']]=i+max(b1)
  print("b2:")
  print(min(list(b2.values())))
  print(max(list(b2.values())))
  print(Repeat(list(b2.values())))
  print(Repeat(list(b2.keys())))


  for i,j in enumerate(d1['images']):
    d1['images'][i]['id']= b1[d1['images'][i]['id']]

  for i,j in enumerate(d2['images']):
    d2['images'][i]['id']= b2[d2['images'][i]['id']]


  print("b3:")
  b3={}
  for i,j in enumerate(d1['annotations']):
    b3[d1['annotations'][i]['id']]=i
  print(min(list(b3.values())))
  print(max(list(b3.values())))
  print(Repeat(list(b3.values())))
  print(Repeat(list(b3.keys())))

  print("b4:")
  b4={}
  for i,j in enumerate(d2['annotations']):
    b4[d2['annotations'][i]['id']]=max(b3)+i
  print(min(list(b4.values())))
  print(max(list(b4.values())))
  print(Repeat(list(b4.values())))
  print(Repeat(list(b4.keys())))

  for i,j in enumerate(d1['annotations']):
      d1['annotations'][i]['id']= b3[d1['annotations'][i]['id']]
      d1['annotations'][i]['image_id']=b1[d1['annotations'][i]['image_id']]
  for i,j in enumerate(d2['annotations']):
      d2['annotations'][i]['id']= b4[d2['annotations'][i]['id']]
      d2['annotations'][i]['image_id']=b2[d2['annotations'][i]['image_id']]

  print('\n\n_________________STEP2_________________________')
  print('d1_i')
  testt(d1['images'])

  print('d2_i')
  testt(d2['images'])

  print('\n\nd1_a')
  testt(d1['annotations'])

  print('d2_a')
  testt(d2['annotations'])


  test=d1.copy()

  for i in d2['images']:
    test['images'].append(i)
  for i in d2['annotations']:
    test['annotations'].append(i)


  print('\n\n_________________STEP3_________________________')
  print("t_a")
  testt(test['annotations'])

  print("t_i")
  testt(test['images'])
  return test

if __name__ == '__main__':
  if len(sys.argv) <= 3:
    print('3 auguments are need.')
    print('Usage: %s json1.json json2.json OUTPU_JSON.json'%(sys.argv[0]))
    exit(1)
  jsona = json.dumps(mm_combo(sys.argv[1], sys.argv[2]))
  f = open(sys.argv[3],"w")
  f.write(jsona)
  f.close()
  print("\n\nThanks for using our service :) !!")
