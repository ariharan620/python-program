class Node:
    def __init__(self,coeff,power):
        self.coeff  = coeff
        self.power = power
        self.next = None

class polynomial:
    def __init__(self):
        self.head = None
    def append(self,coeff,power):
        new_node = Node(coeff,power)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def print_all(self):
        temp = self.head
        res = []
        while temp:
            res.append(f"{temp.coeff}x^{temp.power}")
            temp = temp.next
        print("+".join(res))


    def add_poly(self,p1,p2):
        a = p1
        b = p2
        new_node0 = Node(0,0)
        c = new_node0
        while a is not None or b is not None:
            if a is None:
                c.next = b
                break
            elif b is None:
                c.next = a
                break
            elif a.power == b.power:
                c.next = Node(a.coeff+b.coeff,a.power)
                a = a.next
                b = b.next
            elif a.power>b.power:
                
                c.next = Node(a.coeff,a.power)
                a = a.next
            else:
                c.next = Node(b.coeff,b.power)
                b  = b.next
            c = c.next

        return new_node0.next


x = polynomial()
x.append(5,3)
x.print_all()

x1 =  polynomial()
x1.append(4,2)
x1.print_all()

result = polynomial()
result.head = result.add_poly(x.head,x1.head)
result.print_all()





























            








        
