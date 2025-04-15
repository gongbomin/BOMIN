#5.1
def my_greet():
    print('환영합니다.')
my_greet()
my_greet()
#5.5
def centimeter():
    for n in range(1,6):
        inch = 2.54 * n
        print(f'{n} 인치 = {inch} 센티미터')
        
centimeter()
              
#5.9
def res(*nums):
    nums = list(map(int,input('정수를 입력하세요:').split()))
    mean_of_n= sum(nums) / len(nums)
    max_of_n= max(nums)
    min_of_n= min(nums)
    print('평균값은 ',mean_of_n )
    print('최댓값은 ', max_of_n)
    print('최솟값은 ',min_of_n)
res()

#5.13
#(1)모서리 길이가 12인 정육면체
def hexa():
    cube = 12**3
    return cube

print('(1)모서리의 길이가 12인 정육면체:', hexa())

#(2)모서리 길이가 20인 정육면체
def hexa():
    cube = 20**3
    return cube

print('(2)모서리의 길이가 20인 정육면체:', hexa())
#(3)가로, 세로, 깊이가 각각 3,5,6인 직육면체
def quarter():
    square = 3*5*6
    return square

print('(3)가로, 세로, 깊이가 각각 3,5,6인 직육면체:',quarter())

#(4)반지름의 높이가 각각 20,10인 원뿔
def one():
    r = 20
    h = 10
    pi = 3.14
    res = (pi * r **2 * 20) /3
    return res

print('(4)반지름의 높이가 각각 20,10인 원뿔:',one())

#(5)반지름이 15인 구
def sphere():
    r = 15
    pi = 3.14
    s = (pi * r**3) * 4/3
    return s

print('(5)반지름이 15인 구:',sphere())

#(6)반지름과 높이가 각각 20,10인 원기둥
def cylinder():
    pi = 3.14
    r = 20
    h = 10
    res = pi * r**2 * 10
    return res
print('(6)반지름과 높이가 각각 20,10인 원기둥:', cylinder())


#5.17
n1 = 10
n2 = 20
n3 = 40
n4 = 100
result = 0

for i in range(n1,n2+1):
    result += i
    
print('{}에서 {}까지의 정수의 합:{}'.format(n1,n2,result))

result=0

for i in range(n3,n4+1):
    result += i
    
print('{}에서 {}까지의 정수의 합:{}'.format(n3,n4,result))

#5.21

