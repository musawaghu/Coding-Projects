class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, actual_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.actual_answer = actual_answer

    def __str__(self):
        return "This is the question: " + str(
            self.question) + "\n" + "These are the four possible answers: " + "\n1)" + str(self.answer1) + "\n2)" + str(
            self.answer2) + "\n3)" + str(self.answer3) + "\n4)" + str(self.answer4)

    def guess(self, answer_int):
        if self.actual_answer == answer_int:
            return True
        else:
            return False
