#etapa5.py
import tkinter as tk
from tkinter import ttk
import masks  

def criar_etapa5(self,conteudo):
        ttk.Label(conteudo, text="1. Dados econômicos:", font=self.fonteB).grid(row=1, column=0, pady=20, sticky="w")
        botao_restaurar = ttk.Button(conteudo, text="Restaurar", command= lambda: defaultDadosEconomicos())
        botao_restaurar.grid(row=1, column=3, pady=20)
        
        ttk.Label(conteudo, text="     Horizonte de projeto (anos):").grid(row=2, column=0, sticky="w")
        self.horizonteprojeto = ttk.Entry(conteudo)
        self.horizonteprojeto.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.horizonteprojeto.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Participação do capital próprio (%):").grid(row=3, column=0, sticky="w")
        self.partcaptaproprio = ttk.Entry(conteudo)
        self.partcaptaproprio.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.partcaptaproprio.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Custo do capital próprio:").grid(row=4, column=0, sticky="w")
        self.custocapitalproprio = ttk.Entry(conteudo)
        self.custocapitalproprio.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.custocapitalproprio.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Tipo de amortização:").grid(row=5, column=0, sticky="w")
        opcoes_tipoamortizacao = ["SAC", "Price", "Não Reembolsável"]
        self.tipoamortizacao_var = tk.StringVar(conteudo)
        self.tipoamortizacao_var.set(opcoes_tipoamortizacao[0])  # Define a opção padrão
        tipoamortizacao_menu = ttk.Combobox(conteudo, textvariable=self.tipoamortizacao_var, values=opcoes_tipoamortizacao, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_tipoamortizacao)), '%P'))
        tipoamortizacao_menu.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(conteudo, text="     Período de financiamento (anos):").grid(row=6, column=0, sticky="w")
        self.periodofuncionamento = ttk.Entry(conteudo)
        self.periodofuncionamento.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        self.periodofuncionamento.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Taxa de juros real do financiamento (%):").grid(row=7, column=0, sticky="w")
        self.txjurosreal = ttk.Entry(conteudo)
        self.txjurosreal.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        self.txjurosreal.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Período de carência (anos):").grid(row=8, column=0, sticky="w")
        self.periodocarencia = ttk.Entry(conteudo)
        self.periodocarencia.grid(row=8, column=1, padx=10, pady=5, sticky="w")
        self.periodocarencia.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Custos administrativos do projeto ($/ano):").grid(row=9, column=0, sticky="w")
        self.custosprojeto = ttk.Entry(conteudo)
        self.custosprojeto.grid(row=9, column=1, padx=10, pady=5, sticky="w")
        self.custosprojeto.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     PIS/Confins (%):").grid(row=10, column=0, sticky="w")
        self.pisconfins = ttk.Entry(conteudo)
        self.pisconfins.grid(row=10, column=1, padx=10, pady=5, sticky="w")
        self.pisconfins.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     ICMS (%):").grid(row=11, column=0, sticky="w")
        self.icms = ttk.Entry(conteudo)
        self.icms.grid(row=11, column=1, padx=10, pady=5, sticky="w")
        self.icms.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Imposto de Renda e Contribuição Social (%):").grid(row=12, column=0, sticky="w")
        self.impostorenda = ttk.Entry(conteudo)
        self.impostorenda.grid(row=12, column=1, padx=10, pady=5, sticky="w")
        self.impostorenda.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="2. Oxigênio:", font=self.fonteB).grid(row=13, column=0, pady=20, sticky="w")
        botao_restaurar = ttk.Button(conteudo, text="Restaurar", command= lambda: defaultOxigenio())
        botao_restaurar.grid(row=13, column=3, pady=20)

        ttk.Label(conteudo, text="     Considerar venda de oxigênio:").grid(row=14, column=0, sticky="w")
        opcoes_vendaoxigenio = ["Sim", "Não"]
        self.vendaoxigenio_var = tk.StringVar(conteudo)
        self.vendaoxigenio_var.set(opcoes_vendaoxigenio[0])  # Define a opção padrão
        vendaoxigenio_menu = ttk.Combobox(conteudo, textvariable=self.vendaoxigenio_var, values=opcoes_vendaoxigenio, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_vendaoxigenio)), '%P'))
        ## Adicionei aqui
        vendaoxigenio_menu.bind("<<ComboboxSelected>>", lambda event: habilitar_oxigenio(event))
        ## ate aqui
        vendaoxigenio_menu.grid(row=14, column=1, padx=10, pady=5, sticky="w") 

        ttk.Label(conteudo, text="     Taxa de produção de oxigênio (kg de O₂ /kg de H₂):").grid(row=15, column=0, sticky="w")
        self.taxaprodoxigenio = ttk.Entry(conteudo)
        self.taxaprodoxigenio.grid(row=15, column=1, padx=10, pady=5, sticky="w") 
        self.taxaprodoxigenio.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Preço de venda de oxigênio ($/kg de O₂):").grid(row=16, column=0, sticky="w")
        self.precovendaoxigenio = ttk.Entry(conteudo)
        self.precovendaoxigenio.grid(row=16, column=1, padx=10, pady=5, sticky="w")
        self.precovendaoxigenio.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Taxa de aumento real anual do preço de venda do oxigênio (%):").grid(row=17, column=0, sticky="w")
        self.taxaaumentooxigenio = ttk.Entry(conteudo)
        self.taxaaumentooxigenio.grid(row=17, column=1, padx=10, pady=5, sticky="w")
        self.taxaaumentooxigenio.bind("<KeyRelease>", lambda event: maskParametros(event)) 

        ttk.Label(conteudo, text="3. Uso da Água:", font=self.fonteB).grid(row=18, column=0, pady=20, sticky="w")
        botao_restaurar = ttk.Button(conteudo, text="Restaurar", command= lambda: defaultUsoAgua())
        botao_restaurar.grid(row=18, column=3, pady=20)

        ttk.Label(conteudo, text="     Demanda de água para o eletrolisador (ultrapura) (kg/kgH₂):").grid(row=19, column=0, sticky="w")
        self.demandaagua = ttk.Entry(conteudo)
        self.demandaagua.grid(row=19, column=1, padx=10, pady=5, sticky="w") 
        self.demandaagua.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Demanda de água de processo para o eletrolisador (kg/kgH₂):").grid(row=20, column=0, sticky="w")
        self.demandaaguaeletro = ttk.Entry(conteudo)
        self.demandaaguaeletro.grid(row=20, column=1, padx=10, pady=5, sticky="w")
        self.demandaaguaeletro.bind("<KeyRelease>", lambda event: maskParametros(event))    

        ttk.Label(conteudo, text="     Preço da água pura ($/kg de água):").grid(row=21, column=0, sticky="w")
        self.precoaguapura = ttk.Entry(conteudo)
        self.precoaguapura.grid(row=21, column=1, padx=10, pady=5, sticky="w")
        self.precoaguapura.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Preço da água de processo ($/kg de água):").grid(row=22, column=0, sticky="w")
        self.precoaguaproc = ttk.Entry(conteudo)
        self.precoaguaproc.grid(row=22, column=1, padx=10, pady=5, sticky="w")
        self.precoaguaproc.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Preço de transporte da água, para levar água dessalinizada até a usina ($/(kgH₂*100 km)):").grid(row=23, column=0, sticky="w")
        self.precotranspagua = ttk.Entry(conteudo)
        self.precotranspagua.grid(row=23, column=1, padx=10, pady=5, sticky="w")
        self.precotranspagua.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Distância entre o eletrolisador e a fonte de água (km):").grid(row=24, column=0, sticky="w")
        self.disteletrolisadorfonte = ttk.Entry(conteudo)
        self.disteletrolisadorfonte.grid(row=24, column=1, padx=10, pady=5, sticky="w")
        self.disteletrolisadorfonte.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Taxa de aumento anual dos custos relativos ao consumo de água (%):").grid(row=25, column=0, sticky="w")
        self.taxaaumentoanual = ttk.Entry(conteudo)
        self.taxaaumentoanual.grid(row=25, column=1, padx=10, pady=5, sticky="w")
        self.taxaaumentoanual.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="4. Mercado de carbono:", font=self.fonteB).grid(row=26, column=0, pady=20, sticky="w")
        botao_restaurar = ttk.Button(conteudo, text="Restaurar", command= lambda: defaultMercadoCarbono())
        botao_restaurar.grid(row=26, column=3, pady=20)

        ttk.Label(conteudo, text="     Precificação do carbono ($/gCO₂ eq):").grid(row=27, column=0, sticky="w")
        self.precificacaocarbono = ttk.Entry(conteudo)
        self.precificacaocarbono.grid(row=27, column=1, padx=10, pady=5, sticky="w")
        self.precificacaocarbono.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Aumento anual do preço do carbono (%):").grid(row=28, column=0, sticky="w")
        self.aumentoprecocarbono = ttk.Entry(conteudo)
        self.aumentoprecocarbono.grid(row=28, column=1, padx=10, pady=5, sticky="w")
        self.aumentoprecocarbono.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Valor de referência para emissões da produção por reforma a vapor (gCO₂e/MJ.de H₂):").grid(row=29, column=0, sticky="w")
        self.valoremissoesprod = ttk.Entry(conteudo)
        self.valoremissoesprod.grid(row=29, column=1, padx=10, pady=5, sticky="w")
        self.valoremissoesprod.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="5. Sistema de transmissão:", font=self.fonteB).grid(row=30, column=0, pady=20, sticky="w")
        botao_restaurar = ttk.Button(conteudo, text="Restaurar", command= lambda: defaultTransmissao())
        botao_restaurar.grid(row=30, column=3, pady=20)

        ttk.Label(conteudo, text="     Preço de aquisição da energia da rede ($/kWh):").grid(row=31, column=0, sticky="w")
        self.precoaquisicaoenergia = ttk.Entry(conteudo)
        self.precoaquisicaoenergia.grid(row=31, column=1, padx=10, pady=5, sticky="w")
        self.precoaquisicaoenergia.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Informar se há possibilidade de venda de excedente de energia para a rede:").grid(row=32, column=0, sticky="w")
        opcoes_possibilidadevendaexcedente = ["Sim", "Não"]
        self.possibilidadevendaexcedente_var = tk.StringVar(conteudo)
        self.possibilidadevendaexcedente_var.set(opcoes_possibilidadevendaexcedente[1])  # Define a opção padrão
        possibilidadevendaexcedente_menu = ttk.Combobox(conteudo, textvariable=self.possibilidadevendaexcedente_var, values=opcoes_possibilidadevendaexcedente, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_possibilidadevendaexcedente)), '%P'))
        ##Alterei aqui
        possibilidadevendaexcedente_menu.bind("<<ComboboxSelected>>", lambda event: habilitar_vendaenergia(event))
        #ate aqui
        possibilidadevendaexcedente_menu.grid(row=32, column=1, padx=10, pady=5, sticky="w") 

        ttk.Label(conteudo, text="     Informar preço de venda de excedente de energia para rede ($/kWh):").grid(row=33, column=0, sticky="w")
        self.precovendaenergia = ttk.Entry(conteudo)
        self.precovendaenergia.grid(row=33, column=1, padx=10, pady=5, sticky="w")
        self.precovendaenergia.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Informar custo relativo à construção de novas linhas de transmissão exclusivas para o projeto ($):").grid(row=34, column=0, sticky="w")
        self.custorelativonovaslinhas = ttk.Entry(conteudo)
        self.custorelativonovaslinhas.grid(row=34, column=1, padx=10, pady=5, sticky="w")
        self.custorelativonovaslinhas.bind("<KeyRelease>", lambda event: maskParametros(event))

        ttk.Label(conteudo, text="     Informar fator de emissão da rede (gCO₂ eq/MJ):").grid(row=35, column=0, sticky="w")
        self.fator_emissao_var = tk.StringVar()
        botao_upload = tk.Button(conteudo, text="Upload", command=lambda var=self.fator_emissao_var: self.fazer_upload(var))
        botao_upload.grid(row=35, column=3, pady=10)
        tk.Label(conteudo, wraplength=120, textvariable=self.fator_emissao_var, text="").grid(row=35, column=1)
        
        ttk.Label(conteudo, text="     Informar projeção esperada da participação de renováveis da rede (%):").grid(row=36, column=0, sticky="w")
        self.proj_esperada_var = tk.StringVar()
        botao_upload = tk.Button(conteudo, text="Upload", command=lambda var=self.proj_esperada_var: self.fazer_upload(var))
        botao_upload.grid(row=36, column=3)
        tk.Label(conteudo, wraplength=120, textvariable=self.proj_esperada_var, text="").grid(row=36, column=1)


        ## Valores Default ##
        #         
        def defaultDadosEconomicos():
            self.capex_bateria.delete(0, tk.END)
            self.capex_bateria.insert(0, "150")
            self.horizonteprojeto.delete(0, tk.END)
            self.horizonteprojeto.insert(0, "20")
            self.partcaptaproprio.delete(0, tk.END)
            self.partcaptaproprio.insert(0, "0")
            self.custocapitalproprio.delete(0, tk.END)
            self.custocapitalproprio.insert(0, "0")
            self.tipoamortizacao_var.set("SAC")
            self.periodofuncionamento.delete(0, tk.END)
            self.periodofuncionamento.insert(0, "0")
            self.txjurosreal.delete(0, tk.END)
            self.txjurosreal.insert(0, "0")
            self.periodocarencia.delete(0, tk.END)
            self.periodocarencia.insert(0, "0")
            self.custosprojeto.delete(0, tk.END)
            self.custosprojeto.insert(0, "1000000")
            self.pisconfins.delete(0, tk.END)
            self.pisconfins.insert(0, "2.90")
            self.icms.delete(0, tk.END)
            self.icms.insert(0, "18.00")
            self.impostorenda.delete(0, tk.END)
            self.impostorenda.insert(0, "3.08")

        def defaultOxigenio():
            self.vendaoxigenio_var.set("Sim")
            ##Adicionei aqui
            self.taxaprodoxigenio.config(state='normal')
            self.precovendaoxigenio.config(state='normal')
            self.taxaaumentooxigenio.config(state='normal')
            #ate aqui
            self.taxaprodoxigenio.delete(0, tk.END)
            self.taxaprodoxigenio.insert(0, "8")
            self.precovendaoxigenio.delete(0, tk.END)
            self.precovendaoxigenio.insert(0, "3")
            self.taxaaumentooxigenio.delete(0, tk.END)
            self.taxaaumentooxigenio.insert(0, "0")

        def defaultUsoAgua():    
            self.demandaagua.delete(0, tk.END)
            self.demandaagua.insert(0, "9")
            self.demandaaguaeletro.delete(0, tk.END)
            self.demandaaguaeletro.insert(0, "18")
            self.precoaguapura.delete(0, tk.END)
            self.precoaguapura.insert(0, "0.00121")
            self.precoaguaproc.delete(0, tk.END)
            self.precoaguaproc.insert(0, "0.00116")
            self.precotranspagua.delete(0, tk.END)
            self.precotranspagua.insert(0, "0.06")
            self.disteletrolisadorfonte.delete(0, tk.END)
            self.disteletrolisadorfonte.insert(0, "0")
            self.taxaaumentoanual.delete(0, tk.END)
            self.taxaaumentoanual.insert(0, "0")

        def defaultMercadoCarbono():
            self.precificacaocarbono.delete(0, tk.END)
            self.precificacaocarbono.insert(0, "0")
            self.aumentoprecocarbono.delete(0, tk.END)
            self.aumentoprecocarbono.insert(0, "0")
            self.valoremissoesprod.delete(0, tk.END)
            self.valoremissoesprod.insert(0, "94")

        def defaultTransmissao():
            self.precoaquisicaoenergia.delete(0, tk.END)
            self.precoaquisicaoenergia.insert(0, "0")
            self.possibilidadevendaexcedente_var.set("Não")
            self.precovendaenergia.delete(0, tk.END)
            self.precovendaenergia.insert(0, "0")
            self.precovendaenergia.config(state='disabled')
            self.custorelativonovaslinhas.delete(0, tk.END)
            self.custorelativonovaslinhas.insert(0, "0")
            self.fator_emissao_var.set("")
            self.proj_esperada_var.set("")

        defaultDadosEconomicos()
        defaultOxigenio()
        defaultUsoAgua()
        defaultTransmissao()
        defaultMercadoCarbono()

        #adi aqui
        def habilitar_oxigenio(event):
            opcao_selecionada = self.vendaoxigenio_var.get()
            if opcao_selecionada == "Não":
                self.taxaprodoxigenio.delete(0, tk.END)
                self.taxaprodoxigenio.config(state='disabled')
                self.precovendaoxigenio.delete(0, tk.END)
                self.precovendaoxigenio.config(state='disabled')
                self.taxaaumentooxigenio.delete(0, tk.END)
                self.taxaaumentooxigenio.config(state='disabled')
            else:
                self.taxaprodoxigenio.config(state='normal')
                self.precovendaoxigenio.config(state='normal')
                self.taxaaumentooxigenio.config(state='normal')
                defaultOxigenio()

        def habilitar_vendaenergia(event):
            opcao_selecionada = self.possibilidadevendaexcedente_var.get()
            if opcao_selecionada == "Não":
                self.precovendaenergia.delete(0, tk.END)
                self.precovendaenergia.insert(0, "0")
                self.precovendaenergia.config(state='disabled')
            else:
                self.precovendaenergia.config(state='normal')
                self.precovendaenergia.delete(0, tk.END)
                self.precovendaenergia.insert(0, "0")
        #ate aqui


        ## Máscaras ##
        #
        def maskParametros(event):
            horizonteprojeto = self.horizonteprojeto.get()
            horizonteprojeto_mask = masks.mask_decimal(horizonteprojeto)
            self.horizonteprojeto.delete(0, tk.END)
            self.horizonteprojeto.insert(0, horizonteprojeto_mask)

            partcaptaproprio = self.partcaptaproprio.get()
            partcaptaproprio_mask = masks.mask_decimal(partcaptaproprio)
            self.partcaptaproprio.delete(0, tk.END)
            self.partcaptaproprio.insert(0, partcaptaproprio_mask)

            self.custocapitalproprio
            custocapitalproprio = self.custocapitalproprio.get()
            custocapitalproprio_mask = masks.mask_decimal(custocapitalproprio)
            self.custocapitalproprio.delete(0, tk.END)
            self.custocapitalproprio.insert(0, custocapitalproprio_mask)

            periodofuncionamento = self.periodofuncionamento.get()
            periodofuncionamento_mask = masks.mask_decimal(periodofuncionamento)
            self.periodofuncionamento.delete(0, tk.END)
            self.periodofuncionamento.insert(0, periodofuncionamento_mask)

            txjurosreal = self.txjurosreal.get()
            txjurosreal_mask = masks.mask_decimal(txjurosreal)
            self.txjurosreal.delete(0, tk.END)
            self.txjurosreal.insert(0, txjurosreal_mask)

            periodocarencia = self.periodocarencia.get()
            periodocarencia_mask = masks.mask_decimal(periodocarencia)
            self.periodocarencia.delete(0, tk.END)
            self.periodocarencia.insert(0, periodocarencia_mask)

            custosprojeto = self.custosprojeto.get()
            custosprojeto_mask = masks.mask_decimal(custosprojeto)
            self.custosprojeto.delete(0, tk.END)
            self.custosprojeto.insert(0, custosprojeto_mask)

            pisconfins = self.pisconfins.get()
            pisconfins_mask = masks.mask_decimal(pisconfins)
            self.pisconfins.delete(0, tk.END)
            self.pisconfins.insert(0, pisconfins_mask)

            icms = self.icms.get()
            icms_mask = masks.mask_decimal(icms)
            self.icms.delete(0, tk.END)
            self.icms.insert(0, icms_mask)
            
            impostorenda = self.impostorenda.get()
            impostorenda_mask = masks.mask_decimal(impostorenda)
            self.impostorenda.delete(0, tk.END)
            self.impostorenda.insert(0, impostorenda_mask)

            taxaprodoxigenio = self.taxaprodoxigenio.get()
            taxaprodoxigenio_mask = masks.mask_decimal(taxaprodoxigenio)
            self.taxaprodoxigenio.delete(0, tk.END)
            self.taxaprodoxigenio.insert(0, taxaprodoxigenio_mask)

            precovendaoxigenio = self.precovendaoxigenio.get()
            precovendaoxigenio_mask = masks.mask_decimal(precovendaoxigenio)
            self.precovendaoxigenio.delete(0, tk.END)
            self.precovendaoxigenio.insert(0, precovendaoxigenio_mask)

            taxaaumentooxigenio = self.taxaaumentooxigenio.get()
            taxaaumentooxigenio_mask = masks.mask_decimal(taxaaumentooxigenio)
            self.taxaaumentooxigenio.delete(0, tk.END)
            self.taxaaumentooxigenio.insert(0, taxaaumentooxigenio_mask)

            demandaagua = self.demandaagua.get()
            demandaagua_mask = masks.mask_decimal(demandaagua)
            self.demandaagua.delete(0, tk.END)
            self.demandaagua.insert(0, demandaagua_mask)

            demandaaguaeletro = self.demandaaguaeletro.get()
            demandaaguaeletro_mask = masks.mask_decimal(demandaaguaeletro)
            self.demandaaguaeletro.delete(0, tk.END)
            self.demandaaguaeletro.insert(0, demandaaguaeletro_mask)

            precoaguapura = self.precoaguapura.get()
            precoaguapura_mask = masks.mask_decimal(precoaguapura)
            self.precoaguapura.delete(0, tk.END)
            self.precoaguapura.insert(0, precoaguapura_mask)

            precoaguaproc = self.precoaguaproc.get()
            precoaguaproc_mask = masks.mask_decimal(precoaguaproc)
            self.precoaguaproc.delete(0, tk.END)
            self.precoaguaproc.insert(0, precoaguaproc_mask)

            precotranspagua = self.precotranspagua.get()
            precotranspagua_mask = masks.mask_decimal(precotranspagua)
            self.precotranspagua.delete(0, tk.END)
            self.precotranspagua.insert(0, precotranspagua_mask)

            disteletrolisadorfonte = self.disteletrolisadorfonte.get()
            disteletrolisadorfonte_mask = masks.mask_decimal(disteletrolisadorfonte)
            self.disteletrolisadorfonte.delete(0, tk.END)
            self.disteletrolisadorfonte.insert(0, disteletrolisadorfonte_mask)

            taxaaumentoanual = self.taxaaumentoanual.get()
            taxaaumentoanual_mask = masks.mask_decimal(taxaaumentoanual)
            self.taxaaumentoanual.delete(0, tk.END)
            self.taxaaumentoanual.insert(0, taxaaumentoanual_mask)

            precificacaocarbono = self.precificacaocarbono.get()
            precificacaocarbono_mask = masks.mask_decimal(precificacaocarbono)
            self.precificacaocarbono.delete(0, tk.END)
            self.precificacaocarbono.insert(0, precificacaocarbono_mask)

            aumentoprecocarbono = self.aumentoprecocarbono.get()
            aumentoprecocarbono_mask = masks.mask_decimal(aumentoprecocarbono)
            self.aumentoprecocarbono.delete(0, tk.END)
            self.aumentoprecocarbono.insert(0, aumentoprecocarbono_mask)

            valoremissoesprod = self.valoremissoesprod.get()
            valoremissoesprod_mask = masks.mask_decimal(valoremissoesprod)
            self.valoremissoesprod.delete(0, tk.END)
            self.valoremissoesprod.insert(0, valoremissoesprod_mask)

            precoaquisicaoenergia = self.precoaquisicaoenergia.get()
            precoaquisicaoenergia_mask = masks.mask_decimal(precoaquisicaoenergia)
            self.precoaquisicaoenergia.delete(0, tk.END)
            self.precoaquisicaoenergia.insert(0, precoaquisicaoenergia_mask)

            precovendaenergia = self.precovendaenergia.get()
            precovendaenergia_mask = masks.mask_decimal(precovendaenergia)
            self.precovendaenergia.delete(0, tk.END)
            self.precovendaenergia.insert(0, precovendaenergia_mask)

            custorelativonovaslinhas = self.custorelativonovaslinhas.get()
            custorelativonovaslinhas_mask = masks.mask_decimal(custorelativonovaslinhas)
            self.custorelativonovaslinhas.delete(0, tk.END)
            self.custorelativonovaslinhas.insert(0, custorelativonovaslinhas_mask)