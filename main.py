import random
from math import *
import time
import sympy as sym
from PIL import Image
import pyttsx3 # have to install this and pypiwin32
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sympy import *
from IPython.display import display, Math, Latex
from threading import Timer
from colorama import Fore, Back, Style, init
import cv2

def basic():
    print(Back.BLACK + Fore.RED + 'This will include questions that are to be solved using Vedic Maths in a given time limit')
    print(Fore.RED+Back.BLACK+'These will help you develop your speed of calculation')
    eng.say('This will include questions that are to be solved using Vedic Maths in a given time limit and they will help you develop your speed of calculation')
    eng.runAndWait()
    print(Fore.BLUE + Back.BLACK+'You will have 60 seconds to attempt each question')
    eng.say('You will have 60 seconds to attempt each question')
    eng.runAndWait()
    while True:
        time.sleep(1)
        print(Fore.GREEN + Back.BLACK + "1 --> Double Digit Multiplication; 2 --> Multiplication of a two-digit number by 11... ; 3 --> Go Back")
        eng.say('Type one of the following options. 1 Double Digit Multiplication; 2 Multiplication by number of the form 11; 3 Go Back')
        eng.runAndWait()
        print( Fore.GREEN + Back.BLACK +"Choose one of the following options.")
        choice = int(input())
        if choice== 1: dd()
        if choice== 2: elev()
        if choice== 3: break

def dd():
    print(Back.BLACK +'Do you know about various tricks which are given by Vedic Maths?')
    eng.say('Do you know about various tricks which are given by Vedic Maths?')
    eng.runAndWait()
    print(Fore.RED + Back.BLACK + """
    We are going to learn about one of the basic rules of vedic maths.""" + Fore.BLUE + Back.BLACK + """
    This involves multiplication of two digit numbers.
    Say you have any two digit numbers : ab and cd, where a is in tenth place of number "ab" and b is in ones place, similarly for "cd".
    So the trick is to take the ones digit of both numbers and multiply it (i.e. b x d) and write the ones digit of their product as the ones digit of a new number.
    And carry forward the tens place digit.""" )
    print(Fore.GREEN + """
    Now take the product of "a" and "d" and add it to the product of "b" and "c" (i.e. a x d + b x c).
    Now you need to add the tens place digit of the number obtained on multiplying "b" and "d".
    now take the ones place digit of the number obtained and put it in the tens place of the number and carry forward the tens place digit.
    Now multiply a and c (i.e. a x c) and add the tens place digit that was obtained in the previous step, now write the obtained number in the hundreds place of the new number.
    The number that you have now obtained is the product of ab and cd.)""")

    eng.say("We are going to learn about one of the basic rules of vedic maths.")
    eng.runAndWait()
    eng.say("This involves multiplication of two digit numbers.")
    eng.say("Say you have any two digit numbers : ab and cd, where a is in tenth place of number 'ab' and b is in ones place, similarly for 'cd'.")
    eng.runAndWait()
    eng.say("So the trick is to take the ones digit of both numbers and multiply it (i.e. b x d) and write the ones digit of their product as the ones digit of a new number.")
    eng.runAndWait()
    eng.say("And carry forward the tens place digit.")
    eng.runAndWait()
    eng.say("Now take the product of 'a' and 'd' and add it to the product of 'b' and 'c'")
    eng.runAndWait()
    eng.say("Now you need to add the tens place digit of the number obtained on multiplying 'b' and 'd'.")
    eng.runAndWait()
    eng.say("now take the ones place digit of the number obtained and put it in the tens place of the number and carry forward the tens place digit.")
    eng.runAndWait()
    eng.say("Now multiply a and c and add the tens place digit that was obtained in the previous step, now write the obtained number in the hundreds place of the new number.")
    eng.runAndWait()
    eng.say("The number that you have now obtained is the product of a b and c d.")
    eng.runAndWait()

    time.sleep(1)
    print()
    scr = 0
    while True:
        for i1 in range(4):
            no1 = floor(random.uniform(10, 99))
            no2 = floor(random.uniform(10, 99))
            print( Style.DIM +'Find the product when',no1,'is multiplied by',no2)
            eng.say('Find the product on multiplication of: ')
            eng.runAndWait()
            eng.say(no1)
            eng.runAndWait()
            eng.say('and')
            eng.runAndWait()
            eng.say(no2)
            eng.runAndWait()
            eng.say("Enter the answer . If you don't know just press enter")
            eng.runAndWait()
            right_answer = no1 * no2
            #t= Timer(60, time_up) #x is amount of allowed time in seconds then execute the provided function
            #t.start() #start the timerx = np.linspace(-2,2,100)
            ans = input('Enter the answer, if you dont know it just press enter: ')
            if ans == str(right_answer):
                #t.cancel()
                scr += 1
                print( Fore.GREEN +'Well Done! Your answer is correct')
                eng.say('Well Done! Your answer is correct')
                eng.runAndWait()
            elif ans == "":
                #t.cancel()
                print(Back.BLACK + "The correct answer is {}".format(right_answer))
                eng.say("The correct answer is {}".format(right_answer))
                eng.runAndWait()
            elif ans != str(right_answer):
                #t.cancel()
                print(Back.BLACK + 'Sorry, incorrect answer')
                eng.say('Sorry, incorrect answer')
                eng.runAndWait()
                print(Back.BLACK + 'The correct answer is {}'.format(no1 * no2))
                eng.say('The correct answer is {}'.format(no1 * no2))
                eng.runAndWait()
            print()
        break
    print("You got {} questions right out of 4".format(scr))
    perc = ((int(scr)/4)*100)
    if perc >= 75:
        print("Which means you scored" + Fore.CYAN + " {} %".format(perc))
        print(Fore.GREEN + "WOW !! Nice Score")
    else:
        print("You have scored {} percentage".format(perc))
        print("We know that you can score better."+ Fore.RED +"You should try again")

