# Mesmo com essas alterações no snake game, ainda não é possível gravar a pontuação máxima.
# Embora o jogo tenha a implementação necessária para atender a essa lógica, não existe uma "cache"
# para guardar esse valor, é necessário um arquivo que o jogo possa ler para acessar a pontuação
# e escrever para atualizá-la.

# Não vou mentir, gerenciamento de arquivos em python é bem temperamental, as vezes não é preciso
# copiar o path inteiro, mas nesse caso foi necessário.
file_path = "C:/Users/yuriv/OneDrive/Documentos/Portfólio/100PythonDays/Day 24 - Files, directories and paths/archive.txt"

# Python tem métodos embutidos que possibilitam o manuseamento de arquivos, principalmente de texto

# O método open() abre o arquivo, e retorna um objeto do tipo file
file = open(file_path)
# É possível passar a variável file_path como argumento para o método open(), as vezes é
# recomendado, para evitar reutilização de código, ou para facilitar a leitura do código.

# Porém, é necessária a existência do arquivo para que ele seja aberto.

content = file.read()  # O método read() lê o conteúdo do arquivo e retorna uma string

print(content)

file.close()  # O método close() fecha o arquivo, isso libera os recursos do computador que estavam
# ocupados com o arquivo aberto. É uma boa prática fechar o arquivo após o uso.

# Outra opção de manuseamento de arquivos, é o uso do bloco with, que garante que o arquivo será
# fechado após o uso, mesmo que ocorra algum erro durante a execução do código. É comum o
# esquecimento do comando close(), o uso de with evita esse problema.

# O with espera um método de manuseamento de arquivo, neste caso, o open é utilizado. O as 'file'
# serve como um alias, ou seja, um apelido para o arquivo, que pode ser utilizado dentro do bloco.
# Esse alias pode ser chamado de qualquer maneira, a depender do contexto em que ele está sendo
# utilizado.
with open(file_path) as file:
    content = file.read()
    print(content)

# Além de ler, é possível editar arquivos, para isso, é necessário passar o argumento 'w' para o
# método open(), que significa write, ou seja, escrita. Porém, é necessário ter cuidado, pois
# esse argumento sobrescreve o arquivo, ou seja, se o arquivo já existir, ele será apagado e
# substituído pelo novo conteúdo. Se o arquivo não existir, ele será criado.

with open(file_path, mode="w") as file:
    file.write("New text.")

# Originalmente, o arquivo é tido com o modo apenas de leitura, por isso, é necessário passar o
# argumento mode="w" para o método open(), permitindo a modificação dele por python.

# Outro argumento possível é mode="a", nesse caso, o arquivo é aberto para adição, ou seja, o
# que for escrito será ADICIONADO, e não SOBRESCRITO.

with open(file_path) as file:
    content = file.read()
    print(content)

# Na primeira execução, o arquivo mostra um texto anterior, a partir daí, o texto presente será
# aquele editado pelo método file.write().
