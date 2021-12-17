from models.employee import Employee


class Programmer(Employee):
    position = "Programmer"
    tech_stack = ""
    closed_this_month = ""

    def __str__(self):
        return f"{self.position}:" + f" {self.first_name} {self.last_name}\n"

    @staticmethod
    def work():
        return "I come to the office and start coding"


b = Programmer("Petrov", "Petr", "adasdasda@gmail", "102", 5000)