def elev():
    print(Back.BLACK +'Do you know about various tricks which are given by Vedic Maths?')
    eng.say('Do you know about various tricks which are given by Vedic Maths?')
    eng.runAndWait()
    print( Fore.RED + Back.BLACK +"""
    We will learn about the a trick to ease our calculations when we multiply any 2-digit number by 11.
    When we multiply a 2-digit number for example-43 by 11,using the trick the answer comes out to be 473.
    Let us see how,
    The tens digit(4) of the multiplicant is placed at hundreds place of the product and ones digit (3) of
    the multiplicant is placed at the ones place of product.The sum of the digits of multiplicant is placed
    at tens place in the product.
    Let's take another case our numbers are 67 and 11,
    Here, we will proceed with same steps, the answer will be 737.
    But as we proceed with the 2nd step,the sum of multiplicants (6+7) is 13.So, we put the ones digit(3) at tens place
    and tens digit(1) will be added to the hundreds digit of the answer(6+1)37.
    """)
    eng.say('''We will learn about the a trick to ease our calculations when we multiply any 2-digit number by 11.
    When we multiply a 2-digit number for example-43 by 11,using the trick the answer comes out to be 473.
    Let us see how,
    The tens digit(4) of the multiplicant is placed at hundreds place of the product and ones digit (3) of
    the multiplicant is placed at the ones place of product.The sum of the digits of multiplicant is placed
    at tens place in the product.
    Let's take another case our numbers are 67 and 11,
    Here, we will proceed with same steps, the answer will be 737.
    But as we proceed with the 2nd step,the sum of multiplicants (6+7) is 13.So, we put the ones digit(3) at tens place
    and tens digit(1) will be added to the hundreds digit of the answer(6+1)37.''')
    eng.runAndWait()
    time.sleep(4)
    eng.say('Let\'s Practice')
    eng.runAndWait()
    print( Fore.GREEN +"Let's Practice")
    time.sleep(2)
    scr1 = 0
    while True:
        for ii in range(4):
            no3 = floor(random.uniform(11, 100))
            print( Back.BLACK + Fore.MAGENTA +  'Find the product when', no3,'is multiplied by 111')
            eng.say('Find the product when')
            eng.runAndWait()
            eng.say(no3)
            eng.runAndWait()
            eng.say('is multiplied by 111')
            eng.runAndWait()
            eng.say('Enter the answer. If you dont know just press enter: ')
            eng.runAndWait()
            ans = input("Enter the answer. If you dont know just press enter:")
            # t = Timer(60, time_up) # x is amount of allowed time in seconds then execute the provided function
            # t.start() #start the timer
            rgtans = no3 * 111
            if ans == str(rgtans):
                # t.cancel()
                scr1 += 1
                print( Back.BLACK + 'Well Done! Your answer is correct')
                eng.say('Well Done! Your answer is correct')
                eng.runAndWait()
            elif ans == "":
                print( Back.BLACK + "The correct answer is {}".format(rgtans))
                eng.say("The correct answer is {}".format(rgtans))
                eng.runAndWait()
            elif ans != str(rgtans) :
                # t.cancel()
                print( Fore.RED +'Your answer is incorrect')
                eng.say('Your answer is incorrect')
                eng.runAndWait()
                print( Fore.GREEN + 'The correct answer is', rgtans)
                eng.say('The correct answer is')
                eng.runAndWait()
                eng.say(rgtans)
                eng.runAndWait()



            print()

        break
    print("You got {} questions right out of 4".format(scr1))
    perc1 = ((int(scr1)/4)*100)
    if perc1 >= 75:
        print("Which means you scored" + Fore.CYAN + " {} %".format(perc1))
        print(Fore.GREEN + "WOW !! Nice Score")
    else:
        print("You have scored {} percentage".format(perc1))
        print("We know that you can score better."+ Fore.RED +"You should try again")

