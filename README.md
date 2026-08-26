# Matemática Divertida 

Jogo educativo desenvolvido em **Python** com **Tkinter**, criado para ajudar
crianças do **Ensino Fundamental I** a praticar operações básicas de
matemática (adição, subtração e multiplicação) de forma leve e interativa.

>  **Atividade Acadêmica**
> Este projeto foi desenvolvido como atividade acadêmica do curso de
> **Análise e Desenvolvimento de Sistemas (ADS)**, com fins exclusivamente
> educacionais.

---

##  Sobre o projeto

O jogo apresenta ao aluno uma sequência de 10 perguntas com operações
matemáticas geradas aleatoriamente. Ao final de cada rodada, o desempenho
(quantidade de acertos e erros) é salvo em um banco de dados **SQLite**,
permitindo consultar um **ranking** com os melhores resultados registrados.

### Funcionalidades

- Tela inicial para o aluno informar o nome antes de começar a jogar.
- Geração aleatória de operações de **soma**, **subtração** e
  **multiplicação**, com faixas de números adequadas para o nível
  fundamental.
- Validação da resposta digitada, com feedback visual (certo/errado).
- Tela de resultado final com o total de acertos e erros da sessão.
- Opção de jogar novamente ou voltar ao menu inicial.
- Tela de **ranking** com os 10 melhores resultados já registrados.
- Persistência dos dados em banco de dados SQLite local
  (`pontuacoes.db`), criado automaticamente na primeira execução.

---

## Estrutura do projeto

```
.
├── jogo_matematica.py   # Interface gráfica e lógica principal do jogo (Tkinter)
├── banco_dados.py       # Camada de acesso ao banco de dados (SQLite)
├── pontuacoes.db         # Banco de dados gerado com o histórico de pontuações
├── requirements.txt      # Dependências do projeto
├── .gitignore
└── README.md
```

---

## Tecnologias utilizadas

- **Python 3**
- **Tkinter** — biblioteca padrão do Python para interfaces gráficas
- **SQLite3** — biblioteca padrão do Python para persistência de dados

> Observação: todas as bibliotecas utilizadas fazem parte da biblioteca
> padrão do Python, portanto **não é necessário instalar pacotes externos**
> para executar o projeto (veja `requirements.txt`).

---

## Como executar o projeto

### Pré-requisitos

- Ter o **Python 3** instalado na máquina (recomendado 3.10 ou superior).
- O Tkinter geralmente já vem incluso na instalação padrão do Python. Em
  alguns sistemas Linux, pode ser necessário instalá-lo manualmente:

  ```bash
  sudo apt-get install python3-tk
  ```

### Passo a passo

1. Clone ou baixe este repositório:

   ```bash
   git clone <url-do-repositorio>
   cd <pasta-do-projeto>
   ```

2. (Opcional, mas recomendado) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Instale as dependências listadas em `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o jogo:

   ```bash
   python jogo_matematica.py
   ```

O banco de dados (`pontuacoes.db`) será criado automaticamente na primeira
execução, na mesma pasta do projeto.

---

## Como jogar

1. Digite seu nome na tela inicial e clique em **"Começar a jogar!"**
   (ou pressione Enter).
2. Responda às 10 operações matemáticas apresentadas, digitando o
   resultado no campo de entrada e clicando em **"Confirmar"**.
3. Ao final das 10 perguntas, veja seu resultado (acertos e erros).
4. Escolha entre **jogar novamente** ou **voltar ao menu inicial**.
5. Na tela inicial, clique em **"Mostrar melhores resultados"** para
   visualizar o ranking dos 10 melhores desempenhos já registrados.

---

## Banco de dados

O arquivo `banco_dados.py` é responsável por toda a comunicação com o
SQLite, incluindo:

- `criar_tabela()` — cria a tabela `pontuacoes`, caso ainda não exista.
- `salvar_pontuacao(nome_aluno, acertos, erros)` — salva o resultado de
  uma sessão de jogo.
- `buscar_historico(nome_aluno=None)` — retorna o histórico de partidas,
  podendo ser filtrado por aluno.
- `buscar_ranking(limite=10)` — retorna os melhores resultados,
  ordenados por acertos (decrescente) e erros (crescente).

---

## Contexto acadêmico

Este projeto foi desenvolvido como parte das atividades do curso de
**Análise e Desenvolvimento de Sistemas**, com o objetivo de aplicar,
na prática, conceitos de:

- Lógica de programação em Python;
- Desenvolvimento de interfaces gráficas com Tkinter;
- Persistência de dados com SQLite;
- Organização de código em módulos.

---

## Licença

Projeto de caráter educacional, desenvolvido para fins acadêmicos.