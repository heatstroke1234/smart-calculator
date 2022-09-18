from tkinter import*
import math
from sympy import *

rad = True
deg = False
#jvhy

w=Tk()
w.geometry("715x1000")

w.title("Scientific Calculator")


expression=""
equation = StringVar()

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equate():
    try:
        global deg
        global rad
        global expression
        if 'sin' in expression and 'asin' not in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            expint= eval(expint)


            if rad == True:
                answer= math.sin(expint)
            elif deg == True:
                expint= math.radians(float(expint))
                answer= math.sin(float(expint))
            
            
            equation.set(answer)
            expression=''
        elif 'tan' in expression and 'atan' not in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            
            expint=expression[start_index: end_index]
            expint= eval(expint)
            

            if rad == True:
                answer= math.tan(float(expint))
            elif deg== True:
                expint= math.radians(float(expint))
                answer= math.tan(float(expint))
            equation.set(answer)
            expression=''

        elif 'cos' in expression and 'acos' not in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            expint= eval(expint)

            if rad == True:
                
                answer= math.cos(float(expint))
            elif deg == True:
                expint= math.radians(float(expint))
                answer= math.cos(float(expint))
            
            equation.set(answer)
            expression=''
        elif 'cot' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            expint= eval(expint)

            if rad == True:
                print(expint)
                answer= 1/(math.tan(float(expint)))
                print(answer)
            elif deg == True:
                expint= math.radians(float(expint))
                answer= 1/math.tan((float(expint)))
            
            equation.set(answer)
            expression=''

        elif 'asin' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            expint=eval(expint)

            if rad == True:
                print(expint)
                answer= math.asin(float(expint))
            elif deg == True:
                answer= math.asin(float(expint))
                answer=math.degrees(answer)
            
            
            print(answer)
            equation.set(answer)
            expression=''
        elif 'atan' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            expint=eval(expint)

            if rad == True:
                answer= math.atan(float(expint))
            else:
                answer= math.atan(float(expint))
                answer=math.degrees(answer)
            
            
            equation.set(answer)
            expression=''

        elif 'acos' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            expint=eval(expint)

            if rad == True:
                answer= math.acos(float(expint))
            else:
                answer= math.acos(expint)
                answer=math.degrees(float(answer))
            
            
            equation.set(answer)
            expression=''
       
        elif 'log' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(','))
            start_index_1=int(expression.rfind(',')+1)
            end_index_1 = int(expression.rfind(')'))
            x=expression[start_index:end_index]
            base=expression[start_index_1: end_index_1]
          
            answer= math.log(float(x), float(base))
            print(answer)
            equation.set(answer)
            expression=''
        elif 'abs' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            
            answer= math.fabs(float(expint))
            equation.set(answer)
            expression=''

        elif 'fact' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            
            answer= math.factorial(float(expint))
            equation.set(answer)
            expression=''

        elif 'sqrt' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            
            answer= math.sqrt(float(expint))
            equation.set(answer)
            expression=''
        elif 'rad' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            
            answer= math.radians(float(expint))
            equation.set(answer)
            expression=''
            
        elif 'deg' in expression:
            start_index=int(int(expression.rfind('('))+1)
            end_index=int(expression.rfind(')'))
            expint=expression[start_index: end_index]
            
            answer= math.degrees(float(expint))
            equation.set(answer)
            expression=''
            
            

        
          
            
        else:
            total = str(eval(expression))
            print(total)
            equation.set(total)
            expression=''

    
    except:
        equation.set('error')
        expression = ''

        
def clear():
    global expression
    expression=''
    equation.set('')

def pi():
    global expression
    expression += str(math.pi)
    equation.set(expression)
def exponent():
    global expression
    expression += '**'
    equation.set(expression)

def sin():
    global expression
    expression += 'sin'
    equation.set(expression)

def cos():
    global expression
    expression += 'cos'
    equation.set(expression)

