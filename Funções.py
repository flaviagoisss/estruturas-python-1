def hello():
  print("* Ola mundo *")

#--------------------------------#
def maior(x,y):
  if x > y:
    print(x)
  else:
    print(y)

#------------------------------#
def soma(x,y):
  total = x + y 
  print("total soma = ",total)

#------------------------------#
def soma3(x,y):
  total = x + y
  return total

#------------------------------#
def calcula_juros(valor, taxa = 10):
  juros = valor*taxa/100
  return juros
