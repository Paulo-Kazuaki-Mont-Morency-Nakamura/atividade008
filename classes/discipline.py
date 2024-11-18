class discipline:
    def __init__(self, name):
        self.name = name
        self.students = []

    def append_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        if name in self.students:
            self.students.remove(name)
        else:
            print(f"Estudante {name} não encontrado.")

    def list_students(self):
        print(f"Estudantes de {self.name}:")

        for student in self.students:
            print(f"- {student}")