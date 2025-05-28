from typing import Any

class Element:
    def __init__(self, val : Any, next : 'Element' = None):
        self.val = val
        self.next = next                                                       


class Spisok:
    def __init__(self):
        self.first : 'Element' = None
        
    def add(self, val : Any):
        if self.first is None : self.first = Element(val)
        else:
            cur = self.first
            while cur.next is not None:
                cur = cur.next
            cur.next = Element(val)
    
    def delet(self):
        prev : 'Element' = None
        cur = self.first
        if cur is None : return
        if cur.next is None : 
            self.first = None
            return
        while cur.next is not None:
            prev = cur
            cur = cur.next

        prev.next = None

    def search_by_id(self, id):
        cur = self.first
        if cur is None : return ("Список пуст")
        i = 0
        while i != id:
            if cur.next is None : return ("Нет элемента удовлетворяющего условие поиска")
            cur = cur.next
            i += 1
        return (f'id : {i}, val : {cur.val}')



    def search_by_val(self, val : Any):
        cur = self.first
        if cur is None : return ("Список пуст")
        i = 0
        while cur.val != val:
            if cur.next is None : return ("Нет элемента удовлетворяющего условие поиска")
            cur = cur.next
            i += 1
        return (f'id : {i}, val : {cur.val}')
    
    def __repr__(self):
        s = '{'
        cur = self.first
        if cur is not None :
            s += str(cur.val)
            while cur.next is not None :
                cur = cur.next
                s +=f' > {str(cur.val)}'
        s += '}'
        return s
    
a = Spisok()
print(a)
a.add(1)
print(a)
a.add(11)
a.add(111)
print(a)
a.delet()
print(a)
print(a.search_by_id(1))
print(a.search_by_id(3))
print(a.search_by_val(1))
print(a.search_by_val(2))


