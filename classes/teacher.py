class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.discipline_list = []
        self.names_list = []


    def add_discipline(self, discipline):
        self.discipline_list.append(discipline)

    def list_disciplines(self):
        print(f"Lista de disciplinas de {self.name}")
        for discipline in self.discipline_list:
            print(f"- {discipline.name}")

    def list_names(self, name):
        self.names_list.append(name)

    def remove_teacher(self, teacher_name):
        if teacher_name in self.names_list:
            self.names_list.remove(teacher_name)
        else:
            print("Professor não encontrado.")