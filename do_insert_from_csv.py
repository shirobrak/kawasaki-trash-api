from models.database import db_session
from models.models import Trash, Category, ThrowRule, Area, Town, CollectionRule
from datetime import datetime

FILEPATH = './data/GarbageDataBase.csv'

# CSV ITEMS
INITIAL = 1
GARBAGE_NAME = 2
READING = 3
SIMILAR_WORDS = 4
RULE = 5
OTHER_RULE = 6
HOW_TO = 7

def add_record(record):

    time = datetime.now()
    
    trash_list = [record[GARBAGE_NAME]]
    if record[SIMILAR_WORDS] != "":
        trash_list.extend(record[SIMILAR_WORDS].split(' '))
    
    if record[OTHER_RULE] != "":
        category_list = [record[RULE], record[OTHER_RULE]]
    else:
        category_list = [record[RULE]]

    for trash_name in trash_list:
        # register trash
        trash = Trash()
        trash.name = trash_name
        trash.detail = record[HOW_TO]
        trash.created_at = time
        trash.updated_at = time
        db_session.add(trash)
        db_session.commit()

        # insert categories and throw_rules
        for category_name in category_list:
            category = db_session.query(Category).filter_by(name=category_name).first()
            if(category is None):
                category = Category()
                category.name = category_name
                category.created_at = time
                category.updated_at = time
                db_session.add(category)
                db_session.commit()
        
            throw_rule = ThrowRule()
            throw_rule.trash_id = trash.trash_id
            throw_rule.category_id = category.category_id
            throw_rule.created_at = time
            throw_rule.updated_at = time
            db_session.add(throw_rule)
            db_session.commit()
            

with open(FILEPATH, 'r') as f:
    for line in f:
        rec = line.split(',')
        if(rec[0]!='ID'):
            add_record(rec)