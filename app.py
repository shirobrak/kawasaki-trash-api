from flask import Flask, request, jsonify, render_template
from models.database import db_session
from models.models import Trash, Category, ThrowRule, Area, Town, CollectionRule

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/v1/trashes/<trash_name>/categories', methods=['GET'])
def throw_rule(trash_name):
    response = dict()
    try:
        trash = db_session.query(Trash).filter(Trash.name==trash_name).first()
        categories = []
        for rule in trash.throw_rules:
            tmp = dict()
            tmp['id'] = rule.category.category_id
            tmp['name'] = rule.category.name
            categories.append(tmp)
        
        rule = dict()
        rule['categories'] = categories
        rule['detail'] = trash.detail
        response["rule"] = rule
        response["code"] = 200
    except:
        response = error_message(204)
    return jsonify(response)

@app.route('/api/v2/trashes/<trash_name>/categories', methods=['GET'])
def get_rule(trash_name):
    response = dict()
    try:
        # full match 
        trashes = db_session.query(Trash).filter(Trash.name==trash_name)
        if trashes.count()!=1:
            search_name = '%' + trash_name  # 後方一致
            trashes = db_session.query(Trash).filter(Trash.name.like(search_name))
        if trashes.count()>=1:
            trash_list = []
            for trash in trashes:
                trash_dic = dict()
                trash_dic["trash_name"] = trash.name
                categories = []
                for rule in trash.throw_rules:
                    rule_dic = dict()
                    rule_dic['id'] = rule.category.category_id
                    rule_dic['category_name'] = rule.category.name
                    categories.append(rule_dic)
                trash_dic["categories"] = categories
                trash_dic["detail"] = trash.detail
                trash_list.append(trash_dic)          
            response["result"] = trash_list
            response["code"] = 200
        else:
            response = error_message(204)
    except:
        response = error_message(204)
    return jsonify(response)

@app.errorhandler(400)
def page_not_found(e):
    response = error_message(400)
    return jsonify(response)

@app.errorhandler(404)
def page_not_found(e):
    response = error_message(404)
    return jsonify(response)

def error_message(code):
    error = dict()
    error['code'] = code
    if code == 204:
        message = "No Content"
    elif code == 400:
        message = "Bad Request"
    elif code == 404:
        message = "Not Found"
    else:
        message = "Invalid Status Code"
    error['message'] = message
    return error

if __name__=='__main__':
    app.run()