def tan():
    global expression
    expression += 'tan'
    equation.set(expression)

def cot():
    global expression
    expression += 'cot'
    equation.set(expression)

def log():
    global expression
    expression += 'log'
    equation.set(expression)
def comma():
    global expression
    expression += ','
    equation.set(expression)

def e():
    global expression
    expression+= str(math.e)
    equation.set(expression)

def asin():
    global expression
    expression+= 'asin'
    equation.set(expression)
    
def acos():
    global expression
    expression += 'acos'
    equation.set(expression)

def atan():
    global expression
    expression += 'atan'
    equation.set(expression)

def x():
    global expression
    expression+='x'
    equation.set(expression)

def bspace():
    global expression
    temp = expression[0:len(expression)-1]
    expression = temp
    equation.set(expression)

def rem():
    global expression
    expression+='%'
    equation.set(expression)

def absv():
    global expression
    expression+= 'abs'
    equation.set(expression)

def fact():
    global expression
    expression+= 'fact'
    equation.set(expression)

def sqrt():
    global expression
    expression+= 'sqrt'
    equation.set(expression)

def rad():
    global rad
    global deg
    rad = True
    deg = False

def deg():
    global deg
    global rad
    deg = True
    rad = False

def dif():
    global expression
    
    expression = expression.replace("^", "**")
    if (expression[len(expression)-1] == 'x'):
        expression = expression + '+0'

    for element in range(1, len(expression)):
        if(expression[element - 1].isdigit() and expression[element] == 'x'):
            temp = expression[0: element] + "*" + expression[element: len(expression)]
            expression= temp  
    x = Symbol('x')
   
    
    
    expression=diff(expression, x)
        
    equation.set(nsimplify(expression, tolerance=0.001))

def intg():
    global expression
    
    expression = expression.replace("^", "**")
    if (expression[len(expression)-1] == 'x'):
        expression = expression + '+0'

    for element in range(1, len(expression)):
        if(expression[element - 1].isdigit() and expression[element] == 'x'):
            temp = expression[0: element] + "*" + expression[element: len(expression)]
            expression= temp  
    x = Symbol('x')
   
    
    
    expression=integrate(expression, x)
    expression=nsimplify(expression, tolerance=0.001)
    #1457/536
    if '(1457/536)' in str(expression):
        str(expression).replace('(1457/536)','e')
        
    equation.set(nsimplify(expression, tolerance=0.001))
    
    
    
    

def roots():
    global expression
    
    expression = expression.replace("^", "**")
    if (expression[len(expression)-1] == 'x'):
        expression = expression + '+0'

    for element in range(1, len(expression)):
        if(expression[element - 1].isdigit() and expression[element] == 'x'):
            temp = expression[0: element] + "*" + expression[element: len(expression)]
            expression= temp  
    x = Symbol('x')
    solve_list = solve(expression, x)
    newlist=[]
    for x in range(len(solve_list)):
        newlist.append(nsimplify(solve_list[x], tolerance=0.001))
        
    equation.set(newlist)
    
    
    
    
    

expression_field = Entry(w,textvariable=equation, font=('Arial',18), width=50, bg='ivory3')
expression_field.grid(column=1,columnspan=8)
equation.set("Enter your expression")

b0= Button(w, text='0',padx=20, pady=10, command= lambda: press(0), bg="white", fg="black",width=2, font=14)
b0.grid(row=4, column=2,)

b1= Button(w, text='1',padx=20, pady=10, command= lambda: press(1), bg="white", fg="black",width=2, font=14)
b1.grid(row=1, column=1)

b2= Button(w, text='2',padx=20,pady =10,  command= lambda: press(2), bg="white", fg="black", width=2, font=14)
b2.grid(row=1, column=2)

b3= Button(w, text='3', padx=20, pady=10, command= lambda: press(3), bg="white", fg="black",width=2, font=14)
b3.grid(row=1, column=3)

