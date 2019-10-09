import tkinter
import math
import time
import random
from math import *


# ___________________________________________
tg = lambda x: math.sin(x)/math.cos(x)#     |
ff = lambda x: ((modf(x)[0]+1)/2)**2#       |
ctg = lambda x: 1/tg(x)#                    |
sec = lambda x: 1/cos(x)#                   |
cosec = lambda x: 1/sin(x)#                 |
versin = lambda x: 1-cos(x)#                |
vers = versin#                              |
vercos = lambda x: 1-sin(x)#                |  Functions
cvs = vercos#                               |  from Hypermath
haversin = lambda x: versin(x)/2#           |  
hav = haversin#                             |
havercos = lambda x: vercos(x)/2#           |
hac = havercos#                             |
exsec = lambda x: sec(x)-1#                 |
excsc = lambda x: cosec(x)-1#               |
arcsin = math.asin#                         |
arccos = math.acos#                         |
arctg = lambda x: arcsin(x/(sqrt(1+x**2)))# |
arcctg = lambda x: arctg(1/x)#              |
arcsec = lambda x: arccos(1/x)#             |
arccosec = lambda x: arcsin(1/x)#           |
ln = lambda x: log(x, e)#                   |
sh = lambda x: (e**x-e**(-x))/2#            |
ch = lambda x: (e**x+e**(-x))/2#            |
th = lambda x: sh(x)/ch(x)#                 |
cth = lambda x: ch(x)/sh(x)#                |
sech = lambda x: 1/ch(x)#                   |
csch = lambda x: 1/sh(x)#                   |
arsh = lambda x: ln(x+sqrt(x**2+1))#        |
arch = lambda x: ln(x+sqrt(x**2-1))#        |
arth = lambda x: ln((1+x)/(1-x))/2#         |
arcth = lambda x: ln((x+1)/(x-1))/2#        |
sqrt = lambda x: x**0.5#                    |
Im = lambda x: complex(x).imag#             |
Re = lambda x: complex(x).real#             |
#___________________________________________|

tt=0
randu = [random.random()*20-10 for i in range(16)] # list of random numbers
                                                   # you can use it for random arguements in functions

start_value=eval(input("Enter start value: "))
scale=eval(input("Enter scale: "))
speed=eval(input("Enter speed: "))

rancol = lambda : "#"+hex(int(0xffffff*random.random()))[2:].zfill(6)
name=[]
j=''
ii=['a','b','c','d','e','f']
for i in range(2**10):
    j+=random.choice(ii)
    name.append(j)

print('There is some beautiful functions')
befu = [                                       # Beautiful
  ('50/(math.tan(t*3))', '50*math.sin(t*3)'),  # Functions
  ('50/(math.tan(t*3))', '50*math.cos(t*3)'),  # (x_func, y_func)
  ('(math.tan(t*3))+math.cos(t)*t', '50*math.sin(t*3)'),
  ('math.sin(t)*t', 'math.cos(t)/t')
  ]
print(*befu, sep='\n')

print("\nEnter x and y functions:")
x_func=input("x(t) = ")
y_func=input("y(t) = ")

def tick(pos):
    try:
        global button, tt, x_func, y_func, start_time, scale, speed
        tt+=0.1
        t=(time.time()*speed-start_time+start_value)
        x=t
        button.place(x=eval(x_func)*scale+pos[0]//2, y=eval(y_func)*scale+pos[1]//2)
        a=random.choice(name)
        exec(a+'=tkinter.Frame(root,width=1,heigh=1,bg=rancol(),bd=5)')
        exec(a+'.place(x=eval(x_func)*scale+pos[0]//2, y=eval(y_func)*scale+pos[1]//2)')
        button['bg']=rancol()
    except OverflowError:
        print('Overflow error: result is too large')

def z():
  while 1:
    g=root.geometry()
    pos=int(g[:g.find('x')]),int(g[g.find('x')+1:].split('+')[0])
    tick(pos)
    root.update()

start_time=time.time()
root=tkinter.Tk()
root['width']=800
root['height']=800
button=tkinter.Button(root, bg=rancol())
root.after(5, z)
root.mainloop()
#os.system('py')
input('Exit? (yes/YES)')
exit()
sys.exit(123)
os.abort()
