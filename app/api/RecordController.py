from app.api import RecordApi
from app.extensions import db, redis_client, auth
from app.utils import RET, EORROR_MAP, sql_add_commit
from app.models import Record
from flask import request, jsonify, current_app, g


@RecordApi.route('/', methods=["POST"])
def test_record_api():
    return "DONE"


@RecordApi.route('/add', methods=["POST"])
@auth.login_required
def add_record():
    userId = g.userId
    itemId = request.get_json()['itemId']
    if not all([userId, itemId]):
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    new_record = Record(userId, itemId)
    if not sql_add_commit(new_record):
        return jsonify(code=int(RET.DBERR), msg="数据库插入错误")
    return jsonify(code=int(RET.OK), msg=EORROR_MAP[RET.OK])
