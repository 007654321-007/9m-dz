def sum(a:int): #это def считает сумму цифр одного числа типа int
 s=0
 while a!=0:
  s+=a%10
  a=a//10
 return s
def dest(x:list,a:int): #это def берет число из типа int из списка типа list
 for i in range(0,a):
  x[i]=sum(x[i]) # считает сумму цифр одного числа типа int
a=int(input("введите кол-во чисел типа int в списке типа list:"))
x=[]
for i in range(a,0,-1):
 x.append(int(input("введите число типа int:")))
dest(x,a) #вроде работает
print(x)