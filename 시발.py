def bomin_birthday (x, y, z):
    return x*10000 + y*100 + z

x = int(input("보민이가 태어난 년도를 입력하세요: "))
y = int(input("보민이가 태어난 월을 입력하세요: "))
z = int(input("보민이가 태어난 일자를 입력하세요: "))

result = bomin_birthday (x, y, z)
print (f"보민아 생일 축하해 ... {result}")
