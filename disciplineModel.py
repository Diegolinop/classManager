class Discipline:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        print(f"\nAluno {student.student_name} adicionado em {self.name}!")
        self.students.append(student)
        
    def remove_student(self, student):
        print(f"\nAluno {student.student_name} removido de {self.name}!")
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"{student.student_name} não está em {self.name}")
    
    def list_students(self):
        print(f"\nLista de Alunos de {self.name}")
        for student in self.students:
            print(student)