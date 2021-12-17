from models.employee import Employee


class Recruiter(Employee):
    position = "Recruiter"
    hired_this_month = ""

    def __str__(self):
        return f"{self.position}:" + f" {self.first_name} {self.last_name}"

    @staticmethod
    def work():
        return "I come to the office and start hiring"


a = Recruiter("Ivanov", "Ivan", "asd@gmail", "911", 1000)
