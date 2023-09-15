# ETL - Gera Relatório de Fomento Rural, por Grupo Populacional Tradicional e Específico (GPTE)

Este projeto é um trabalho para o curso de Ciência de Dados da Dio.me com a parceria do Santander.

Este trabalho consiste em utilizar o pipeline ETL para gerar relatórios anuais (2012-2022) de Fomento Rural, por Grupo Populacional Tradicional e Específico (GPTE)

## Como utilizar:

**Dependência:** `^Python3.8`


Clone esse repositório na sua máquina local:
```bash
git clone https://github.com/lucasedson/etl-rural-gpte.git
```
Instale as bibliotecas:

```bash
pip install -r requirements.txt
```
Execute o arquivo:
```bash
python3 app.py
```


## Relatório: 
Será gerado um arquivo .csv na pasta `/resultado_analise` relativo ao ano digitado.
Onde terá informações totais da soma anual relativo aos grupos **(GPTE)**.