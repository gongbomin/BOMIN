#8.1
from datetime import date, timedelta

start_date = date(2019, 2, 14)

today = date.today()

days_passed = (today - start_date).days

print("춘향이와 몽룡이의 연애 시작일 :", start_date)
print("연애 시작일로부터 경과한 날짜 :", days_passed, "일")

days = [100, 200, 500, 1000]

for d in days:
    anniversary = start_date + timedelta(days=d)
    print(f"{d}일 기념일 :", anniversary)

#8.5
import math

for degree in range(0, 181, 10):
    rad = math.radians(degree)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    tan_val = math.tan(rad
    print(f"sin({degree:3}) = {sin_val: .3f}, cos({degree:3}) = {cos_val: .3f}, tan({degree:3}) = {tan_val: .3f}")
#8.9
import random

answer = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("1~20까지의 숫자를 입력하세요: "))
    attempts += 1

    if guess < answer:
        print(f"{guess} 보다 큽니다!")
    elif guess > answer:
        print(f"{guess} 보다 작습니다!")
    else:
        print("정답입니다!")
        if attempts <= 3:
            print(f"{attempts}번만에 맞춘 당신은 천재!")
        elif 4 <= attempts <= 6:
            print(f"{attempts}번만에 맞추셨네요. 잘했어요^^")
        else:
            print(f"{attempts}번만에 맞추다니 쩝쩝...")
        break