# def linear():
#     print(Fore.RED + 'These questions will test your basic knowledge of Linear Equations')
#     print(Fore.RED + 'A linear equation of the form ax + by + c will be given')
#     eng.say('These questions will test your basic knowledge of Linear Equations. A linear equation of the form ax + by + c will be given')
#     eng.runAndWait()
#     print(Style.DIM + 'You have to find the value of x only')
#     eng.say('You have to find the value of x only')
#     eng.runAndWait()
#     time.sleep(2)
#     scr2 = 0
#     while True:
#         for i in range(4):
#             num1 = floor(random.uniform(-10, 10))
#             num2 = floor(random.uniform(-10, 10))
#             con = floor(random.uniform(-10, 10))
#             var = floor(random.uniform(-10, 10))
#             sym.init_printing()
#             x,y = sym.symbols('x,y')
#             a = sym.Eq(num1*x + num2*y + con,0)
#             b = sym.Eq((num1+var)*x + num2*var*y + (con/var),0)
#             d = {}
#             d = sym.solve([a,b],(x,y))
#             print( Style.DIM + 'equation 1 is', num1,x, '+', num2,y, '+', con, '=', '0')
#             eng.say('equation 1 is')
#             eng.runAndWait()
#             eng.say(num1)
#             eng.runAndWait()
#             eng.say('x plus')
#             eng.runAndWait()
#             eng.say(num2)
#             eng.runAndWait()
#             eng.say('y plus')
#             eng.runAndWait()
#             eng.say(con)
#             eng.runAndWait()
#             eng.say('equal to zero')
#             eng.runAndWait()
#             print( Back.BLACK + 'equation 2 is', (num1+var),x, '+', (num2*var)+y, '+', con/var, '=', '0')
#             print( Fore.CYAN + 'Enter the value of x')
#             #display(Math(r'nudef cg():
#     print( Back.BLACK + 'These questions will test your basic knowledge of Coordinate Geometry more specifically the section formula')
#     print( Back.BLACK + 'The coordinates of the two end points and the ratio with which the line is internally divided will be given')
#     print( Back.BLACK + 'You have to find the coordinates of the point which divides the line internally in the given ratio')
#     scr3 = 0
#     while True:
#         for i2 in range(4):
#             x1 = floor(random.uniform(-10, 10))
#             x2 = floor(random.uniform(-10, 10))
#             y1 = floor(random.uniform(-10, 10))
#             y2 = floor(random.uniform(-10, 10))
#             m = floor(random.uniform(-10, 10))
#             n = floor(random.uniform(-10, 10))
#             lmb = lambda x1,x2,m,n : (x1*n + x2*m)/m+n
#             lmb1 = lambda y1,y2,m,n : (y1*n + y2*m)/m+n
#             print(Fore.CYAN + 'coordinates of point1 are', '(',x1,',',y1,')')
#             print( Fore.CYAN + 'coordinates of point2 are', '(',x2,',',y2,')')
#             print( Back.BLACK +'The line is internally divided in a ratio of m:n where m = {} and n = {}'.format(m,n))
#             x3 = int(input('Enter the x coordinate of point '))
#             y3 = int(input('Enter the y coordinate of point '))
#             kaw = floor(lmb(x1,x2,m,n))
#             koo = floor(lmb1(y1,y2,m,n))
#             t= Timer(120, time_up) #x is amount of allowed time in seconds then execute the provided function
#             t.start() #start the timer
#             if x3 == kaw and y3 == koo:
#                 t.cancel()
#                 scr3 += 1
#                 print( Fore.GREEN + 'Good Job! Your answer is correct')
#                 eng.say('Good Job! Your answer is correct')
#                 eng.runAndWait()
#             else :
#                 t.cancel()
#                 print( Style.DIM + 'Your answer is incorrect')
#                 eng.say('Your answer is incorrect')
#                 eng.runAndWait()
#                 print( Fore.YELLOW + 'The correct answer is, x coordinate = {} and y coordinate = {}'.format(kaw, koo))
#                 eng.say('The correct answer is, x coordinate = {} and y coordinate = {}'.format(kaw, koo))
#                 eng.runAndWait()
#             print()
#             time.sleep(5)
#         break
#     print('You got {} questions right out of 4'.format(scr3))
#     perc3 = int((scr3)/4)*100
#     if perc3 >= 75:
#         print("Which means you scored" + Fore.CYAN + {} + "percentage".format(perc3))
#         print(Fore.GREEN + "WOW !! Nice Score")
#     else:
#         print("You have scored {} percentage".format(perc3))
#         print("We know that you can score better."+ Fore.RED +"You should try again")
# m1 x + num2 y + con = 0'))

