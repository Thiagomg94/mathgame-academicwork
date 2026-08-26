import random
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
    COR_CERTO = "#4CAF50"
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

        self.mostrar_tela_inicial()

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
        botao_iniciar.pack(pady=20, ipady=5, ipadx=10)

        botao_ranking = tk.Button(
            self.container,
            text="Mostrar melhores resultados",
            font=self.fonte_normal,
            bg=ConfiguracoesJogo.COR_BOTAO.value,
            fg="white",
            command=self.mostrar_tela_ranking,
        )
        botao_ranking.pack(pady=5)

    # Inicia o jogo após o aluno informar o nome
    def iniciar_jogo(self):
        nome_usuario = self.entrada_nome.get().strip()

        if not nome_usuario:
            nome_usuario = "Aluno(a)"

        self.nome_aluno = nome_usuario
        self.acertos = 0
        self.erros = 0
        self.pergunta_atual = 0

        self.proxima_pergunta()

    # Tela 2: Tela da pergunta
    def proxima_pergunta(self):
        # Verifica se o aluno respondeu todas as perguntas da sessão
        if self.pergunta_atual >= self.perguntas:
            self.finalizar_jogo()
            return

        self.pergunta_atual += 1
        self.limpar_tela()
        self.gerar_operacao()

    def gerar_operacao(self):
        operador = random.choice(ConfiguracoesJogo.OPERACOES.value)

        if operador == "+":
            numero1 = random.randint(1, ConfiguracoesJogo.LIMITE_SOMA_SUBTRACAO.value)
            numero2 = random.randint(1, ConfiguracoesJogo.LIMITE_SOMA_SUBTRACAO.value)
            resposta = numero1 + numero2

        elif operador == "-":
            numero1 = random.randint(1, ConfiguracoesJogo.LIMITE_SOMA_SUBTRACAO.value)
            numero2 = random.randint(1, numero1) # evita operacões com resultado negativo
            resposta = numero1 - numero2

        else:
            numero1 = random.randint(1, ConfiguracoesJogo.LIMITE_MULTIPLICACAO.value)
            numero2 = random.randint(1, ConfiguracoesJogo.LIMITE_MULTIPLICACAO.value)
            resposta = numero1 * numero2

        self.resposta_correta = resposta

        texto_conta = tk.Label(
            self.container,
            text=f"{numero1} {operador} {numero2} = ? ",
            font=self.fonte_normal,
            bg=ConfiguracoesJogo.COR_FUNDO.value,
            fg=ConfiguracoesJogo.COR_TEXTO.value,
        )
        texto_conta.pack(pady=10)

        self.entrada_resposta = tk.Entry(
            self.container,
            justify="center",
            font=self.fonte_normal,
        )
        self.entrada_resposta.pack(pady=10, ipady=5)
        self.entrada_resposta.focus()

        botao_confirmar = tk.Button(
            self.container,
            text="Confirmar",
            font=self.fonte_normal,
            bg=ConfiguracoesJogo.COR_BOTAO.value,
            fg="white",
            command=self.conferir_resposta,
        )
        botao_confirmar.pack(pady=5)

        self.label_feedback = tk.Label(
            self.container,
            text= "",
            font=self.fonte_normal,
            bg=ConfiguracoesJogo.COR_FUNDO.value,
            fg=ConfiguracoesJogo.COR_TEXTO.value,
        )
        self.label_feedback.pack(pady=10)

        return numero1, numero2, operador, resposta

    def conferir_resposta(self):
        texto_digitado = self.entrada_resposta.get().strip()

        # Valida se a entrada do aluno é número válido
        if not texto_digitado.lstrip("-").isdigit():
            self.label_feedback.config(text="Digite apenas números.",
                                       fg=ConfiguracoesJogo.COR_ERRADO.value)
            return

        resposta_aluno = int(texto_digitado)

        if resposta_aluno == self.resposta_correta:
            self.acertos += 1
            self.label_feedback.config(text="✅ Certo! Muito bem!",
                                       fg=ConfiguracoesJogo.COR_CERTO.value)

        else:
            self.erros += 1
            self.label_feedback.config(text=f"❌ Errado! A resposta é {self.resposta_correta}.",
                                       fg=ConfiguracoesJogo.COR_ERRADO.value)

        # Desabilita o campo e o botão para evitar respostas duplicadas
        self.entrada_resposta.config(state="disabled")

        # Aguarda 1,5 seg exibindo o feedback
        # e então avança para a próxima pergunta
        self.after(1500, self.proxima_pergunta)

    # Tela 3: Tela final, exibida ao término das perguntas

    def finalizar_jogo(self):
        self.limpar_tela()

        # Salva o resultado da sessão no banco de dados
        banco_dados.salvar_pontuacao(self.nome_aluno, self.acertos, self.erros)

        titulo = tk.Label(
            self.container,
            text="Fim de jogo!",
            font=self.fonte_titulo,
            bg=ConfiguracoesJogo.COR_FUNDO.value,
            fg=ConfiguracoesJogo.COR_TEXTO.value,
        )
        titulo.pack(pady=30)

        resultado = tk.Label(
            self.container,
            text=f"Parabéns, {self.nome_aluno}!\n\n"
            f"Acertos: {self.acertos}\n"
            f"Erros: {self.erros}",
            font=self.fonte_normal,
            bg=ConfiguracoesJogo.COR_FUNDO.value,
            fg=ConfiguracoesJogo.COR_TEXTO.value,
            justify="center",
        )
        resultado.pack(pady=10)

        botao_jogar_novamente = tk.Button(
            self.container,
            text="Jogar Novamente",
            font=self.fonte_botao,
            bg=ConfiguracoesJogo.COR_BOTAO.value,
            fg="white",
            command=self.reiniciar_jogo,
        )
        botao_jogar_novamente.pack(pady=15, ipadx=10, ipady=5)

        botao_menu = tk.Button(
            self.container,
            text="Voltar ao Menu Inicial",
            font=self.fonte_normal,
            bg="#B0BEC5",
            fg="white",
            command=self.mostrar_tela_inicial,
        )
        botao_menu.pack(pady=5)

    def reiniciar_jogo(self):
        self.acertos = 0
        self.erros = 0
        self.pergunta_atual = 0

        self.proxima_pergunta()

    def mostrar_tela_ranking(self):
        self.limpar_tela()

        titulo = tk.Label(
            self.container,
            text="🏆 Melhores Resultados",
            font=self.fonte_titulo,
            bg=ConfiguracoesJogo.COR_FUNDO.value,
            fg=ConfiguracoesJogo.COR_TEXTO.value,
        )
        titulo.pack(pady=20)

        ranking = banco_dados.buscar_ranking(limite=10)

        # Área de texto para listar resultados
        area_lista = tk.Frame(self.container, bg=ConfiguracoesJogo.COR_FUNDO.value)
        area_lista.pack(pady=10, fill="both", expand=True, padx=20)

        if not ranking:
            tk.Label(
                area_lista,
                text="Ainda não há resultados salvos.",
                font=self.fonte_normal,
                bg=ConfiguracoesJogo.COR_FUNDO.value,
                fg=ConfiguracoesJogo.COR_TEXTO.value,
            ).pack()
        else:
            cabecalho = tk.Label(
                area_lista,
                text=f"{'Nome':<15}{'Acertos':>10}{'Erros':>10}",
                font=("Courier", 12, "bold"),
                bg=ConfiguracoesJogo.COR_FUNDO.value,
                fg=ConfiguracoesJogo.COR_TEXTO.value,
            )
            cabecalho.pack()

            # Lista cada resultado, um por linha
            for nome, acertos, erros, data_hora in ranking:
                linha = tk.Label(
                    area_lista,
                    text=f"{nome:<15}{acertos:>10}{erros:>10}",
                    font=("Courier", 12),
                    bg=ConfiguracoesJogo.COR_FUNDO.value,
                    fg=ConfiguracoesJogo.COR_TEXTO.value,
                )
                linha.pack()

        botao_voltar = tk.Button(
            self.container,
            text="Voltar",
            font=self.fonte_botao,
            bg=ConfiguracoesJogo.COR_BOTAO.value,
            fg="white",
            command=self.mostrar_tela_inicial,
        )
        botao_voltar.pack(pady=20)

# Ponto de entrada do programa
if __name__ == "__main__":
    app = JogoMatematica()
    app.mainloop()