b4= Button(w, text='4', padx=20, pady=10, command= lambda: press(4), bg="white", fg="black",width=2, font=14)
b4.grid(row=2, column=1)

b5 = Button(w, text='5', padx = 20, pady = 10, command= lambda: press(5), bg="white", fg="black",width=2, font=14)
b5.grid(row=2,column=2)

b6= Button(w, text='6', padx=20, pady=10, command= lambda: press(6), bg="white", fg="black",width=2, font=14)
b6.grid(row=2, column=3)

b7= Button(w, text='7', padx=20, pady=10, command= lambda: press(7), bg="white", fg="black",width=2, font=14)
b7.grid(row=3, column=1)

b8= Button(w, text='8', padx=20, pady=10, command= lambda: press(8), bg="white", fg="black",width=2, font=14)
b8.grid(row=3, column=2)

b9= Button(w, text='9', padx=20, pady=10, command= lambda: press(9), bg="white", fg="black",width=2, font=14)
b9.grid(row=3, column=3)

bc= Button(w, text= 'C', padx=20, pady =10, command= clear, bg="firebrick1", fg='black',width=2, font=14)
bc.grid(row=4, column=1)

bdot= Button(w, text='.', padx=20, pady =10, command= lambda: press('.'), bg="grey", fg='black',width=2, font=14)
bdot.grid(row=4, column=3)

bob= Button(w, text='(', padx=20, pady =10, command= lambda: press('('), bg="grey", fg='black',width=2, font=14)
bob.grid(row=5, column=1)

bcb= Button(w, text=')', padx=20, pady =10, command= lambda: press(')'), bg="grey", fg='black',width=2, font=14)
bcb.grid(row=5, column=2)

bsin= Button(w, text='pi', padx=20, pady =10, command= pi, bg="azure", fg='black',width=2, font=14)
bsin.grid(row=3, column=7)

bplus=Button(w,text="+",padx=20,pady=10,command=lambda:press('+'),bg="grey", fg='black',width=2, font=14)
bplus.grid(row=1,column=4)

bmin=Button(w,text="-",padx=20,pady=10,command=lambda:press("-"),bg="grey", fg='black',width=2, font=14)
bmin.grid(row=2,column=4)

bdiv=Button(w,text="/",padx=20,pady=10,command=lambda:press("/"),bg="grey", fg='black',width=2, font=14)
bdiv.grid(row=3,column=4)

bmul=Button(w,text="*",padx=20,pady=10,command=lambda:press("*"),bg="grey", fg='black',width=2, font=14)
bmul.grid(row=4,column=4)

beq=Button(w,text="=",padx=20,pady=10,command=equate,bg="SteelBlue1", fg='black',width=2, font=14)
beq.grid(row=5,column=3)

bexp=Button(w,text="^",padx=20,pady=10,command=exponent,bg="grey", fg='black',width=2, font=14)
bexp.grid(row=1,column=5)

bsin=Button(w,text="sin",padx=20,pady=10,command=sin,bg="lemon chiffon", fg='black',width=2, font=14)
bsin.grid(row=2,column=5)

bcos=Button(w,text="cos",padx=20,pady=10,command=cos,bg="lemon chiffon", fg='black',width=2, font=14)
bcos.grid(row=3,column=5)

btan=Button(w,text="tan",padx=20,pady=10,command=tan,bg="lemon chiffon", fg='black',width=2, font=14)
btan.grid(row=4,column=5)

bcot=Button(w,text="cot",padx=20,pady=10,command=cot,bg="lemon chiffon", fg='black',width=2, font=14)
bcot.grid(row=5,column=5)

blog=Button(w,text="log",padx=20,pady=10,command=log,bg="grey", fg='black',width=2, font=14)
blog.grid(row=1,column=6)

bcom=Button(w,text=",",padx=20,pady=10,command=comma,bg="grey", fg='black',width=2, font=14)
bcom.grid(row=2,column=6)

