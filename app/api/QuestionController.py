from app.api import QuestionApi
from app.extensions import db, redis_client, auth
from app.utils import RET, EORROR_MAP, sql_add_commit
from app.models import Question, Answer
from flask import request, jsonify, current_app, g


@QuestionApi.route('/', methods=['POST'])
def test_question_api():
    return "DONE"


@QuestionApi.route('/add', methods=["POST"])
@auth.login_required
def post_question():
    body = request.form['body']
    itemId = int(request.form['itemId'])
    userId = g.userId
    if not all([body, itemId, userId]):
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    try:
        question = Question.query.filter(Question.body == body).first()
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    # 避免重复上传问题
    if question:
        return jsonify(code=int(RET.DATAEXIST), msg=EORROR_MAP[RET.DATAEXIST])
    new_question = Question(userId, itemId, body)
    if not sql_add_commit(new_question):
        return jsonify(code=int(RET.DBERR), msg="数据库插入错误")
    return jsonify(code=int(RET.OK), msg=EORROR_MAP[RET.OK])


@QuestionApi.route('/get', methods=['POST'])
@auth.login_required
def get_question():
    itemId = int(request.get_json()['itemId'])
    if not all([itemId]):
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    try:
        questions = Question.query.filter(Question.itemId == itemId)
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    return jsonify(code=int(RET.OK), questions=[x.as_dict() for x in questions])
