print("Exercicio 01 estrutura de decisão\n")
nota1 = float(input("digite a 1ª nota do aluno : "))
nota2 = float(input("digite a 2ª nota do aluno : "))
média = (nota1+nota2)/2
print("média = ",média)
if média >= 6:
  print("aprovado")

else:
  print("reprovado")
#--------------------------------------------------------#
print("\nExercicio 02 estrutura de decisão\n")
nota1 = float(input("digite a 1ª nota do aluno : "))
nota2 = float(input("digite a 2ª nota do aluno : "))
média = (nota1+nota2)/2
print("média = ",média)
if média >= 6:
  print("aprovado")
elif média >= 4:
  print("exame")
else:
  print("reprovado")