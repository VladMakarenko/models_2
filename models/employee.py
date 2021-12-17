from datetime import date, datetime
import numpy as np


class Employee:
    def __init__(self, first_name, last_name, email, phone, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.salary = salary

    @staticmethod
    def work():
        return "I come to the office"

    def check_salary(self, month):
        d1 = date(2021, month, 1)
        d2 = datetime.now()
        work_day = np.busday_count(d1.strftime("%Y-%m-%d"), d2.strftime("%Y-%m-%d"))
        work_day = work_day + 1
        salary_day = self.salary * work_day
        return salary_day

    def level_salary(self, salary_recruiter, salary_programmer):

        if salary_recruiter < salary_programmer:
            return "a programmer with a higher salary\n"
        else:
            return "a recruiter with a higher salary\n"
