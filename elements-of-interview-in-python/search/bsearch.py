import bisect
import collections


Student = collections.namedtuple('Student', ('name', 'GPA'))


def compare_gpa(student):
    return (-student.GPA, student.name)


def search_student(students, target, compare_gpa):
    i = bisect.bisect_left([compare_gpa(s) for s in students], compare_gpa(target))
    return 0 <= i < len(students) and students[i] == target
