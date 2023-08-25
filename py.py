1
num = int(input('월을 입력하세요 : '))

if num <3 :
    print('봄입니다')
elif num <9 :
    print('여름입니다')
elif num <11 :
    print('가을입니다')
else:
    print('겨울입니다')


2
num = int(input('숫자를 입력하세요 : '))

if num %20 == 0 :
    print('4와 5의 공배수입니다')
    print('5의배수입니다.')elif num %5 == 0 :

elif num %4 == 0 :
    print('4의배수입니다')
else:
    print('X')
