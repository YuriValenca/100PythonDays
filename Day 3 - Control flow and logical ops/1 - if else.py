print("Bem vindo à montanha-russa!")
altura = float(input("Qual sua altura? "))

if altura > 1.2:    # O operador de comparação > irá, nesse caso, excluir aqueles que tem exatamente 1.2m, para incluir aqueles com essa altura, é necessário usar >=
    print("Você pode andar na montanha-russa!")
else:
    print("Você não tem altura pra ir na montanha-russa...")

# Dois aspectos importantes a serem observados são a IDENTAÇÃO do código e o posicionamento da estrutura condicional. Para compensar a falta de chaves após o if e else, Python requer que o usuário deixe um espaço antes da linha de código para ele saber o que está dentro do bloco condicional e o que não está, essa é a IDENTAÇÃO da estrutura condicional. Contudo, tanto o if quanto o else devem estar no "nível" de identação do restante do código, o que deve ser identado é apenas o bloco que cada uma dessas condições irá executar!
# Outros operadores de comparação: <, <=, == (igualdade), != (desigualdade)