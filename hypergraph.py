# coding: utf-8
#

__version__ = "v0.2.0"

# Imports
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from threading import Thread
from math import *

import random
import sys
import os
import math
import cmath
import time
import __main__ as _

# Variables
k = 1 #8.9875517873681764*(10**9)
q = 0.5 #1.602176565*(10**(-19))
R = 0.1 #26*(10**(-11))
Qt = QtCore.Qt

tg = lambda x: math.sin(x)/math.cos(x)
ff = lambda x: ((modf(x)[0]+1)/2)**2
ctg = lambda x: 1/tg(x)
sec = lambda x: 1/cos(x)
cosec = lambda x: 1/sin(x)
versin = lambda x: 1-cos(x)
vers = versin
vercos = lambda x: 1-sin(x)
cvs = vercos
haversin = lambda x: versin(x)/2
hav = haversin
havercos = lambda x: vercos(x)/2
hac = havercos
exsec = lambda x: sec(x)-1
excsc = lambda x: cosec(x)-1
arcsin = math.asin
arccos = math.acos
arctg = lambda x: arcsin(x/(sqrt(1+x**2)))
arcctg = lambda x: arctg(1/x)
arcsec = lambda x: arccos(1/x)
arccosec = lambda x: arcsin(1/x)
a = lambda x, R = R, q = q, k = k: (k*((q*q)/((x-2*R)**2)))-(2*k*((q*q)/((x-R)**2)))
ln = lambda x: log(x, e)
sh = lambda x: (e**x-e**(-x))/2
ch = lambda x: (e**x+e**(-x))/2
th = lambda x: sh(x)/ch(x)
cth = lambda x: ch(x)/sh(x)
sech = lambda x: 1/ch(x)
csch = lambda x: 1/sh(x)
arsh = lambda x: ln(x+sqrt(x**2+1))
arch = lambda x: ln(x+sqrt(x**2-1))
arth = lambda x: ln((1+x)/(1-x))/2
arcth = lambda x: ln((x+1)/(x-1))/2
sqrt = lambda x: x**0.5
sgn = lambda x: abs(x)/x if x != 0 else 0
Im = lambda x: complex(x).imag
Re = lambda x: complex(x).real
r = True
flist = []

color = QColor(0, 0, 255)
black = QColor(0, 0, 0)
pen = lambda: QPen(color)
blackPen = QPen(black)
inf = 1e+1000000000

sizeX = [-10**300, 10**300]
sizeY = [-10**300, 10**300]
frequency = 300
center = 0, 0
cursor = QCursor()
LC = cursor.pos().x(), cursor.pos().y()
zoom = 6
isCoords = 0*(19102001-4082001)
b1 = 10
b2 = 10

# A's-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def dv(x, xbl):
    x=str(x)
    qwerty=0
    bbc=55
    n = """"""
    nn=str(n)
    xx=x[:x.find(""".""")]
    xxx="""0"""+x[x.find("""."""):]
    xx=int(xx)
    xxx=float(xxx)
    while xx > 0:
        y = str(xx % xbl)
        if int(y)>9:
            y=str(chr(bbc+int(y)))
        n = y + n
        xx = int(xx / xbl)
    yy=str(xxx)
    yyy=int(yy[(yy.find('.')+1):])
    while yyy!=0:
        qwerty=qwerty+1
        xxx=xxx*xbl
        yy=str(xxx)
        yx=int(yy[:yy.find('.')])
        if int(yx)>9:
            yx=str(chr(bbc+int(yx)))
        nn=nn+str(yx)
        if int(yy[:yy.find(""".""")])>0:
            xxx=float("""0"""+yy[yy.find("""."""):])
        yyy=int(yy[(yy.find(""".""")+1):])
        qwerty=qwerty+1
        if qwerty==32:
            qwerty=0
            break
    nnnn=(n+"""."""+nn)   
    return nnnn

def ndv(x,xb):
    qwerty=0
    bbc=55
    n = """"""
    x=int(x)

    while x > 0:
        y = str(x % xb)
        if int(y)>9:
            y=str(chr(bbc+int(y)))
        n = y + n
        x = int(x / xb)
    return n

def isnd(x, xx):
    xxx=int(x, base=xx)
    return xxx

