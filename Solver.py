import math

_author_ = 'klaudia'

class Solver:
    def demo(self):
        author = "Klaudia"
        calc = 2**3
        print("My name is %s and the result of my calculation is %d.\nThank you." % (author,calc))
        check = 1
        while check:
            a = int(input("a   "))
            b = int(input("b   "))
            c = int(input("c   "))
            d = b ** 2 - 4 *a * c
            if d>=0:
                disc = math.sqrt(d)
                root1 = (-b + disc) / (2 * a)
                root2 = (-b - disc) / (2 * a)
                print(root1, root2)
                check = 0
            else:
                print('error')
                check = 1

Solver().demo()