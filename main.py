from classes import university
from classes import department
from classes import teacher
from classes import discipline

def main():
    print("- Universidade -\n")
    university.name = "UEA"
    university.local = "Amazonas"

    print("- Departamentos em faculdade -\n")
    dept1 = "Ciências Exatas"
    dept2 = "Ciências Humanas"
    add_department(dept1)
    add_department(dept2)

    print("- Professores -\n")
    teacher1 = "Marcio Pereira"
    teacher2 = "Mônica Lopes"
    list_names(teacher1, teacher2)
    print(teacher.names_list)

    print("- Disciplinas -\n")
    disc1 = "Fundamentos de Sistemas de Informação"
    disc2 = "Direiro Constitucional"
    add_discipline(disc1, disc2)
    print(discipline.disc_list)

main()


