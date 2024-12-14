class ChoiceQuestion:
    """Класс вопроса с одним ответом"""

    def __init__(self, count=1, subquestions=None, answers=None):

        super().__init__()
        self.count = count
        self.question = []
        self.questionIsOne = True

        if subquestions is None:
            self.subquestions = []
        elif len(subquestions) == 1:
            self.subquestions = subquestions
        else:
            print("Только один вопрос доступен!")

        if answers is None:
            self.answers = []
        else:
            self.answers = answers

    '''
    def addQuestion(self, quest):

        if self.questionIsOne:
            self.subquestions = quest
            self.questionIsOne = False
        else:
            print("Только один вопрос доступен!")

    def addAnsver(self, ansv):

        self.answers.append(ansv)

    def createChoiceQuestion(self):
        if self.count == 1:
            """Создание вопроса с одним ответом"""
            self.question.append(self.subquestions)
            self.question.append(self.answers)
            self.question.append("single")
        else:
            self.question.append(self.subquestions)
            self.question.append(self.answers)
            self.question.append("multiple")

    Check last commit in DB-moduls branch, we don't need this part
    Delete this part and others where we use it
    '''

    def show(self):
        print(self.question[0][0])
        for i in range(len(self.answers)):
            print(f"{i + 1}) {self.answers[i]}")


class ComparisonQuestion:
    """Класс вопроса с сопоставлением"""

    def __init__(self, count=0, subquestions=None, answers=None):

        super().__init__()
        self.count = count
        self.question = []
        self.questionIsOne = True

        if subquestions is None:
            self.subquestions = []
        else:
            self.subquestions = subquestions

        if answers is None:
            self.answers = []
        else:
            self.answers = answers

    def addSubquestion(self):
        self.count += 1

    def createComparisonQuestion(self):
        """Создание вопроса с сопоставлением"""
        pass


class TestCreator:
    """Класс создания вопросов теста"""

    def __init__(self, types, variants=1):
        super().__init__()
        self.types = types
        self.questions = []
        self.totalQuestions = 0
        self.variants = variants

    def createQuestion(self):
        if self.types == "1":
            """Вопрос с одним ответом"""
            self.questions[self.totalQuestions] = OneChoiceQuestion(self.variants)
            self.totalQuestions += 1

        elif self.types == "2":
            """Вопрос с множественным ответом"""
            self.questions[self.totalQuestions] = ManyChoiceQuestion(self.variants)
            self.totalQuestions += 1

        elif self.types == "3":
            """Вопрос с сопоставлением вариантов"""
            self.questions[self.totalQuestions] = ComparisonQuestion(self.variants)
            self.totalQuestions += 1


if __name__ == '__main__':
    q = ChoiceQuestion(1, ["WHY?"], ["Yes", "No", "Because"])
    q.createChoiceQuestion()
    # a.show()
    going = True
    while (going):
        print("--------------")
        print("-----QuiZ-----")
        print("--------------")
        q.show()
        a = []
        for item in input().split():
            a.append(item)
        print(a)

    print("end")