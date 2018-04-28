import json
from models.database import db_session
from models.models import Trash, Category, ThrowRule, Area, Town, CollectionRule
from datetime import datetime

BASEPATH = './data/backup/'

data = dict()

def convert_rec2dic(records):
    arr = []
    for record in records:
        tmp = dict()
        for k,v in record.__dict__.items():
            if k != '_sa_instance_state':
                tmp[k] = v
        arr.append(tmp)
    
    return arr

trashes = db_session.query(Trash).all()
categories = db_session.query(Category).all()
throw_rules = db_session.query(ThrowRule).all()
areas = db_session.query(Area).all()
towns = db_session.query(Town).all()
collection_rules = db_session.query(CollectionRule).all()

data['trashes'] = convert_rec2dic(trashes)
data['categories'] = convert_rec2dic(categories)
data['throw_rules'] = convert_rec2dic(throw_rules)
data['areas'] = convert_rec2dic(areas)
data['town'] = convert_rec2dic(towns)
data['collection_rules'] = convert_rec2dic(collection_rules)

time = datetime.now().strftime("%Y%m%d%H%M%S")
output_path = BASEPATH + time + '.json'

with open(output_path, 'w') as f:
    json.dump(data, f, indent=2, sort_keys=False, ensure_ascii=False)