def isd(x, xbl):
    bbc=55
    x=str(x)
    mm=0
    mmmm=0
    xx=x[:x.find('.')]
    xxx=x[x.find('.')+1:]
    i=1
    mm=isnd(xx, xbl)
    while xxx!='':
        mmm=xxx[0:1]
        
        if ord(mmm)>57:
            mmm=int(ord(mmm)-55)
        mmm=int(mmm)
        mmm=mmm*(xbl**(-i))
        mmmm=mmmm+mmm
        i=i+1
        xxx=xxx[1:]
        if i>16:
            break
    
    mmmm=str(mmmm)
    mmmm=mmmm.replace('.','')
    bnm=str(str(mm)+'.'+str(mmmm)[1:])
    return bnm
# No A's-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Functions
def ihyper2(x, a):
    '''Return x↑↑(1/a)'''
    def f(x):
        ans = 1
        for i in range(a):
            ans = x ** ans
        return ans
    l, r = 1/e, 144
    i = 0
    while r - l and i < 2100:
        i += 1
        q = (l + r) / 2
        try:
            if f(q) > x:
                r = q
            else:
                l = q
        except OverflowError:
            r = q
    if f(l) <= x:
        return l
    raise ValueError('no real x that x**x={}'.format(x))

def X(i, k):
	sum = 0
	for j in range(min(0, i), max(0, i)+1):
		sum += k**(j+(sgn(i)-1)/-2)*sgn(j)  #int(i<0)
	return sum

def F(x, k, start, end):
	sum = 0
	for i in range(start, end+1):
		sum += 2*k**(i)*((x-X(i, k))*(x-X(i+1, k))-abs((x-X(i, k))*(x-X(i+1, k))))/(2*X(i, k)*X(i+1, k)-X(i, k)**2-X(i+1, k)**2)
	return sum

def v(x, f=200):
    s = 0
    for i in range(f):
        s += modf(10**float(i)*x)[0]/10**float(i)
    return s
def r(x, f=200):
    s = 0
    for i in range(1, f):
        s += sin(i**2*x)/i**2
    return s
def w(x, r=False, a=5, b=0.5, f=200):
    if r:
        a = random.randint(1,3)*2+1
        b = int(random.random()*10)/10
    s = 0
    for i in range(f):
        s += b**i*cos(a**i*pi*x)
    return s

def wheelEvent(self, event):
    global grv
    plus_zoom = (2 ** 0.5) ** (event.angleDelta().y() / 240)
    grv.scale(plus_zoom, plus_zoom)

def plotGraph(function, From = -10, To = 10, frequency = frequency):
    try: From, To = eval(From), eval(To)
    except: From, To = -10, 10
    listX = [i/frequency for i in range(int(From*frequency), int(To*frequency))]
    listY = []
    funcY = lambda x: eval(function)
    _.flist.append(funcY)
    #try:
    #    funcY(random.random()*100+1)
    #except Exception as err:
    #    if type(err)==SyntaxError or type(err)==NameError or type(err)==TypeError:
    #        QMessageBox.warning(_.win, 'Ошибка в уравнении', 'Уравнение введено неверно! \nПовторите попытку ')
    #        return
    #    elif type(err)==ValueError or type(err)==ZeroDivisionError:
    #        pass
    m = 0
    for i in range(len(listX)):
        try: listY.append(-funcY(listX[i]))
        except: listY.append(None)
    '''for i in range(len(listX)):
        try:
            try:
                float(listY[i-m])
            except:
                listX.pop(i-m)
                listY.pop(i-m)
                m += 1
        except:
            pass'''
    for i in range(len(listX)):
        try:
            line = QtCore.QLineF(listX[i], listY[i], listX[i+1], listY[i+1])
            grs.addLine(line, slim_pen())
        except:
            pass

def plotGraphSlot(*args):
    plotGraph(win.lineEdit.text(), win.lineEdit_2.text(), win.lineEdit_3.text(), _.win.spinBox.value())

def clearGraphSlot(*args):
    globals()['flist'] = []
    for i in globals()['grs'].items():
        globals()['grs'].removeItem(i)
    _.grs.addLine(-1, 0.1, -1, -0.1, blackPen)
    _.grs.addLine(1, 0.1, 1, -0.1, blackPen)
    _.grs.addLine(0.1, 1, -0.1, 1, blackPen)
    _.grs.addLine(0.1, -1, -0.1, -1, blackPen)
    _.grs.addLine(0, sizeX[0], 0, sizeX[1], blackPen)
    _.grs.addLine(sizeY[0], 0, sizeY[1], 0, blackPen)


