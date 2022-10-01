lower=int(input("enter 1 value:"))
upper=int(input("enter 2 value:"))
for num in range(lower,upper):
    if num>1:
      for i in range(2,num):
          if(num%i)==0:
             break
      else:
       print(num)
