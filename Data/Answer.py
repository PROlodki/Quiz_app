import sqlalchemy
from .DB_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class answer(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'question'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    answer = sqlalchemy.Column(sqlalchemy.String)
    id_question = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Question.id"))
    is_right = sqlalchemy.Column(sqlalchemy.Boolean, default=False)