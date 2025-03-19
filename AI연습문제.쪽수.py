#연습문제 (짝수)
#2.2
width =30
height =60 
print(width)
print(height)

#2.4
width=40
height=20
print("삼각형의 면적:", width * height /2)

#2.6
sum = 1+2+3+4+5+6+7+8+9+10
print("1에서 10까지의 합:", sum)

#2.8
n=2
print("a  n  a**n")
for a in range(2,7):
    print(f"{a}  {n}  {a**2}")

#2.10
C= int(input("섭씨 온도를 입력하세요:"))
print("섭씨", C, "도는 화씨",C * 9/5 + 32, "도 입니다.")

#2.12
radius = 11
PI= 3.141592
P= 2* PI * radius
A= PI * radius**2
print("원의 반지름=", radius, ",원의 둘레=", P, ",원의 면적=", A)

#2.14

for a in range(2, 11):
    result = a**0.5
    print(f"{a}의 제곱근={result}")

#2.18
n= int(input("정수를 입력하세요: "))
if n % 2 == 0:
    print("이 수가 짝수인가요? True")
else:
    print("이 수가 짝수인가요? False")

#2.20
a = 5 & 6
print(bin(5), "&", bin(6), "= ", bin(a))
b = 5 | 6
print(bin(5), "|", bin(6), "= ", bin(b))
c = 5 ^ 6
print(bin(5), "^", bin(6), "= ", bin(c))

#2.22
f_num = int(input("정수 a를 입력하시오:"))
s_num = int(input("정수 b를 입력하시오:"))
print("a 와 b의 몫:", f_num // s_num)
print("a와 b의 나머지:", f_num % s_num)

#2.24
num = int(input("세 자리 정수를 입력하시오: "))
while num > 0:
    print(num % 10)
    num = num // 10
