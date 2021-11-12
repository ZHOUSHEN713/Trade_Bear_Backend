from flask import Blueprint
UserApi = Blueprint('UserApi', __name__, url_prefix="/user")
ItemApi = Blueprint('ItemApi', __name__, url_prefix="/item")
# 导入需要调用的每一个视图
from . import UserController
from . import ItemController
