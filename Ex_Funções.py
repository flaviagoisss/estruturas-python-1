def linha(n):
  for i in range(n):
    print(end = '_')
  print(" ")
print("\n")

def imprime_lista(l):
  contador = 0
  for valor in l:
    contador = contador + 1 
    print(contador,')',valor)
print("\n")