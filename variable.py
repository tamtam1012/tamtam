1
r = int(input('반지름을 입력하세요 : '))

length = 2 * 3.14 * r
area = r * r * 3.14

print('반지름 : %d cm' % r)
print('원의 둘레 : %.2f cm' % length)
print('원의 면적 : %.2f cm2' % area)


2
book_price = int(input('책 값을 입력하세요 : '))
discount = float(input('할인율을 입력하세요(%) : '))
shipping = int(input('배송료를 입력하세요 : '))

total_price = book_price - (book_price * discount/100) + shipping

print("결제 금액 : %.0f원" % total_price)

3
name = input('이름을 입력하세요 : ') 
current = int(input('현재년을 입력하세요 : '))
birth = int(input('탄생년을 입력하세요 : ')) 

age = current - birth + 1; 
print('%s님의 나이는 %d세 입니다!' % (name, age)) 


4
year = int(input('연을 입력하세요 : '))
month = int(input('월을 입력하세요 : '))
day = int(input('일을 입력하세요 : '))

print('%d-%02d-%02d' % (year, month, day))
