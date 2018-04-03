""" @author Kshiti Rana
    Code for assignment 10
"""

from collections import defaultdict
from prettytable import PrettyTable
import os
import unittest


        
class Repository():
    students = dict()
    instructors = dict()
    majors = dict()
    def __init__(self, dir_name):
        self.wdir = dir_name
        self.get_students()
        self.get_instructors()
        self.get_majors()
        self.get_grades()
        print("Majors Summary:")
        self.maj_table()
        print("Student Summary:")
        self.stu_table()
        print("Instructor Summary:")
        self.ins_table()
        
        
    
    def get_students(self):
        stud_file = read_file('students.txt')
        for cwid, name, dept in stud_file:
            self.students[cwid] = Student(cwid, name, dept)
        
    def get_instructors(self):
        ins_file = read_file('instructors.txt')
        for cwid, name, dept in ins_file:
            self.instructors[cwid] = Instructor(cwid, name, dept)

    def get_grades(self):
        gra_file = read_file('grades.txt')
        for stud_cwid, course, grade, ins_cwid in gra_file:
            if stud_cwid in self.students.keys():
                self.students[stud_cwid].stud_courses[course] = grade
                if ins_cwid in self.instructors.keys():
                    self.instructors[ins_cwid].ins_courses[course] += 1

    def get_majors(self):
        major_file = read_file('majors.txt')
        for name, flag, course in major_file:
            self.majors[name] = Major(name)
        maj_file = read_file('majors.txt')
        for name, flag, course in maj_file:
            self.majors[name].add_course(flag, course)
        for cwid, stud in self.students.items():
            stud.rem_req = self.majors[stud.dept].required - set(stud.stud_courses.keys())
            stud.rem_elec = self.majors[stud.dept].electives - set(stud.stud_courses.keys())
    
    def stu_table(self):
        x_stud = PrettyTable()
        x_stud.field_names = ["CWID", "Name", "Major", "Completed Courses","Remaining Required", "Remaining Electives"]
        for cwid, stud in self.students.items():
            x_stud.add_row([stud.cwid, stud.name, stud.dept, sorted(stud.stud_courses.keys()),  sorted(stud.rem_req), sorted(stud.rem_elec)])
        print(x_stud)
           
    def ins_table(self):
        x_ins = PrettyTable()
        x_ins.field_names = ["CWID", "Name", "Dept", "Course", "Students"]
        for cwid, instructor in self.instructors.items():
            for course in instructor.ins_courses:
                x_ins.add_row([cwid, instructor.name, instructor.dep, course, instructor.ins_courses[course]])
        print(x_ins)

    def maj_table(self):
        t_major = PrettyTable()
        t_major.field_names = ["Dept", "Required Courses", "Elective Courses"]
        for name,major in self.majors.items():
            t_major.add_row([major.dept,major.required, major.electives])
        print(t_major)
    
        
class Student():
    "to store all data about students"
    def __init__(self, cwid, name, dept):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.stud_courses = defaultdict(str)
        self.rem_req = set()
        self.rem_elec = set()

    def add_course(self, course, grade):
        self.stud_courses[course] = grade
        
    def get_course():
        return self.stud_courses.keys()

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
    def __init__(self, stud_cwid, course, grade, ins_cwid):
        self.stud_cwid = stud_cwid
        self.course = course
        self.grade = grade
        self.ins_cwid = ins_cwid

class Major():
    def __init__(self,dept):
        self.dept = dept
        self.required = set()
        self.electives = set()

    def add_course(self,flag,course):
        if flag == 'R':
            self.required.add(course)
        elif flag == 'E':
            self.electives.add(course)
        else:
            raise ReaderError('Invalid Flag')

def read_file(fname):
    try:
        fp = open(fname)
    except FileNotFoundError:
        print("read_file Error '{}'".format(fname))
    else:
        with fp:
            for line in fp:
                yield tuple(line.strip().split('\t'))  

def main():
    """main function"""
    stevens = Repository('C:/Users/kshit/Documents/Stevens/Semester 2/SSW 810 - Special Topics - Python/old code')
    
        
if __name__ == "__main__":
    main()
    
