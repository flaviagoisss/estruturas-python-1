print("Exercicio 01 Estrutura de repetição\n")
s = 0
for x in range(3,334,3):
  s += x
print("soma = ",s)
#---------------------------------------#
print("\nExercicio 02 Estrutura de repetição\n")
s = 0
for contador in range(1,11):
  nota = float(input("digite a nota "+str(contador)+": "))
  s += nota
print("média = ",s/10)
#---------------------------------------#
print("\nExercicio 03 estrutura de repetição\n")
numero = int(input("digite o numero para a tabuada:"))
for sequencia in range(1,11):
  print("%2d x %2d = %3d" %(sequencia,numero,sequencia*numero))
             
             