#     #        num1,x, '+', num2,y, '+', con, '=', '0')
#             eng.say('equation 2 is')
#             eng.runAndWait()
#             eng.say(num1+var)
#             eng.runAndWait()
#             eng.say('x plus')
#             eng.runAndWait()
#             eng.say(num2*var)
#             eng.runAndWait()
#             eng.say('y plus')
#             eng.runAndWait()
#             eng.say(con/var)
#             eng.runAndWait()
#             eng.say('equal to zero')
#             eng.runAndWait()
#             eng.say("Enter the value of x. If you don't know the answer press space")
#             eng.runAndWait()
#             inp = int(input())
#             k = floor(d[x])
#             #t= Timer(120, time_up) #x is amount of allowed time in seconds then execute the provided function
#             #t.start() #start the timer
#             if inp == k:
#                 #t.cancel()
#                 scr2 += 1
#                 eng.say('Enter the value of x and wait for 2 minutes')
#                 eng.runAndWait()
#                 print( Fore.GREEN +'Good Job! Your answer is correct')
#             elif inp == "":
#                 print(Fore.MAGENTA+"The correct answer is {}".format(k))
#                 eng.say("The correct answer is {}".format(k))
#                 eng.runAndWait()
#             else :
#                 #t.cancel()
#                 print( Fore.RED + 'Your answer is incorrect')
#                 eng.say('Your answer is incorrect')
#                 eng.runAndWait()
#                 print( Back.BLACK + 'The correct answer is', k)
#                 eng.say('The correct answer is' + str(floor(d[x])))
#                 eng.runAndWait()
#                 eng.say(floor(d[x]))
#                 eng.runAndWait()
#             print()
#             time.sleep(2)
#         break
#     print('You got {} questions right out of 4'.format(scr2))
#     perc2 = int((scr2)/4)*100
#     if perc2 >= 75:
#         print("Which means you scored" + Fore.CYAN + {} + "percentage".format(perc2))
#         print(Fore.GREEN + "WOW !! Nice Score")
#     else:
#         print("You have scored {} percentage".format(perc2))
#         print("We know that you can score better."+ Fore.RED +"You should try again")


def cg():
    print("Do you know about the method to calculate the coordinates of any point dividing a line in a particular ratio?")
    eng.say("Do you know about the method to calculate the coordinates of any point dividing a line in a particular ratio?")
    time.sleep(2)
    print("""Consider a line with the coordinates of the end points as (x1, y1) and (x2, y2), which is divided in a ratio m:n by a point (x3, y3).
    Now there is a formula known as the section formula :- x3 = (m*x2 + n*x1)/(m + n), similarly in order to find y3 just replace "x" with "y".
    """)
    eng.say("""Consider a line with the coordinates of the end points as (x1, y1) and (x2, y2), which is divided in a ratio m:n by a point (x3, y3).
    Now there is a formula known as the section formula :- x3 = (m*x2 + n*x1)/(m + n), similarly in order to find y3 just replace "x" with "y".
    """)
    print(Back.BLACK + "These questions will test your basic knowledge of Coordinate Geometry more specifically the section formula")
    print(Back.BLACK + "The coordinates of the two end points and the ratio with which the line is internally divided will be given")
    print(Back.BLACK + "You have to find the coordinates of the point which divides the line internally in the given ratio")
    eng.say('These questions will test your basic knowledge of Coordinate Geometry more specifically the section formula. The coordinates of the two end points and the ratio with which the line is internally divided will be given. You have to find the coordinates of the point which divides the line internally in the given ratio')
    scr3 = 0
    while True:
        for i2 in range(4):
            x1 = floor(random.uniform(-10, 10))
            x2 = floor(random.uniform(-10, 10))
            y1 = floor(random.uniform(-10, 10))
            y2 = floor(random.uniform(-10, 10))
            m = floor(random.uniform(-10, 10))
            n = floor(random.uniform(-10, 10))
            lmb = lambda x1,x2,m,n : (x1*n + x2*m)/m+n
            lmb1 = lambda y1,y2,m,n : (y1*n + y2*m)/m+n
            print(Fore.CYAN + "coordinates of point1 are", "(",x1,",",y1,")")
            print( Fore.CYAN + "coordinates of point2 are", "(",x2,",",y2,")")
            print( Back.BLACK +"The line is internally divided in a ratio of m:n where m = {} and n = {}".format(m,n))
            x3 = int(input('Enter the x coordinate of point '))
            y3 = int(input('Enter the y coordinate of point '))
            kaw = floor(lmb(x1,x2,m,n))
            koo = floor(lmb1(y1,y2,m,n))
            t= Timer(120, time_up) #x is amount of allowed time in seconds then execute the provided function
            t.start() #start the timer
            if x3 == kaw and y3 == koo:
                t.cancel()
                scr3 += 1
                print( Fore.GREEN + 'Good Job! Your answer is correct')
                eng.say('Good Job! Your answer is correct')
                eng.runAndWait()
            else :
                t.cancel()
                print( Style.DIM + 'Your answer is incorrect')
                eng.say('Your answer is incorrect')
                print( Fore.YELLOW + 'The correct answer is, x coordinate = {} and y coordinate = {}'.format(kaw, koo))
                eng.say('The correct answer is, x coordinate = {} and y coordinate = {}'.format(kaw, koo))
                eng.runAndWait()
            print()
            time.sleep(1)
        break
    print("You got {} questions right out of 4".format(scr3))
    perc3 = ((int(scr3)/4)*100)
    if perc3 >= 75:
        print("Which means you scored" + Fore.CYAN + " {} %".format(perc3))
        print(Fore.GREEN + "WOW !! Nice Score")
    else:
        print("You have scored {} percentage".format(perc3))
        print("We know that you can score better."+ Fore.RED +"You should try again")




