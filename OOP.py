"""
student: orel twito
ID: 209004092
Assignment no.5
Program: OOP.py
""" 

class Point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y 
    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y
        
            
    def __str__(self):
        return f'({self.__x},{self.__y})'
        
class Line:
    def __init__(self,p,q):
        self.__p = p  
        self.__q = q

    def get_p(self):
        return self.__p
    
    def get_q(self):
        return self.__q
    
    def slope(self):
        if (self.__p.x-self.__q.x) == 0:
            return "Slope does not exist"
        return f'the Slope is {(self.__p.y-self.__q.y)/(self.__p.x-self.__q.x)}X'
    def y_intercept(self,uno):
        if (self.__p.x-self.__q.x) ==0:
            return None
        return ((self.__p.y-self.__q.y)/(self.__p.x-self.__q.x)*-self.__p.x ) + self.__p.y
    
    def isParallel(self,dos,uno):
        if uno.slope() == dos.slope(): 
            return f'True, the lines isParallel'
        else:
            return f'False, the lines is not Parallel'
        
    def __str__(self):
        
        return f'{self.__p},{self.__q}'
        
def main():
    
    print("welcome, pls choose 4 Qurdinat, so we can make 2 Lines") 
    
    x1,y1 = (int(num) for num in input("\nchoose the first X,Y for the first Line: ").split())
    p1 = Point(x1,y1)
    x2,y2 = (int(num) for num in input("choose the second X,Y for the second Line : ").split())
    q1 = Point(x2,y2)
    x3,y3 = (int(num) for num in input("choose the first X,Y for the first Line: ").split())  
    p2 = Point(x3,y3)
    x4,y4 = (int(num) for num in input("choose the second X,Y for the second Line: ").split())
    q2 = Point(x4,y4)

    uno = Line(p1, q1)
    dos = Line(p2, q2)  
    
    print(uno.slope())
    print(f'Y = {uno.y_intercept(uno)}')
    print(uno.isParallel(dos, uno))
 
main()
    
            
            