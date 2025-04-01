


#3.7    
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n=int(input('숫자를 입력하세요:'))
if is_prime(n):
      print(f'{n}은 소수입니다.')
else:
    print(f'{n}은 소수가 아닙니다.')

      
#3.9
def sum(n):
    total=0
    for i in range(1,n+1):
        total += i**2
    
    return  total
n = int(input('숫자를 입력하세요.'))
result = sum(n)
print(f"결과는 {result}입니다.")

#3.11
depth = 30

def days_to_escape(depth):
    height = 0  
    days = 0  
    while height < depth:
        days += 1  
        height += 7
        if height >= depth: 
            break
        height -= 5
        print(f'day:{days}      달팽이의 위치:{height}미터')
    return days

result = days_to_escape(depth)
print(f"우물을 탈출하는데 걸린 날은 {result}입니다.")

#3.13

def find_armstrong_numbers():
    armstrong_numbers = []  

    for num in range(100, 1000):  
        
        hundreds = num // 100 
        tens = (num // 10) % 10
        ones = num % 10 

        if hundreds**3 + tens**3 + ones**3 == num:
            armstrong_numbers.append(num)

    return armstrong_numbers

armstrong_numbers = find_armstrong_numbers()
print("세 자리 암스트롱 수:", armstrong_numbers)

#3.15
f_fule= 30

def days_to_use(fuel):  
    while True:
            num = input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오:')
            if num.startswith('+'):
                amount = int(num [1:])
                fuel += amount
                print(f'현재 태크양은 {fuel} 입니다.')
                
            elif num.startswith('-'):
                amount = int(num [1:])
                fuel -= amount
                if fuel <10:
                    print('경고: 연료가 10%미만이니 충전하세요!')
                break
num = int(input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오:'))

fuel = 30
days_to_use(fuel)


