import datetime
next_year = datetime.date.today().year
last_year = next_year - 1

bday = input().split('.')

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

a, b, c, d, e = 0, 0, 0, 0, 0

a = int(bday[0])
b = int(bday[1])
if a > 22:
    a = sum_of_digits(a)
if b > 22:
    b = sum_of_digits(b)

c = sum_of_digits(int(bday[2]))
if c > 22:
    c = sum_of_digits(c)

d = a + b + c
if d > 22:
    d = sum_of_digits(d)

e = a + b + c + d
if e > 22:
    e = sum_of_digits(e)


y4_l = sum_of_digits(last_year)
y4_n = sum_of_digits(next_year)

a_l = a + y4_l
if a_l > 22:
    a_l = sum_of_digits(a_l)
b_l = b + y4_l
if b_l > 22:
    b_l = sum_of_digits(b_l)
c_l = c + y4_l
if c_l > 22:
    c_l = sum_of_digits(c_l)
d_l = d + y4_l
if d_l > 22:
    d_l = sum_of_digits(d_l)
e_l = a_l + b_l + c_l + d_l
if e_l > 22:
    e_l = sum_of_digits(e_l)

a_n = a + y4_n
if a_n > 22:
    a_n = sum_of_digits(a_n)
b_n = b + y4_n
if b_n > 22:
    b_n = sum_of_digits(b_n)
c_n = c + y4_n
if c_n > 22:
    c_n = sum_of_digits(c_n)
d_n = d + y4_n
if d_n > 22:
    d_n = sum_of_digits(d_n)
e_n = a_n + b_n + c_n + d_n
if e_n > 22:
    e_n = sum_of_digits(e_n)

print(a, b, c, d, e, a_l, b_l, c_l, d_l, e_l, a_n, b_n, c_n, d_n, e_n)