# DEFINING THE CLASS COURSE
class Course:
    '''Class implementation of a course'''
    
    def __init__(self, code, credit_hours, enrollment, room_number):
        self.code = code
        self.credit_hours = credit_hours
        self.enrollment = enrollment
        self.room_number = room_number

test_course = Course("TEST101", 4, 30, "Z01")
assert test_course.code == "TEST101"
assert test_course.credit_hours == 4
assert test_course.enrollment == 30
assert test_course.room_number == "Z01"
print("TEST 1: Course creation passed.")



# PROGRAM OUTPUT INTRODUCTION
print("OOP Example by Darien Prall")
print("Course objects each have a code (e.g. IT1006), credit hours (e.g. 6), enrollment, and room number.")
print("\nCourse Code\tCredits\tEnrollment\tRoom Number")

# STORING EACH COURSE CLASS IN A LIST TO ALLOW ITERATION
courses = [
    Course("IT1006", 6, 45, "B28"),
    Course("IT4782", 3, 22, "C34"),
    Course("IT4789", 3, 34, "H05"),
    Course("IT4079", 6, 34, "K25"),
    Course("IT2230", 3, 18, "A17"),
    Course("IT3345", 3, 34, "B16"),
    Course("IT2249", 6, 4, "A20")
]

assert len(courses) == 7
print("TEST 2: Course list contains 7 elements")

# LOOPING THROUGH THE COURSES LIST TO DISPLAY COURSE INFORMATION
for course in courses:
    print(f"{course.code}\t\t{course.credit_hours}\t\t{course.enrollment}\t\t{course.room_number}")

# CLOSING OUT THE PROGRAM WITH A MESSAGE
print("\nProgram has ended. Thank you!")


