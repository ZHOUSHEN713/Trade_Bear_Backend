from app.api import OrderApi
from app.extensions import db, redis_client, auth
from app.utils import RET, EORROR_MAP, sql_add_commit
from app.models import Order, Item
from flask import request, jsonify, current_app, g


@OrderApi.route('/', methods=['POST'])
def test_order_api():
    return "DONE"


@OrderApi.route('/add', methods=['POST'])
@auth.login_required
def add_order():
    request_data = request.get_json()
    buyerId = g.userId
    sellerId = request_data['sellerId']
    itemId = request_data['itemId']
    if not all([buyerId, sellerId, itemId]):
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    try:
        order = Order.query.filter(Order.buyerId == buyerId, Order.sellerId == sellerId, Order.itemId == itemId).first()
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    if order:
        return jsonify(code=int(RET.DATAEXIST), msg=EORROR_MAP[RET.DATAEXIST])
    new_order = Order(buyerId, sellerId, itemId)
    if not sql_add_commit(new_order):
        return jsonify(code=int(RET.DBERR), msg="数据库插入错误")
    return jsonify(code=int(RET.OK), msg=EORROR_MAP[RET.OK])


@OrderApi.route('/get_by_buyerId', methods=['POST'])
@auth.login_required
def get_order_by_buyer():
    # 查看用户购买的商品
    buyerId = g.userId
    if not buyerId:
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    try:
        orders = Order.query.filter(Order.buyerId == buyerId)
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    return jsonify(code=int(RET.OK), orders=[x.as_dict() for x in orders])


@OrderApi.route('/get_by_sellerId', methods=['POST'])
@auth.login_required
def get_order_by_seller():
    # 查看用户卖出的商品
    sellerId = g.userId
    if not sellerId:
        return jsonify(code=int(RET.PARAMERR), msg=EORROR_MAP[RET.PARAMERR])
    try:
        orders = Order.query.filter(Order.sellerId == sellerId)
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    return jsonify(code=int(RET.OK), orders=[x.as_dict() for x in orders])
