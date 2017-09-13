rep=(1)
print("Choose FROM which base and TO which base, you want to convert,")
while rep==1:
    print("______________________________________________________________________________")
    y=int(input("From(1-binary,2-octal,3-decimal,4-hexadecimal): "))
    x=int(input("To(1-binary,2-octal,3-decimal,4-hexadecimal): "))
    b=[]
    d=[]
    print("______________________________________________________________________________")
    #following is binary to octal, decimal, hexadecimal
    if y==1:
        a=str(input("Input your number: "))
        for i in (a):
            d.append(i)
        d.reverse()
        t1=0
        n=0
        d1=[]
        for j in (d):
            j=int(j)
            p1=int(j*2**n)
            d1.append(p1)
            n=int(n+1)
        for j1 in (d1):
            t1=t1+j1
        #t1 is binary number in decimal.
        if x==2:
            while t1>0:
                c=(t1%8)
                b.append(c)
                t1=(t1//8)
            b.reverse()
            print("______________________________________________________________________________")
            print("The answer is:",b)
            print("______________________________________________________________________________")
        elif x==3:
            print("______________________________________________________________________________")
            print("The answer is:",t1)
            print("______________________________________________________________________________")
        elif x==4:
            while t1>0:
                c=(t1%16)
                if c==10:
                    c=("A")
                elif c==11:
                    c=("B")
                elif c==12:
                    c=("C")
                elif c==13:
                    c=("D")
                elif c==14:
                    c=("E")
                elif c==15:
                    c=("F")
                else:
                    c=c
                b.append(c)
                t1=(t1//16)
            b.reverse()
            print("______________________________________________________________________________")
            print("The answer is:",b)
            print("______________________________________________________________________________")
        elif x==1:
            print("______________________________________________________________________________")
            print("Are you telling me to convert your binary number to a binary number?")
            print("OK, then the answer is ",a)
            print("______________________________________________________________________________")
        else:
            print("______________________________________________________________________________")
            print("Your second selection input(",x,") is invalid. Please input carefuly")
            print("______________________________________________________________________________")
    #following is octal to binary, decimal, hexadecimal
    elif y==2:
        a=str(input("Input your number: "))
        for i in a:
            d.append(i)
        d.reverse()
        t1=0
        n=0
        d1=[]
        for j in (d):
            j=int(j)
            p1=int(j*8**n)
            d1.append(p1)
            n=int(n+1)
        for j1 in (d1):
            t1=t1+j1
        #t1 is octal number in decimal
        if x==1:
            while t1>0:
                c=(t1%2)
                b.append(c)
                t1=(t1//2)
            b.reverse()
            print("______________________________________________________________________________")
            print("The answer is:",b)
            print("______________________________________________________________________________")
        elif x==2:
            print("______________________________________________________________________________")
            print("Are you telling me to convert your octal number to a octal number?")
            print("OK, then the answer is ",a)
            print("______________________________________________________________________________")
        elif x==3:
            print("______________________________________________________________________________")
            print("The answer is:",t1)
            print("______________________________________________________________________________")
        elif x==4:
            while t1>0:
                c=(t1%16)
                if c==10:
                    c=("A")
                elif c==11:
                    c=("B")
                elif c==12:
                    c=("C")
                elif c==13:
                    c=("D")
                elif c==14:
                    c=("E")
                elif c==15:
                    c=("F")
                else:
                    c=c
                b.append(c)
                t1=(t1//16)
            b.reverse()
            print("______________________________________________________________________________")
            print("The answer is:",b)
            print("______________________________________________________________________________")
        else:
            print("______________________________________________________________________________")
            prin("Your second selection input(",x,") is invalid. Please input carefuly")
            print("______________________________________________________________________________")
    #following is decimal to binary, octal, hexadecimal
    elif y==3:
        a=int(input("Input your number: "))
        if x==1:
            while a>0:
                c=(a%2)
                b.append(c)
                a=(a//2)
            b.reverse()
            print("The answer is:",b)
        elif x==2:
            while a>0:
                c=(a%8)
                b.append(c)
                a=(a//8)
            b.reverse()
            print("______________________________________________________________________________")
            print("The answer is:",b)
            print("______________________________________________________________________________")
        elif x==3:
            print("______________________________________________________________________________")
            print("Are you telling me to convert your decimal number to a decimal number?")
            print("OK, then the answer is ",a)
            print("______________________________________________________________________________")
        elif x==4:
            while a>0:
                c=(a%16)
                if c==10:
                    c=("A")
                elif c==11:
                    c=("B")
                elif c==12:
                    c=("C")
                elif c==13:
                    c=("D")
                elif c==14:
                    c=("E")
                elif c==15:
                    c=("F")
                else:
                    c=c
                b.append(c)
                a=(a//16)
            b.reverse()
            print("______________________________________________________________________________")
            print("The answer is:",b)
            print("______________________________________________________________________________")
        else:
            print("______________________________________________________________________________")
            print("Your second selection input(",x,") is invalid. Please input carefuly")
            print("______________________________________________________________________________")
    #following is hexadecimal to binary, octal, decimal
    elif y==4:
        a=str(input("Input your number: "))
        for i in (a):
            if i=="A":
                i=(10)
            elif i=="B":
                i=(11)
            elif i=="C":
                i=(12)
            elif i=="D":
                i=(13)
            elif i=="E":
                i=(14)
            elif i=="F":
                i=(15)
            else:
                i=i
            d.append(i)
        d.reverse()
        t1=0
        n=0
        d1=[]
        for j in (d):
            j=int(j)
            p1=int(j*16**n)
            d1.append(p1)
            n=int(n+1)
        for j1 in (d1):
            t1=t1+j1
        #t1 is hexadecimal number in decimal
        if x==1:
            while t1>0:
                c=(t1%2)
                b.append(c)
                t1=(t1//2)
            b.reverse()
            print("______________________________________________________________________________")
            print("The answer is:",b)
            print("______________________________________________________________________________")
        elif x==2:
            while t1>0:
                c=(t1%8)
                b.append(c)
                t1=(t1//8)
            b.reverse()
            print("______________________________________________________________________________")
            print("The answer is:",b)
            print("______________________________________________________________________________")
        elif x==3:
            print("______________________________________________________________________________")
            print("The answer is:",t1)
            print("______________________________________________________________________________")
        elif x==4:
            print("______________________________________________________________________________")
            print("Are you telling me to convert your hexadecimal number to a hexadecimal number?")
            print("OK, then the answer is ",a)
            print("______________________________________________________________________________")
        else:
            print("______________________________________________________________________________")
            print("Your second selection input(",x,") is invalid. Please input carefuly")
            print("______________________________________________________________________________")
    else:
        print("______________________________________________________________________________")
        print("your first selection input(",y,") is invalide")
        print("==============================================================================")
    g4=int(input("Do you want to convert a number? (1-Yes/Others-No): "))
    if g4==(1):
        rep=(1)
    else:
        rep=(2)
        print("______________________________________________________________________________")
        print("OK then, have a nice day")
        
