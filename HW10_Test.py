import unittest
import os
from HW10_KshitiRana import Repository, Student, Instructor, Grade, Major, read_file

class TestRepository(unittest.TestCase):
    repo = Repository('C:/Users/kshit/Documents/Stevens/Semester 2/SSW 810 - Special Topics - Python/old code')

    def test_Student(self):
        self.assertEqual(self.repo.students['10103'].cwid, '10103')
        self.assertEqual(self.repo.students['10103'].name, 'Baldwin, C')
        self.assertEqual(self.repo.students['10115'].display_data(),('Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'],{'SSW 564', 'SSW 555', 'SSW 540', 'SSW 567'},{'CS 513', 'CS 501', 'CS 545'}))

    def test_Instructor(self):
         self.assertEqual(self.repo.instructors['98765'].cwid,'98765')
         self.assertEqual(self.repo.instructors['98765'].display_data(), ('Einstein, A', 'SFEN', ['SSW 540', 'SSW 567']))
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
