tn=4

while True:
    ns=[]
    x=tn/2
    x=int(x)
    for i in range (x):
        a=0
        b=0
        m=x-i
        n=x+1
        for i in range(2,n):
            if n % i != 0 :
                a=1
                break
        for i in range(2,m):
            if m % i != 0 :
                a=1
                break
        if a==1 and b==1 :
            print('we can show the number ',tn,' as sum of two prime numbers')
            break
        else:
            print('we CAN NOT show the number ',tn,' as sum of two prime numbers')
    tn=tn+2
            
        
            
    