def helpSlot(*args):
    QMessageBox.information(_.win, 'Справка к программе ГиперГрафик', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">'\
                                   '<html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space:'\
                                   ' pre-wrap; }</style></head><body style=" font-family:\'MS Shell Dlg 2\'; font-size:8pt;'\
                                   ' font-weight:400; font-style:normal;"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px;'\
                                   ' margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;'\
                                   '">Справка к программе ГиперГрафик</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; '\
                                   'margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Для того, чтобы построить график '\
                                   'функции сначала</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px;margin-right:0px; -qt-block-indent:0;'\
                                   ' text-indent:0px;"><span style=" font-size:12pt;">введите функцию в поле </span><span style=" font-size:12pt; font-weight:600;">'\
                                   'y(x)=</span><span style=" font-size:12pt;">,</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;'\
                                   ' -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">затем отрезок значений </span><span style=" font-size:12pt; font-weight:600;'\
                                   '">x</span><span style=" font-size:12pt;">, точность пocтpoeня,</span></p><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px;'\
                                   ' margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">выберете цвет нажав кнопку <b>Цвет</b>,'\
                                   ' и нажмите </span><span style=" font-size:12pt; font-weight:600;">Enter</span></p></body></html>')

def setR(self, n = 255):
    color.setRed(n)

def calculator(self):
    a = _.win.geometry()
    _.win.setGeometry(a.x(), a.y(), a.x() + 303, a.y() + 60)

def setG(self, n = 255):
    color.setGreen(n)

def setB(self, n = 255):
    color.setBlue(n)

def setA(self, n = 255):
    color.setAlpha(n)

def CS(*args):
    _.isCoords = int(not _.isCoords)

def move(*args):
    if not (win.isVisible() or window.isVisible()):
        pass
        #exit()
    if _.isCoords:
      center = _.grv.mapToScene(_.grv.viewport().rect().center())
      z = -center.x(), -center.y()
      a = _.window.geometry().x()/_.zoom, (_.window.geometry().y())/_.zoom
      b = QCursor().pos().x()/_.zoom, QCursor().pos().y()/_.zoom
      c = _.grv.geometry().width()/_.zoom/2, _.grv.geometry().height()/_.zoom/2
      d = (int((b[0]-a[0]-c[0]-z[0])*10000)/10000, -int((b[1]-a[1]-c[1]-z[1])*10000)/10000)
      try:
        llll = '\n'
        for i in range(len(_.flist)):
          try:
            s=_.flist[i](float(d[0]))
            if s==0:
                s=0
            llll+="f"+str(i+1)+" = "+str(s)+"\n"
          except:
            llll+="f"+str(i+1)+" = "+''+"\n"
        llll = llll[:-1]
        QToolTip.showText(cursor.pos(), "x = {0}\ny = {1}{2}".format(str(d[0]), str(d[1]), llll), _.grv)
      except:
        QToolTip.showText(cursor.pos(), "x = {0}\ny = {1}".format(str(d[0]), str(d[1])), _.grv)

def rs(*args):
    _.win.raise_()

def op(*args):
    ll = [i for i in 'commandLinkButton centralwidget commandLinkButton_2 commandLinkButton_3'\
                      ' commandLinkButton_4 label_2 label_4 label_6 lblb lineEdit '\
                      'lineEdit_2 lineEdit_3 spinBox spinBox_2 spinBox_3 spinBox_4 spinBox_5'.split()]
    l = [int(eval('_.win.'+i+'.hasFocus()')) for i in ll]
    z = max(l)
    _.win.setWindowOpacity(0.75+0.25*z)

def tt():
    _.grv.timerEvent = move
    _.grv.startTimer(10)

def calc(*args):
    try:
        s = eval(_.win.lineEdit_4.text())
        _.win.lineEdit_5.setText(str(s))
        print(s)
    except:
        _.win.lineEdit_5.setText('Oшибкa')

def per(*args):
    try:
        s = _.win.lineEdit_6.text()
        if not s.find('.')+1:
            s+='.0'
        f = str(isd(s, _.b1))
        g = str(dv(f, _.b2))
        if g[-1]=='.':
            g = g.replace('.','')
            g+='.0'
            print(g)
        if g[-2]+g[-1]=='.0':
            g = g.replace('.0','')
            print(g)
        _.win.lineEdit_7.setText(str(g))
    except:
        _.win.lineEdit_7.setText('Oшибкa')

def setB1(*args):
    _.b1 = _.win.spinBox_6.value()

def setB2(*args):
    _.b2 = _.win.spinBox_7.value()

