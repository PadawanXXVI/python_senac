# Variáveis em Python

Python é uma linguagem dinamicamente tipada, o que significa que não é necessário declarar o tipo de variável ou fazer casting (mudar o tipo de variável), pois o Interpretador se encarrega disso para nós!<br>
Isso significa também que o tipo da variável poder variar durante a execução do programa.

##  Definição de variável

Uma variável é um nome que aponta para um valor armazenado na memória. Você cria uma variável atribuindo um valor a ela usando o operador =

### Atribuição de variáveis em Python

```
nome = 'Anderson'
idade = 25
altura = 1.74
```

## Tipos de variáveis

### Tipo inteiro (int)

O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.<br>
É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ter ou não sinal, isto é: ser positivo ou negativo.<br>
Por exemplo, 21, 4, 0, e −2048 são números inteiros, enquanto 9.75, 1/2, 1.5 não são.

#### Exemplo
```
idade = 18
ano = 2024
```

### Tipo ponto flutuante ou decimal (float)

É um tipo composto por caracteres numéricos (algarismo) decimais.<br>
O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.

#### Exemplo

```
altura = 1.74
peso = 87.6
```

### Tipo complexo (complex)

Tipo de dado usado para representar números complexos (isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).<br>
Esse tipo normalmente é usado em cálculos geométricos e científicos.<br>
Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo.<br>
A função complex(real[, imag]) do Python possibilita a criação de números imaginários passando como argumento: real, que é a parte Real do número complexo e o argumento opcional imag, representando a parte imaginária do número complexo.

#### Exemplo

```
a = 5+2j
b = 20+6j
```

### Tipo string (str)

É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.

#### Exemplo

```
nome = "Anderson"
profissão = 'Cientista de Dados'
```

#### Observações

1. Para as strings, devemos colocar a informação entre aspas simples ou entre aspas duplas.<br>
1. Caso você digite um número e coloque entre as aspas, ele será reconhecido como uma string.

### Tipo booleano (bool)

Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python).<br>
Na lógica computacional, podem ser considerados como 0 ou 1.

#### Exemplo
```
fim_de_semana = True
feriado = False
```
#### Observação

Observe que as palavras True e False sempre são escritas com a letra inicial maiúscula para representar os valores booleanos.

### Listas (list)

Tipo de dado muito importante e que é muito utilizado no dia a dia do desenvolvedor Python!<br>
Listas agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos.<br>
Elas são definidas utilizando-se colchetes para delimitar a lista e vírgulas para separar os elementos.

#### Exemplo

```
alunos = ['Anderson', 'Maria', 'João', 'Paula']
notas = [9.8, 7.9, 4.5, 10.0]
```

### Tuplas (tuple)

Assim como Lista, Tupla é um tipo que agrupa um conjunto de elementos.<br>
Porém sua forma de definição é diferente: utilizamos parênteses e vírgula para separar os elementos.<br>
A diferença para Lista é que Tuplas são imutáveis, ou seja, após sua definição, Tuplas não podem ser modificadas.

#### Exemplo

```
valores = (90, 120, 33, 44, 87)
pontos = (100, 150, 24)
```

### Dicionários (dict)

Dict é um tipo de dado muito flexível do Python.<br>
Eles são utilizados para agrupar elementos através da estrutura de chave e valor, onde a chave é o primeiro elemento seguido por dois pontos e pelo valor.

#### Exemplo

```
altura = {'Anderson': 1.74, 'Maria': 1.65, 'Marta': 1.84}
peso = {'Anderson': 87.9, 'Maria': 55.0, 'Marta': 68.4}
```

## Função type

A função type( ) em Python é usada para determinar o tipo de um objeto. No caso das variáveis, ela retornará o tipo de dado contido na variável.

#### Exemplo

```
x = 10
y = 'Maria'
z = 1.78
k = True
a = [1, 2, 2]
b = (m, n, o)
c = {'nome': 'Alberto', 'idade': 25, 'estado_civil': 'solteiro'}
j = 2-3j
print(type(x))
print(type(y))
print(type(z))
print(type(k))
print(type(a))
print(type(b))
print(type(c))

# As saídas seriam:
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'complex'>
```

## Mudança de tipo de variável

Em determinados cenários pode ser necessário mudar o tipo de uma variável e no Python isso é muito fácil, uma das vantagens de uma linguagem dinamicamente tipada.

### Decimal (float) para String (str)

#### Exemplo

```
# Antes da conversão
altura = 1.80
print(type(altura))

# Conversão do tipo
altura = str(altura)

# Depois da conversão
type(altura)
print(altura)

# Saída
<class 'float'>
<class 'str'>
'1.8'
```
