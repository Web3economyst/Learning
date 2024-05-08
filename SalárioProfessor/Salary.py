#---------------------------------------

#Programa: TeacherSalary
#Descrição: Esse programa irá calcular o salário bruto e liquído de um professor da faculdade XYZ
#Autor: Gabriel Follmer de Mattos
#Data: 08/05/2024
#Versão: 0.0.3

#--------------------------------------

#Alocação de Memória

valor_hora = int(40)

desconto = int(12)

hora = 0

salario_bruto = 0

salario_desconto = 0

#Entrada de dados

hora = input('Quantas horas você trabalha?')

#Processamento de dados

hora2 = int(hora)

salario_bruto = (hora2 * valor_hora)

salario_desconto = (salario_bruto - desconto)

#Saída de dados

print (f' Você recebe no total {salario_bruto}, porém com os descontos, este valor fica {salario_desconto}')