def mod():
    print(Fore.YELLOW + 'There will be a total of 4 questions')
    print(Fore.YELLOW + 'You will have 2 minutes to solve each question, after the time ends the answer will be displayed.')
    print(Back.BLACK + 'While answering the question enter the closest integer value')
    print()
    while True:
        print(Fore.YELLOW + 'Choose one of the following options.')
        print(Fore.RED + '1 --> Linear Equations; 2 --> Coordinate Geometry (section formula); 3 --> Visualise Equations; 4 --> Go Back')
        c1 = int(input())
        if c1 == 1: into()  #; linear()
        if c1 == 2: cg()
        if c1 == 3:
            visualise_eqn1()
            visualise_eqn2()
        if c1 == 4: break

def calculus():
    print( Back.BLACK + 'These questions will test your basic knowledge of differentiation')
    print( Style.DIM + 'A function will be given, you will have to find the derivative of that function')
    scr4 = 0
    while True:
        for i5 in range(4):
            coeff1 = floor(random.uniform(-3, 3))
            coeff2 = floor(random.uniform(-3, 3))
            coeff3 = floor(random.uniform(-3, 3))
            x = symbols('x')
            init_printing(use_unicode=True)
            expression = coeff1*exp(coeff2*x**coeff1)*sin(coeff3*x**coeff2)+cos(x)
            l =[]
            l.append(diff(expression))
            l.append(coeff1*diff(expression)+coeff1)
            l.append(diff(expression)/coeff2+coeff3)
            op1 = random.choice(l)
            l.remove(op1)
            op2 = random.choice(l)
            l.remove(op2)
            op3 = random.choice(l)
            print( Back.BLACK + "Find the derivative of f(x) =" ,expression)
            eng.say("Find the derivative of f(x) =" ,expression)
            eng.runAndWait()
            print( Fore.CYAN + "Choose the correct option. If you don't know just press enter")
            print(Back.BLACK +'1 -->', op1, '; 2 -->', op2, '; 3 -->', op3)
            eng.say("Choose the correct option. If you don't know just press enter")
            eng.runAndWait()
            it = input()
            if it == "1":
                annn = op1
            elif it == "":
                print("The correct option is".format(diff(expression)))
            elif it == "2":
                annn = op2
            elif it == "3":
                annn = op3

            #t = Timer(150, time_up) #x is amount of allowed time in seconds then execute the provided function
            #t.start()
            if annn == diff(expression):
              #  t.cancel()
                scr4 += 1
                print('Good Job! your answer is correct')
                eng.say('Good Job! your answer is correct')
                eng.runAndWait()
            else:
               # t.cancel()
                print('Sorry, incorrect answer')
                print("The correct answer is", diff(expression))
                eng.say('Sorry, incorrect answer')
                eng.runAndWait()
            print()
            time.sleep(1)
        break
    print("You got {} questions right out of 4".format(scr4))
    perc4 = ((int(scr4)/4)*100)
    if perc4 >= 75:
        print("Which means you scored" + Fore.CYAN + " {} %".format(perc4))
        print(Fore.GREEN + "WOW !! Nice Score")
    else:
        print("You have scored {} percentage".format(perc4))
        print("We know that you can score better."+ Fore.RED +"You should try again")

