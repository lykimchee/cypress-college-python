class Question:
    def __init__(self, question, a1, a2, a3, a4, answer):
        self._question = question
        self._a1 = a1
        self._a2 = a2
        self._a3 = a3
        self._a4 = a4
        self._answer = answer

    def __str__(self):
        result = self._question + "\n"
        result += "1. " + self._a1 + "\n"
        result += "2. " + self._a2 + "\n"
        result += "3. " + self._a3 + "\n"
        result += "4. " + self._a4 + "\n"
        return result

    def guess(self, user_answer):
        if user_answer == self._answer:
            return True
        return False

    def answer_string(self):
        if self._answer == 1:
            return self._a1
        elif self._answer == 2:
            return self._a2
        elif self._answer == 3:
            return self._a3
        return self._a4
