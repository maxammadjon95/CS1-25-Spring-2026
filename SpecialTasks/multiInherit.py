class Student:
    def __init__(self, sid: int, deptid: int):
        self.sid = sid
        self.deptid = deptid

    def get_info(self) -> str:
        return f"StudentID:{self.sid} DepartmentID:{self.deptid}"


class Faculty:
    def __init__(self, eid: int, deptid: int):
        self.eid = eid
        self.deptid = deptid

    def get_info(self) -> str:
        return f"EmployeeID:{self.eid} DepartmentID:{self.deptid}"


class PhDStudent(Student, Faculty):
    def __init__(self, sid: int, eid: int, deptid: int):
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)

    def get_info(self) -> str:
        return f"Student ID:{self.sid} EmployeeID:{self.eid} DepartmentID:{self.deptid}"


if __name__ == "__main__":
    sid = 101
    eid = 555
    deptid = 42

    student = Student(sid, deptid)
    faculty = Faculty(eid, deptid)
    phd = PhDStudent(sid, eid, deptid)

    print(student.get_info())
    print(faculty.get_info())
    print(phd.get_info())