class university:
    def __init__(self, name, local):
        self.departments = []
        self.name = name
        self.local = local


    def list_name(self):
        print(f"- {self.name}")

    def list_departments(self):
        print(f"Departamentos da {self.name}:")
        for department in self.departments:
            print(f"- {department.name}")

    def list_teachers(self, teacher_list):
        print(f"Professores da {self.name}:")
        for teacher in teacher_list:
            print(f"- {teacher.name}")

    def append_deparment(self, department):
        print(f'Adicionando departemaneto {department.name}')
        self.departments.append(department)

    def remove_deparment(self, department):
        print(f'Removendo departemaneto {department.name}')
        self.departments.remove(department)