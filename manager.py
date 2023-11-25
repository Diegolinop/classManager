from disciplineModel import Discipline
from studentModel import Student

class manager:    
    dic_students = {
        1: Student("Diego Pimenta Suárez", "08-10-2006", "Rua João Paulo, 87"),
        2: Student("Rafael Cunha", "04-04-1999", "Avenida Almirante Pedro, 120"),
        3: Student("João Pedro", "24-02-2008", "Rua Emiliano Martinez, 23")
    }
    dic_disciplines = {
        1: Discipline("Matemática"),
        2: Discipline("Português")
    }
    
    def list_students(students):
        print("\nLista de Alunos: ")
        for student_id, student_obj in students.items():
            print(f"{student_id}:{student_obj}")
    
    list_students(dic_students)
    
    Student.modify_address(dic_students[1], "Avenida Jorge Algusto, 99")
    
    print(f"{dic_students[1]}")
    
    dic_disciplines[1].add_student(dic_students[1])
    dic_disciplines[1].add_student(dic_students[2])
    dic_disciplines[1].add_student(dic_students[3])
    
    dic_disciplines[2].add_student(dic_students[3])
    dic_disciplines[2].add_student(dic_students[1])
    
    dic_disciplines[1].list_students()
    dic_disciplines[2].list_students()
    
    dic_disciplines[1].remove_student(dic_students[1])
    dic_disciplines[1].list_students()
    dic_disciplines[1].add_student(dic_students[1])
    dic_disciplines[1].list_students()