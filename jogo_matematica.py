import tkinter as tk
from tkinter import font as tkfont
from enum import Enum
import banco_dados

# Cores usadas na interface
class ConfiguracoesJogo(Enum):
    OPERACOES = ["+", "-", "*"]
    LIMITE_SOMA_SUBTRACAO = 20 # números de 1 a 20 para soma e subtração
    LIMITE_MULTIPLICACAO = 10 # números de 1 a 10 para multiplicação
    COR_FUNDO = "#FFF8E7"
    COR_CERTO = "4CAF50"
    COR_ERRADO = "#E53935"
    COR_BOTAO = "#4A90E2"
    COR_TEXTO = "#333333"

class JogoMatematica(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Matemática Divertida")
        self.geometry("500x450")
        self.resizable(False,False)

        # Fontes personalizadas
        self.fonte_titulo = tkfont.Font(family="Arial", size=22, weight="bold")
        self.fonte_normal = tkfont.Font(family="Arial", size=14)
        self.fonte_botao = tkfont.Font(family="Arial", size=14, weight="bold")
        self.fonte_pergunta = tkfont.Font(family="Arial", size=32, weight="bold")

        # Garante que o banco de dados e a tabela existam antes de começar
        banco_dados.criar_tabela()

        # Variáveis de controle do jogo
        self.nome_aluno = ""
        self.acertos = 0
        self.erros = 0
        self.resposta_correta = 0
        self.perguntas = 10 # quantidade de perguntas por sessão
        self.pergunta_atual = 0

        # Container onde os frames serão trocados
        self.container = tk.Frame(self, bg=ConfiguracoesJogo.COR_FUNDO.value)
        self.container.pack(fill="both", expand=True)

    # Função auxiliar: Limpa a tela atual antes de desenhar outra
    def limpar_tela(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # Tela 1: Tela inicial onde o aluno digita o nome
    def mostrar_tela_inicial(self):
        self.limpar_tela()

        titulo = tk.Label(
            self.container,
            text="Matemática Divertida!",
            font=self.fonte_titulo,
            bg=ConfiguracoesJogo.COR_FUNDO.value,
            fg=ConfiguracoesJogo.COR_TEXTO.value,
        )
        titulo.pack(pady=30)

        instrucao = tk.Label(
            self.container,
            text="Digite seu nome para começar: ",
            font=self.fonte_normal,
            bg=ConfiguracoesJogo.COR_FUNDO.value,
            fg=ConfiguracoesJogo.COR_TEXTO.value,
        )
        instrucao.pack(pady=10)

        # Campo de entrada para o nome do aluno
        self.entrada_nome = tk.Entry(
            self.container,
            font=self.fonte_normal,
            justify="center",
        )
        self.entrada_nome.pack(pady=10, ipady=5)
        self.entrada_nome.focus()

        # Permite começar o jogo pressionando Enter
        self.entrada_nome.bind("<Return>", lambda evento: self.iniciar_jogo())

        botao_iniciar = tk.Button(
            self.container,
            text="Começar a jogar!",
            font=self.fonte_botao,
            bg=ConfiguracoesJogo.COR_BOTAO.value,
            fg="white",
            command=self.iniciar_jogo,
        )
        botao_iniciar.pack(pady=20, ipady=5, ipadyx=10)

        botao_ranking = tk.Button(
            self.container,
            text="Mostrar melhores resultados",
            font=self.fonte_normal,
            bg=ConfiguracoesJogo.COR_BOTAO.value,
            fg="white",
            command=self.mostrar_tela_ranking,
        )
        botao_ranking.pack(pady=5)