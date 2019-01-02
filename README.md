# Máquina de Turing

Uma máquina de Turing consiste em um controle finito, uma fita e um cabeçote que pode ser utilizado para leituras ou gravações na fita. A definição formal das máquina de Turing e sua operação e idêntico aos autônomos finitos e de pilha. A sua forma básica consiste de um controle finito, uma fita e um cabeçote que pode realizar leituras ou escritas na fita. (ver figura 1).

Uma máquina de Turing é alimentada gravando-se previamente a cadeia de entrada nas células mais à esquerda da fita, imediatamente à direita do símbolo >. O restante da fita fica preenchido, nesse momento, com símbolos que representam espaço em branco, 
aqui denotados por <img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/branco.jpg"/>. A máquina é livre para modificar o conteúdo da sua fita de entrada, de qualquer maneira que se considere apropriada, bem como para gravar símbolos nos infinitos espaços em branco encontrados após a cadeia de entrada, na parte direita da fita. Dado que a máquina pode mover o seu cabeçote somente uma célula de cada vez, conclui-se que, após qualquer computação finita, apenas um número finito de células da fita terá sido visitado. 




Apresentando uma definição formal para a máquina de Turing, podemos entender que ela é uma quíntupla <img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/quintopla.png"/>, onde:
 K é um conjunto finito de estados;
∑ é o alfabeto de entrada, que contém o símbolo de espaço em branco  e o símbolo de extremidade esquerda >, mas que não contém os símbolos → e ←; 
s ϵ K é o seu estado inicial;
 ⸦ K é o conjunto de estados de parada; 
 δ, a função de transição, é uma função de (K-H) x ∑ para K x (∑ U {→, ←}), tal que,
(a)Para todos os q ϵ K- H, se δ (q, >) = (p, b), então b = →
(b)Para todos os q ϵ K- H e a ϵ ∑, se δ(q, a) = (p, b), então b ≠ >.

<p align="center"><img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/maquina.jpg"/></p>




## Regra para combinar máquina

As maquinas de Turing podem ser combinadas para formarem máquinas mais evoluídas e formando estruturas semelhantes aos Autômatos Finitos. Desta forma, as máquinas individualmente podem ser comparadas aos estados nos autômatos, sendo que uma só pode iniciar depois que outra parar 

<p align="center"><img alt="" src="https://github.com/ericoandre/Maquina-de-turing-pygame/blob/master/maquina%20M.jpg"/></p>
