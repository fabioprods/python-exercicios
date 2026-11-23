# Exercícios de Python

Seleção dos exercícios que mais gostei de resolver no curso de Python do Curso em Vídeo
(Gustavo Guanabara, 120h). Os enunciados são do curso; a solução de cada um é minha.

Os arquivos mantêm o número do desafio original (por exemplo, `ex095`).

## Conteúdo

| Pasta | Exercício | O que pratica |
|---|---|---|
| `01-controle-de-fluxo` | `ex059` menu de operações | Laço `while`, `if/elif/else` e menu interativo |
| `02-listas-e-dicionarios` | `ex089` boletim de notas | Listas compostas, média e consulta por posição |
| | `ex094` cadastro de pessoas | Dicionários dentro de listas, média de idade e filtros |
| | `ex095` aproveitamento de jogadores | Dicionários, listas e consulta de dados por jogador |
| `03-funcoes` | `ex105` analisa notas | `*args`, parâmetro opcional, `docstring` e retorno de dicionário |
| | `ex113` leitura segura | Tratamento de erros com `try/except/else` e `KeyboardInterrupt` |
| `04-modulos` | `ex112` resumo de preços | Módulos próprios (`moeda` e `dado`) organizados em pacote |

## Como rodar

Precisa do Python 3. Cada exercício roda sozinho, dentro da sua pasta:

```bash
cd 03-funcoes
python ex105_analisa_notas.py
```

O de módulos precisa ser executado de dentro da pasta `04-modulos`, para o Python encontrar o
pacote `utilidades`:

```bash
cd 04-modulos
python ex112_resumo_de_precos.py
```
