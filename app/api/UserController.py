from app.api import UserApi
from app.extensions import db
from app.utils import RET, EORROR_MAP
from app.models import User
from flask import request, jsonify, current_app
import re


@UserApi.route('/', methods=['GET'])
def test_user_api():
    return "user gone"


@UserApi.route('/register', methods=['POST'])
def user_register():
    request_data = request.get_json()
    userName = request_data['userName']
    password = request_data['password']
    email = request_data['email']
    gender = int(request_data['gender'])
    region = str(request_data['region'])
    if not all([userName, password, email, gender, region]):
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    if not re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', email):
        return jsonify(re_code=int(RET.PARAMERR), msg='请填写正确的邮箱')
    try:
        user = User.query.filter(User.email == email).first()
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    if user:
        return jsonify(code=int(RET.DATAEXIST), msg=EORROR_MAP[RET.DATAEXIST])
    new_user = User(userName, password, email, gender, region)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        current_app.logger.debug(e)
        db.session.rollback()
        return jsonify(code=int(RET.DBERR), msg="数据库插入错误")
    return jsonify(code=int(RET.OK), msg=EORROR_MAP[RET.OK])


@UserApi.route('/login', methods=['POST'])
def user_login():
    request_data = request.get_json()
    userName = request_data['userName']
    password = request_data['password']
    if not all([userName, password]):
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    try:
        user = User.query.filter(User.userName == userName).first()
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    if not user:
        return jsonify(code=int(RET.NODATA), msg="用户不存在")
    if user.password == password:
        return jsonify(code=int(RET.OK), msg=EORROR_MAP[RET.OK])
    else:
        return jsonify(code=int(RET.PWDERR), msg=EORROR_MAP[RET.PWDERR])