def quad():
    print("""A quadratic equation is an algebraic equation which can be rearranged in the following standard form: ax^2 + bx + c.
    The solution to such equations can be easily found by using Shri Dharacharya's formula,
    which goes, x = (-b + sqrt(b^2 - 4ac))/(2a) and x = (-b - sqrt(b^2 - 4ac))/(2a).""")
    print()
    time.sleep(1)
    print(Style.DIM + 'These questions will test your basic knowledge of Quadratic Equations')
    print(Back.BLACK + Fore.RED + 'An Equations of the form ax^2 + bx + c = 0 will be given')
    print( Back.BLACK +'You have to find the value of x and input it in the closest possible integer')
    scr5 = 0
    while True:
        for i3 in range(4):
            a1 = floor(random.uniform(-10, 10))
            b1 = floor(random.uniform(-10, 10))
            co = floor(random.uniform(-10, 10))
            v = floor(random.uniform(-10, 10))
            sym.init_printing()
            x = sym.symbols('x')
            rr = sym.Eq(a1*(x**2) + b1*x + co,0)
            dict = {}
            dict = sym.solve([rr],(x))
            print( Back.BLACK + 'equation is', a1,'x^2', '+', '('+str(b1)+')','x', '+', '('+str(co)+')', '=', '0')
            answer = str(input("Enter the value of x, if i(iota) is coming in the solution then write it as 'I'. If you don't know just press enter : "))
            hehe = floor(dict[0][0])
            huh = floor(dict[1][0])
            #t = Timer(5, time_up)
            #t.start()
            if answer == str(hehe) or answer == str(huh):
              #  t.cancel()
                scr5 += 1
                print( Back.BLACK + 'Good Job! Your answer is correct')
            if answer == "":
               # t.cancel()
                print("The correct answer is", hehe, "or", huh)
            else:
               # t.cancel()
                print(Back.BLACK + 'Your answer is incorrect')
                print("The correct answer is", hehe, "or", huh)
            print()
            time.sleep(2)
        break
    print("You got {} questions right out of 4".format(scr5))
    perc5 = ((int(scr5)/4)*100)
    if perc5 >= 75:
        print("Which means you scored" + Fore.CYAN + " {} %".format(perc5))
        print(Fore.GREEN + "WOW !! Nice Score")
    else:
        print("You have scored {} percentage".format(perc5))
        print("We know that you can score better."+ Fore.RED +"You should try again")



def adv():
    print('There will be a total of 4 questions')
    print('You will have 2 minutes and 30 seconds to answer each question')
    print('While answering the question enter the closest integer value')
    while True:
        print(Back.BLACK + 'Choose one of the following options')
        print( Fore.RED + '1 --> Calculus;  2 --> Quadratic Equations; 3 --> Go Back')  # 2 --> Quadratic Equations;
        c2 = int(input())
        if c2 == 1: calculus()
        if c2 == 2: quad()
        elif c2 == 3: break



