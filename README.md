# Máquina de Turing

Uma máquina de Turing consiste em um controle finito, uma fita e um cabeçote que pode ser utilizado para leituras ou gravações na fita. A definição formal das máquina de Turing e sua operação e idêntico aos autônomos finitos e de pilha. A sua forma básica consiste de um controle finito, uma fita e um cabeçote que pode realizar leituras ou escritas na fita. (ver figura 1).

Uma máquina de Turing é alimentada gravando-se previamente a cadeia de entrada nas células mais à esquerda da fita, imediatamente à direita do símbolo >. O restante da fita fica preenchido, nesse momento, com símbolos que representam espaço em branco, 
aqui denotados por <img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/branco.jpg"/>. A máquina é livre para modificar o conteúdo da sua fita de entrada, de qualquer maneira que se considere apropriada, bem como para gravar símbolos nos infinitos espaços em branco encontrados após a cadeia de entrada, na parte direita da fita. Dado que a máquina pode mover o seu cabeçote somente uma célula de cada vez, conclui-se que, após qualquer computação finita, apenas um número finito de células da fita terá sido visitado. 




Apresentando uma definição formal para a máquina de Turing, podemos entender que ela é uma quíntupla (K, ∑, δ, s, {h}), onde:
<ul>
<li>K é um conjunto finito de estados;</li>
<li>∑ é o alfabeto de entrada, que contém o símbolo de espaço em branco  e o símbolo de extremidade esquerda >, mas que não contém os símbolos → e ←;</li>
<li>s ϵ K é o seu estado inicial;</li> 
<li>{h} ⸦ K é o conjunto de estados de parada;</li>
<li>δ, a função de transição, é uma função de (K-H) x ∑ para K x (∑ U {→, ←}), tal que,</li>
<ul><li>(a)Para todos os q ϵ K- H, se δ (q, >) = (p, b), então b = →</li>
<li>(b)Para todos os q ϵ K- H e a ϵ ∑, se δ(q, a) = (p, b), então b ≠ >.</li></ul>
 
 </li></ul>

<p align="center"><img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/maquina.jpg"/></p>


Exemplo: considera-se uma máquina de Turing M = (K, ∑, δ, s, {h}), onde<br>
K = {q0, q1, h}<br>
∑ = {a, <img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/branco.jpg"/>, >}<br>
s = q0

Sendo δ dado pela tabela abaixo:

<p align="center"><img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/transicao.jpg"/></p>


### Regra para combinar máquina

As maquinas de Turing podem ser combinadas para formarem máquinas mais evoluídas e formando estruturas semelhantes aos Autômatos Finitos. Desta forma, as máquinas individualmente podem ser comparadas aos estados nos autômatos, sendo que uma só pode iniciar depois que outra parar 

<p align="center"><img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/maquina%20M.jpg"/></p>



### Computação usando a máquina de Turing

As máquinas de Turing foram propostas com a promessa de que elas podem substituir, como reconhecedores de linguagem, todos os autômatos apresentados anteriormente. Máquina de Turing são como computadores sem teclado, unidade de disco ou tela, isto é, sem um mecanismo para armazenar e recuperar informações nelas contidas. Torna-se oportuno, fixar algumas regras para a utilização das máquinas de Turing.: a cadeia de entrada, isenta de espaços em branco, é gravada à direita do símbolo >, com um espaço em branco à sua esquerda e espaços em branco à sua direita: o cabeçote é colocado na posição da fita que contém o espaço em branco entre o > e a cadeia de entrada; e a máquina é posicionada em seu estado inicial. Se M= (K, ∑,  δ, s, H) é uma máquina de Turing, e W ϵ (∑-{<img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/branco.jpg"/>, >})*, então a configuração inicial de M com entrada W é (s, >w).  Com isso podemos agora definir que a máquina de Turing como reconhecedores de linguagem.<br>

#### Maquina que Computa divisão de um numero Binário por dois.

```
M = (K, ∑, δ, s, {h})
∑ = {>, #, 1, 0}
K = {s, r, t, u, v, x, h}
δ = {("s",">"):("s","R"),("s","#"):("r","R"),("r","#"):("h","L"),("r","0"):("r","R"),("r","1"):("t","R"),
("t","0"):("u","R"),("t","1"):("u","R"),("t","#"):("x","L"),("u","0"):("u","R"),("u","1"):("u","R"),
("u","#"):("v","L"),("v","0"):("v","#"),("v","1"):("v","#"),("v","#"):("x","L"),("x","0"):("x","L"),
("x","1"):("x","L"),("x","#"):("h","#")}
```
<p align="center"><img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/screenshot.23.jpg"/></p>


#### Maquina que Computa Soma de dois numero Binário.
```
M = (K, ∑, δ, s, {h})
K = {"s","t","p","q","h","z","a","a0","b0","c0","c0","a1","b1","c1","c1","a+","b+","c+","c+"}
∑ = {>, #, 1, 0,+}
δ = { ("s",">"):("s","R"),("s","#"):("t","R"),("t","0"):("t","R"),("t","1"):("t","R"),("t","+"):("j","R"),
("t","#"):("h","L"),("j","0"):("j","R"),("j","1"):("g","R"),("j","#"):("n","L"),("n","0"):("k","#"),
("k","#"):("n","L"),("n","+"):("h","#"),("g","0"):("g","R"),("g","1"):("g","R"),("g","#"):("u","L"),
("u","0"):("v","1"),("u","1"):("v","0"),("v","1"):("u","L"),("v","0"):("x","L"),("x","0"):("x","L"),
("x","1"):("x","L"),("x","+"):("p","L"),("p","#"):("z","1"),("p","0"):("q","1"),("p","1"):("q","0"),
("q","0"):("p","L"),("q","1"):("m","L"),("m","0"):("m","L"),("m","1"):("m","L"),("m","#"):("s","#"),
("z","0"):("z","R"),("z","1"):("z","R"),("z","+"):("z","R"),("z","#"):("a","L"),("a","0"):("a0","#"),
("a","1"):("a1","#"),("a","+"):("a+","#"),("a0","#"):("b0","R"),("b0","#"):("c0","0"),("c0","0"):("c0","L"),
("c0","#"):("a","L"),("a1","#"):("b1","R"),("b1","#"):("c1","1"),("c1","1"):("c1","L"),("c1","#"):("a","L"),
("a+","#"):("b+","R"),("b+","#"):("c+","+"), ("c+","+"):("c+","L"),("c+","#"):("a","L"),("a",">"):("s","R")}
```
<p align="center"><img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/screenshot.27.jpg"/></p>


### Instalação

Requer [Python 3.5](https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe) ou superior.

```sh
$ git clone https://github.com/ericoandre/Maquina-de-turing-pygame.git
$ cd Maquina-de-turing-pygame
$ pip install pygame
$ cd Maquina de turing pygame
$ python3 setup.py
```
