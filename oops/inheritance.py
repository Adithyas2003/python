# class synnefo:
#     def __init__(s):
#         print("register")
#     def python(s):
#         print("python")
#     def php(self):
#         print("php")


# class novavi(synnefo):
#     def dm(self):
#         print("dm")
#     def web_dev(self):
#         print("web_dev")
# manu=synnefo()
# manu.python()
# sanu=novavi()
# sanu.php()


# class synnefo:
#     def __init__(s):
#         print("register")
#     def python(s):
#         print("python")
#     def php(self):

#     def dm(self):
#         print("dm")
#     def web_dev(self):
#         print("web_dev")
# class student(novavi,synnefo):
#     def reg(self):
#         print("reg")
# manu=synnefo()
# manu.python()
# sanu=novavi()
# sanu.web_dev()
# anu=student()
# anu.reg()

#multilevel inheritance:


# class synnefo:
#     def __init__(s):
#         print("register")
#       def__init__(s)def python(s):
#         print("python")
#     def php(self):
#         print("php")
# class novavi:
#     def dm(self):
#         print("dm")
#     def web_dev(self):
#         print("web_dev")
# class staff(novavi):
#     def reg(self):
#         print("reg")
# manu=synnefo()
# manu.python()
# sanu=novavi()
# sanu.web_dev()
# anu=staff()
# anu.reg()

#hierarchial inheritance:
#   def__init__(s)

# class synnefo:
#     def __init__(s):
#         print("register")
#     def python(s):
#         print("python")
#     def php(self):
#         print("php")
# class novavi:
#     def dm(self):
#         print("dm")
#     def web_dev(self):
#         print("web_dev")
# class student(synnefo):
#     def reg(self):
#         print("reg")
# manu=synnefo()
# manu.python()
# sanu=novavi()
# sanu.web_dev()
# anu=student()
# anu.reg()


#hybrid inheritance:

# class A:
#     def a1(self):
#         print("a1")

# class B:
#     def b1(self):
#         print("b1")
# class F:
#     def f1(self):
#         print("f1")
# class C(A,B):
#     def c1(self):
#         print("c1")
# class D(B,F):
#     def d1(self):
#         print("d1")
# class E(C,D):
#     def e1(self):
#         print("e1")
# abc=A()
# abc.a1()class Birds:



#example program:
class Birds:
    def __init__(self,species):
        self.species=species
    def speak(self):
        
class parrot(Birds):
    def speak(self):
        print("squark")
class kingfisher(Birds):
    def speak(self):
        print("tweet tweet")
class crow(Birds):
    def speak(self):
        print("craa craa")

parrot=Birds()
parrot.speak()
kingfisher=Birds()
kingfisher.speak()
crow=Birds()
crow.speak()










