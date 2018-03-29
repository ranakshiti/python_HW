from collections import defaultdict
from prettytable import PrettyTable
import os
import unittest


        
class Repository():
    students = dict()
    instructors = dict()
    def __init__(self, dir_name):
        self.wdir = dir_name
        self.get_students()
        self.get_instructors()
        self.get_grades()
        print("Student Summary:")
        self.stu_table()
        print("Instructor Summary:")
        self.ins_table()
    
    def get_students(self):
        stu_file = read_file('students.txt')
        for cwid, name, dept in stu_file:
            self.students[cwid] = Student(cwid, name, dept)
        
    def get_instructors(self):
        ins_file = read_file('instructors.txt')
        for cwid, name, dept in ins_file:
            self.instructors[cwid] = Instructor(cwid, name, dept)

    def get_grades(self):
        gra_file = read_file('grades.txt')
        for stu_cwid, course, grade, ins_cwid in gra_file:
            if stu_cwid in self.students.keys():
                self.students[stu_cwid].stu_courses[course] = grade
                if ins_cwid in self.instructors.keys():
                    self.instructors[ins_cwid].ins_courses[course] += 1

    
    def stu_table(self):
        x_stu = PrettyTable()
        x_stu.field_names = ["CWID", "Name", "Completed Courses"]
        for cwid, stu in self.students.items():
            x_stu.add_row([cwid, stu.name, sorted(stu.stu_courses.keys())])
        print(x_stu)
           
    def ins_table(self):
        x_ins = PrettyTable()
        x_ins.field_names = ["CWID", "Name", "Dept", "Course", "Students"]
        for cwid, instructor in self.instructors.items():
            for course in instructor.ins_courses:
                x_ins.add_row([cwid, instructor.name, instructor.dep, course, instructor.ins_courses[course]])
        print(x_ins)
		
    
        
class Student():
    "to store all data about students"
    def __init__(self, cwid, name, dep):
        self.cwid = cwid
        self.name = name
        self.dep = dep
        self.stu_courses = defaultdict(str)

    def add_course(self, course, grade):
        self.stu_courses[course] = grade
        
    def get_course():
        return self.stu_courses.keys()

    def __str__(self):
        return "<student: " + self.cwid + " " + self.name +">"

class Instructor():
    "to store all data about instructors"
    def __init__(self, cwid, name, dep):
        self.cwid = cwid
        self.name = name
        self.dep = dep
        self.ins_courses = defaultdict(int)
        """add_student, getcourses, get student_cnt"""

    def __str__(self):
        return "<instructor: " + self.cwid + ' ' + self.name + ">"

    def add_student(self,course):
        self.ins_courses[course] += 1

    def get_course(self):
        return self.ins_courses.keys()

    def get_student_cnt(self,course):
        return self.ins_courses[course]

class Grade():
    def __init__(self, stu_cwid, course, grade, ins_cwid):
        self.stu_cwid = stu_cwid
        self.course = course
        self.grade = grade
        self.ins_cwid = ins_cwid
        
def read_file(fname):
    try:
        fp = open(fname)
    except FileNotFoundError:
        print("Can't find",fname)
    else:
        with fp:
            for line in fp:
                yield tuple(line.strip().split('\t'))  

def main():
    """main function"""
    stevens = Repository('C://Users//kshit//Desktop//stevens')
    
        
if __name__ == "__main__":
    main()
    