be=Button(w,text="e",padx=20,pady=10,command=e,bg="azure", fg='black',width=2, font=14)
be.grid(row=1,column=7)

basin=Button(w,text="asin",padx=20,pady=10,command=asin,bg="peach puff", fg='black',width=2, font=14)
basin.grid(row=4,column=6)

bacos=Button(w,text="acos",padx=20,pady=10,command=acos,bg="peach puff", fg='black',width=2, font=14)
bacos.grid(row=5,column=6)

batan=Button(w,text="atan",padx=20,pady=10,command=atan,bg="peach puff", fg='black',width=2, font=14)
batan.grid(row=3,column=6)


bx=Button(w,text="x",padx=20,pady=10,command=x,bg="azure", fg='black',width=2, font=14)
bx.grid(row=2,column=7)

broots=Button(w,text="roots",padx=20,pady=10,command=roots,bg="SteelBlue1", fg='black',width=2, font=14)
broots.grid(row=5,column=4)

bspace=Button(w,text="<x|",padx=20,pady=10,command=bspace,bg="firebrick1", fg='black',width=2, font=14)
bspace.grid(row=4,column=7)

brem=Button(w,text="%",padx=20,pady=10,command=rem,bg="grey", fg='black',width=2, font=14)
brem.grid(row=5,column=7)

babs=Button(w,text="abs",padx=20,pady=10,command=absv,bg="grey", fg='black',width=2, font=14)
babs.grid(row=1,column=8)

bfact=Button(w,text="fact",padx=20,pady=10,command=fact,bg="grey", fg='black',width=2, font=14)
bfact.grid(row=2,column=8)

bsqrt=Button(w,text="sqrt",padx=20,pady=10,command=sqrt,bg="grey", fg='black',width=2, font=14)
bsqrt.grid(row=3,column=8)

brad=Button(w,text="rad",padx=20,pady=10,command=rad,bg="grey", fg='black',width=2, font=14)
brad.grid(row=4,column=8)


bdeg=Button(w,text="deg",padx=20,pady=10,command=deg,bg="grey", fg='black',width=2, font=14)
bdeg.grid(row=5,column=8)

bdif=Button(w,text="dif",padx=20,pady=10,command=dif,bg="grey", fg='black',width=2, font=14)
bdif.grid(row=1,column=9)

bintg=Button(w,text="intg",padx=20,pady=10,command=intg,bg="grey", fg='black',width=2, font=14)
bintg.grid(row=2,column=9)


score=0          
q1flag=0
q2flag=0
q3flag=0
q4flag=0
q5flag=0


