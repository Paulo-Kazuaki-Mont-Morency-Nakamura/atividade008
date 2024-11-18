class department:
    def __init__(self, name):
        self.name = name
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Professor {teacher.name} adicionado com sucesso!")

    def list_names(self):
        for teacher in self.teachers:
            print(f"> {teacher.name}, {teacher.age} anos.")

    def remove_teacher(self, teacher_name):
        for teacher in self.teachers:
            if teacher.name == teacher_name:
                self.teachers.remove(teacher)
                print(f"Professor {teacher.name} removido com sucesso!")
            else:
                print(f"Professor {teacher.name} não encontrado.")