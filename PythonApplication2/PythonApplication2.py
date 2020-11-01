import math


print("Перлин Л.В. ИУ5-53Б")

def end():
    return 0 


print("Уравнение вида AX^4+BX^2+C=0\n")
while(True):
    try:
        a, b , c = float(input("Введите коэф A:")),float(input("Введите коэф B:")),float(input("Введите коэф C:"))
        break
    except (TypeError, ValueError):
        print ("Ошибка ввода. Попробуйте снова")


#no roots

if(a==0 and b==0 and c==0):
    print("0=0 при любом X")
elif (a==0 and b==0 and c!=0):
    print("Нет корней!")
elif (a==0 and b!=0 and c<0):
    print("Квадратное уравнение!")
    print("X1="+str(math.sqrt(-c))+"-"+str(math.sqrt(-c)))
elif (a!=0 and b==0 and c<0):
    print("Квадратное уравнение!")
    print("X1/X2=+/-"+str(math.sqrt(math.sqrt(-c))))
elif ((a==0 and b!=0 and c==0) or (c==0 and (a*b>0))):
    print("X=0")
elif (c==0 and (a*b<0)):
    print("3 корня")
    print("X1=0")
    print("X2/X3="+"+/-"+str(math.sqrt(-b/a)))
else:
    D=b*b-(4*a*c) 
    if(D>=0):
        x1ns=(-b+math.sqrt(D))/2*a
        x2ns=(-b-math.sqrt(D))/2*a
        if(x1ns>0):
            print("X1/X2=+/-"+str(math.sqrt(x1ns)))
        if(x2ns>0):
            print("X3/X4=+/-"+str(math.sqrt(x2ns)))
    elif(D<0):
        print("Нет решений.")
    
