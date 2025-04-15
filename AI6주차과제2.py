#7.1
price = {'김밥': 5000, '어묵': 3000, '떡볶이': 2000}

print(price['김밥'])
price['김밥'] = 6000
print(price)
print(price.values())
print(price.keys())
print('이 식당의 메뉴 개수는', len(price), '개 입니다.')

#7.5
t=(10,20,30,40)
print(t[0])
print(t[0:2])
print(t[1:])
print(t[:3])
print(t[1::2])
print(t[::-1])

#7.9
tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
tup_no_dup = tuple(set(tup))
print('주어진 튜플:', tup)
print('중복 제거 튜플:', tup_no_dup)

#7.13
lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print('정렬된 결과는 =', lst)

#7.17
population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_B = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

vote_A = sum(population_A[2:])
vote_B = sum(population_B[2:])

print('마을 A와 B에 보낼 투표용지의 개수는 각각', vote_A, '장과', vote_B, '장입니다.')

#7.21
text = input('문자열을 입력하세요: ')

text = text.lower()

cleaned = ''
for char in text:
    if char.isalnum(): 
        cleaned += char


if cleaned == cleaned[::-1]:
    print('회문입니다.')
else:
    print('회문이 아닙니다.')

#7.25
dictionary = {}

print("사전 프로그램 시작... 종료는 'q'를 입력")

while True:
    command = input('$ ').strip()
    
    if command == 'q':
        print("사전 프로그램을 종료합니다.")
        break
    
    try:
        if command[0] == '<': 
            eng_kor = command[1:].strip().split(':')
            if len(eng_kor) == 2:
                eng = eng_kor[0].strip()
                kor = eng_kor[1].strip()
                dictionary[eng] = kor
            else:
                print("입력오류가 발생했습니다.")
        elif command[0] == '>':
            word = command[1:].strip()
            if word in dictionary:
                print(dictionary[word])
            else:
                print(f"{word}가 사전에 없습니다.")
        else:
            print("입력오류가 발생했습니다.")
    except:
        print("입력오류가 발생했습니다.")