def into():
    eng.say("Do you know what an algebric equation is ")
    eng.runAndWait()
    intro_ques = input("Do you know what an algebric equation is (yes/no): ")
    if intro_ques == "yes":
        print( Style.DIM + "Ok then lets directly move to visualsing linear equations")
        visualise_eqn1()


    if  intro_ques == "no":
        print( Fore.GREEN+ "well its basically just a simple equation with variables")
        eng.say("well its basically just a simple equation with variables")
        eng.runAndWait()
        eng.say("Do you know what variables are")
        eng.runAndWait()
        intro_ques1 = input("Do you know what variables are (yes/no): ")
        if intro_ques1 == "no":
            print( Back.BLACK + """
            In simple terms variables is something whose value can change(or vary).

            Let me explain you this in simpler terms for example Ram has 5 apples. Now if he will never eat those apples the quantity of those apples will never change
            Those apples are 5 and will remain 5 untill someone eats them. So here we have a constant 5 But now Shyam comes
            and he says that he has "some" apples now how can we define that "some" we don't have any definate to put in the place
            of "some" so "some" is a variable quantity it can be 2,3,4,5.... anything.
             """)
            eng.say("In simple terms variables is something whose value can't change.")
            eng.say("""Let me explain you this in simpler terms for
            example Ram has 5 apples. Now if he will never eat those apples the quantity of those apples will never change
            Those apples are 5 and will remain 5 untill someone eats them. So here we have a constant 5 But now Shyam comes
            and he says that he has "some" apples now how can we define that "some" we don't have any definate to put in the place
            of "some". So "some" is a variable quantity it can be 2,3,4,5.... anything.
            """ )
            eng.runAndWait()
            print( Back.BLACK + """Now if we ask ourself,how we can we identify variables,
            well just ask yourself, can we define that particular value? if yes then it's a constant else a variable""")
            eng.say("Now if we ask ourself,how we can we identify variables, well just ask yourself, can we define that particular value? if yes then it's a constant else a variable")
            eng.runAndWait()
            print(Fore.CYAN + "Lets move to ")
            eng.say("Lets move to")
            eng.runAndWait()
            print("examples of linear equations. :")
            eng.say("examples of linear equations. ")
            eng.runAndWait()
            ln_examples = cv2.imread('Types-of-linear-equation.png',1)
            not_ln_examples = cv2.imread('not-linear-equations.png',1)
          
            cv2.imshow("Types-of-linear-equation",ln_examples)
            k = cv2.waitKey(33)
            print("These are the examples of types of linear equation. The window will automatically after 6 seconds ")
            eng.say("These are the examples of types of linear equation. The window will close automatically after 6 seconds")
            eng.runAndWait()
            time.sleep(6)
            cv2.destroyWindow("Types-of-linear-equation")

            cv2.imshow("Not linear equations",not_ln_examples)
            k = cv2.waitKey(33)
            print("They are not linear equation. The window will close automatically after 6 seconds")
            eng.say("They are not linear equation. The window will close automatically after 6 seconds")
            eng.runAndWait()
            time.sleep(6)
            cv2.destroyWindow("Not linear equations")
    


# examples to be added using image or anything

def img():
    graph_table = cv2.imread("table.png",1)
    cv2.imshow("How to get coordinates of linear equation",graph_table)
    k = cv2.waitKey(33)
    print("This table explains, how we have to find coordinates. The window will close automatically after 6 seconds")
    eng.say("This table explains, how we have to find coordinates. The window will close automatically after 6 seconds")
    time.sleep(6)
    cv2.destroyWindow("How to get coordinates of linear equation")




def visualise_eqn1():
    print( Back.BLACK + "Lets say if we want a graph of y = 2x+3. How to make that ?")
    eng.say("Lets say if we want a graph of y = 2x+3. How to make that ?")


    print( Fore.YELLOW + """
    we basically see variation in x with respect to y. This means that we put y = 2x+3 and we will put random value to x like 1,2,3,4 .... and will see what is the value of y.
    When y becomes 0 we say that the equation satisfies and we have a zero for that equation.
    """)
    eng.say("we basically see variation in x with respect to y. This means that we put y = 2x+3 and we will put random value to x like 1,2,3,4 .... and will see what is the value of y. When y becomes 0 we say that the equation satisfies and we have a zero for that equation.")
    eng.runAndWait()
    img()

    print("So we plot using these points/coordinates we found i.e. (0,3), (1,5), (2,7) and (3,9). We join these points and we get the graph of the equation")
    eng.say("So we plot using these points/coordinates we found that is 0 comma 3  1 comma 5  2 comma 7  and 3 comma 9 . We join these points to get the graph of the equation")

def visualise_eqn2():
    x = np.linspace(-2,2,100)
    # the function, which is y = x^3 here
    y = 2*x+3
    roots =[]
    x1 = 0
    y1 = 2*x1+3

    x2 = -3/2
    y2 = 0
    # setting the axes at the centre
    fig = plt.figure(figsize=(12,7))
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    # explain linear equations with graph more
    plt.plot(x,y,'purple')
    plt.plot(x1,y1,marker="o")
    plt.plot(x2,y2,marker="o")
    plt.grid()
    plt.savefig("GRAPH.jpeg")
    time.sleep(2)
    print("If you don't see a graph pop out please check the folder for a file named GRAPH.png")
    eng.say("If you don't see a graph pop out please check the folder for a file named GRAPH.png")
    eng.runAndWait()


    print(Fore.RED + """
    The orange dot represents the zero of the linear equation here the value of whole equation becomes 0 the blue dot just represents
    the point where the line intersects with Y axis. After you have viewed the program please close it to move forward""")  # explain how to find zeros theoretically
    eng.say("The orange dot represents the zero of the linear equation here the value of whole equation becomes 0 the blue dot just represents the point where the line intersects with Y axis.After you have viewed the program please close it to move forward")
    eng.runAndWait()
    img = cv2.imread("GRAPH.jpeg",1)
    cv2.imshow("GRAPH.jpeg",img)
    print("This is how the graph will look like. The window will close automatically after 6 seconds")
    eng.say("This is how the graph will look like. The window will close automatically after 6 seconds")
    eng.runAndWait()
    k = cv2.waitKey(33)
    time.sleep(6)
    cv2.destroyWindow("GRAPH.jpeg")
    
    # eng.say("Do you want to plot a of your own equation:")
    # eng.runAndWait()
    # user_input()

