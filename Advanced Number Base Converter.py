print("***************************************C.N.S Programme*********************************************************")
print("______________________________Convert Number System Programme__________________________________________________")
print("""

       """)
print("READ ME FIRST....")
print("""
       """)
print("""binary(2),octal(8),decimal(10)hexa(16)------->>>>>---------binary(2),octal(8),decimal(10),hexa(16)""")
print("")
print("""For advanced users:-you can convert 2-16 based  number system in to any other number system.
          ex:-      *(Selection 1 =)input number system of your digit{ex:3=3 based number system
                                                                        5=5 based number system
                                                                        11=11 based number system}
                    DO NOT USE LARGER NUMBER SYSTEM THAN 16 BASED NUMBER SYSTEM(hexadecimal)                                                       
                                                                    
                    *(Selection 2 =)input any number system you need to convert.
          NOTE (1)- if you input 2-10 based number system to 'selection 1',you can't use any letter
                    in alphabet.
                    but 11-16 based number system,you can use relevant letters,(A,B,C,D,E,F)
                    
          NOTE (2)- if you input large number system than hexadecimal, in to {{{selection 2=}}}
                    programme will use hexadecimal symbols to the answer""")
print("""
        """)
print("_______________________________________________________________________________________________________________")
#first part---hexadecimal,number systems>16--- convert to any other number system         
y=int(input("your selection 1 ="))
q=int(input("your selection 2 =")) 
ra=[]
wa=[]
p=1
t=0
ooo='o'
if y>=11:
  if y<17:
   a=input('your number =')    #    11<=selection 1<17 ,this part avtivate
   print("")
   for g in a:
    g=ord(g)
    if y==11:                     #checking invalid letters in your number system,
      if g>=66:
           ooo='ooo'
           g=chr(g)
           print(g,"is invalid.please check again")
    elif y==12:
      if g>=67:
           ooo='ooo'
           g=chr(g)
           print(g,"is invalid.please check again")   
    elif y==13:
      if g>=68:
           ooo='ooo'
           g=chr(g)
           print(g,"is invalid.please check again")
    elif y==14:
      if g>=69:
           ooo='ooo'
           g=chr(g)
           print(g,"is invalid.please check again")
    elif y==15:
      if g>=70:
           ooo='ooo'
           g=chr(g)
           print(g,"is invalid.please check again")
    else:
      if g>=71:
           ooo='ooo'
           g=chr(g)
           print(g,"is invalid.please check again")
   if ooo=='o':
     for b in a:
      ra.append(b)
     for x in ra:
      if x=='A':
        wa.append('10')
      elif x=='B':
        wa.append('11')         
      elif x=='C':
        wa.append('12')
      elif x=='D':
        wa.append('13')
      elif x=='E':
        wa.append('14')
      elif x=='F':
        wa.append('15')
      else:
        wa.append(x)
     wa.reverse()
     for i in wa:
      i=int(i)
      d=i*p
      t=t+d
      p=p*y
#------second part decimal convert to binary ,octal, hexadecimal ---------------------------------------------------
     la=[]
     pa=[]
     while t>0:
      u=t%q
      la.append(u)
      t=t//q
     la.reverse()
     for e in la:
      if e==10:
        pa.append('A')
      elif e==11:
        pa.append('B')
      elif e==12:
        pa.append('C')
      elif e==13:
        pa.append('D')
      elif e==14:
        pa.append('E')
      elif e==15:
        pa.append('F')
      else:
        pa.append(e)
     tot=pa[0]
     tot=str(tot)
     print('_________________________________________________________________________________________________________________')
     print('_________________________________________________________________________________________________________________')
     if q==2:
       for k in pa[1:]:
        k=str(k)
        tot=tot+k
       print("your binary number =",tot)
     elif q==8:
       for k in pa[1:]:
        k=str(k)
        tot=tot+k
       print("your octal number =",tot)
     elif q==10:
       for k in pa[1:]:
        k=str(k)
        tot=tot+k
       print("your decimal number =",tot)
     elif q==16:
       for k in pa[1:]:
        k=str(k)
        tot=tot+k
       print("your hexadecimal number =",tot)
     else:
       if q>16:
        print(q,"based number =",pa)
       else:
        for k in pa[1:]:
         k=str(k)
         tot=tot+k
        print(q,"based number =",tot) 
     print('_________________________________________________________________________________________________________________')
     print('_________________________________________________________________________________________________________________')
  else:
   print("")
   print("Invalid number system detected.Please read terms and conditions.")
   print("")
   print("REPORT==========================================================")
   print("")
   print(y,"based number system is invalid.you can only use 2-16 based number systems for the 'selection 1'")
   print("but you can use any number system to the 'selection 2'.thank you and try again")

#binary,decimal,octal,number system<16 convert ---any number system
elif y<=10:
  a=input('your number=')
  print("")
  for g in a:
    g=ord(g)
    if g>=58:
      if g>=y:
       ooo='ooo'
       g=chr(g)
       print("letter",g,"is invalid.please check again") #cheking letters,if any leter ,this part activate
    else:
      g=chr(g)
      g=int(g)
      if g>=y:
       ooo='ooo'
       print("number",g,"is invalid.please check again")#cheking numbers larger than (y)=based of number system(selection 1)
      
  if ooo=='o':
   for b in a:
    ra.append(b)
   for x in ra:
    if x=='A':
        wa.append('10')
    elif x=='B':
        wa.append('11')
    elif x=='C':
        wa.append('12')
    elif x=='D':
        wa.append('13')
    elif x=='E':
        wa.append('14')
    elif x=='F':
        wa.append('15')
    else:
        wa.append(x)
   wa.reverse()
   for i in wa:
    i=int(i)
    d=i*p
    t=t+d
    p=p*y
#------second part decimal convert to binary ,octal, hexadecimal ---------------------------------------------------
   la=[]
   pa=[]
   while t>0:
    u=t%q
    la.append(u)
    t=t//q
   la.reverse()
   for e in la:
    if e==10:
        pa.append('A')
    elif e==11:
        pa.append('B')
    elif e==12:
        pa.append('C')
    elif e==13:
        pa.append('D')
    elif e==14:
        pa.append('E')
    elif e==15:
        pa.append('F')
    else:
        pa.append(e)
   tot=pa[0]
   tot=str(tot)
   print('________________________________________________________________________________________________________________')
   print('________________________________________________________________________________________________________________')
   if q==2:
     for k in pa[1:]:
      k=str(k)
      tot=tot+k
     print("your binary number =",tot)
   elif q==8:
     for k in pa[1:]:
      k=str(k)
      tot=tot+k
     print("your octal number =",tot)
   elif q==10:
     for k in pa[1:]:
      k=str(k)
      tot=tot+k
     print("your decimal number =",tot)
   elif q==16:
     for k in pa[1:]:
      k=str(k)
      tot=tot+k
     print("your hexadecimal number =",tot)
   else:
     if q>16:
       print(q,"based number =",pa)
     else:
       for k in pa[1:]:
         k=str(k)
         tot=tot+k
       print(q,"based number=",tot) 
   print('________________________________________________________________________________________________________________')
   print('________________________________________________________________________________________________________________')
else:
  print("")
  print("Invalid number system detected.Please read terms and conditions.")
  print("")
  print("REPORT==========================================================")#selection 1 >16--this part activate
  print("")
  print(y,"based number system is invalid.you can only use 2-16 based number systems for the 'selection 1'")

 
    

