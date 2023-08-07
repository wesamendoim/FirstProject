
'''
Nome: Wesley Valadão
Data: 26/07/2023
Versao 1.0
'''
'''
Meu primeiro codigo 
print("Wesley é o meu nome")
print("Teste")
''' 
'''
Meu segundo codigo 
Aula Variáveis
x = 4
print(x + x)
print(x + x)
print(x + x)
'''

'''
AULA DE FRASES 
O Wesley tem 29 anos de idade e mora em São Paulo 
'''

'''
AULA DE INTERAÇÃO COM O PROGRAMA USANDO INPUT
nome = input('Qual o seu nome: ')
idade = input('Qual é a sua idade:' )
cidade = input('Qual a sua cidade: ')
idade = str(idade)
print('O ' + nome + ' tem ' + idade + ' anos de idade e mora em ' + cidade)
'''

'''
AULA DE CALCULAR A DATA ATRAVES DO ANO QUE NASCEU
Data: 27/07/2023
função type para saber o tipo de dado que está sendo apresentado
ano_nascimento = 1993 
ano_atual = 2023

idade = int(ano_atual) - int(ano_nascimento)
print('Wesley a sua idade é: ' + str(idade))

'''
'''
Aula 18 
27/07/2023
fruta = 'Laranja'
#print(fruta[2:6])
print(fruta[2:])
'''

'''
Aula 19
31/07/2027
nome = 'Wesley'
sobrenome = 'Valadao'
profissao = 'Programador' 

#Wesley é um excelete [Programador]

text = 'O ' + nome + ' ' + sobrenome + ' e um excelente ' + '[' + profissao + ']'
print(text)

text2 = f'O {nome} {sobrenome} e um excelente [{profissao}]'
print(text2)
'''
'''
AULA 20 
31/07/2023
mensagem = 'O Péle sempre sera Rei do Futebol'
#print(mensagem.upper())
#print(mensagem.lower())
#print(mensagem.capitalize())
#print(mensagem.find('Rei'))
#print(mensagem.replace('R', 'r'))
#print(mensagem.replace('Péle', 'Ronaldo'))
#print(mensagem.strip())
'''

'''
Aula 21 
Operadores de comparação 
31/07/2023
operadores = 10 == 10 

print(operadores)

#==Equal 
#!=Not equal 
#> Greater than
#<Less then
#>=Greater than or equal too 
#<=Less than or equal to 
'''


'''
Aula de Operadores de COmparação IF/ELSE 
01/08/2023
velocidade = 40
if velocidade > 110:
   print('Acima da velocidade permitida')
   print('Favor reduzir a sua velocidade para 100KM')
elif velocidade < 60: 
  print('Favor dirigir mais rapido acima de 80KM')
else:
  print('Velocidade OK')
'''

'''
Aula de Operadores Logicos 
01/08/2023

renda_principal = True
nome_limpo = True

if renda_principal or nome_limpo: 
  print('Financiamento aprovado !')
else:
  print('Financiamento negado !')
'''

'''
Aula 26 Operadores Multiplos 
01/08/2023

valor = 19

#Condicaçao Comum
#if valor >=20 and valor <= 40:

#Condição Melhorada 
#if 20 <= valor < 40:

if 20 <= valor < 40:
  print('Produto contabilizado')
else:
  print('Valor abaixo ou acima do intervalo permitido')
'''

'''
Aula 27 For Loop para Numeros
01/08/2027
#imprimir de 1 a 5 

for numero in range(1,20,2):
  print(numero)
'''

'''
Aula 28 For Loops para Strings 
01/08/2023

palavra = 'Ronaldo'

for letra in palavra:
  #print(letra)
  print(f' {letra} esta dentro da palavra {palavra}')
'''

'''
Aula 29 - Utilizando IF E ELSE 
02/08/2023
ompra_confirmada = True
dados_compra = "Compra no valor de R$ 5.00..."

for enviar in range(3):
  if compra_confirmada:
    print(dados_compra)
    print('Detalhes enviados para o seu email...')
    break
else:
  print('Falha na compra')

'''

'''
Aula 30 - Nested Loops
02/08/2023
for numero in range(1,6):
  print('Produto' + str(numero))
  for numero1 in range(11):
    print(numero,numero1)
'''

'''
AULA 31 - LOOPING COM STRINGS 
03/08/2023
palavra = 'FANTASTICO'

for space in palavra:
  print(f' {space}',end='')
'''

'''
AULA 32 - Criando um retangulo 
03/08/2023

linhas = 6
colunas = 6
simbolos = '@'

for l in range(linhas):
  for c in range(colunas):
    print(simbolos,end='')
  print()
'''

'''
AULA 33 - While Loop
03/08/2023

valor = 100
dia = 0
while valor > 20:
  dia += 1
  print(f'No dia {dia} o produto vai ser vendido por R$ {valor}')
  valor-= 5
'''

'''
Aula 34 - Operador ternário
07/08/2023

idade = 16 

if idade >= 16:
  print('Voto permitido')
else:
  print('Voto nao permitido')

idade = 13

#IF IN LINE 
resultado = 'Voto Permitido' if idade >= 16 else 'Voto nao permitido'
print(resultado)

'''
