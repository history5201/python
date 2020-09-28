# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:15:49 2020

@author: history
"""

from fractions import Fraction   #fraction:分数，即在此导入分数模块
import random      #用于随机生成题目
import profile

#整数四则运算
def newint():
    fh = ['＋', '－', '×', '÷']
    k = random.randint(0, 3)  #随机生成0到3内的整数,用于fh的下标
    n1 = random.randint(0, 50)
    n2 = random.randint(0, 50)
    result = 0   #存运算结果
    if k == 0:
        result = n1 + n2
    elif k == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 - n2
    elif k == 2:
        result = n1 * n2
    elif k == 3:
        while n2 == 0 or float(n1/n2)*1000%10!=0:  #分母不能为0,运算结果控制在2位小数内。
            n1 = random.randint(0, 50)
            n2 = random.randint(0, 50)
        result = float(n1 / n2)
    print(n1, fh[k], n2, '= ', end='')
    return result

#分数四则运算
def newfra():
    fh = ['＋', '－', '×', '÷']
    k = random.randint(0, 3)
    t1 = random.randint(1,20)
    t2 = random.randint(t1, 20)  #做分母，控制为真分数
    n1 = Fraction(t1, t2)   #即表示n1为分数
    t1 = random.randint(1, 20)
    t2 = random.randint(t1, 20)
    n2 = Fraction(t1, t2)
    result = 0
    if k == 0:
        result = n1 + n2
    elif k == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 - n2
    elif k == 2:
        result = n1 * n2
    elif k == 3:
        result = n1 / n2
    print(n1, fh[k], n2, '= ', end='')
    return result


#分数与整数的四则运算
def newfi():
    fh = ['＋', '－', '×', '÷']
    k = random.randint(0, 3)  # 随机生成0到3内的整数,用于fh的下标
    n1 = random.randint(0, 10)
    t1 = random.randint(1, 20)  #做分子
    t2 = random.randint(t1, 20)  # 做分母，控制为真分数
    n2 = Fraction(t1, t2)  # 即表示n2为分数
    result = 0  # 存运算结果
    if k == 0:
        result = n1 + n2
    elif k == 1:
        n1, n2pi = max(n1, n2), min(n1, n2)
        result = n1 - n2
    elif k == 2:
        result = n1 * n2
    elif k == 3:
        result = n1 / n2
    print(n1, fh[k], n2, '= ', end='')
    return result

##############################综合算式#############################
def jisuan(a,b,k):   #两个数字的计算
    if k==0:
        return a+b
    elif k==1:
        return a-b
    elif k==2:
        if a*b * 10000 % 10 == 0:  # 如果结果为3为小数内，则输出小数，反之输出为分数
            return a*b
        else:
            return Fraction(a*b)
    else:
        if a/b * 10000 % 10 == 0:  # 如果结果为3为小数内，则输出小数，反之输出为分数
            return a/b
        else:
            return Fraction(a,b)

def num():  #产生随机数
    k=random.randint(0,1)
    if k==0:
        a=random.randint(0,20)
    else:
        t1 = random.randint(1, 20)  # 做分子
        t2 = random.randint(t1, 20)  # 做分母，控制为真分数
        a = Fraction(t1, t2)  # 即表示a为分数
    return a

def hunhe():  #综合算式
    fh = ['＋', '－', '×', '÷']
    k1= random.randint(0, 3)
    k2= random.randint(0, 3)
    n=[num(),num(),num()]
    if k1>=2:   #加减乘除运算顺序
        jieguo=jisuan(n[0],n[1],k1)
        while k2 == 1 and n[2] > jieguo:
            n[2] = num()
        result=jisuan(jieguo,n[2],k2)
    elif k1<=1 and k2>=2:
        jieguo = jisuan(n[1], n[2], k2)
        while k1==1 and n[0]<jieguo:
            n[0]=num()
        result = jisuan(n[0],jieguo,k1)
    else:
        while k1==1 and n[0]<n[1]:
            n[0]=num()
            n[1] = num()
        jieguo = jisuan(n[0],n[1],k1)
        while k2==1 and jieguo<n[2]:
            n[2]=num()
        result = jisuan(jieguo,n[2],k2)
    print(n[0], fh[k1], n[1],fh[k2], n[2], '= ', end='')

    if result*10000%10==0:  # 如果结果为3为小数内，则输出小数，反之输出为分数
        return result
    else:
        return Fraction(result)

################################################################3



#newtest()函数是要求用户输入一个整数来输出算式的数量，采用while循环随机生成整数或者真分数运算，
# 将答案保存在result列表的同时输出算式直到算式数量达到要求。最后输出result列表即输出答案。
def newtest():
    fh = ['＋', '－', '×', '÷']
    print('输入题库所需要的题目数量')
    n=int(input())
    result=[]
    m=0
    while m<=(n-1):
        k = random.randint(0, 3)   #0表示真分数的运算，1表示整数的运算,2表示整数与分数的运算,3表示混合运算
        if k==0:
            print(m+1,end='、')
            result.append(newfra())
            print(' ')
        elif k==1:
            print(m+1,end='、')
            result.append(newint())
            print(' ')
        elif k==2:
            print(m+1,end='、')
            result.append(newfi())
            print(' ')
        else:
            print(m + 1, end='、')
            result.append(hunhe())
            print(' ')
        m=m+1
    m=0
    print('答案：')
    while m<=(n-1):
        print(m+1,'、',result[m])
        m=m+1

#下列为主函数，第一个模式负责调用上述newint()、new函数，
# 并获得函数返回值即算式答案，与用户输入值进行比较。第二个模式则是生成算式题目。
print('请选择需要进行的操作（输入数字代号）')
print('1、四则运算')
print('2、制作题库')
n=int(input())
if n==1:
    print('请输入在线答题的数量：')
    sm=int(input())
    print('input "exit" to Quit')
    cj=0                                  #记录学生成绩（百分比形式）
    while True:
        for i in range(1,sm+1):
            k = random.randint(0, 3)  #0表示真分数的运算，1表示整数的运算,2表示整数与分数的混合运算,3表示混合运算
                                      #同时此处亦可控制计算题型输出的比例
            print(i,end='、')
            if k == 0:
                result = newfra()
            elif k == 1:
                result = newint()
            elif k==2:
                result = newfi()
            else:
                result=hunhe()
            jg = input()
            if jg == 'exit':
                break;
            sr = Fraction(jg)  #化为分数形式
            if sr == result: #检测输入（sr）的答案与正确答案是否一致
                print('right \n')
                cj+=1
            else:
                print('error. the Tight answer is', result,'\n')
            i+=1
        break
    print('您最后的总成绩为：{:.2f}%'.format(cj/sm*100))

if n==2:
    newtest()