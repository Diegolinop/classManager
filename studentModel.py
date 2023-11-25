class Student:
    def __init__(self, name, dob, address):
        self.student_name = name
        self.dob = dob
        self.address = address

    def modify_address(self, new_address):
        print(f"\nEndereço de {self.student_name} modificado de '{self.address}' para '{new_address}'")
        self.address = new_address
        
    def __str__(self):
        return f" Name: {self.student_name}, DOB: {self.dob}, Address: {self.address}"