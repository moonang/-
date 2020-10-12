import datetime
import argparse
import re
import random
from fractions import Fraction

global r
r = 10

##整数运算模块
def countone(sign, a, a1, b):
    if sign == '+': #加法
        string = '(' + a1 + '+' + b + ')'
        c = a + int(b)
    elif sign == '-': #减法
        if a > int(b):
            string = '(' + a1 + '-' + b + ')'
            c = a - int(b)
        else:
            string = '(' + b + '-' + a1 + ')'
            c = int(b) - a
    elif sign == '*': #乘法
        string = '(' + a1 + '×' + b + ')'
        c = a * int(b)
    else: #除法保证分母不为0

        if int(b) != 0 and a == 0:
            string = '(' + a1 + '÷' + b + ')'
            c = Fraction(a, int(b))
        else:
            c = random.randint(1, int(a)+1)
            string = '(' + a1 + '÷' + str(c) + ')'
            c = Fraction(a, c)
    return string, c



##整数的四则运算
def count1(exercises, data1):
    sign = random.randint(1, 3) #随机决定是两个还是三个运算符
    sign1 = random.choice(['+', '-', '*', '/']) #第一个随机符号的产生
    sign2 = random.choice(['+', '-', '*', '/']) #第二个随机符号的产生
    sign3 = random.choice(['+', '-', '*', '/']) #第二个随机符号的产生
    a1 = random.randint(0, r)
    a2 = random.randint(0, r)
    a3 = random.randint(0, r)
    a4 = random.randint(0, r)
    
    tuple1 = countone(sign1, a1, str(a1), str(a2))
    if sign == 1: #一个运算符
        exercises.append(tuple1[0] + '=')
        data1.append(tuple1[1])
    else:
        tuple2 = countone(sign2, tuple1[1], tuple1[0], str(a3))
        if sign == 2:  #两个运算符
            exercises.append(tuple2[0] + '=')
            data1.append(tuple2[1])
        else:  #三个运算符
            tuple3 = countone(sign3, tuple2[1], tuple2[0], str(a4))
            exercises.append(tuple3[0] + '=')
            data1.append(tuple3[1])


##随机生成分数
def createF():
    fz1 = random.randint(0, r)
    if fz1 == 0:
        fm1 = random.randint(1, r)
    else:
        fm1 = random.randint(1, fz1 + 1)
    f1 = Fraction(fz1, fm1)
    return f1

##分数转换为合法格式
def f(f): 
    a = f.numerator #分子
    b = f.denominator #分母
    if a%b == 0: #计算为整数
        return '%d'%(a/b)
    elif a < b: #计算为真分数
        return '%d%s%d'%(a, '/', b)
    else: #计算为带分数
        c = int(a/b)
        a = a - c * b
        return '%d%s%d%s%d'%(c, '′', a, '/', b) ##带分数


##分数运算模块two
def counttwo(sign, f, f1, f2):
    if sign == '+':
        string = '(' + f1 + '+' + f2 + ')'
        result = f + Fraction(f2)
    elif sign == '-':
        #保证出现的数字为正数
        if(f > Fraction(f2)):
            string = '(' + f1 + '-' + f2 + ')'
            result = f - Fraction(f2)
        else:
            string = '(' + f2 + '-' + f1 + ')'
            result = Fraction(f2) - f
    elif sign == '*':
        string = '(' + f1 + '×' + f2 + ')'
        result = f * Fraction(f2)
    else:
        while Fraction(f2) == 0:
            f2 = createF()
        string = '(' + f1 + '÷' + str(f2) + ')'
        result = Fraction(f) / Fraction(f2)
    return string, result


##分数的四则运算
def count2(exercises, data1):
    sign = random.choice(['+', '-', '*', '/'])
    sign = random.randint(1, 3) #随机决定是两个还是三个运算符
    sign1 = random.choice(['+', '-', '*', '/']) #第一个随机符号的产生
    sign2 = random.choice(['+', '-', '*', '/']) #第二个随机符号的产生
    sign3 = random.choice(['+', '-', '*', '/']) #第二个随机符号的产生
    f1= createF()
    f2= createF()
    f3= createF()
    f4= createF()
    
    tuple1 = counttwo(sign1, f1, str(f1), str(f2))
    if sign == 1: #一个运算符
        exercises.append(tuple1[0] + '=')
        data1.append(tuple1[1])
    else:
        tuple2 = counttwo(sign2, tuple1[1], tuple1[0], str(f3))
        if sign == 2:  #两个运算符
            exercises.append(tuple2[0] + '=')
            data1.append(tuple2[1])
        else:  #三个运算符
            tuple3 = counttwo(sign3, tuple2[1], tuple2[0], str(f4))
            exercises.append(tuple3[0] + '=')
            data1.append(tuple3[1])



##主类
def main():
    while 1:
        print("输入题目的数量：", end = "")
        n = int(input())
        temp = 100 / n
        score = 0
        exercises = []
        data1 = [] ##（若有分数）分数转换合法格式前
        data2 = [] ##（若有分数）分数转换合法格式后
        data3 = [] ##人为输入的答案
        correct = [] ##答对的题目序号
        wrong = [] ##答错的题目序号
        for i in range(n):
            flag = random.randint(1, 3)
            if flag == 1:
                count1(exercises, data1) #整数的四则运算
                g = Fraction(data1[i]) #将数据转化为分数
                data2.append(f(g))  #将分数转换为合法格式并存入列表data2
            else:
                count2(exercises, data1) #分数的四则运算
                g = Fraction(data1[i]) #将数据转化为分数
                data2.append(f(g)) #记录带分数答案
        ##输出题目到Exercises.txt文件       
        with open('Exercises.txt', 'w') as fw:
            for i in range(n):
                fw.write("{}.四则运算题目{}: {}\n".format(i+1, i+1, exercises[i]))

        for i in range(n):
            print("第{}题：{}".format(i + 1, exercises[i]), end = "")
            a = input()
            data3.append(a)
            if a == str(data1[i]):
                score = score + temp
        print("\n所得的分数为：{}".format(score))
        print("\n正确答案:")
        ##输出答案到Answers.txt文件
        with open('Answers.txt', 'w') as fw:
          for i in range(n):
              fw.write("{}.答案{}: {}\n".format(i+1, i+1, data2[i]))
        ##比较人为输入答案和正确答案
        for i in range(n):
            if(data1[i] == data3[i] or data2[i] == data3[i]):
                correct.append(i)
            else:
                wrong.append(i)
        ##将题目对错情况输出到文件Grade.txt
        with open('Grade.txt', 'w') as fw:
            fw.write("Correct:{}(".format(len(correct)))
            for i in range(len(correct)-1):
                fw.write(str(correct[i] + ','))
            fw.write(str(correct[len(correct)-2]))##这里为什么是-2
            fw.write(")\nWrong:{}(".format(len(wrong)))
            for i in range(len(wrong)-1):##这里是-1是正确的 而上面为什么是-2
                fw.write(str(wrong[i]) + ',')
            fw.write(str(wrong[len(wrong)-1]))
            fw.write(")")
        ##输出正确答案    
        for i in range(n):
            if str(data1[i]) == str(data2[i]):
                print(exercises[i] + str(data1[i]))
            else:
                print("{}{}或{}".format(exercises[i], str(data2[i]), str(data1[i])))
        print("\n")

if __name__ == '__main__':
    main()
