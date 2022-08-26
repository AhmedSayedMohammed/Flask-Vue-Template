import uuid

import sqlalchemy
from flask import render_template, Blueprint, request, jsonify
from pip._internal.locations import user_site

from DbConnection import conn

user = Blueprint('User', __name__)


@user.route('/', methods=['GET'])
def get_users():
    query = sqlalchemy.text("Select * from users")
    users = conn.execute(query)
    users_dict = [
        {
            "id": u[0],
            "name": u[1],
        }
        for u in users
    ]

    return jsonify(users_dict)


@user.route('/add', methods=['POST'])
def add_user():
    post_data = request.get_json()
    query = sqlalchemy.text("insert into users(name) values(:name)")
    conn.execute(query, name=post_data.get('name'))
    return "success"


@user.route('/update/<user_id>', methods=['PUT'])
def update_user(user_id):
    post_data = request.get_json()
    name = post_data.get('name')
    _id = user_id
    query = sqlalchemy.text("update users set name=:name where id=:id ")
    conn.execute(query, name=name, id=_id)
    return "success"


@user.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    _id = user_id
    query = sqlalchemy.text("delete from  users where id=:id ")
    conn.execute(query, id=_id)
    return "success"
