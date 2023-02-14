import datetime
next_year = datetime.date.today().year
last_year = next_year - 1

bday = input().split('.')

def sum_of_digits(num):
    if num > 22:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
    else:
        return num

#a=А, b=Б, c=В, d=Г, e=Я
a = sum_of_digits(int(bday[0]))
b = sum_of_digits(int(bday[1]))
c = sum_of_digits(sum_of_digits(int(bday[2])))
d = sum_of_digits(a + b + c)
e = sum_of_digits(a + b + c + d)

#f=Д, g=Е, h=Ж, i=З
f = sum_of_digits(a + b)
h = sum_of_digits(c + d)
g = sum_of_digits(b + c)
i = sum_of_digits(a + d)

#j=И, k=К, l=Л, m=М, n=Н, o=О, p=П, r=Р, s=С, t=Т, u=У, v=Ф, x=Х, z=Ц
j = sum_of_digits(a + e)
k = sum_of_digits(a + j)
l = sum_of_digits(c + e)
m = sum_of_digits(c + l)
n = sum_of_digits(b + e)
o = sum_of_digits(d + e)
p = sum_of_digits(b + n)
r = sum_of_digits(d + o)
s = sum_of_digits(c + d)
t = sum_of_digits(m + r)
u = sum_of_digits(l + o)
v = sum_of_digits(j + n)
x = sum_of_digits(k + p)
z = sum_of_digits(a + b)

#А-Д = a-f
af1 = sum_of_digits(a + f)
af2 = sum_of_digits(a + af1)
af3 = sum_of_digits(f + af1)
af4 = sum_of_digits(af1 + af2)
af5 = sum_of_digits(af1 + af3)
af6 = sum_of_digits(a + af2)
af7 = sum_of_digits(f + af3)
a_f = [af6, af2, af4, af1, af5, af3, af7]

#Д-Б = f-b
fb1 = sum_of_digits(f + b)
fb2 = sum_of_digits(f + fb1)
fb3 = sum_of_digits(b + fb1)
fb4 = sum_of_digits(fb1 + fb2)
fb5 = sum_of_digits(fb1 + fb3)
fb6 = sum_of_digits(f + fb2)
fb7 = sum_of_digits(b + fb3)
f_b = [fb6, fb2, fb4, fb1, fb5, fb3, fb7]

#Б-Е = b-g
bg1 = sum_of_digits(b + g)
bg2 = sum_of_digits(b + bg1)
bg3 = sum_of_digits(g + bg1)
bg4 = sum_of_digits(bg1 + bg2)
bg5 = sum_of_digits(bg1 + bg3)
bg6 = sum_of_digits(b + bg2)
bg7 = sum_of_digits(g + bg3)
b_g = [bg6, bg2, bg4, bg1, bg5, bg3, bg7]

#Е-В = g-c
gc1 = sum_of_digits(g + c)
gc2 = sum_of_digits(g + gc1)
gc3 = sum_of_digits(c + gc1)
gc4 = sum_of_digits(gc1 + gc2)
gc5 = sum_of_digits(gc1 + gc3)
gc6 = sum_of_digits(g + gc2)
gc7 = sum_of_digits(c + gc3)
g_c = [gc6, gc2, gc4, gc1, gc5, gc3, gc7]

#В-Ж = c-h
ch1 = sum_of_digits(c + h)
ch2 = sum_of_digits(c + ch1)
ch3 = sum_of_digits(h + ch1)
ch4 = sum_of_digits(ch1 + ch2)
ch5 = sum_of_digits(ch1 + ch3)
ch6 = sum_of_digits(c + ch2)
ch7 = sum_of_digits(h + ch3)
c_h = [ch6, ch2, ch4, ch1, ch5, ch3, ch7]

#Ж-Г = h-d
hd1 = sum_of_digits(h + d)
hd2 = sum_of_digits(h + hd1)
hd3 = sum_of_digits(d + hd1)
hd4 = sum_of_digits(hd1 + hd2)
hd5 = sum_of_digits(hd1 + hd3)
hd6 = sum_of_digits(h + hd2)
hd7 = sum_of_digits(d + hd3)
h_d = [hd6, hd2, hd4, hd1, hd5, hd3, hd7]

#Г-З = d-i
di1 = sum_of_digits(d + i)
di2 = sum_of_digits(d + di1)
di3 = sum_of_digits(i + di1)
di4 = sum_of_digits(di1 + di2)
di5 = sum_of_digits(di1 + di3)
di6 = sum_of_digits(d + di2)
di7 = sum_of_digits(i + di3)
d_i = [di6, di2, di4, di1, di5, di3, di7]

#З-А = i-a
ia1 = sum_of_digits(i + a)
ia2 = sum_of_digits(i + ia1)
ia3 = sum_of_digits(a + ia1)
ia4 = sum_of_digits(ia1 + ia2)
ia5 = sum_of_digits(ia1 + ia3)
ia6 = sum_of_digits(i + ia2)
ia7 = sum_of_digits(a + ia3)
i_a = [ia6, ia2, ia4, ia1, ia5, ia3, ia7]


matrix_a_i = [a, b, c, d, e, f, g, h, i]
matrix_j_r = [j, k, l, m, n, o, p, r]
matrix_s_z = [s, t, u, v, x, z]
matrix_4 = [a_f, f_b, b_g, g_c, c_h, h_d, d_i, i_a]


y4_l = sum_of_digits(last_year)
y4_n = sum_of_digits(next_year)

a_l = sum_of_digits(a + y4_l)
b_l = sum_of_digits(b + y4_l)
c_l = sum_of_digits(c + y4_l)
d_l = sum_of_digits(d + y4_l)
e_l = sum_of_digits(a_l + b_l + c_l + d_l)

a_n = sum_of_digits(a + y4_n)
b_n = sum_of_digits(b + y4_n)
c_n = sum_of_digits(c + y4_n)
d_n = sum_of_digits(d + y4_n)
e_n = sum_of_digits(a_n + b_n + c_n + d_n)