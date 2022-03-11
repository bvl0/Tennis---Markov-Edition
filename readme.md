# Tennis Markov Edition
## _(Aplicação de Cadeias de Markov na Simulação de um Jogo de Tênis)_

Simula uma partida de tênis representando o jogo por meio de uma Cadeia de
Markov. A partir desta representação, descreve o comportamento do jogo variando-se a
diferença técnica, representada pela probabilidade de se vencer uma partida, entre os
jogadores.
O projeto utiliza Python 3.

## Instalação e Execução
Para instalar as dependências utilizadas no projeto, faça:
```
pip3 install numpy tabulate 
```
O projeto é dividido em dois subprojetos, *tennis_markov_edition* e *data_analysis*. 
| Diretório    | Descrição   |
|----------|--------|
| tennis_markov_edition     | Projeto de simulação das partidas + logs da simulação |
| data_analysis             | Análise de dados dos logs da simulação | 

Para executar a simulação:
```
python3 .\tennis_markov_edition\main.py
```
Saída: *resultados.json*
**Foi escolhido o formato de log em json pela facilidade de estruturar/ler o dataset.**

Para analisar os logs: **[Necessário ter rodado a simulação anteriormente]**
```
python3 .\data_analysis\main.py
```
Saída: 
```
With 3 Samples

| Label   |   Mean M1 |   Std M1 |   Mean M2 |   Std M2 |
|---------+-----------+----------+-----------+----------|
| A wins  |   1       |  0       |  0.487222 | 0.353868 |
| B wins  |   0       |  0       |  0.512778 | 0.353868 |
| Sets    |   2       |  0       |  2.41856  | 0.349154 |
| Games   |  12.7077  |  0.6184  | 22.926    | 4.31581  |
| Points  |   2.73603 |  1.77523 |  3.35767  | 1.88042  |

With 10 samples

| Label   |   Mean M1 |   Std M1 |   Mean M2 |   Std M2 |
|---------+-----------+----------+-----------+----------|
| A wins  |   1       | 0        |  0.493467 | 0.473199 |
| B wins  |   0       | 0        |  0.506533 | 0.473199 |
| Sets    |   2       | 0        |  2.41867  | 0.465677 |
| Games   |  12.7049  | 0.832691 | 22.9689   | 5.44876  |
| Points  |   2.73928 | 1.78374  |  3.35808  | 1.89245  |
```
# Detalhes de implementação

A Cadeia de Markov foi representada através de um Grafo Direcionado.
Cada vértice do grafo representa um estado da cadeia de Markov.

Para percorrer os vértices, utilizamos os valores de P e Q definidos.
Cada vértice tem exatamente 2 vértices adjacentes, com exceção dos
estados finais "A Wins" e "B Wins" que não possuem vértices adjacêntes 
(ou mudanças de estado), pois representam o fim de um jogo em uma partida.

# Análise dos resultados obtidos

Para obter os dados abaixos, foram feitas **N = 3000** simulações.
Dentre os testes realizados, foi escolhido o número **3000 repetições** para cada teste
realizado, visando melhoria da precisão dos resultados obtidos.
E ara P e Q:
- P na partida 1 é aleatóriamente sorteado entre **[.70, .80]**
- P na partida 2 é aleatoriamente sorteado entre **[.45, .55]**
- E em ambas partidas o valor de Q é **Q = 1 - P**

##### Qual a probabilidade do Jogador A/B vencerem as Partidas 1 e a Partidas 2?
##### Para responder, considere Xi uma VA que representa o número de vitórias do
##### jogador i em cada caso, e que nosso espaço amostral contem 3 partidas. Mostre
##### uma análise estatística baseada em média e desvio padrão em cada caso.

Levando em consideração os resultados obtidos, a probabilidade do jogador A 
ganhar a partida 1 é de 100%, e o jogador B ganhar a partida 1 é de 0%.
Já na partida 2, onde os jogadores possuem nível técnico equivalente, tanto a 
probabilidade do jogador A ganhar quanto a do jogador B ganhar são de 
aproximadamente 50% (variando pouco de teste para teste).
```
| Label   |   Mean M1 |   Std M1 |   Mean M2 |   Std M2 |
|---------+-----------+----------+-----------+----------|
| A wins  |   1       |  0       |  0.487222 | 0.353868 |
| B wins  |   0       |  0       |  0.512778 | 0.353868 |
```
##### Qual a distribuição do número de sets, games e pontos nas Partidas 1 e 2?
##### Mostre uma análise estatística baseada em média e desvio padrão em cada
##### caso.
A distribuição de probabilidade do número de sets, segue a distribuição binomial,
tendi em vista que é uma sequência de experimentos de Bernoulli independentes 
(temos apenas, dois resultados possíveis: 2 ou 3 sets).
O número de games e pontos seguem uma distribuição normal, pois a maioria de seus 
valores estão em volta da média, com menor densidade nos cantos.
```
| Label   |   Mean M1 |   Std M1 |   Mean M2 |   Std M2 |
|---------+-----------+----------+-----------+----------|
| Sets    |   2       |  0       |  2.41856  | 0.349154 |
| Games   |  12.7077  |  0.6184  | 22.926    | 4.31581  |
| Points  |   2.73603 |  1.77523 |  3.35767  | 1.88042  |
```

##### Selecione aleatoriamente, com distribuição uniforme, 10 simulações dentre as
##### n existentes em seus datasets originais. Refaça as 2 análises anteriores e
##### explique as diferenças e semelhanças entre os resultados obtidos.
Repetindo as análises anteriores, utilizando 10 simulações dentre n existentes, percebemos que:
Os valores de média ficam mais próximos ao intuitivamente esperado (como por exemplo, 
a média de A ou B ganhar na partida 2, em que os jogadores possuem nivel técnico equivalente, estar
mais próximo ao 50%).
Já os valores de desvio padrão são bem maiores, pois como há mais variação de resultados,
aumenta a dispersão em torno da média conhecida.
Utilizando o número de 3 simulações, o resultado é consideravelmente menos confiável que
utilizando 10 simulações, justamente pelo volume de dados não ser suficientemente conclusivo.
```
| Label   |   Mean M1 |   Std M1 |   Mean M2 |   Std M2 |
|---------+-----------+----------+-----------+----------|
| A wins  |   1       | 0        |  0.493467 | 0.473199 |
| B wins  |   0       | 0        |  0.506533 | 0.473199 |
| Sets    |   2       | 0        |  2.41867  | 0.465677 |
| Games   |  12.7049  | 0.832691 | 22.9689   | 5.44876  |
| Points  |   2.73928 | 1.78374  |  3.35808  | 1.89245  |
```
