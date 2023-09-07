import Courses, Students

courses = {}
students = {}


def add_new_course(name):
    name=name.capitalize()
    c = Courses.Course(name)
    count = 0
    for i in courses:
        if i[:3] == name[:3]: count+=1
    cid = name[:3] + "." + str(count+1).zfill(3)
    courses.update({cid:c})


def add_new_student(name, email, phoneNumber, birth,s_courses):
    s = Students.Student(name, email, phoneNumber, birth)
    s.set_courses(s_courses)
    sid = 'BI12-' + str((len(students)+1)).zfill(3)
    for course in courses:
        if course in s_courses:
            courses[course].add_student(sid)
    students.update({sid:s})

def edit_info(id,name, email, phoneNumber, birth,s_courses):
    for i in students[id].get_courses():
        if i not in s_courses:
            courses[i].remove_student(id)
    for i in s_courses:
        if i not in students[id].get_courses():
            courses[i].add_student(id)
    students[id].edit_student(name,email,phoneNumber,birth,s_courses)

def remove(sid,cid):
    students[sid].remove_course(cid)
    courses[cid].remove_student(sid)

add_new_course("Math")
add_new_course("Physics")
add_new_course("Math 2")
add_new_student('a','qwer@qwer.com','012431234','20/04/03',['Mat.001','Mat.002'])
add_new_student('b','qwer@qwer.com','012431234','20/04/03',['Mat.001','Phy.001'])
add_new_student('c','qwer@qwer.com','012431234','20/04/03',['Mat.001','Phy.001'])
add_new_student('d','qwer@qwer.com','012431234','20/04/03',['Mat.002','Phy.001'])
