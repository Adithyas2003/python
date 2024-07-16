#single:

# class school:
#     def __init__(s):
#         print("student details")
#     def regno(s):
#         print("regno")
#     def address(s):
#         print("address")
# class student(school):
#     def std_id(s):
#         print("std_id")
#     def course(s):
#         print("course")

# manu=school()
# manu.regno()
# anu=student()
# anu.address()


#multiple:


# class school:
#     def __init__(s):
#         print("student details")
#     def regno(s):
#         print("regno")
#     def address(s):
#         print("address")
# class teachers:
#     def teach_sub(s):
#         print("teach_sub")
#     def teach_class(s):
#         print("teach_class")
#     def salary(s):
#         print("salary")
# class student(school,teachers):
#     def std_div(s):
#         print("division")
#     def medium(s):
#         print("medium")
#     def rollno(s):
#         print("rollno")
# abc=school()
# abc.address()
# anu=teachers()
# anu.salary()
# manu=student()
# manu.medium()


#multilevel:


# class school:
#     def __init__(s):
#         print("school_det")
#     def location(s):
#         print("location")
#     def address(s):
#         print("address")
# class teacher:
#     def teach_sub(s):
#         print("teach_sub")
#     def teach_period(self):
#         print("teach_period")
# class office_staff(teacher):
#     def account_det(s):
#         print("account_det")
# abc=school()
# abc.address
# sanu=teacher()
# sanu.teach_period
# anu=office_staff()
# anu.account_det()

#hierarchial:

# class school:
#     def __init__(s):
#         print("school_det")
#     def location(s):
#         print("location")
#     def address(s):
#         print("address")
# class management:
#     def management_det(s):
#         print("management_det")
#     def m_contact(s):
#         print("m_contact")
# class student(school):
#     def reg(self):
#         print("reg")
# manu=school()
# manu.location()
# sanu=management()
# sanu.management_det
# anu=student()
# anu.reg()



#hybrid:

class college:
    def __init__(s):
        print("college_name")
    def dept_detail(s):
        print("dept_detail")
    def address(s):
        print("address")
class principal:
    def instruction(s):
        print("instruction")
    def evaluation(s):
        print("evaluation")
    def curriculum_dev(s):
        print("curriculam_dev")

class teachers:
    def subject(s):
        print("subject")
    def salary(s):
        print("salary")
    def activities(s):
        print("activity")

class management(college,principal):
    def organisation(s):
        print("organisation")
    def leadership(s):
        print("leadership")
    def controlling(s):
        print("controlling")
    
class hod(teachers,college):
    def staff_mang(s):
        print("staff_mang")
    def acd_dev(s):
        print("acd_dev")
    def staff_mang(s):
        print("staff-mang")
abc=college()
abc.dept_detail()



