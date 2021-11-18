from app.api import ItemApi
from app.extensions import db, redis_client, auth
from app.utils import RET, EORROR_MAP, allowed_img_format, file_operator, sql_add_commit
from app.models import Item, ImgBox
from flask import request, jsonify, current_app, g


# from ..recommender.Recommend_API import recommender


@ItemApi.route('/', methods=["GET"])
def test_item_api():
    return "DONE"


@ItemApi.route('/post', methods=["POST"])
@auth.login_required
def post_item():
    title = request.form['title']
    description = request.form['description']
    price = float(request.form['price'])
    category = request.form['category']
    userId = g.userId
    new_item = Item(title, price, description, category, userId)
    if not sql_add_commit(new_item):
        return jsonify(code=int(RET.DBERR), msg="数据库插入错误")

    for i in range(1, len(request.files) + 1):
        img = request.files[f'img{i}']
        if not img or not allowed_img_format(img.filename):
            return jsonify(re_code=int(RET.PARAMERR), msg="请上传符合规定的图片")
        url = file_operator.save_img(img)
        new_img = ImgBox(new_item.itemId, url)
        if not sql_add_commit(new_img):
            return jsonify(code=int(RET.DBERR), msg="数据库插入错误")
    return jsonify(code=int(RET.OK), msg="上传成功")


@ItemApi.route('/get', methods=["POST"])
@auth.login_required
def get_page_item():
    data = request.get_json()
    page = data['page']
    page_num = data['page_num']
    items_query = Item.query.paginate(page=page, per_page=page_num).items
    res = []
    for x in items_query:
        imgs_query = ImgBox.query.filter(ImgBox.itemId == x.itemId)
        x = x.as_dict()
        x['imgs'] = []
        for index, img in enumerate(imgs_query):
            x['imgs'].append(img.imgUrl)
        res.append(x)
    length = Item.query.count()
    return jsonify(code=int(RET.OK), items=res, length=length)


@ItemApi.route('/get_item_info', methods=["GET"])
@auth.login_required()
def get_item_info():
    itemId = int(request.args['itemId'])
    try:
        item = Item.query.filter(Item.itemId == itemId).first()
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(code=int(RET.DATAERR), msg="查询数据库失败")
    if not item:
        return jsonify(code=int(RET.NODATA), msg="商品不存在")
    item = item.as_dict()
    item['imgs'] = []
    imgs_query = ImgBox.query.filter(ImgBox.itemId == itemId)
    for index, img in enumerate(imgs_query):
        item['imgs'].append(img.imgUrl)
    return jsonify(code=int(RET.OK), item=item)
