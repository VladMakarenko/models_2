
from models.ProgClass import b
from models.RecrutClass import a
from models.Vacancy import Vacancy


def main():
    print("Salary recruiter = " + str(a.check_salary(12)))
    print("Salary programmer = " + str(b.check_salary(12)) + "\n")
    print(a.level_salary(1000, 5000))

    print(a.__str__())
    print(b.__str__())

    print(a.work())
    print(b.work())
    qwe = Vacancy("Recruiter", "Adsasd", "asdasd")
    print(qwe.__str__())
    P1 = ("Programmer", "Adsqwdqwdasd", "asqwdqwdasd")
    P2 = Vacancy("Programmer", "A", "ads")
    print(P1.__str__())
    print(P2.__str__())
    candidate1 = Vacancy("123", "Adsasd", "asdasd")
    candidate2 = Vacancy("35", "Adsasd", "asdasd")
    candidate3 = Vacancy("1254", "Adsasd", "asdasd")
    print(candidate1.__str__())
    print(candidate2.__str__())
    print(candidate3.__str__())
    vac1 = Vacancy("1254", "Adsasd", "asdasd")
    vac2 = Vacancy("1254", "Adsasd", "asdasd")
    print(vac1.__str__())
    print(vac2.__str__())


if __name__ == "__main__":
    main()
