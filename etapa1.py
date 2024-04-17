#etata1.py
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from PIL import Image, ImageTk
import masks
from tooltip import Tooltip
     
def criar_etapa1(self,conteudo):

        self.criterioA_intensidade_carbono = tk.StringVar()
        self.criterioA_part_minima = tk.StringVar()
        self.criterioA_contratacao_planta_temporal = tk.StringVar()
        self.criterioA_contratacao_planta_espacial = tk.StringVar()
        self.criterioA_contratacao_planta_adicionalidade = tk.StringVar()
        self.criterioB_intensidade_carbono = tk.StringVar()
        self.criterioB_part_minima = tk.StringVar()
        self.criterioB_contratacao_planta_temporal = tk.StringVar()
        self.criterioB_contratacao_planta_espacial = tk.StringVar()
        self.criterioB_contratacao_planta_adicionalidade = tk.StringVar()
        self.criterioC_intensidade_carbono = tk.StringVar()
        self.criterioC_part_minima = tk.StringVar()
        self.criterioC_contratacao_planta_temporal = tk.StringVar()
        self.criterioC_contratacao_planta_espacial = tk.StringVar()
        self.criterioC_contratacao_planta_adicionalidade = tk.StringVar()
        self.criterioD_intensidade_carbono = tk.StringVar()
        self.criterioD_part_minima = tk.StringVar()
        self.criterioD_contratacao_planta_temporal = tk.StringVar()
        self.criterioD_contratacao_planta_espacial = tk.StringVar()
        self.criterioD_contratacao_planta_adicionalidade = tk.StringVar()
        self.criterioE_intensidade_carbono = tk.StringVar()
        self.criterioE_part_minima = tk.StringVar()
        self.criterioE_contratacao_planta_temporal = tk.StringVar()
        self.criterioE_contratacao_planta_espacial = tk.StringVar()
        self.criterioE_contratacao_planta_adicionalidade = tk.StringVar()
        self.criterioF_intensidade_carbono = tk.StringVar()
        self.criterioF_part_minima = tk.StringVar()
        self.criterioF_contratacao_planta_temporal = tk.StringVar()
        self.criterioF_contratacao_planta_espacial = tk.StringVar()
        self.criterioF_contratacao_planta_adicionalidade = tk.StringVar()
        fonte = tkfont.Font(family="Helvetica", size=10, weight="bold")
        ttk.Label(conteudo, text="1. Tipo de Certificação:",font=fonte).grid(row=1, column=0, pady=20, sticky="w")
        #botao_restaurar = ttk.Button(conteudo, text="Restaurar")
        #botao_restaurar.grid(row=1, column=3, pady=20)
        self.certif_var = tk.StringVar()
        self.op_certfic_var = tk.StringVar()
                
        tk.Radiobutton(conteudo, text="Certificação de Energia Fornecida", variable=self.certif_var, value="energia_fornecida", command= lambda:on_certificacao_changed()).grid(row=2, column=0, columnspan=2, padx=10, sticky="w")
        tk.Radiobutton(conteudo, text="Certificação de Hidrogênio Produzido", variable=self.certif_var, value="hidrgenio_produzido", command= lambda:on_certificacao_changed()).grid(row=2, column=2, columnspan=2, sticky="w")

        ttk.Label(conteudo, text="2. Selecione uma opção de esquemas de certificação:", font=self.fonteB).grid(row=3, pady=20, column=0, columnspan=4, sticky="w")
        self.certificacao_selecionadas = []
        certificacao_opcoes = ["24 7 CFE (Carbon Free Energy)", "RED - Renewable Energy Directive", "Low Carbon Hydrogen Standard", "CHPS - Clean Hydrogen Production Standard", "Outro"]
        for col, opcao in enumerate(certificacao_opcoes):
            certificacao_var = tk.BooleanVar(),
            self.certificacao_selecionadas.append((opcao, certificacao_var))

            imagem = Image.open(f"{opcao.lower().replace(' ', '_')}.png")
            largura_maxima = 50
            imagem.thumbnail((largura_maxima, largura_maxima))
            imagem = ImageTk.PhotoImage(imagem)

            imagem_label = tk.Label(conteudo, image=imagem)
            imagem_label.grid(row=4, column=col, padx=10, sticky="w")
            tk.Radiobutton(conteudo, text=opcao, justify="left", variable=self.op_certfic_var, value=opcao, wraplength=110, command= lambda:on_opcertificacao_changed()).grid(row=5, column=col, padx=10, sticky="w")
            imagem_label.image = imagem  

        ttk.Label(conteudo, text="3. Especificações dos critérios para uso da Energia da rede:", font=self.fonteB).grid(row=6, column=0, columnspan=5, pady=20, sticky="w")
        ttk.Label(conteudo, wraplength=360, text="- No caso de Certificação de Energia Fornecida, qual a participação mínima de fontes de baixo carbono? (%)").grid(row=7, column=0, columnspan=6, padx=20, sticky="w")
        self.part_minima = ttk.Entry(conteudo)
        self.part_minima.grid(row=7, column=3, padx=10, sticky="w")
        self.part_minima.bind("<KeyRelease>", lambda event: maskEnergiaFornecida(event))
        ttk.Label(conteudo, text="- No caso das Certificações do Hidrogênio, marque as opções de métricas apresentadas na tabela abaixo que compõe cada possível critério.").grid(row=8, column=0, columnspan=6, padx=20, pady=12, sticky="w")
        
        add_criterio_botao = ttk.Button(conteudo, text="Ajuda")
        add_criterio_botao.grid(row=9, column=0, pady=20)
        tooltip_text = """A matriz de critérios apresentada ao lado permite criar relações de métricas
do tipo “e” (isto é, precisam ser atendidas conjuntamente) e do tipo “ou” 
(isto é, precisam ser atendidas de forma forma independente entre si). Dessa
forma, ao marcar métricas na mesma linha (relação tipo “e”) de critério,
significa que o cálculo irá considerar condições de atendimento conjunto
àquelas métricas selecionadas. Caso estejam marcadas em linhas diferentes
(relação tipo “ou”), formam-se critérios distintos com conjunto de métricas
que serão atendidas de forma independente. Por fim, note que os valores 
relativos a cada métrica são especificados na sequência da tela."""

        Tooltip(add_criterio_botao, tooltip_text)
        tk.Label(conteudo, wraplength=110, justify="center", text="Intensidade de carbono no Grid").grid(row=9, column=1, padx=5, pady=20, sticky="w")
        tk.Label(conteudo, wraplength=110, justify="center", text="Participação mínima de renováveis no grid").grid(row=9, column=2, padx=5, pady=20, sticky="w")
        tk.Label(conteudo, wraplength=110, justify="center", text="Contratação de planta de baixo carbono com correlação temporal").grid(row=9, column=3, padx=5, pady=20, sticky="w")
        tk.Label(conteudo, wraplength=110, justify="center", text="Contratação de planta de baixo carbono com correlação espacial").grid(row=9, column=4, padx=5, pady=20, sticky="w")
        tk.Label(conteudo, wraplength=100, justify="center", text="Contratação de planta de baixo carbono com adicionalidade").grid(row=9, column=5, padx=25, pady=20, sticky="w")
        
        tk.Label(conteudo, wraplength=100, justify="center", text="Critério A").grid(row=10, column=0, padx=20, sticky="w")        
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioA_intensidade_carbono, command= lambda:trocar_para_outro()).grid(row=10, column=1, padx=40, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioA_part_minima, command= lambda:trocar_para_outro()).grid(row=10, column=2, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioA_contratacao_planta_temporal, command= lambda:trocar_para_outro()).grid(row=10, column=3, padx=50, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioA_contratacao_planta_espacial, command= lambda:trocar_para_outro()).grid(row=10, column=4, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioA_contratacao_planta_adicionalidade, command= lambda:trocar_para_outro()).grid(row=10, column=5, padx=55, sticky="w")

        tk.Label(conteudo, wraplength=100, justify="center", text="Critério B").grid(row=11, column=0, padx=20, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioB_intensidade_carbono, command= lambda:trocar_para_outro()).grid(row=11, column=1, padx=40, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioB_part_minima, command= lambda:trocar_para_outro()).grid(row=11, column=2, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioB_contratacao_planta_temporal, command= lambda:trocar_para_outro()).grid(row=11, column=3, padx=50, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioB_contratacao_planta_espacial, command= lambda:trocar_para_outro()).grid(row=11, column=4, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioB_contratacao_planta_adicionalidade, command= lambda:trocar_para_outro()).grid(row=11, column=5, padx=55, sticky="w")

        tk.Label(conteudo, wraplength=100, justify="center", text="Critério C").grid(row=12, column=0, padx=20, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioC_intensidade_carbono, command= lambda:trocar_para_outro()).grid(row=12, column=1, padx=40, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioC_part_minima, command= lambda:trocar_para_outro()).grid(row=12, column=2, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioC_contratacao_planta_temporal, command= lambda:trocar_para_outro()).grid(row=12, column=3, padx=50, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioC_contratacao_planta_espacial, command= lambda:trocar_para_outro()).grid(row=12, column=4, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioC_contratacao_planta_adicionalidade, command= lambda:trocar_para_outro()).grid(row=12, column=5, padx=55, sticky="w")

        tk.Label(conteudo, wraplength=100, justify="center", text="Critério D").grid(row=13, column=0, padx=20, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioD_intensidade_carbono, command= lambda:trocar_para_outro()).grid(row=13, column=1, padx=40, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioD_part_minima, command= lambda:trocar_para_outro()).grid(row=13, column=2, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioD_contratacao_planta_temporal, command= lambda:trocar_para_outro()).grid(row=13, column=3, padx=50, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioD_contratacao_planta_espacial, command= lambda:trocar_para_outro()).grid(row=13, column=4, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioD_contratacao_planta_adicionalidade, command= lambda:trocar_para_outro()).grid(row=13, column=5, padx=55, sticky="w")

        tk.Label(conteudo, wraplength=100, justify="center", text="Critério E").grid(row=14, column=0, padx=20, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioE_intensidade_carbono, command= lambda:trocar_para_outro()).grid(row=14, column=1, padx=40, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioE_part_minima, command= lambda:trocar_para_outro()).grid(row=14, column=2, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioE_contratacao_planta_temporal, command= lambda:trocar_para_outro()).grid(row=14, column=3, padx=50, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioE_contratacao_planta_espacial, command= lambda:trocar_para_outro()).grid(row=14, column=4, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioE_contratacao_planta_adicionalidade, command= lambda:trocar_para_outro()).grid(row=14, column=5, padx=55, sticky="w")

        tk.Label(conteudo, wraplength=100, justify="center", text="Critério F").grid(row=15, column=0, padx=20, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioF_intensidade_carbono, command= lambda:trocar_para_outro()).grid(row=15, column=1, padx=40, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioF_part_minima, command= lambda:trocar_para_outro()).grid(row=15, column=2, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioF_contratacao_planta_temporal, command= lambda:trocar_para_outro()).grid(row=15, column=3, padx=50, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioF_contratacao_planta_espacial, command= lambda:trocar_para_outro()).grid(row=15, column=4, padx=45, sticky="w")
        tk.Checkbutton(conteudo, justify="center", variable=self.criterioF_contratacao_planta_adicionalidade, command= lambda:trocar_para_outro()).grid(row=15, column=5, padx=55, sticky="w")

        ttk.Label(conteudo, text="Especificações das Métricas selecionadas na tabela anterior:").grid(row=16, column=0, columnspan=6, padx=20, pady=14, sticky="w")
        ttk.Label(conteudo, text="- Limite de Intensidade de Carbono do Grid (gCO₂/MJ):").grid(row=17, column=0, columnspan=6, padx=20, pady=6, sticky="w")
        self.limite_intensidade = ttk.Entry(conteudo)
        self.limite_intensidade.grid(row=17, column=3, padx=10, sticky="w")
        self.limite_intensidade.bind("<KeyRelease>", lambda event: maskCertificacao(event))
        ttk.Label(conteudo, wraplength=390, text="- Limite de Participação mínima de renováveis da energia da rede (%):").grid(row=18, column=0, columnspan=6, padx=20, pady=6, sticky="w")
        self.limite_particiapacao = ttk.Entry(conteudo)
        self.limite_particiapacao.grid(row=18, column=3, padx=10, sticky="w")
        self.limite_particiapacao.bind("<KeyRelease>", lambda event: maskCertificacao(event))
        ttk.Label(conteudo, wraplength=390, text="- Matching para balanço de energia:").grid(row=19, column=0, columnspan=6, padx=20, pady=6, sticky="w")
        opcoes_balanco_energia = ["Mensal", "Semanal", "Horária", "A cada 30 min"]
        self.balanco_energia = tk.StringVar(conteudo)
        self.balanco_energia.set(opcoes_balanco_energia[0])
        self.menu_balanco_energia = ttk.Combobox(conteudo, textvariable=self.balanco_energia, values=opcoes_balanco_energia, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_balanco_energia)), '%P'))
        self.menu_balanco_energia.bind("<<ComboboxSelected>>", lambda event: maskCertificacao(event))
        self.menu_balanco_energia.grid(row=19, column=3, padx=10, sticky="w")
        ttk.Label(conteudo, wraplength=390, text="- Limite da Bidding Zone:").grid(row=20, column=0, columnspan=6, padx=20, pady=6, sticky="w")
        opcoes_limite_bidding_zone = ["SIN", "Subsistema", "Distância (Informar valor)"]
        self.limite_bidding_zone = tk.StringVar(conteudo)
        self.limite_bidding_zone.set(opcoes_limite_bidding_zone[0])
        self.menu_limite_bidding_zone = ttk.Combobox(conteudo, textvariable=self.limite_bidding_zone, values=opcoes_limite_bidding_zone, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_limite_bidding_zone)), '%P'))
        self.menu_limite_bidding_zone.bind("<<ComboboxSelected>>", lambda event: habilitar_bidding_zone(event))
        self.menu_limite_bidding_zone.grid(row=20, column=3, padx=10, columnspan=3, sticky="w")

        self.limite_bidding_zone_distancia = ttk.Entry(conteudo, state='disabled')
        self.limite_bidding_zone_distancia.grid(row=20, column=4, columnspan=3, sticky="w")
        
        ttk.Label(conteudo, wraplength=390, text="- Limite para adicionalidade (anos):").grid(row=21, column=0, columnspan=6, padx=20, pady=6, sticky="w")
        self.limite_adicionalidade = ttk.Entry(conteudo)
        self.limite_adicionalidade.grid(row=21, column=3, padx=10, columnspan=3, sticky="w")
        self.limite_adicionalidade.bind("<KeyRelease>", lambda event: maskCertificacao(event))
        
        ttk.Label(conteudo, text="4. Especificações da contabilização das Emissões de CO₂ do projeto:", font=self.fonteB).grid(row=22, column=0, columnspan=5, pady=20, sticky="w")
        ttk.Label(conteudo, wraplength=360, text="- Limite de emissões da cadeia de produção (gCO₂e/MJ de H₂):").grid(row=23, column=0, columnspan=6, padx=20, sticky="w")
        self.limite_emissoes_cadeira_producao = ttk.Entry(conteudo)
        self.limite_emissoes_cadeira_producao.grid(row=23, column=3, padx=10, sticky="w")
        self.limite_emissoes_cadeira_producao.bind("<KeyRelease>", lambda event: maskCertificacao(event))

        ttk.Label(conteudo, wraplength=390, text="- Periodicidade das checagens de emissões:").grid(row=24, column=0, columnspan=6, padx=20, pady=6, sticky="w")
        opcoes_periodicidade_checagens = ["Anual", "Mensal", "Semanal", "N/A"]
        self.periodicidade_checagens = tk.StringVar(conteudo)
        self.periodicidade_checagens.set(opcoes_periodicidade_checagens[1])
        self.periodicidade_checagens_menu = ttk.Combobox(conteudo, textvariable=self.periodicidade_checagens, values=opcoes_periodicidade_checagens, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_periodicidade_checagens)), '%P'))
        self.periodicidade_checagens_menu.bind("<<ComboboxSelected>>", lambda event: maskCertificacao(event))
        self.periodicidade_checagens_menu.grid(row=24, column=3, padx=10, sticky="w")

        ttk.Label(conteudo, wraplength=390, text="- Fronteira de análise das emissões:").grid(row=25, column=0, columnspan=6, padx=20, pady=6, sticky="w")
        opcoes_fronteira_analise = ["Até a produção", "Até a entrega"]
        self.fronteira_analise = tk.StringVar(conteudo)
        self.fronteira_analise.set(opcoes_fronteira_analise[0])
        self.menu_fronteira_analise = ttk.Combobox(conteudo, textvariable=self.fronteira_analise, values=opcoes_fronteira_analise, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_fronteira_analise)), '%P'))
        self.menu_fronteira_analise.bind("<<ComboboxSelected>>", lambda event: maskCertificacao(event))
        self.menu_fronteira_analise.grid(row=25, column=3, padx=10, sticky="w")
        
        ttk.Label(conteudo, wraplength=360, text="- Imaterialidade (gCO₂e/MJ de H₂):").grid(row=26, column=0, columnspan=6, padx=20, sticky="w")
        self.imaterialidade = ttk.Entry(conteudo)
        self.imaterialidade.grid(row=26, column=3, padx=10, sticky="w")
        self.imaterialidade.bind("<KeyRelease>", lambda event: maskCertificacao(event))

        ttk.Label(conteudo, wraplength=390, text="- Critério de emissões da cadeia de produção:").grid(row=27, column=0, columnspan=6, padx=20, pady=6, sticky="w")
        opcoes_criterio_fator_emissão_hidrogenio = ["Somente combustão", "Combustão + Upstream"]
        self.criterio_fator_emissão_hidrogenio = tk.StringVar(conteudo)
        self.criterio_fator_emissão_hidrogenio.set(opcoes_criterio_fator_emissão_hidrogenio[0])
        self.menu_criterio_fator_emissão_hidrogenio = ttk.Combobox(conteudo, textvariable=self.criterio_fator_emissão_hidrogenio, values=opcoes_criterio_fator_emissão_hidrogenio, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_criterio_fator_emissão_hidrogenio)), '%P'))
        self.menu_criterio_fator_emissão_hidrogenio.bind("<<ComboboxSelected>>", lambda event: maskCertificacao(event))
        self.menu_criterio_fator_emissão_hidrogenio.grid(row=27, column=3, padx=10, sticky="w")
        
        ttk.Label(conteudo, wraplength=390, text="- Período de validade da aprovação como grid fully renewable (anos):").grid(row=28, column=0, columnspan=6, padx=20, sticky="w")
        self.periodo_validade_aprovacao = ttk.Entry(conteudo)
        self.periodo_validade_aprovacao.grid(row=28, column=3, padx=10, sticky="w")
        self.periodo_validade_aprovacao.bind("<KeyRelease>", lambda event: maskCertificacao(event))

        ttk.Label(conteudo, text="5. Especificações de padronização do H₂:", font=self.fonteB).grid(row=29, column=0, columnspan=5, pady=20, sticky="w")
        tk.Checkbutton(conteudo, wraplength=250, justify="left", text="Considerar padrão de pressão para H₂. Informar valor ao lado (MPa): ", command= lambda:trocar_para_outro()).grid(row=30, column=0, columnspan=3, padx=10, sticky="w")
        self.padrao_pressao_hidrogenio = ttk.Entry(conteudo)
        self.padrao_pressao_hidrogenio.grid(row=30, column=2, padx=10, sticky="w")
        self.padrao_pressao_hidrogenio.bind("<KeyRelease>", lambda event: maskCertificacao(event))
        self.padrao_pureza = tk.StringVar()
        tk.Checkbutton(conteudo, justify="left", text="Considerar um padrão de 99,9% de pureza para o H₂", variable=self.padrao_pureza, command= lambda:trocar_para_outro()).grid(row=31, column=0, columnspan=3, padx=10, sticky="w")


        ## Interações entre campos ##
        #
        def on_certificacao_changed():
            selected_option = self.certif_var.get()
            if selected_option == "energia_fornecida":
                self.op_certfic_var.set("24 7 CFE (Carbon Free Energy)")
                for widget in conteudo.winfo_children():
                    if isinstance(widget, tk.Radiobutton) and widget.cget("text") == "24 7 CFE (Carbon Free Energy)":
                        widget.config(state=tk.NORMAL)
                    elif isinstance(widget, tk.Radiobutton) and widget.cget("text") == "RED - Renewable Energy Directive":
                        widget.config(state=tk.DISABLED)
                    elif isinstance(widget, tk.Radiobutton) and widget.cget("text") == "Low Carbon Hydrogen Standard":
                        widget.config(state=tk.DISABLED)
                    elif isinstance(widget, tk.Radiobutton) and widget.cget("text") == "CHPS - Clean Hydrogen Production Standard":
                        widget.config(state=tk.DISABLED)
                    elif isinstance(widget, tk.Radiobutton) and widget.cget("text") == "Outro":
                        widget.config(state=tk.DISABLED)
                self.part_minima.config(state=tk.NORMAL),
                defaultCriterios()
                self.criterioA_part_minima.set(1)
                self.criterioB_contratacao_planta_temporal.set(1)
                self.criterioB_contratacao_planta_espacial.set(1)
                self.criterioB_contratacao_planta_adicionalidade.set(1)
                self.criterioC_intensidade_carbono.set(1)
                self.criterioC_contratacao_planta_temporal.set(1)
                self.criterioC_contratacao_planta_espacial.set(1)                
                self.limite_intensidade.config(state=tk.NORMAL)
                self.limite_intensidade.delete(0, tk.END)
                self.limite_intensidade.insert(0, "")
                self.limite_particiapacao.delete(0, tk.END)
                self.limite_particiapacao.insert(0, "")
                self.menu_balanco_energia.set("A cada 30 min")
                self.menu_limite_bidding_zone.set("SIN")
                self.limite_bidding_zone_distancia.config(state='disabled')
                self.periodicidade_checagens_menu.set("Mensal")
                self.limite_adicionalidade.config(state=tk.NORMAL)
                self.limite_adicionalidade.delete(0, tk.END)
                self.limite_adicionalidade.insert(0, "")
                self.limite_emissoes_cadeira_producao.delete(0, tk.END)
                self.limite_emissoes_cadeira_producao.insert(0, "")
                self.menu_fronteira_analise.set("Até a produção")
                self.imaterialidade.config(state=tk.NORMAL)
                self.imaterialidade.delete(0, tk.END)
                self.imaterialidade.insert(0, "")
                self.limite_adicionalidade.config(state=tk.NORMAL)
                self.menu_criterio_fator_emissão_hidrogenio.set("Combustão + Upstream")
                self.periodo_validade_aprovacao.config(state=tk.NORMAL)
                self.periodo_validade_aprovacao.delete(0, tk.END)
                self.periodo_validade_aprovacao.insert(0, "")
                for widget in conteudo.winfo_children():
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar padrão de pressão para H₂. Informar valor ao lado (MPa): ":
                        widget.select()
                        widget.config(state=tk.NORMAL)
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar um padrão de 99,99% de pureza para o H₂":
                        widget.select()
                        widget.config(state=tk.NORMAL)
                self.padrao_pressao_hidrogenio.config(state=tk.NORMAL)
                self.padrao_pressao_hidrogenio.delete(0, tk.END)
                self.padrao_pressao_hidrogenio.insert(0, "")

            elif selected_option == "hidrgenio_produzido":
                self.op_certfic_var.set("RED - Renewable Energy Directive")
                for widget in conteudo.winfo_children():
                    if isinstance(widget, tk.Radiobutton) and widget.cget("text") == "24 7 CFE (Carbon Free Energy)":
                        widget.config(state=tk.DISABLED)
                    elif isinstance(widget, tk.Radiobutton) and widget.cget("text") == "RED - Renewable Energy Directive":
                        widget.config(state=tk.NORMAL)
                    elif isinstance(widget, tk.Radiobutton) and widget.cget("text") == "Low Carbon Hydrogen Standard":
                        widget.config(state=tk.NORMAL)
                    elif isinstance(widget, tk.Radiobutton) and widget.cget("text") == "CHPS - Clean Hydrogen Production Standard":
                        widget.config(state=tk.NORMAL)
                    elif isinstance(widget, tk.Radiobutton) and widget.cget("text") == "Outro":
                        widget.config(state=tk.NORMAL)
                self.part_minima.config(state=tk.DISABLED)
        
        def on_opcertificacao_changed():
            selected_option = self.op_certfic_var.get()
            if selected_option == "RED - Renewable Energy Directive":
                defaultCriterios()
                self.limite_intensidade.config(state=tk.NORMAL)
                self.limite_intensidade.delete(0, tk.END)
                self.criterioA_part_minima.set(1)
                self.criterioB_contratacao_planta_temporal.set(1)
                self.criterioB_contratacao_planta_espacial.set(1)
                self.criterioB_contratacao_planta_adicionalidade.set(1)
                self.criterioC_intensidade_carbono.set(1)
                self.criterioC_contratacao_planta_temporal.set(1)
                self.criterioC_contratacao_planta_espacial.set(1)
                self.limite_intensidade.insert(0, "18")
                self.limite_particiapacao.delete(0, tk.END)
                self.limite_particiapacao.insert(0, "90")
                self.menu_balanco_energia.set("Horária")
                self.menu_limite_bidding_zone.set("SIN")
                self.limite_bidding_zone_distancia.config(state='disabled')
                self.periodicidade_checagens_menu.set("Mensal")
                self.limite_adicionalidade.config(state=tk.NORMAL)
                self.limite_adicionalidade.delete(0, tk.END)
                self.limite_adicionalidade.insert(0, "3")
                self.limite_emissoes_cadeira_producao.delete(0, tk.END)
                self.limite_emissoes_cadeira_producao.insert(0, "28.2")
                self.menu_fronteira_analise.set("Até a entrega")
                self.imaterialidade.delete(0, tk.END)
                self.imaterialidade.insert(0, "N/A")
                self.imaterialidade.config(state=tk.NORMAL)
                self.menu_criterio_fator_emissão_hidrogenio.set("Combustão + Upstream")
                self.periodo_validade_aprovacao.config(state=tk.NORMAL)
                self.periodo_validade_aprovacao.delete(0, tk.END)
                self.periodo_validade_aprovacao.insert(0, "5")
                for widget in conteudo.winfo_children():
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar padrão de pressão para H₂. Informar valor ao lado (MPa): ":
                        widget.deselect()
                        widget.config(state=tk.NORMAL)
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar um padrão de 99,9% de pureza para o H₂":
                        widget.deselect()
                        widget.config(state=tk.NORMAL)
                self.padrao_pressao_hidrogenio.delete(0, tk.END)
                self.padrao_pressao_hidrogenio.insert(0, "N/A")
                self.padrao_pressao_hidrogenio.config(state=tk.NORMAL)
            elif selected_option == "Low Carbon Hydrogen Standard":
                defaultCriterios()
                self.criterioA_contratacao_planta_espacial.set(1)
                self.limite_intensidade.delete(0, tk.END)
                self.limite_intensidade.insert(0, "N/A")
                self.limite_intensidade.config(state=tk.NORMAL)
                self.limite_particiapacao.delete(0, tk.END)
                self.limite_particiapacao.insert(0, "0")
                self.menu_balanco_energia.set("A cada 30 min")
                self.menu_limite_bidding_zone.set("SIN")
                self.limite_bidding_zone_distancia.config(state='disabled')
                self.periodicidade_checagens_menu.set("Mensal")
                self.limite_adicionalidade.delete(0, tk.END)
                self.limite_adicionalidade.insert(0, "N/A")
                self.limite_adicionalidade.config(state=tk.NORMAL)
                self.limite_emissoes_cadeira_producao.delete(0, tk.END)
                self.limite_emissoes_cadeira_producao.insert(0, "20")
                self.menu_fronteira_analise.set("Até a produção")
                self.imaterialidade.config(state=tk.NORMAL)
                self.imaterialidade.delete(0, tk.END)
                self.imaterialidade.insert(0, "0.2")
                self.menu_criterio_fator_emissão_hidrogenio.set("Combustão + Upstream")
                self.periodo_validade_aprovacao.config(state=tk.NORMAL)
                self.periodo_validade_aprovacao.delete(0, tk.END)
                self.periodo_validade_aprovacao.insert(0, "5")
                for widget in conteudo.winfo_children():
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar padrão de pressão para H₂. Informar valor ao lado (MPa): ":
                        widget.select()
                        widget.config(state=tk.NORMAL)
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar um padrão de 99,9% de pureza para o H₂":
                        widget.select()
                        widget.config(state=tk.NORMAL)
                self.padrao_pressao_hidrogenio.config(state=tk.NORMAL)
                self.padrao_pressao_hidrogenio.delete(0, tk.END)
                self.padrao_pressao_hidrogenio.insert(0, "3")
            ##Adicionei aqui
            elif selected_option == "CHPS - Clean Hydrogen Production Standard":
                defaultCriterios()
                self.limite_intensidade.delete(0, tk.END)
                self.limite_intensidade.insert(0, "N/A")
                self.limite_intensidade.config(state=tk.NORMAL)
                self.limite_particiapacao.delete(0, tk.END)
                self.limite_particiapacao.insert(0, "0")
                self.menu_balanco_energia.set("Horária")
                self.menu_limite_bidding_zone.set("SIN")
                self.limite_bidding_zone_distancia.config(state='disabled')
                self.periodicidade_checagens_menu.set("Mensal")
                self.limite_adicionalidade.delete(0, tk.END)
                self.limite_adicionalidade.insert(0, "N/A")
                self.limite_adicionalidade.config(state=tk.NORMAL)
                self.limite_emissoes_cadeira_producao.delete(0, tk.END)
                self.limite_emissoes_cadeira_producao.insert(0, "27.6")
                self.menu_fronteira_analise.set("Até a produção")
                self.imaterialidade.config(state=tk.NORMAL)
                self.imaterialidade.delete(0, tk.END)
                self.imaterialidade.insert(0, "0")
                self.menu_criterio_fator_emissão_hidrogenio.set("Combustão + Upstream")
                self.periodo_validade_aprovacao.config(state=tk.NORMAL)
                self.periodo_validade_aprovacao.delete(0, tk.END)
                self.periodo_validade_aprovacao.insert(0, "0")
                for widget in conteudo.winfo_children():
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar padrão de pressão para H₂. Informar valor ao lado (MPa): ":
                        widget.deselect()
                        widget.config(state=tk.NORMAL)
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar um padrão de 99,9% de pureza para o H₂":
                        widget.deselect()
                        widget.config(state=tk.NORMAL)
                self.padrao_pressao_hidrogenio.delete(0, tk.END)
                self.padrao_pressao_hidrogenio.insert(0, "N/A")
                self.padrao_pressao_hidrogenio.config(state=tk.NORMAL)
            ##Até aqui
            elif selected_option == "Outro":
                defaultCriterios()
                self.limite_intensidade.config(state=tk.NORMAL)
                self.limite_intensidade.delete(0, tk.END)
                self.limite_intensidade.insert(0, "")
                self.limite_particiapacao.delete(0, tk.END)
                self.limite_particiapacao.insert(0, "")
                self.menu_balanco_energia.set("A cada 30 min")
                self.menu_limite_bidding_zone.set("SIN")
                self.limite_bidding_zone_distancia.config(state='disabled')
                self.periodicidade_checagens_menu.set("Mensal")
                self.limite_adicionalidade.config(state=tk.NORMAL)
                self.limite_adicionalidade.delete(0, tk.END)
                self.limite_adicionalidade.insert(0, "")
                self.limite_emissoes_cadeira_producao.delete(0, tk.END)
                self.limite_emissoes_cadeira_producao.insert(0, "")
                self.menu_fronteira_analise.set("Até a produção")
                self.imaterialidade.config(state=tk.NORMAL)
                self.imaterialidade.delete(0, tk.END)
                self.imaterialidade.insert(0, "")
                self.limite_adicionalidade.config(state=tk.NORMAL)
                self.menu_criterio_fator_emissão_hidrogenio.set("Combustão + Upstream")
                self.periodo_validade_aprovacao.config(state=tk.NORMAL)
                self.periodo_validade_aprovacao.delete(0, tk.END)
                self.periodo_validade_aprovacao.insert(0, "")
                for widget in conteudo.winfo_children():
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar padrão de pressão para H₂. Informar valor ao lado (MPa): ":
                        widget.select()
                        widget.config(state=tk.NORMAL)
                    if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar um padrão de 99,9% de pureza para o H₂":
                        widget.select()
                        widget.config(state=tk.NORMAL)
                self.padrao_pressao_hidrogenio.config(state=tk.NORMAL)
                self.padrao_pressao_hidrogenio.delete(0, tk.END)
                self.padrao_pressao_hidrogenio.insert(0, "")
                

        def habilitar_bidding_zone(event):
            self.op_certfic_var.set("Outro")
            opcao_selecionada = self.limite_bidding_zone.get()
            if opcao_selecionada == "Distância (Informar valor)":
                self.limite_bidding_zone_distancia.config(state='normal')
            else:
                self.limite_bidding_zone_distancia.config(state='disabled')
        
        def trocar_para_outro():
            self.op_certfic_var.set("Outro")


        ## Valores Default ##
        #         
        def defaultCertificacao():
            self.certif_var.set("hidrgenio_produzido")
            self.op_certfic_var.set("RED - Renewable Energy Directive")
            for widget in conteudo.winfo_children():
                if isinstance(widget, tk.Radiobutton) and widget.cget("text") == "24 7 CFE (Carbon Free Energy)":
                    widget.config(state=tk.DISABLED)
            self.part_minima.config(state=tk.DISABLED)
            defaultCriterios()
            self.criterioA_part_minima.set(1)
            self.criterioB_contratacao_planta_temporal.set(1)
            self.criterioB_contratacao_planta_espacial.set(1)
            self.criterioB_contratacao_planta_adicionalidade.set(1)
            self.criterioC_intensidade_carbono.set(1)
            self.criterioC_contratacao_planta_temporal.set(1)
            self.criterioC_contratacao_planta_espacial.set(1) 
            self.limite_intensidade.delete(0, tk.END)
            self.limite_intensidade.insert(0, "18")
            self.limite_particiapacao.delete(0, tk.END)
            self.limite_particiapacao.insert(0, "90")
            self.menu_balanco_energia.set("Horária")
            self.menu_limite_bidding_zone.set("SIN")
            self.periodicidade_checagens_menu.set("Mensal")
            self.limite_adicionalidade.delete(0, tk.END)
            self.limite_adicionalidade.insert(0, "3")
            self.limite_emissoes_cadeira_producao.delete(0, tk.END)
            self.limite_emissoes_cadeira_producao.insert(0, "28.2")
            self.menu_fronteira_analise.set("Até a entrega")
            self.imaterialidade.delete(0, tk.END)
            self.imaterialidade.insert(0, "N/A")
            self.imaterialidade.config(state=tk.NORMAL)
            self.menu_criterio_fator_emissão_hidrogenio.set("Combustão + Upstream")
            self.periodo_validade_aprovacao.config(state=tk.NORMAL)
            self.periodo_validade_aprovacao.delete(0, tk.END)
            self.periodo_validade_aprovacao.insert(0, "5")
            for widget in conteudo.winfo_children():
                if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar padrão de pressão para H₂. Informar valor ao lado (MPa): ":
                    widget.deselect()
                    widget.config(state=tk.NORMAL)
                if isinstance(widget, tk.Checkbutton) and widget.cget("text") == "Considerar um padrão de 99,9% de pureza para o H₂":
                    widget.deselect()
                    widget.config(state=tk.NORMAL)
            self.padrao_pressao_hidrogenio.delete(0, tk.END)
            self.padrao_pressao_hidrogenio.insert(0, "N/A")
            self.padrao_pressao_hidrogenio.config(state=tk.NORMAL)

        def defaultCriterios():
            self.criterioA_intensidade_carbono.set(0)
            self.criterioA_part_minima.set(0)
            self.criterioA_contratacao_planta_temporal.set(0)
            self.criterioA_contratacao_planta_espacial.set(0)
            self.criterioA_contratacao_planta_adicionalidade.set(0)
            self.criterioB_intensidade_carbono.set(0)
            self.criterioB_part_minima.set(0)
            self.criterioB_contratacao_planta_temporal.set(0)
            self.criterioB_contratacao_planta_espacial.set(0)
            self.criterioB_contratacao_planta_adicionalidade.set(0)
            self.criterioC_intensidade_carbono.set(0)
            self.criterioC_part_minima.set(0)
            self.criterioC_contratacao_planta_temporal.set(0)
            self.criterioC_contratacao_planta_espacial.set(0)
            self.criterioC_contratacao_planta_adicionalidade.set(0)
            self.criterioD_intensidade_carbono.set(0)
            self.criterioD_part_minima.set(0)
            self.criterioD_contratacao_planta_temporal.set(0)
            self.criterioD_contratacao_planta_espacial.set(0)
            self.criterioD_contratacao_planta_adicionalidade.set(0)
            self.criterioE_intensidade_carbono.set(0)
            self.criterioE_part_minima.set(0)
            self.criterioE_contratacao_planta_temporal.set(0)
            self.criterioE_contratacao_planta_espacial.set(0)
            self.criterioE_contratacao_planta_adicionalidade.set(0)
            self.criterioF_intensidade_carbono.set(0)
            self.criterioF_part_minima.set(0)
            self.criterioF_contratacao_planta_temporal.set(0)
            self.criterioF_contratacao_planta_espacial.set(0)
            self.criterioF_contratacao_planta_adicionalidade.set(0)
        defaultCriterios()

        ## Máscaras ##
        #
        def maskEnergiaFornecida(event):
            part_minima = self.part_minima.get()
            part_minima_mask = masks.mask_decimal(part_minima)
            self.part_minima.delete(0, tk.END)
            self.part_minima.insert(0, part_minima_mask)

        def maskCertificacao(event):
            #Troca quando ativa Máscara
            self.op_certfic_var.set("Outro")
            limite_intensidade = self.limite_intensidade.get()
            limite_intensidade_mask = masks.mask_decimal(limite_intensidade)
            self.limite_intensidade.delete(0, tk.END)
            self.limite_intensidade.insert(0, limite_intensidade_mask)

            limite_particiapacao = self.limite_particiapacao.get()
            limite_particiapacao_mask = masks.mask_decimal(limite_particiapacao)
            self.limite_particiapacao.delete(0, tk.END)
            self.limite_particiapacao.insert(0, limite_particiapacao_mask)

            limite_adicionalidade = self.limite_adicionalidade.get()
            limite_adicionalidade_mask = masks.mask_decimal(limite_adicionalidade)
            self.limite_adicionalidade.delete(0, tk.END)
            self.limite_adicionalidade.insert(0, limite_adicionalidade_mask)

            limite_emissoes_cadeira_producao = self.limite_emissoes_cadeira_producao.get()
            limite_emissoes_cadeira_producao_mask = masks.mask_decimal(limite_emissoes_cadeira_producao)
            self.limite_emissoes_cadeira_producao.delete(0, tk.END)
            self.limite_emissoes_cadeira_producao.insert(0, limite_emissoes_cadeira_producao_mask)

            imaterialidade = self.imaterialidade.get()
            imaterialidade_mask = masks.mask_decimal(imaterialidade)
            self.imaterialidade.delete(0, tk.END)
            self.imaterialidade.insert(0, imaterialidade_mask)

            periodo_validade_aprovacao = self.periodo_validade_aprovacao.get()
            periodo_validade_aprovacao_mask = masks.mask_numeral(periodo_validade_aprovacao)
            self.periodo_validade_aprovacao.delete(0, tk.END)
            self.periodo_validade_aprovacao.insert(0, periodo_validade_aprovacao_mask)

            padrao_pressao_hidrogenio = self.padrao_pressao_hidrogenio.get()
            padrao_pressao_hidrogenio_mask = masks.mask_decimal(padrao_pressao_hidrogenio)
            self.padrao_pressao_hidrogenio.delete(0, tk.END)
            self.padrao_pressao_hidrogenio.insert(0, padrao_pressao_hidrogenio_mask)

        defaultCertificacao()

