class University:
    def __init__(self, name):
        self.name = name
        self.classes = []  # List of Class objects
        self.humans = []   # List of Human objects (students and teachers)

    def add_class(self, class_obj):
        self.classes.append(class_obj)

    def add_human(self, human_obj):
        self.humans.append(human_obj)

    def display_info(self):
        print(f"\nUniversity: {self.name}")
        print("Classes Offered:")
        for cls in self.classes:
            print(f" - {cls.name}, taught by {cls.teacher.name}, Timings: {cls.timings}")
            for section in cls.sections:
                print(f"   Section: {section.section_name}, Timings: {section.timings}, Teacher: {section.teacher.name}")

class Class:
    def __init__(self, name, timings, teacher):
        self.name = name
        self.timings = timings
        self.teacher = teacher
        self.sections = []

    def add_section(self, section_obj):
        self.sections.append(section_obj)

class Human:
    def __init__(self, name, human_id, contact):
        self.name = name
        self.human_id = human_id
        self.contact = contact

class Teacher(Human):
    def __init__(self, name, human_id, contact, subjects):
        super().__init__(name, human_id, contact)
        self.subjects = subjects
        self.classes = []

    def assign_class(self, class_obj):
        self.classes.append(class_obj)

class Student(Human):
    def __init__(self, name, human_id, contact, major):
        super().__init__(name, human_id, contact)
        self.major = major
        self.classes = []

    def enroll_class(self, class_obj):
        self.classes.append(class_obj)

class Section:
    def __init__(self, section_name, timings, teacher):
        self.section_name = section_name
        self.timings = timings
        self.teacher = teacher
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

def main():
    # Create a university
    university_name = input("Enter the university name: ")
    my_university = University(university_name)

    # Input for teachers
    num_teachers = int(input("Enter the number of teachers: "))
    for _ in range(num_teachers):
        name = input("Enter teacher's name: ")
        human_id = int(input("Enter teacher's ID: "))
        contact = input("Enter teacher's contact: ")
        subjects = input("Enter subjects (comma-separated): ").split(',')
        teacher = Teacher(name, human_id, contact, [subject.strip() for subject in subjects])
        my_university.add_human(teacher)

    # Input for classes
    num_classes = int(input("Enter the number of classes: "))
    for _ in range(num_classes):
        class_name = input("Enter class name: ")
        timings = input("Enter class timings: ")
        teacher_name = input("Enter teacher's name for this class: ")

        # Find the teacher object
        teacher = next((h for h in my_university.humans if isinstance(h, Teacher) and h.name == teacher_name), None)
        if teacher:
            new_class = Class(class_name, timings, teacher)
            my_university.add_class(new_class)
            # Add sections for the class
            num_sections = int(input(f"Enter the number of sections for {class_name}: "))
            for _ in range(num_sections):
                section_name = input("Enter section name: ")
                section_timings = input("Enter section timings: ")
                section = Section(section_name, section_timings, teacher)
                new_class.add_section(section)

    # Input for students
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        name = input("Enter student's name: ")
        human_id = int(input("Enter student ID: "))
        contact = input("Enter student's contact: ")
        major = input("Enter student's major: ")
        student = Student(name, human_id, contact, major)
        my_university.add_human(student)

        # Enroll student in sections
        for cls in my_university.classes:
            print(f"Available sections for {cls.name}:")
            for section in cls.sections:
                print(f" - {section.section_name} (Timings: {section.timings})")
            section_name = input(f"Enroll {name} in section (enter section name): ")
            section = next((s for s in cls.sections if s.section_name == section_name), None)
            if section:
                section.enroll_student(student)

    # Display university information
    my_university.display_info()

if __name__ == "__main__":
    main()

"""
Enter the university name: OpenAI University of Technology
Enter the number of teachers: 2
Enter teacher's name: Alice Smith
Enter teacher's ID: 1
Enter teacher's contact: alice@university.com
Enter subjects (comma-separated): Data Structures, Algorithms
Enter teacher's name: Bob Johnson
Enter teacher's ID: 2
Enter teacher's contact: bob@university.com
Enter subjects (comma-separated): Software Engineering, Database Systems
Enter the number of classes: 2
Enter class name: Data Structures
Enter class timings: Mon-Wed-Fri 9:00-10:00
Enter teacher's name for this class: Alice Smith
Enter the number of sections for Data Structures: 1
Enter section name: Section A
Enter section timings: Mon-Wed-Fri 9:00-10:00
Enter class name: Software Engineering
Enter class timings: Tue-Thu 11:00-12:30
Enter teacher's name for this class: Bob Johnson
Enter the number of sections for Software Engineering: 1
Enter section name: Section B
Enter section timings: Tue-Thu 11:00-12:30
Enter the number of students: 1
Enter student's name: John Doe
Enter student ID: 1001
Enter student's contact: john@university.com
Enter student's major: Computer Science
Available sections for Data Structures:
 - Section A (Timings: Mon-Wed-Fri 9:00-10:00)
Enroll John Doe in section (enter section name): Section A
Available sections for Software Engineering:
 - Section B (Timings: Tue-Thu 11:00-12:30)
Enroll John Doe in section (enter section name): Section B

University: OpenAI University of Technology
Classes Offered:
 - Data Structures, taught by Alice Smith, Timings: Mon-Wed-Fri 9:00-10:00
   Section: Section A, Timings: Mon-Wed-Fri 9:00-10:00, Teacher: Alice Smith
 - Software Engineering, taught by Bob Johnson, Timings: Tue-Thu 11:00-12:30
   Section: Section B, Timings: Tue-Thu 11:00-12:30, Teacher: Bob Johnson
"""

