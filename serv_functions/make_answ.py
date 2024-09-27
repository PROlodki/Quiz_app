from Data import DB_session
from Data.Answer import answer


def create_answer(answer_text, id_question, is_right=False):
    db_sess = DB_session.create_session()
    new_answer = answer(answer_text=answer_text,
                        id_question=id_question,
                        is_right=is_right)
    db_sess.add(new_answer)
    db_sess.commit()