class OneChoiceQuestion:
    """Класс вопроса с одним ответом"""

    def __init__(self, count=0, subquestions=None, answers=None):
        super().__init__()
        self.count = count
        self.question = []
        if subquestions is None:
            self.subquestions = []
        else:
            self.subquestions = subquestions
        if answers is None:
            self.answers = []
        else:
            self.answers = answers



    def addQuestion(self):
        self.count += 1

    def createOneChoiceQuestion(self):
        """Создание вопроса с одним ответом"""
        pass


class ManyChoiceQuestion:
    """Класс вопроса с множественным ответом"""

    def __init__(self, count=0):
        super().__init__()
        self.count = count

    def addQuestion(self):
        self.count += 1

    def createManyChoiceQuestion(self):
        """Создание вопроса с множественным ответом"""
        pass


class ComparisonQuestion:
    """Класс вопроса с сопоставлением"""

    def __init__(self, count=0):
        super().__init__()
        self.count = count

    def addQuestion(self):
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
    print("end")