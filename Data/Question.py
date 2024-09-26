import sqlalchemy
from .DB_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Question(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'Answers'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    Unit = sqlalchemy.Column(sqlalchemy.String)
    Question = sqlalchemy.Column(sqlalchemy.String)
    id_answer_right = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Answers.id"))