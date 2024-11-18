class department(university):
    def __init__(self):
        self.list = {
            'Ciências Biológicas',
            'Ciências Humanas',
            'Ciências Exatas'
        }

        def add_department(dept_name):
            self.list.add(dept_name)
            print(f"Departamento {dept_name} adicionado com sucesso!")

        def remove_department(dept_name):
            if dpet_name in self.list:
                self.list.remove(dept_name)
            else:
                print("Departamento não encontrado.")

        def list_departments():
            return self.list

        self.teacher = []
