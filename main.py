import math
#intro to state the purpose of this code
yeet = input("Hello. This is the converter. Are you tired of all your calculations between different number bases? Do you suck at maths? Well, worry no more! I shall do all your conversions for you. First of all, enter the form you want to convert from.")
list = ["Denary","Binary","Hexadecimal"]
yeet = yeet.capitalize()
#input sanitisation to make sure code isn't broken
while yeet not in list:
  yeet = input("Sorry, that does not work. We can only convert from binary, hexadecimal or denary")
yeti = input("Which form do you want to convert to?")
yeti = yeti.capitalize()
while yeti not in list:
  yeti = input("Sorry, that does not work. We can only convert to binary, hexadecimal or denary")
#make sure number forms are different because some students are stoopid
X = yeet == yeti
if X == True:
  print("Well! No need to worry, no conversion is required!")
else:
    #input should be different depending because some Hexadecimal values cannot be stored as integers, but binary (only zeroes and ones) and denary can
  if yeet == "Hexadecimal":
    nomnom = input("enter your number")
  else:
    nomnom = int(input("enter your number"))
    #binary input sanitisation
    if yeet == "Binary":
      while 1:
        a = 0
        for i in nomnom:
          if i != 0 and i != 1:
            a = 1
        if a == 0:
          break
        else:
          nomnom = int(input("not a valid binary number"))
if yeet == "Denary":
  if yeti == "Binary":
    def denary_to_binary(n):
      array = []
      #almost always way more than the highest power of two any number could reach
      deus = 100
      while n/2**deus < 1:
       deus = deus-1
      for i in range(deus+1):
        #slowly building the array of zeroes and ones for the final number later
        if n-2**deus >= 0:
          array.append(1)
          n = n-2**deus
          deus = deus - 1
        else:
          array.append(0)
          deus = deus - 1
      deus = int(len(array))
      binar = 1
      for i in range(1,deus):
        #now combine the digits to make the final number
        bob = int(array[i])
        binar = int(str(binar)+(str(bob)))
      return binar
    x = denary_to_binary(nomnom)
    print(x,"is your number in binary.")
  elif yeti == "Hexadecimal":
    def denary_to_hex(n):
      array = []
      #same as binary put to power of 16
      deus = 100
      while n/16**deus < 1:
        deus = deus - 1
      #more complex than to binary as 2 base vs 16 base
      for i in range(deus+1):
        if n-15*(16**deus)>=0:
          array.append("F")
          n = n-15*(16**deus)
        elif n-14*(16**deus)>=0:
          n = n-14*(16**deus)
          array.append("E")
        elif n-13*(16**deus)>=0:
          array.append("D")
          n = n-13*(16**deus)
        elif n-12*(16**deus)>=0:
          array.append("C")
          n = n-12*(16**deus)
        elif n-11*(16**deus)>=0:
          array.append("B")
          n = n-11*(16**deus)
        elif n-10*(16**deus)>=0:
          array.append("A")
          n = n-10*(16**deus)
        else:
          chinna = n//(16**deus)
          array.append(chinna)
          n = n-chinna*(16**deus)
        deus -= 1
      deus = int(len(array))
      hexad = array[0]
      for i in range(1,deus):
        #combine the digits again to make the final number
        bob = array[i]
        hexad = str(hexad)+str(bob)
      return hexad
    print(denary_to_hex(nomnom),"is your number in hexadecimal")
elif yeet == "Binary":
  if yeti == "Denary":
    def binary_to_denary(n):
      array = []
      a = len(str(n))
      f = str(n)
      for i in range(int(a)):
        array.append(f[i])
      denar = 0
      a = int(len(array))
      for i in range(a):
        b = int(array[i])
        if b == 1:
          b = 2**(a-1)
          denar = denar+b
          a = a-1
        else:
          a = a-1
      print(denar,"is your number in good ol' denary")
    binary_to_denary(nomnom)
  elif yeti == "Hexadecimal":
    def binary_to_hex(n):
      array = []
      a = len(str(n))
      f = str(n)
      for i in range(int(a)):
        array.append(f[i])
      denar = 0
      a = int(len(array))
      for i in range(a):
        b = int(array[i])
        if b == 1:
          b = 2**(a-1)
          denar = denar+b
          a = a-1
        else:
          a = a-1
      deus = 100
      while denar/16**deus<1:
        deus -= 1
      array = []
      for i in range(deus+1):
        if denar-15*(16**deus)>=0:
          array.append("F")
          denar = denar-15*(16**deus)
        elif denar-14*(16**deus)>=0:
          array.append("E")
          denar = denar-14*(16**deus)
        elif denar-13*(16**deus)>=0:
          array.append("D")
          denar = denar-13*(16**deus)
        elif denar-12*(16**deus)>=0:
          array.append("C")
          denar = denar-12*(16**deus)
        elif denar-11*(16**deus)>=0:
          array.append("B")
          denar = denar-11*(16**deus)
        elif denar-10*(16**deus)>=0:
          array.append("A")
          denar = denar-10*(16**deus)
        else:
          chinna = denar//(16**deus)
          array.append(chinna)
          denar = denar-chinna*(16**deus)
        deus -= 1
      deus = int(len(array))
      hexad = array[0]
      for i in range(1,deus):
        bob = array[i]
        hexad = str(hexad)+str(bob)
      print(hexad,"is your number in hexadecimal.")
    binary_to_hex(nomnom)
elif yeet == "Hexadecimal":
  if yeti == "Denary":
    def hex_to_denary(n):
      a = len(str(n))
      denar = 0
      b = a-1
      for i in range(a):
        if n[i] == "F":
          denar = denar+((16**b)*15)
        elif n[i] == "E":
          denar = denar+((16**b)*14)
        elif n[i] == "D":
          denar = denar+((16**b)*13)
        elif n[i] == "C":
          denar = denar+((16**b)*12)
        elif n[i] == "B":
          denar = denar+((16**b)*11)
        elif n[i] == "A":
          denar = denar+((16**b)*10)
        elif int(n[i])/1 >= 0:
          denar = denar+((16**b)*int(n[i]))
        b = b-1
      print(denar,"is yo numba in gud ol' denarrie")
    hex_to_denary(nomnom)
  elif yeti == "Binary":
    def hex_to_binary(n):
      a = len(str(n))
      array = []
      for i in range(a):
        if n[i] == "F":
          for i in range(4):
            array.append(1)
        elif n[i] == "E":
          for i in range(3):
            array.append(1)
          array.append(0)
        elif n[i] == "D":
          array.append(1)
          array.append(1)
          array.append(0)
          array.append(1)
        elif n[i] == "C":
          array.append(1)
          array.append(1)
          array.append(0)
          array.append(0)
        elif n[i] == "B":
          array.append(1)
          array.append(0)
          array.append(1)
          array.append(1)
        elif n[i] == "A":
          array.append(1)
          array.append(0)
          array.append(1)
          array.append(0)
        else:
          try:
            deus = 4
            c = deus-1
            b = int(n[i])
            while deus != 0:
              if b-2**c>=0:
                array.append(1)
              b = b-2**c
              else:
                array.append(0)
              deus = deus - 1
              c = c-1
          except:
            print("this is not a valid hexadecimal number, you have ruined the integrity of this converter!!!!")
            exit()
      binar = array[0]
      D = int(len(array))
      for i in range(1,D):
        bob = int(array[i])
        binar = int(str(binar)+str(bob))
      print(binar,"is your number in binary.")
    hex_to_binary(nomnom)
