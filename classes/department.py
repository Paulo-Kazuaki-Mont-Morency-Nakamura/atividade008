class department:
    def __init__(self, name):
        self.name = name
        self.teachers = []

    def list_name(self):
        print(f"- {self.name}")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def list_teachers(self):
        for teacher in self.teachers:
            print(f"> {teacher.name}, {teacher.age} anos.")

    def remove_teacher(self, teacher_name):
        for teacher in self.teachers:
            if teacher.name == teacher_name:
                self.teachers.remove(teacher)
                print(f"Professor {teacher.name} removido com sucesso!")
            else:
                print(f"Professor {teacher.name} não encontrado.")