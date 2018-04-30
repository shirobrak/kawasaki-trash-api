from flask import Flask, request, jsonify
from models.database import db_session
from models.models import Trash, Category, ThrowRule, Area, Town, CollectionRule

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello():
    return "kawasaki-trash-api"

@app.route('/api/v1/throw_rule', methods=['GET'])
def throw_rule():
    response = dict()
    if 'trash_name' in request.args:
        try:
            trash = db_session.query(Trash).filter(Trash.name==request.args['trash_name']).first()
            categories = []
            for rule in trash.throw_rules:
                tmp = dict()
                tmp['id'] = rule.category.category_id
                tmp['name'] = rule.category.name
                categories.append(tmp)
            rule = dict()
            rule['categories'] = categories
            rule['detail'] = trash.detail
            response["rule"] = [rule]
            response["code"] = 200
        except:
            response = error_message(400)
    else:
        response = error_message(400)
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
