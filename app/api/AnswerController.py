from app.api import AnswerApi
from app.extensions import db, redis_client, auth
from app.utils import RET, EORROR_MAP, sql_add_commit
from app.models import Question, Answer
from flask import request, jsonify, current_app, g


@AnswerApi.route('/', methods=['POST'])
def test_answer_api():
    return "DONE"


@AnswerApi.route('/add', methods=['POST'])
@auth.login_required
def answer_question():
    body = request.form['body']
    questionId = request.form['questionId']
    userId = g.userId
    try:
        question = Question.query.filter(Question.questionId == questionId).first()
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    if not question:
        return jsonify(code=int(RET.NODATA), msg="问题不存在")
    new_answer = Answer(userId, questionId, body)
    if not sql_add_commit(new_answer):
        return jsonify(code=int(RET.DBERR), msg="数据库插入错误")
    return jsonify(code=int(RET.OK), msg=EORROR_MAP[RET.OK])


@AnswerApi.route('/get', methods=['POST'])
@auth.login_required
def get_question_answers():
    questionId = int(request.get_json()['questionId'])
    if not all([questionId]):
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    try:
        question = Question.query.filter(Question.questionId == questionId).first()
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    if not question:
        return jsonify(code=int(RET.NODATA), msg="问题不存在")
    res = []
    for x in question.answers:
        res.append(x.as_dict())
    return jsonify(code=int(RET.OK), answers=res)
