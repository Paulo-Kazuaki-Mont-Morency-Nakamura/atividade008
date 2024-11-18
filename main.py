from classes import university
from classes import department
from classes import teacher
from classes import discipline

def main():
    print("- Universidade -")

    current_university = university.university("UEA", "Amazonas")
    teacher_list = []
    student_list = []
    current_university.list_name()

    print("\n- Departamentos em faculdade -")
    dept1 = department.department("Ciências Exatas")
    dept2 = department.department("Ciências Humanas")
    dept1.list_name()
    dept2.list_name()

    current_university.append_deparment(dept1)
    current_university.append_deparment(dept2)

    print("\n- Professores -")
    teacher1 = teacher.teacher("Marcio Pereira", 33)
    teacher2 = teacher.teacher("Mônica Lopes", 27)
    teacher_list.append(teacher1)
    teacher_list.append(teacher2)

    dept1.add_teacher(teacher1)
    dept2.add_teacher(teacher2)

    current_university.list_teachers(teacher_list)

    print("\n- Disciplinas -")
    disc1 = discipline.discipline("Fundamentos de Sistemas de Informação")
    disc2 = discipline.discipline("Direiro Constitucional")

    teacher1.add_discipline(disc1)
    teacher2.add_discipline(disc2)
    teacher1.list_disciplines()
    teacher2.list_disciplines()

    print("\n- Estudantes -")
    disc1.append_student("Arthur")
    disc1.append_student("Paulo")
    disc1.append_student("Maria")
    disc2.append_student("Yan")
    disc2.append_student("Alexandre")
    disc2.append_student("Elias")

    disc1.list_students()
    disc2.list_students()


main()


