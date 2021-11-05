from app.api import UserApi


@UserApi.route('/', methods=['GET'])
def test_user_api():
    return "user gone"
