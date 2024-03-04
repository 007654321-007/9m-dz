def iranoutoftitleideas(x:list):
 for i in range(len(x)-1):
  for j in range(len(x)-1-i):
   if len(x[j])>len(x[j+1]):
    x[j],x[j+1]=x[j+1],x[j] #сортировка пузырьком, но вместо размера чисел длина строки
a=int(input("введите кол-во чисел типа int в списке типа list:"))
x=[]
for i in range(0,a):
 x.append(str(input("введите строку типа str:")))
iranoutoftitleideas(x) #здесь работает функция (функция берет список типа list)
print(x)