class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.discipline_list = []


    def add_discipline(self, discipline):
        self.discipline_list.append(discipline)

    def list_disciplines(self):
        print(f"Lista de disciplinas de {self.name}")
        for discipline in self.discipline_list:
            print(f"- {discipline.name}")

    def remove_discipline(self, discipline_name):
        if discipline_name in self.discipline_list:
            self.discipline_list.remove(discipline_name)
        else:
            print(f"Disciplina {discipline_name} não encontrado.")