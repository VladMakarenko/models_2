class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return (
            f"Вакансия - {self.title} "
            + f"\nSkills: {self.main_skill_level, self.main_skill}"
        )
