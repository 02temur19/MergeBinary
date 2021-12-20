from merge_sort import mergeSort
from Binary_search import binary_search
import json
from dict_to_json import dict_to_json


def getList(dict):
    list = []
    for key in dict.keys():
        list.append(int(key))

    return list



#with list1
with open('name.json') as json_file:
    data = json.load(json_file)

list1 = getList(data)
n = len(list1)
mergeSort(list1, 0, n-1)

#with list2
with open('name1.json') as json_file:
    data1 = json.load(json_file)
list2 = getList(data1)


data2 = {}

for k in list2:
    if binary_search(list1, 0, n-1, k) != -1:
        data2[str(k)] = data[str(k)]

dict_to_json(data2)
