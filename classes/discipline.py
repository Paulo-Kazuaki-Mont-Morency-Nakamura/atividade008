class discipline:
    def __init__(self):
        self.disc_list = []

        def add_disc(disc_name):
            self.disc_list.append(disc_name)
            print(f"Disciplina {disc_name} adicionado com sucesso!")

        def remove_discipline(disc_name):
            if disc_name in self.disc_list:
                self.list.remove(dept_name)
            else:
                print("Disciplina não encontrado.")