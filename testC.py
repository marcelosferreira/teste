import tkinter as tk

class FormularioPassoAPasso:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Esboço da Jornada")

        self.etapas = [
            "Especificação do esquema de certificação",
            "Especificação da demanda",
            "Especificação das fontes de geração de energia"
        ]
        self.etapa_atual = tk.StringVar(value=self.etapas[0])

        # Defina o tamanho fixo da janela (largura x altura)
        largura_janela = 800
        altura_janela = 600
        self.janela.geometry(f"{largura_janela}x{altura_janela}")

        # Configurar menu lateral
        self.menu_lateral = tk.Frame(self.janela, bg="lightgray", width=200)
        self.menu_lateral.pack(side="left", fill="y")

        for etapa in self.etapas:
            tk.Radiobutton(self.menu_lateral, text=etapa, wraplength=200, justify="left", variable=self.etapa_atual, value=etapa, command=self.mostrar_etapa).pack(anchor="w")

        # Configurar o conteúdo da etapa
        self.conteudo_etapa = tk.Frame(self.janela, padx=20, pady=20)
        self.conteudo_etapa.pack(side="right", fill="both", expand=True)

        # Botões de navegação
        self.botao_anterior = tk.Button(self.conteudo_etapa, text="Anterior", command=self.etapa_anterior)
        self.botao_anterior.pack(side="left")
        self.botao_proximo = tk.Button(self.conteudo_etapa, text="Próximo", command=self.proxima_etapa)
        self.botao_proximo.pack(side="right")

        # Configurar conteúdo das etapas
        self.conteudo_etapas = [self.criar_etapa1(), self.criar_etapa2(), self.criar_etapa3()]

        # Mostrar a primeira etapa por padrão
        self.mostrar_etapa()

    def criar_etapa1(self):
        etapa1 = tk.Frame(self.conteudo_etapa)

        # Campo de seleção de certificação
        tk.Label(etapa1, text="Selecionar uma opção de esquemas de certificação:").pack()
        opcoes_certificacao = ["H2Global", "CCEE", "Outros"]
        self.certificacao_var = tk.StringVar(etapa1)
        self.certificacao_var.set(opcoes_certificacao[0])  # Define a opção padrão
        certificacao_menu = tk.OptionMenu(etapa1, self.certificacao_var, *opcoes_certificacao)
        certificacao_menu.pack()

        # Campo de seleção de fronteira
        tk.Label(etapa1, text="Selecionar uma opção de fronteira:").pack()
        opcoes_fronteira = ["Ponto de Uso", "Ponto de Produção", "Inclui metano..."]
        self.fronteira_var = tk.StringVar(etapa1)
        self.fronteira_var.set(opcoes_fronteira[0])  # Define a opção padrão
        fronteira_menu = tk.OptionMenu(etapa1, self.fronteira_var, *opcoes_fronteira)
        fronteira_menu.pack()

        # Conjunto de checkboxes para seleção de fontes
        tk.Label(etapa1, text="Selecionar fontes de energia autorizadas:").pack()
        self.fontes_selecionadas = []  # Armazena as fontes selecionadas
        fontes_opcoes = ["Eólica", "Solar", "Elétrica", "Outras"]

        for opcao in fontes_opcoes:
            fonte_var = tk.BooleanVar()
            checkbox = tk.Checkbutton(etapa1, text=opcao, variable=fonte_var)
            checkbox.pack(anchor="w")
            self.fontes_selecionadas.append((opcao, fonte_var))

        # Valor da meta de participação
        tk.Label(etapa1, text="Informar valor da meta de participação de renováveis:").pack()
        self.vlMeta_entry = tk.Entry(etapa1)
        self.vlMeta_entry.pack()

        # Informar especificação da pressão do H2
        tk.Label(etapa1, text="Informar especificação da pressão do H2:").pack()
        self.vlPressao_entry = tk.Entry(etapa1)
        self.vlPressao_entry.pack()

        # Informar especificação da pureza do H2
        tk.Label(etapa1, text="Informar especificação da pureza do H2:").pack()
        self.vlPureza_entry = tk.Entry(etapa1)
        self.vlPureza_entry.pack()

        # Campo de seleção de periodo de contabilização
        tk.Label(etapa1, text="Selecionar periodo de contabilização:").pack()
        opcoes_periodo = ["30 min", "horário", "diário", "semanal", "mensal"]
        self.periodo_var = tk.StringVar(etapa1)
        self.periodo_var.set(opcoes_periodo[0])  # Define a opção padrão
        periodo_menu = tk.OptionMenu(etapa1, self.periodo_var, *opcoes_periodo)
        periodo_menu.pack()

        return etapa1

    def criar_etapa2(self):
        etapa2 = tk.Frame(self.conteudo_etapa)

        tk.Label(etapa2, text="Mensagem:").pack()
        self.mensagem_entry = tk.Entry(etapa2)
        self.mensagem_entry.pack()

        tk.Label(etapa2, text="Comentário:").pack()
        self.comentario_entry = tk.Entry(etapa2)
        self.comentario_entry.pack()

        tk.Label(etapa2, text="Caminho:").pack()
        self.caminho_entry = tk.Entry(etapa2)
        self.caminho_entry.pack()

        return etapa2

    def criar_etapa3(self):
        etapa3 = tk.Frame(self.conteudo_etapa)

        tk.Label(etapa3, text="Nível de Satisfação:").pack()
        self.satisfacao_entry = tk.Entry(etapa3)
        self.satisfacao_entry.pack()

        tk.Label(etapa3, text="Nota do Atendimento:").pack()
        self.nota_entry = tk.Entry(etapa3)
        self.nota_entry.pack()

        tk.Button(etapa3, text="Enviar", command=self.enviar_formulario).pack()

        return etapa3

    def mostrar_etapa(self):
        etapa_atual_index = self.etapas.index(self.etapa_atual.get())
        for etapa in self.conteudo_etapas:
            etapa.pack_forget()
        self.conteudo_etapas[etapa_atual_index].pack(fill="both", expand=True)
        self.botao_anterior.config(state="normal" if etapa_atual_index > 0 else "disabled")
        self.botao_proximo.config(state="normal" if etapa_atual_index < len(self.etapas) - 1 else "disabled")

    def etapa_anterior(self):
        etapa_atual_index = self.etapas.index(self.etapa_atual.get())
        if etapa_atual_index > 0:
            self.etapa_atual.set(self.etapas[etapa_atual_index - 1])
            self.mostrar_etapa()

    def proxima_etapa(self):
        etapa_atual_index = self.etapas.index(self.etapa_atual.get())
        if etapa_atual_index < len(self.etapas) - 1:
            self.etapa_atual.set(self.etapas[etapa_atual_index + 1])
            self.mostrar_etapa()

    def enviar_formulario(self):
        a=0
        # Aqui você pode adicionar o código para enviar os dados do formulário para onde desejar
        # Por exemplo, você pode acessar os valores dos campos usando self.nome_entry.get(), self.email_entry.get(), etc.
        # E então, enviar esses dados para um servidor, banco de dados, ou onde quer que você precise.

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioPassoAPasso(root)
    root.mainloop()
