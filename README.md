Para rodar o código vai ser necessário instalar apenas a biblioteca `bs4` e `requests`, para isso basta rodar o código 
```sh
pip install bs4 requests
```
E então basta rodar os códigos
```sh
python calculadora_desafio1.py
python calculadora_desafio2.py
```

Para o `desafio 1` não foi utilizado nenhuma biblioteca, criei um dicionário chamando `descontos`para evitar o uso de vários `if's`. 
Também usei a mesma lógica para as `coberturas`.

De acordo com a média, defino a faixa de consumo sendo 1, 2 ou 3, buscando-a posteriormente para calculo da economia mensal.

Para o `desafio 2` a lógica dos calculos permanece a mesma, apenas criei uma classe `Calculadora`, que tem a função `calcular_desconto` recebe a bandeira e a classe, então é buscado na classe se já possui os dados das tarifas, se não é feito uma solicitação GET com a biblioteca requests, dessa solicitação é passado para a biblioteca BeautifulSoap, para podermos efetivamente extrair os dados.
Pelas pesquisas efetuadas no site da Cemig, verifiquei que as tarifas da classe Comercial e Industrial eram retirados da tabela "B3 - Demais Classes", portanto assumi para o código buscar as tarifas dessa tabela, já para a classe Residencial foi utilizado a primeira tabela, "B1 - Residencial Normal", caso essas premissas assumidas estejam erradas, elas são facilmente corrigidas no código.

O maior desafio que enfrentei nesse código foi entender o negócio, e qual das tabelas da cemig extrair o valor da tarifa.

Em caso de dúvidas estou disponível para esclarecimentos.
___

<p style="text-align:center" dir="auto">
  <a href="#desafio1">Desafio 1</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#desafio2">Desafio 2</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<h2 id="desafio1" style="text-align:center;border-bottom:none">Desafio 1</h2>

Uma empresa de assinatura de energia deseja criar uma calculadora de economia para seu site e contratou você para desenvolver essa solução. Como requisito, foi estabelecido que a aplicação deve ser desenvolvida utilizando a linguagem Python.

### Sua aplicação receberá as seguintes entradas:

- Três valores representando o consumo de energia elétrica dos últimos 3 meses
- Valor da tarifa da distribuidora
- Tipo de tarifa (Comercial, Residencial e Industrial)

### Os resultados da sua aplicação serão:

- Economia Anual
- Economia Mensal
- Desconto Aplicado
- Cobertura

#### A empresa de assinatura de energia te forneceu as seguintes premissas para o desconto:

| Consumo (Média) | Desconto (Residencial) | Desconto (Comercial) | Desconto (Industrial) |
| --- | --- | --- | --- |
| < 10.000 kWh | 18% | 16% | 12% |
| >= 10.000 kWh e <= 20.000 kWh | 22% | 18% | 15% |
| > 20.000 kWh | 25% | 22% | 18% |

#### Alem disso, deve-se considerar os seguintes percentuais de cobertura baseado no consumo:

| Consumo (Média) - kWh | < 10.000 kWh | >= 10.000 kWh e <= 20.000 kWh | > 20.000 kWh |
| --- | --- | --- | --- |
| Cobertura*** | 90% | 95% | 99% |

*** Cobertura é o valor da energia que o consumidor irá receber da empresa de assinatura de energia em relação à energia consumida

<h2 id="desafio2" style="text-align:center;border-bottom:none">Desafio 2</h2>

Para tornar a aplicação mais versátil e de ampla aplicabilidade, foi solicitado que a tarifa não seja mais uma entrada fixa. Agora, a tarifa deve ser obtida automaticamente a partir do <a href="https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/" target="_blank">site da CEMIG</a>. Com base na classe de consumo e na bandeira tarifária, será possível determinar a tarifa que será utilizada pela calculadora.

Portanto, desenvolva um código de web scraping que obtenha a tarifa diretamente do site e integre essa funcionalidade à calculadora criada no Desafio 1. Certifique-se de que a tarifa capturada seja corretamente utilizada nos cálculos.

### Requisitos dos Desafios:
1. A linguagem Python deverá ser utilizada para o desenvolvimento das soluções;
2. A calculadora deve ser implementada nos arquivos calculadora_desafio1.py e calculadora_desafio2.py, especificamente dentro da função calculadora();
3. Todos os testes contidos nos dois arquivos devem ser executados sem apresentar erros;
4. No Desafio 2, a escolha de bibliotecas e ferramentas para web scraping é livre, contanto que sejam implementadas em Python;
5. Inclua neste mesmo README uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação;
6. A entrega deve ser realizada dentro do prazo estabelecido;
7. O candidato deve fazer um fork do repositório. A entrega pode ser realizada por meio de um pull request para o repositório original (o que será considerado um diferencial) ou enviando o link do seu repositório para o e-mail lucas@dg.energy.
