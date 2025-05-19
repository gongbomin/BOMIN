#10.1
(1)
result1=(123).__add__(334)
print(result1)
(2)
result2=(123).__sub__(334)
print(result2)
(3)
result3=(123).__mul__(334)
print(result3)
(4)
result4=(123).__truediv__(3)
print(result4)

#10.3
#문자열 s는 upper()을 제외한 모든 메소드가 사용불가능 합니다.

#10.5
a=1
b=1
c=2
d=3
e=3

#10.7
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
my_dog =Dog('Mango',3)

print(f"my_dog의 이름은 {my_dog.name}이고 나이는 {my_dog.age}살 입니다.")

#10.9
class Counter:
    def __init__(self,number):
        self.number=number
        
    def __add__(self,other):
        result = self.number + other.number
        if result >= 100:
            result = 0
        return Counter(result)
    def __sub__(self, other):
        result = self.number - other.number
        if result <= -1:
            result = 0
        return Counter(result)
    def __str__(self):
        return str(self.number)
    

c1= Counter(10)
c2= Counter(20)
c3= c1+c2
c4= c1-c2

print('c3=',c3)
print('c4=',c4)
