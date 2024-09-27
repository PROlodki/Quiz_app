from Data.Question import question
from Data.Answer import answer
from Data import DB_session



def get_question_data(effictive_question_id, return_sess=False):
    db_sess = DB_session.create_session()
    current_question = db_sess.query(question).filter(question.id == effictive_question_id).first()
    if return_sess:
        return current_question, db_sess
    return current_question

def get_answer_data(effictive_answer_id, return_sess=False):
    db_sess = DB_session.create_session()
    current_answer = db_sess.query(answer).filter(answer.id == effictive_answer_id).first()
    if return_sess:
        return current_answer, db_sess
    return current_answer