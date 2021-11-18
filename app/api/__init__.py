from flask import Blueprint
UserApi = Blueprint('UserApi', __name__, url_prefix="/user")
ItemApi = Blueprint('ItemApi', __name__, url_prefix="/item")
QuestionApi = Blueprint('QuestionApi', __name__, url_prefix="/question")
AnswerApi = Blueprint('AnswerApi', __name__, url_prefix='/answer')
OrderApi = Blueprint('OrderApi', __name__, url_prefix='/order')
RecordApi = Blueprint('RecordApi', __name__, url_prefix="/record")
# 导入需要调用的每一个视图
from . import UserController
from . import ItemController
from . import QuestionController
from . import RecordController
from . import AnswerController
from . import OrderController
