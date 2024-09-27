from Data import DB_session
from Data.Question import question

def create_question(question_text, unit, right_answer_id, is_multi_answer=False):
    db_sess = DB_session.create_session()
    new_question = question(Unit=unit,
                            Question=question_text,
                            id_answer_right=right_answer_id,
                            is_multi=is_multi_answer)
    db_sess.add(new_question)
    db_sess.commit()