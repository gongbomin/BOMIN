#9.1
#(1)
try:
    a, b = input('두 수를 입력하세요: ').split()
    result = int(a) * int(b)
except ValueError:
    print("입력이 잘못되었습니다. 두 개의 정수를 입력하세요.")
else:
    print("결과:", result)

#(2)
try:
    a, b = input('두 수를 입력하세요: ').split()
    result = int(a) * int(b)
except ValueError:
    print("입력이 잘못되었습니다. 정수를 입력하세요.")
else:
    print("결과:", result)

#(3)
a_list = [200, 300, 400]
print('a_list :', a_list)

try:
    idx = int(input('구하고자 하는 값의 인덱스를 0,1,2 중에서 입력하세요 : '))
    result = a_list[idx]
except (ValueError, IndexError):
    print("잘못된 인덱스입니다. 0, 1, 2 중에서 입력하세요.")
else:
    print("결과 :", result)

#9.5
with open('number1to10.txt', 'w') as f:
    for i in range(1, 11):
        f.write(str(i) + '\n')

#9.9
with open('coord.txt', 'r') as f:
    n = int(f.readline())
    coords = []

    for _ in range(n):
        x, y = map(int, f.readline().split())
        coords.append((x, y))

coords.sort()

for x, y in coords:
    print(x, y)
