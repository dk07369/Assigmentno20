def prime_num(a):
    if(a==1):
      print("Num is not prime")
    elif(a==2):
      print("Num is prime")
    else:
       for e in range(2,a):
          if(a%e==0):
             print("num is not prime")
prime_num(13)

