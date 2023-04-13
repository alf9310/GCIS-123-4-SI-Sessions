"""
Session 11B: Practice with Classes
@author: Audrey Fuller
@author: Zoe Bingham
"""

# Make a person class that holds the state for a name, age, and mood
class Person():
    __slots__ = ["name", "age", "mood", "courses", "hobby"]
    
    def __init__(self, name, age, mood = "nuetral"):
        self.name = name
        self.age = age
        self.mood = mood
        self.courses = []
        self.hobby = None

# Make a course class that holds the state for course_name, course_number, and number_of_students
# Once you have completed the above step, add a state for courses to the person class
class Courses():
    __slots__ = ["course_name", "course_section", "number_of_students"]
    
    def __init__(self, course_name, course_section, number_of_students = 0):
        self.course_name = course_name
        self.course_section = course_section
        self.number_of_students = number_of_students

# Make a class for a favorite hobby that has fields for hobby_name and description
# Once you've have completed this step, add a state for favorite hobby to the person class
class Hobby():
    __slots__ = ["hobby_name", "description"]
    
    def __init__(self, hobby_name, description):
        self.hobby_name = hobby_name
        self.description = description

def main():
    # instantiate the person class with your name, age, and mood
    person = Person("Josie", 19)

    # print the instance of this class. what happens?
    # print(person)
    # print the individual fields of the class. what happens?
    print(person.name, person.age, person.mood)

    # instantiate the course class with the GCIS-123 class information
    # add this course to the person class
    gcis = Courses("GCIS-123", 4, 20)
    josieCourses = gcis
    person.courses.append(josieCourses)
    print(person.courses[0].course_name)

    # Create some hobbies and assign people the hobbies
    hobby = Hobby("Dancing", "Smoovin around")
    person.hobby = hobby
    print(person.hobby.hobby_name, person.hobby.description)

if __name__ == "__main__":
    main()