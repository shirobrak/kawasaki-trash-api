import json
import re

FILEPATH = './data/GarbageDataBase.csv'
OUTPUTPATH = './data/trash_name.json'


# Sample Json
# {
#     "name": {
#         "value": "アームスタンド",
#         "synonyms": [
#             "モニタースタンド"
#         ]
#     }
# },

# CSV ITEMS
INITIAL = 1
GARBAGE_NAME = 2
READING = 3
SIMILAR_WORDS = 4
RULE = 5
OTHER_RULE = 6
HOW_TO = 7

def add_record(rec):
    # output : record の内容を json のリストにして返す
    tmp_set = set()
    if (rec[GARBAGE_NAME]!=""):
        # （hogehoge）は除外する
        trash_name = re.sub(r'(\(|（).*(\)|）)',"",rec[GARBAGE_NAME])
        
        tmp_set.add(trash_name)
    return tmp_set

trash_dict = dict()
trash_set = set()

with open(FILEPATH, 'r') as f:
    for line in f:
        rec = line.split(',')
        if(rec[0]!='ID'):
            trash_set = trash_set|add_record(rec)

dic_list = []
for trash in trash_set:
    name_dic = dict()
    val_dic = dict()
    if trash!="":
        val_dic['value'] = trash
        name_dic['name'] = val_dic
        dic_list.append(name_dic)

trash_dict["name"] = "TrashName"
trash_dict["values"] = dic_list


with open(OUTPUTPATH, 'w') as f:
    json.dump(trash_dict, f, indent=4, ensure_ascii=False)

