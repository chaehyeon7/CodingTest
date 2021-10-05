grade={'S':5,'G':10,'V':15}
def discount(grade, price):
    if grade == 'S':
        price = price*0.95
    elif grade == 'G':
        price = price*0.9
    elif grade == 'V':
        price = price*0.85
    return price

return1 = int(discount('V',2500))
print('손님 A의 할인된 가격은', return1,'입니다.')

return2 = int(discount('S',96900))
print('소님 B의 할인된 가격은',return2,'입니다.')