# def user_input(): # this is how you do recusrsion babyyyy
    # inp1 = input("Do you want to plot a of your own equation(yes/no): ")
    # if inp1 == "":
    #     user_input()
    # if inp1 == "yes":
    #     print( Back.BLACK + """
    #     Write your equation using following rules or the application will not work and may crash
    #     **Rules**
    #     Use * for multiplication example 4x = 4*x and (4)(3) = 4*3
    #     Use ** for exponent example if you want to represent x² = x**2 ; for 2x² = 2*x**2
    #     use / for divisiond
    #     use + for addition and - for subtraction
    #     Write equation in one variable using only 'x'
    #     Do not use equal to sign, just write LHS part of that equation.
    #     """)  # cahnge colour for last 2 . To highlight them
    #     eng.say("Write your equation using following rules or the application will not work and may crash")
    #     eng.runAndWait()
    #     eng.say("Rules")
    #     eng.runAndWait()
    #     eng.say("Use astericks for multiplication")
    #     eng.runAndWait()
    #     eng.say("use slash for division")
    #     eng.runAndWait()
    #     eng.say("use plus for addition and minus for subtraction")
    #     eng.runAndWait()
    #     eng.say("Write equation in one variable using only 'x'")
    #     eng.runAndWait()
    #     eng.say("Do not use equal to sign, just write LHS part of that equation.")
    #     eng.runAndWait()
    #     x = np.linspace(-2,2,100)
    #     Y = input("enter your equation here using above rules: ")
    #     plt.plot(x,Y,color="Brown",title="Your Equation's plot")
    #     plt.grid()
    #     plt.show(block=True)
    #     plt.savefig("Your-Graph.png")
    #     your_graph = Image.open("Your-Graph.png")
    #     your_graph.show()
    #     print("If you don't see a graph pop out please check the folder for a file named GRAPH.png")
    #     eng.say("If you don't see a graph pop out please check the folder for a file named GRAPH.png")
    #     eng.runAndWait()
    #     if inp1 == "no":
    #         pass

def time_up():
    answer= None
    option2 = "You failed to answer within the given time limit" #what to do if the player does not enter an answer within the allowed time
    option1 = 'You failed to input an answer within the time limit'
    optimize = 'You took too long to answer the time is over'
    arr = [option1, option2, optimize]
    r = random.choice(arr)
    print(r)
    eng.say(r)
    eng.runAndWait()

def welcome():
    print(Fore.CYAN+Back.BLACK+
"""

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝


"""
)

def game_over():
    print(Fore.CYAN + Back.BLACK +
"""

   ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████       ▄██████▄   ▄█    █▄     ▄████████    ▄████████
  ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███
  ███    █▀    ███    ███ ███   ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀    ███    ███
 ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
  ███    ███   ███    ███ ███   ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ▀███████████
  ███    ███   ███    ███ ███   ███   ███   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███
  ████████▀    ███    █▀   ▀█   ███   █▀    ██████████       ▀██████▀   ▀██████▀    ██████████   ███    ███
                                                                                                 ███    ███

"""
)




def main():
    while True:
        print(Fore.YELLOW + "Choose one of the following options.")
        print(Fore.RED + '1 --> Basic Level; 2 --> Moderate Level; 3 --> Advance Level; 4 --> End Game')
        c = int(input())
        if c == 1:
            basic()
        if c == 2:
            mod()
        if c == 3:
            adv()
        if c == 4 : # scr+scr1+scr2+scr3+scr4+scr5 is not working so removed
            print( Fore.RED +  'You have successfully exited the game.')
            break

if __name__ == '__main__':
    # text to speech engine
    init()
    eng = pyttsx3.init()  # not making a function
    volume = eng.getProperty('volume')  # volume
    print(Fore.RED + "Your current volume level is:" + str(volume))
    vol_inp = float(input("We recommend you to set volume to max. Max volume is 1 and minimum is 0 you can choose either of them or you can choose between them using decimal: "))
    eng.setProperty('volume', vol_inp)  # max volume is 1.0
    eng.setProperty('rate',132)
    welcome()
    main()
    game_over()
