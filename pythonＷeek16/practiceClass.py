import json
import os

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def add_course(self, course_code, course_name, semester):
        self.courses.setdefault(semester, []).append({"code": course_code, "name": course_name})

    def delete_course(self, course_code, semester):
        courses_semester = self.courses.get(semester, [])
        self.courses[semester] = [course for course in courses_semester if course["code"] != course_code]
        print(f"Course {course_code} deleted for {self.name} in semester {semester}.")

    def get_courses_by_semester(self, semester):
        return self.courses.get(semester, [])

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump({"student_id": self.student_id, "name": self.name, "courses": self.courses}, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.student_id, self.name, self.courses = data.get("student_id"), data.get("name"), data.get("courses", {})

def create_or_load_student_profile(student_id, student_name):
    student_filename = f"{student_id}_profile.json"
    student = Student(student_id, student_name)
    student.load_from_file(student_filename)
    return student, student_filename

def add_courses(student, courses):
    for course in courses:
        student.add_course(*course)

def display_courses(student_name, semester, courses_taken):
    print(f"Courses taken by {student_name} in {semester}:")
    for course in courses_taken:
        print(f"{course['code']}: {course['name']}")

def delete_and_save_course(student, course_code, semester):
    student.delete_course(course_code, semester)
    student.save_to_file(student_filename)

# Example usage:
student_id = "123456"
student_name = "John Doe"

# Create or load student profile
student, student_filename = create_or_load_student_profile(student_id, student_name)

# Add courses
courses_to_add = [("CS101", "Introduction to Computer Science", "Fall 2023"),
                  ("ENG201", "English Literature", "Fall 2023")]
add_courses(student, courses_to_add)

# Save the updated profile to file
student.save_to_file(student_filename)

# Display courses for a specific semester
semester_to_search = "Fall 2023"
courses_taken = student.get_courses_by_semester(semester_to_search)
display_courses(student_name, semester_to_search, courses_taken)

# Delete a course
course_to_delete = "CS101"
delete_and_save_course(student, course_to_delete, semester_to_search)
