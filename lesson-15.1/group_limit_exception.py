class GroupLimitError(Exception):
    def __init__(self, message="Group limit reached (maximum 10 students)"):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'


if __name__ == "__main__":
    gr = Group('PD1')

    for i in range(10):
        student = Student('Male', 18 + i, f'Name{i}', f'LastName{i}', f'AN{100 + i}')
        gr.add_student(student)

    print(gr)
    print(f"Number of students in group: {len(gr.group)}")

    extra_student = Student('Female', 20, 'Liza', 'Taylor', 'AN145')

    try:
        gr.add_student(extra_student)
    except GroupLimitError as e:
        print(f"Error: {e}")

    print("OK") 