def rightanswer1():
    global score
    global q1flag
    if q1flag==0:
        score+=1
        slabel.config(text="score= "+str(score))
        '''right=Label(w,text="Correct answer",bg="green")
        right.grid(row=18,column=2,padx=20,pady=20)'''
        q1flag=1
        q1a=Button(w,text="a)0.9613",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q1c=Button(w,text="c)-0.9851",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q1d=Button(w,text="d)0.1236",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q1b=Button(w,text="a)4.22,1.55",command=rightanswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='seagreen2')
        q1a.grid(row=11,column=1)
        q1b.grid(row=11,column=2)
        q1c.grid(row=11,column=3)
        q1d.grid(row=11,column=4)

def rightanswer2():
    global score
    global q2flag
    if q2flag==0:
        score+=1
        slabel.config(text="score= "+str(score))
        '''right=Label(w,text="Correct answer",bg="green")
        right.grid(row=18,column=2,padx=20,pady=20)'''
        q2flag=1
        q2a=Button(w,text="a)Cos(7deg)",command=rightanswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='seagreen2')
        q2b=Button(w,text="b)Cos(4deg)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q2c=Button(w,text="c)Cos(3rad)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q2d=Button(w,text="c)Tan(3rad)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')        
        q2a.grid(row=14,column=1)
        q2b.grid(row=14,column=2)
        q2c.grid(row=14,column=3)
        q2d.grid( row=14,column=4)

def rightanswer3():
    global score
    global q3flag
    if q3flag==0:
        score+=1
        slabel.config(text="score= "+str(score))
        '''right=Label(w,text="Correct answer",bg="green")
        right.grid(row=18,column=2,padx=20,pady=20)'''
        q3flag=1
        q3a=Button(w,text="a)17.626",command=wronganswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q3b=Button(w,text="b)-18.668",command=rightanswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='seagreen2')
        q3c=Button(w,text="c)-17.628",command=wronganswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q3d=Button(w,text="d)18.668",command=wronganswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')         
        q3a.grid(row=17,column=1)
        q3b.grid(row=17,column=2)
        q3c.grid(row=17,column=3)
        q3d.grid(row=17,column=4)
        
        

'''def rightanswer4():
    global score
    global q4flag
    if q4flag==0:
        score+=1
        slabel.config(text="score= "+str(score))
        right=Label(w,text="Correct answer",bg="green")
        right.grid(row=25,column=2)
        q4flag=1
'''
def rightanswer5():
    global score
    global q5flag
    if q5flag==0:
        score+=1
        slabel.config(text="score= "+str(score))
        '''right=Label(w,text="Correct answer",bg="green")
        right.grid(row=25,column=2)'''
        q5flag=1
        q5a=Button(w,text="a)4.22,1.55",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q5b=Button(w,text="b)1.36,-0.36",command=rightanswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='seagreen2')
        q5c=Button(w,text="c)2.66,1.34",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
        q5d=Button(w,text="d)3.214,1.33",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')         
        q5a.grid(row=23,column=1)
        q5b.grid(row=23,column=2)
        q5c.grid(row=23,column=3)
        q5d.grid(row=23,column=4)    


    

def wronganswer1():
    global score
    '''wrong=Label(w,text="Wrong answer",bg="Red")
    wrong.grid(row=18,column=2,padx=20,pady=20)'''
    q1a=Button(w,text="a)0.9613",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q1c=Button(w,text="c)-0.9851",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q1d=Button(w,text="d)0.1236",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q1b=Button(w,text="a)4.22,1.55",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='seagreen2')
    q1a.grid(row=11,column=1)
    q1b.grid(row=11,column=2)
    q1c.grid(row=11,column=3)
    q1d.grid(row=11,column=4)

def wronganswer2():
    global score
    '''wrong=Label(w,text="Wrong answer",bg="Red")
    wrong.grid(row=18,column=2,padx=20,pady=20)'''
    q2a=Button(w,text="a)Cos(7deg)",command=rightanswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='seagreen2')
    q2b=Button(w,text="b)Cos(4deg)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q2c=Button(w,text="c)Cos(3rad)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q2d=Button(w,text="c)Tan(3rad)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')        
    q2a.grid(row=14,column=1)
    q2b.grid(row=14,column=2)
    q2c.grid(row=14,column=3)
    q2d.grid( row=14,column=4)

def wronganswer3():
    global score
    '''wrong=Label(w,text="Wrong answer",bg="Red")
    wrong.grid(row=18,column=2,padx=20,pady=20)'''
    q3a=Button(w,text="a)17.626",command=wronganswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q3b=Button(w,text="b)-18.668",command=rightanswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='seagreen2')
    q3c=Button(w,text="c)-17.628",command=wronganswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q3d=Button(w,text="d)18.668",command=wronganswe3r3,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')         
    q3a.grid(row=17,column=1)
    q3b.grid(row=17,column=2)
    q3c.grid(row=17,column=3)
    q3d.grid(row=17,column=4)



def wronganswer5():
    global score
    '''wrong=Label(w,text="Wrong answer",bg="Red")
    wrong.grid(row=18,column=2,padx=20,pady=20)'''
    q5a=Button(w,text="a)4.22,1.55",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q5b=Button(w,text="b)1.36,-0.36",command=rightanswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='seagreen2')
    q5c=Button(w,text="c)2.66,1.34",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')
    q5d=Button(w,text="d)3.214,1.33",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='firebrick1')         
    q5a.grid(row=23,column=1)
    q5b.grid(row=23,column=2)
    q5c.grid(row=23,column=3)
    q5d.grid(row=23,column=4)        


    
q=Label(w,text= "QUIZ",font=('Arial', 14), bg='lightgoldenrod')
q1=Label(w,text="Q1)Evaluate the sine of 47 degrees",font=('Arial', 10), bg='papaya whip')
q2=Label(w,text="Q2)Which of the following equals 0.9925",font=('Arial', 10), bg='papaya whip')
q3=Label(w,text="Q3)Evaluate 1.03-9.8*2.01",font=('Arial', 10), bg='papaya whip')
#q4=Label(w,text="Q4)Calculate how many seconds there are in 19 full days",font=('Arial', 10), bg='papaya whip')
q5=Label(w,text="Q4)Find the roots for the following equation:2x^2 -2x -1 = 0",font=('Arial', 10), bg='papaya whip')

slabel=Label(w,text="score= "+str(score))
slabel.grid(row=24,column=1)

q.grid(row=8,column=1, columnspan=1)
q1.grid(row=10,column=1,columnspan=3)
q2.grid(row=13,column=1,columnspan=3)
q3.grid(row=16,column=1,columnspan=2)
#q4.grid(row=19,column=1, columnspan=4)
q5.grid(row=22,column=1,columnspan=4)

q1a=Button(w,text="a)0.9613",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q1b=Button(w,text="b)0.7314",command=rightanswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q1c=Button(w,text="c)-0.9851",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q1d=Button(w,text="d)0.1236",command=wronganswer1,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')

q1a.grid(row=11,column=1)
q1b.grid(row=11,column=2)
q1c.grid(row=11,column=3)
q1d.grid(row=11,column=4)

q2a=Button(w,text="a)Cos(7deg)",command=rightanswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q2b=Button(w,text="b)Cos(4deg)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q2c=Button(w,text="c)Cos(3rad)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q2d=Button(w,text="d)Tan(3rad)",command=wronganswer2,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')        
        


q2a.grid(row=14,column=1)
q2b.grid(row=14,column=2)
q2c.grid(row=14,column=3)
q2d.grid( row=14,column=4)       

q3a=Button(w,text="a)17.626",command=wronganswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q3b=Button(w,text="b)-18.668",command=rightanswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q3c=Button(w,text="c)-17.628",command=wronganswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q3d=Button(w,text="d)18.668",command=wronganswer3,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')        
        

q3a.grid(row=17,column=1)
q3b.grid(row=17,column=2)
q3c.grid(row=17,column=3)
q3d.grid(row=17,column=4)        

'''q4a=Button(w,text="a)1926400",command=wronganswer,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q4b=Button(w,text="b2384526)",command=wronganswer,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q4c=Button(w,text="c)1735268",command=wronganswer,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q4d=Button(w,text="d)1641600",command=rightanswer4,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')        
        

q4a.grid(row=20,column=1)
q4b.grid(row=20,column=2)
q4c.grid(row=20,column=5)
q4d.grid(row=20,column=7)'''        

q5a=Button(w,text="a)4.22,1.55",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q5b=Button(w,text="b)1.36,-0.36",command=rightanswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q5c=Button(w,text="c)2.66,1.34",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')
q5d=Button(w,text="d)3.214,1.33",command=wronganswer5,padx=20,pady=20,width=2,font=('Arial', 10), bg='ivory3')        

q5a.grid(row=23,column=1)
q5b.grid(row=23,column=2)
q5c.grid(row=23,column=3)
q5d.grid(row=23,column=4)        






