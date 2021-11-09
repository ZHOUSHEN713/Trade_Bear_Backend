from app.extensions import db
from flask import current_app


def sql_add_commit(data):
    try:
        db.session.add(data)
        db.session.commit()
        return True
    except Exception as e:
        current_app.logger.debug(e)
        db.session.rollback()
        return False
