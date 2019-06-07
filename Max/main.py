from calculadora import calculadora
calc1=calculadora()
for x in range(1,10):
	for y in range(1,10):
		if (calc1.somar(x,y) == (x+y)):
			print("teste ok")
         else:
           print("teste erro")
 for x in range(10,1 -1):
       for y in range(1,x+1):
           if(calc1.subtrair(x,y) == (x,y)):
         	 print("teste ok")
         		else:
         	 print("teste erro")
 for x in range(1,10):
       for y in range(1,10):
         	if (calc1.multiplicar(x,y) == (x+y)):
         	 	print("teste ok")
              else:
                print("teste erro")
 for x in range(1,10):
         for y in range(1,10):
              if(calc1.dividir(x,y) == (x/y)):
              print("teste ok")
          else:
          	print("teste erro")