class A:
    def algo(self):
        print("hola")

class B:
    def algo(self):
        print("adios")
        

if __name__ == "__main__":
    ah = [A, B]
    ah[0]().algo()
    ah[1]().algo()
    print(A == B)
    print(A() == A)
    print(A().__class__ == A)