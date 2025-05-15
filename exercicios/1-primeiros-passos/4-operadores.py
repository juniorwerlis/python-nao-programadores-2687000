ano_nascimento = 1991
ano_formatura = 2024

# Considerando que as variáveis acima correspondem a 'Werlis Junior', descubra a idade dele no ano da sua formatura

idade = ano_formatura - ano_nascimento

print (idade) 

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas

a = ano_formatura > ano_nascimento
b = ano_formatura <= ano_nascimento
c = ano_formatura == ano_formatura
d = ano_formatura == ano_nascimento
e = ano_formatura != ano_nascimento

print (a)
print (b)
print (c)
print (d)
print (e)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas

print (not a==b)
print (a==c and b==d)
print (a==a or e==d)