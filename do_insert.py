import json
from models.database import db_session
from models.models import Trash, Category, ThrowRule, Area, Town, CollectionRule
from datetime import datetime

FILEPATH = './data/seeds.json'

def insert_data(key, data_list):
    time = datetime.now()
    if key == 'trashes':
        for data in data_list:
            trash = Trash()
            trash.trash_id = data['trash_id']
            trash.name = data['name']
            trash.reading = data['reading']
            trash.detail = data['detail']
            trash.created_at = time
            trash.updated_at = time
            db_session.add(trash)
            db_session.commit()
    elif key == 'categories':
        for data in data_list:
            category = Category()
            category.category_id = data['category_id']
            category.name = data['name']
            category.created_at = time
            category.updated_at = time
            db_session.add(category)
            db_session.commit()
    elif key == 'towns':
        for data in data_list:
            town = Town()
            town.town_id = data['town_id']
            town.area_id = data['area_id']
            town.name = data['name']
            town.created_at = time
            town.updated_at = time
            db_session.add(town)
            db_session.commit()
    elif key == 'areas':
        for data in data_list:
            area = Area()
            area.area_id = data['area_id'] 
            area.name = data['name']
            area.created_at = time
            area.updated_at = time
            db_session.add(area)
            db_session.commit()
    elif key == 'collection_rules':
        for data in data_list:
            collection_rule = CollectionRule()
            collection_rule.collection_rule_id = data['collection_rule_id']
            collection_rule.town_id = data['town_id']
            collection_rule.category_id = data['category_id']
            collection_rule.data = data['data']
            collection_rule.created_at = time
            collection_rule.updated_at = time
            db_session.add(collection_rule)
            db_session.commit()
    elif key == 'throw_rules':
        for data in data_list:
            throw_rules = ThrowRule()
            throw_rules.throw_rule_id = data['throw_rule_id']
            throw_rules.trash_id = data['trash_id']
            throw_rules.category_id = data['category_id']
            throw_rules.created_at = time
            throw_rules.updated_at = time
            db_session.add(throw_rules)
            db_session.commit()

with open(FILEPATH, 'r') as f:
    data = json.load(f)
    for k, v in data.items():
        insert_data(k, v)

    