def setColor(*args):
    c = QColorDialog.getColor(QtCore.Qt.white, _.win, 'Цвет')
    r = c.red()
    g = c.green()
    b = c.blue()
    a = color.alpha()
    color.setRed(r)
    color.setGreen(g)
    color.setBlue(b)
    color.setAlpha(a)
    _.win.spinBox_2.setValue(r)
    _.win.spinBox_3.setValue(g)
    _.win.spinBox_4.setValue(b)
    _.win.spinBox_5.setValue(a)

def slim_pen(qcolor = None):
    if qcolor != None:
        return QtGui.QPen(qcolor, 0)
    return QtGui.QPen(color, 0)

def Core():
    _.icon = QIcon('icon.png')
    QGraphicsView.wheelEvent = wheelEvent
    QMainWindow.plotGraphSlot = plotGraphSlot
    QMainWindow.clearGraphSlot = clearGraphSlot
    QMainWindow.eggs = lambda a: _.grv.centerOn(0,0)
    QMainWindow.helpSlot = helpSlot
    QMainWindow.setColor = setR
    QMainWindow.setR = setR
    QMainWindow.setG = setG
    QMainWindow.setB = setB
    QMainWindow.setA = setA
    QMainWindow.setColor = setColor
    QMainWindow.CS = CS
    QMainWindow.s_enterom = calc
    QMainWindow.setB1 = setB1
    QMainWindow.setB2 = setB2
    QMainWindow.per = per
    QMainWindow.calculator = calculator

    _.window = QMainWindow()
    _.window.show()
    _.window.showMaximized()
    _.win = uic.loadUi('hypergraph.ui')
    _.win.show()
    _.win.lineEdit.setFocus()
    _.window.setWindowIcon(icon)
    _.win.setWindowIcon(icon)
    _.window.setWindowTitle('ГиперГрафик')
    _.grs = QGraphicsScene()
    _.grs.setSceneRect(sizeX[0], sizeY[0], abs(sizeX[0]-sizeX[1]), abs(sizeY[0]-sizeY[1]))
    _.grv = QGraphicsView(_.grs, _.window)
    _.window.setCursor(Qt.CrossCursor)
    _.win.timerEvent = rs
    _.win.startTimer(10)
    _.window.setCentralWidget(_.grv)
    _.grv.show()
    _.grv.setDragMode(_.grv.ScrollHandDrag)
    _.grv.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    _.grv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    _.grv.centerOn(0, 0)
    _.grv.scale(6, 6)
    _.grs.addLine(-1, 0.1, -1, -0.1, pen=slim_pen(QColor(0, 0, 0)))
    _.grs.addLine(1, 0.1, 1, -0.1, pen=slim_pen(QColor(0, 0, 0)))
    _.grs.addLine(0.1, 1, -0.1, 1, pen=slim_pen(QColor(0, 0, 0)))
    _.grs.addLine(0.1, -1, -0.1, -1, pen=slim_pen(QColor(0, 0, 0)))
    _.grv.startTimer(1)
    _.grv.timerEvent = op

    _.grs.addLine(0, sizeX[0], 0, sizeX[1], pen=slim_pen(QColor(0, 0, 0)))
    _.grs.addLine(sizeY[0], 0, sizeY[1], 0, pen=slim_pen(QColor(0, 0, 0)))
    for btnn in range(43):
        try:
            if btnn==0 or btnn==37 or btnn==39 or btnn == 41: continue
            s = 'pushButton_'+str(btnn)
            exec(("def insertF(a): import __main__ as _; _.win.lineEdit.setText((_.win.lineEdit.text()+self.text()[:self.text().find('(')+1]).replace('∏','product').replace('∑','summation').replace('√','root').replace('Г','gamma'))"\
                 ";_.win.lineEdit.setFocus()").replace('self', '_.win.'+s))
            exec('_.win.'+s+'.mousePressEvent = insertF')
        except: pass
    for btmn in list(range(44,82))+[41]:
        try:
            s = 'pushButton_'+str(btmn)
            exec(("def insertF(a): import __main__ as _; _.win.lineEdit_4.setText((_.win.lineEdit_4.text()+self.text()[:self.text().find('(')+1]).replace('∏','product').replace('∑','summation').replace('√','root').replace('Г','gamma'))"\
                 ";_.win.lineEdit_4.setFocus()").replace('self', '_.win.'+s))
            exec('_.win.'+s+'.mousePressEvent = insertF')
        except: pass

# Creating Application
app = QtWidgets.QApplication(sys.argv)

# Interface
Core()
tt()

# Starting Application
app.exec_()
isCoords = 0
