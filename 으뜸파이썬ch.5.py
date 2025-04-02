#5.1
list_ex = [10,20,30,40,50,60,70]
high = 5
low = 3
print(list_ex[low])#40
print(list_ex[low + 2])#60
print(list_ex[high-low])#30
print(list_ex[low-high])#60
print(list_ex[-1])#70
print(list_ex[-low])#50
print(list_ex[2*3])#70
print(list_ex[2]*3)#30*3=90
print(list_ex[5%4])#20
print(len(list_ex))#길이

#5.3
list1 = [3,5,7]
list2 = [2,3,4,5,6]

for i in range(len(list1)):
    for j in range(len(list2)):
        result=list1[i]*list2[j]
        print(f'{list1[i]}*{list2[j]}=',result)

#5.5
list1=['I like', 'I love']
list2=[' pancakes.',' kiwi juice.',' espresso.']
for i in range(len(list1)):
    for j in range(len(list2)):
        st = list1[i] + list2[j]
        print(st)
#5.7
n_list = [10,20,30,50,60]
s=0
for i in n_list:
    s = s + i
print('리스트 원소들:',n_list)
print('리스트 원소들의 합:',s)
    
#5.9
n_list =[10,20,30,50,60]
m = n_list[-1]
print('리스트의 원소들:', n_list)
print('리스트 원소들 중 최댓값:', m)

#5.11
n_list = list(map(int,input('5개의 수를 입력하세요:').split()))
s = sum(n_list)
a = sum(n_list)/ len(n_list)
x = max(n_list)
n = min(n_list)
print('합:', s)
print('평균:', a)
print('최댓값',x)
print('최솟값:',n)

#5.15
greet = 'Have a beautiful day.'
print(f"'{greet[0:4]}'")
print(f"'{greet[7:16]}'")
print(f"'{greet[-4:-1]}'")

#5.17
#1)
animals = ['dog','cat','tiger','lion']
print('animals =', animals)
#2)
animals.append(animals[0])
animals.remove(animals[0])
print(animals)
#3)
text = 'I love '
for i in range(len(animals)):
    st = text + animals[i]
    print(st)

#5.19
s_list = ['abc', 'bcd', 'abc','abba','cddc','opq','opq']
new_s_list= []
for item in s_list:
    if item not in new_s_list:
        new_s_list.append(item)
print(new_s_list)

#5.23
#1)
person1 = ['온달',20,1,180.0,100.0]
person2 = ['이사부',25,1,170.0,70.0]
person3 = ['평강',22,0,169.0,60.0]
person4 = ['혁거세',40,1,150.0,50.0]

person_list = [person1,person3,person4]

n_person = len(person_list)

print(str(n_person)+'명의 정보가 담겨 있습니다.')
#2)
person_list=[person1,person2,person3,person4]
n_person = len(person_list)
average_age = sum(person[1]for person in person_list)/ n_person
print(f'평균 나이는 {average_age:.2f}세 입니다.')

#3)
n_male=[]
n_female=[]

for person in person_list:
    if person[2] == 1:
        n_male.append(person)
    else:
        n_female.append(person)
m = len(n_male)
f = len(n_female)
print(f'리스트에는 남자가{m}명, 여자가{f}명 입니다.')
#4)
person1 = ['온달', 20, 1, 180.0, 100.0]  
person2 = ['이사부', 25, 1, 170.0, 70.0]  
person3 = ['평강', 22, 0, 169.0, 60.0]  
person4 = ['혁거세', 40, 1, 150.0, 50.0]  

person_list = [person1, person2, person3, person4]

separated_lists = [list(person) for person in person_list]

for idx, person in enumerate(separated_lists, start=1):
    print(f"📌 [Person {idx}] {person}")
