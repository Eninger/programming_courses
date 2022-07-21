#validade tamanho cpf

cpf = input('primeiros digitos do cpf')

while len(cpf) != 11:
    cpf = input('primeiros digitos do cpf')

cpf = list(map(int,cpf))

# primeiro digito
soma = 0
mult = range(10,1,-1)

for x, z in zip(cpf,mult):
    soma = soma + (x*z)
    
primeiro_digito = 11 - (soma % 11)
if primeiro_digito > 9:
    primeiro_digito = 0
print(f'o primeiro digito é {primeiro_digito}')

# segundo digito
cpf_append = cpf

mult = range(11,1,-1)
cpf_append.append(primeiro_digito)

soma_2 = 0
for x, z in zip(cpf_append,mult):
    soma_2 = soma_2 + (x*z) 
segundo_sigito = 11 - (soma_2 % 11)
print(f'O segundo digito é {segundo_sigito}')