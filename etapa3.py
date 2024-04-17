#etapa3.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import masks
from validations import validate_latitude, validate_longitude, CoordenadasInvalidasError
import folium
import webbrowser    

def criar_etapa3(self,conteudo,etapa3):

        botao_restaurar = ttk.Button(etapa3, text="Restaurar", command= lambda: defaultEnergia())
        botao_restaurar.grid(row=0, column=1, pady=20)
        
        label_var = []
        self.nome_usina_entries = []

        # Adicione a primeira linha com títulos
        titulos = ["Seleção de usinas para a simulação", "Nome da usina", "Fonte de energia", "Latitude", "Longitude", " ", "Potência [MW]", "Capacidade do reservatório em caso de PCH [h]", "Aumentar fator de capacidade da geração eólica", "IP: Taxa de paradas programadas [%]", "IP: Taxa de paradas não programadas [%]", "Taxa de risco de curtailment [%]", "Taxa de degradação [%/ano]", "Taxa de depreciação contábil", "CAPEX [$]", "OPEX [$/kW*Ano]", "Pagamento de TUSTg [$/kWh]", "Geração no mesmo local do consumo", "Idade da usina [anos]", "Previsão da geração [kWh/h]", "Caminho do Arquivo           ", "Estimar LCOE da usina ou deseja inserir projeção de preço/custo da usina?", "Custo/Preço de Energia [$/kWh]", "Caminho do Arquivo           "]
        label_var.append([tk.StringVar() for _ in range(24)])

        for coluna in range(24):
            label_var[0][coluna].set(titulos[coluna])
            tk.Label(conteudo, justify="left",wraplength=120,textvariable=label_var[0][coluna]).grid(row=0, column=coluna+1, padx=10, pady=5)
    
        self.nome_usina_entries = []
        self.selecionar_entries = []
        self.fonte_energia_entries = []
        self.lat_entries = []
        self.long_entries = []
        self.potencia_entries = []
        self.capacidade_reservatorio_entries = []
        self.aumentar_fator_entries = []
        self.ip_paradas_prog_entries = []
        self.ip_paradas_nao_prog_entries = []
        self.tx_risco_curtailment_entries = []
        self.tx_degradacao_entries = []
        self.tx_depreciacao_contabil_entries = []
        self.capex_fontes_entries = []
        self.opex_fontes_entries = []
        self.pagamento_tustg_entries = []
        self.geracao_local_entries = []
        self.idade_usina_entries = []
        self.proj_preco_custo_entries = []
        self.prev_geracao_entries = []
        self.custo_preco_energia_entries = []
        for i in range(20):
            selecionar_var = tk.StringVar()
            tk.Checkbutton(conteudo, justify="left", text="Selecionar", variable=selecionar_var).grid(row=i+1, column=1, padx=10, pady=5, sticky="w")
            self.selecionar_entries.append(selecionar_var)
            
            nome_usina = tk.StringVar()
            self.entry_nome_usina = ttk.Entry(conteudo, textvariable=nome_usina).grid(row=i+1, column=2, padx=10, pady=5, sticky="w")
            self.nome_usina_entries.append(nome_usina)
            
            #aqui estava fontes energia

            lat_var = tk.StringVar()
            lat_entry = ttk.Entry(conteudo, textvariable=lat_var)
            lat_entry.grid(row=i+1, column=4, padx=10, sticky="w")
            self.lat_entries.append(lat_var)
            lat_entry.bind("<KeyRelease>", lambda event, entry=lat_entry, var=lat_var: masklat(event, entry, var))
            
            long_var = tk.StringVar()
            long_entry = ttk.Entry(conteudo, textvariable=long_var)
            long_entry.grid(row=i+1, column=5, padx=10, sticky="w")
            self.long_entries.append(long_var)
            long_entry.bind("<KeyRelease>", lambda event, entry=long_entry, var=long_var: masklat(event, entry, var))
            
            #atualizar_abrir_botao = ttk.Button(conteudo, text="Atualizar e Abrir Mapa", command=self.atualizar_e_abrir_mapa)
            atualizar_abrir_botao = ttk.Button(conteudo, text="Atualizar e Abrir Mapa", command=lambda i=i: atualizar_e_abrir_mapa(i))
            atualizar_abrir_botao.grid(row=i+1, column=6)

            potencia_var = tk.StringVar()
            potencia_entry = ttk.Entry(conteudo, textvariable=potencia_var)
            potencia_entry.grid(row=i+1, column=7, padx=10, pady=5, sticky="w")
            self.potencia_entries.append(potencia_var)
            potencia_entry.bind("<KeyRelease>", lambda event, entry=potencia_entry, var=potencia_entry: maskDec(event, entry, var))

            capacidade_reservatorio_var = tk.StringVar()
            #alterei aqui
            capacidade_reservatorio_entry = ttk.Entry(conteudo, textvariable=capacidade_reservatorio_var, state='disabled')
            #fim
            capacidade_reservatorio_entry.grid(row=i+1, column=8, padx=10, pady=5, sticky="w")
            self.capacidade_reservatorio_entries.append(capacidade_reservatorio_var)
            capacidade_reservatorio_entry.bind("<KeyRelease>", lambda event, entry=capacidade_reservatorio_entry, var=capacidade_reservatorio_entry: maskDec(event, entry, var))

            #alterei aqui, estava acima, passei para baixo e add algumas linhas
            fonte_energia_var = tk.StringVar()
            opcoes_fonte_energia = ["Eólica", "FV", "PCH"]
            self.menu_fonte_energia = ttk.Combobox(conteudo, textvariable=fonte_energia_var, values=opcoes_fonte_energia, validate="all", validatecommand=(conteudo.register(lambda P: self.validar_combobox_input(P, opcoes_fonte_energia)), '%P'))
            self.menu_fonte_energia.grid(row=i+1, column=3, padx=10, pady=5, sticky="w")
            self.menu_fonte_energia.bind("<<ComboboxSelected>>", lambda event, entry=capacidade_reservatorio_entry, var=fonte_energia_var: habilitar_pch(event, entry, var))
            self.fonte_energia_entries.append(fonte_energia_var)
            #fim

            aumentar_fator_var = tk.StringVar()
            tk.Checkbutton(conteudo, justify="left", text="Sim", variable=aumentar_fator_var).grid(row=i+1, column=9, padx=10, pady=5, sticky="w")
            self.aumentar_fator_entries.append(aumentar_fator_var)

            ip_paradas_prog_var = tk.StringVar()
            ip_paradas_prog_entry = ttk.Entry(conteudo, textvariable=ip_paradas_prog_var)
            ip_paradas_prog_entry.grid(row=i+1, column=10, padx=10, pady=5, sticky="w")
            self.ip_paradas_prog_entries.append(ip_paradas_prog_var)
            ip_paradas_prog_entry.bind("<KeyRelease>", lambda event, entry=ip_paradas_prog_entry, var=ip_paradas_prog_entry: maskDec(event, entry, var))

            ip_paradas_nao_prog_var = tk.StringVar()
            ip_paradas_nao_prog_entry = ttk.Entry(conteudo, textvariable=ip_paradas_nao_prog_var)
            ip_paradas_nao_prog_entry.grid(row=i+1, column=11, padx=10, pady=5, sticky="w")
            self.ip_paradas_nao_prog_entries.append(ip_paradas_nao_prog_var)
            ip_paradas_nao_prog_entry.bind("<KeyRelease>", lambda event, entry=ip_paradas_nao_prog_entry, var=ip_paradas_nao_prog_entry: maskDec(event, entry, var))
            
            tx_risco_curtailment_var = tk.StringVar()
            tx_risco_curtailment_entry = ttk.Entry(conteudo, textvariable=tx_risco_curtailment_var)
            tx_risco_curtailment_entry.grid(row=i+1, column=12, padx=10, pady=5, sticky="w")
            self.tx_risco_curtailment_entries.append(tx_risco_curtailment_var)
            tx_risco_curtailment_entry.bind("<KeyRelease>", lambda event, entry=tx_risco_curtailment_entry, var=tx_risco_curtailment_entry: maskDec(event, entry, var))
            
            tx_degradacao_var = tk.StringVar()
            tx_degradacao_entry = ttk.Entry(conteudo, textvariable=tx_degradacao_var)
            tx_degradacao_entry.grid(row=i+1, column=13, padx=10, pady=5, sticky="w")
            self.tx_degradacao_entries.append(tx_degradacao_var)
            tx_degradacao_entry.bind("<KeyRelease>", lambda event, entry=tx_degradacao_entry, var=tx_degradacao_entry: maskDec(event, entry, var))
            
            tx_depreciacao_contabil_var = tk.StringVar()
            tx_depreciacao_contabil_entry = ttk.Entry(conteudo, textvariable=tx_depreciacao_contabil_var)
            tx_depreciacao_contabil_entry.grid(row=i+1, column=14, padx=10, pady=5, sticky="w")
            self.tx_depreciacao_contabil_entries.append(tx_depreciacao_contabil_var)
            tx_depreciacao_contabil_entry.bind("<KeyRelease>", lambda event, entry=tx_depreciacao_contabil_entry, var=tx_depreciacao_contabil_entry: maskDec(event, entry, var))
            
            capex_fontes_var = tk.StringVar()
            capex_fontes_entry = ttk.Entry(conteudo, textvariable=capex_fontes_var)
            capex_fontes_entry.grid(row=i+1, column=15, padx=10, pady=5, sticky="w")
            self.capex_fontes_entries.append(capex_fontes_var)
            capex_fontes_entry.bind("<KeyRelease>", lambda event, entry=capex_fontes_entry, var=capex_fontes_entry: maskDec(event, entry, var))

            opex_fontes_var = tk.StringVar()
            opex_fontes_entry = ttk.Entry(conteudo, textvariable=opex_fontes_var)
            opex_fontes_entry.grid(row=i+1, column=16, padx=10, pady=5, sticky="w")
            self.opex_fontes_entries.append(opex_fontes_var)
            opex_fontes_entry.bind("<KeyRelease>", lambda event, entry=opex_fontes_entry, var=opex_fontes_entry: maskDec(event, entry, var))
            
            pagamento_tustg_var = tk.StringVar()
            pagamento_tustg_entry = ttk.Entry(conteudo, textvariable=pagamento_tustg_var)
            pagamento_tustg_entry.grid(row=i+1, column=17, padx=10, pady=5, sticky="w")
            self.pagamento_tustg_entries.append(pagamento_tustg_var)
            pagamento_tustg_entry.bind("<KeyRelease>", lambda event, entry=pagamento_tustg_entry, var=pagamento_tustg_entry: maskDec(event, entry, var))

            geracao_local_var = tk.StringVar()
            tk.Checkbutton(conteudo, justify="left", text="Sim", variable=geracao_local_var).grid(row=i+1, column=18, padx=10, pady=5, sticky="w")
            self.geracao_local_entries.append(geracao_local_var)
            
            idade_usina_var = tk.StringVar()
            idade_usina_entry = ttk.Entry(conteudo, textvariable=idade_usina_var)
            idade_usina_entry.grid(row=i+1, column=19, padx=10, pady=5, sticky="w")
            self.idade_usina_entries.append(idade_usina_var)
            idade_usina_entry.bind("<KeyRelease>", lambda event, entry=idade_usina_entry, var=idade_usina_entry: maskDec(event, entry, var))
            
            prev_geracao_var = tk.StringVar()
            prev_geracao_button = tk.Button(conteudo, text="Upload", command=lambda var=prev_geracao_var: self.fazer_upload(var))
            prev_geracao_button.grid(row=i+1, column=20, padx=10, pady=5, sticky="w")
            self.prev_geracao_entries.append(prev_geracao_var)
            tk.Label(conteudo, wraplength=120, textvariable=prev_geracao_var, text="").grid(row=i+1, column=21, padx=10, pady=5)

            proj_preco_custo_var = tk.StringVar()
            proj_preco_custo_entry = ttk.Entry(conteudo, textvariable=proj_preco_custo_var)
            proj_preco_custo_entry.grid(row=i+1, column=22, padx=10, pady=5, sticky="w")
            self.proj_preco_custo_entries.append(proj_preco_custo_var)
            proj_preco_custo_entry.bind("<KeyRelease>", lambda event, entry=proj_preco_custo_entry, var=proj_preco_custo_entry: maskDec(event, entry, var))
            
            custo_preco_energia_var = tk.StringVar()
            custo_preco_energia_button = tk.Button(conteudo, text="Upload", command=lambda var=custo_preco_energia_var: self.fazer_upload(var))
            custo_preco_energia_button.grid(row=i+1, column=23, padx=10, pady=5, sticky="w")
            self.custo_preco_energia_entries.append(custo_preco_energia_var)
            tk.Label(conteudo, wraplength=120, textvariable=custo_preco_energia_var, text="").grid(row=i+1, column=24, padx=10, pady=5)


        ## Valores Default ##
        #  
        def defaultEnergia():
                for i in range(20):
                    self.selecionar_entries[i].set(0)
                    self.aumentar_fator_entries[i].set(0)
                    self.geracao_local_entries[i].set(0)
                    self.nome_usina_entries[i].set("")
                    self.fonte_energia_entries[i].set("")
                    self.lat_entries[i].set("")
                    self.long_entries[i].set("")
                    self.potencia_entries[i].set("")
                    self.capacidade_reservatorio_entries[i].set("")
                    self.aumentar_fator_entries[i].set(0)
                    self.ip_paradas_prog_entries[i].set("")
                    self.ip_paradas_nao_prog_entries[i].set("")
                    self.tx_risco_curtailment_entries[i].set("")
                    self.tx_degradacao_entries[i].set("")
                    self.tx_depreciacao_contabil_entries[i].set("")
                    self.capex_fontes_entries[i].set("")
                    self.opex_fontes_entries[i].set("")
                    self.pagamento_tustg_entries[i].set("")
                    self.idade_usina_entries[i].set("")
                    self.proj_preco_custo_entries[i].set("")
                self.nome_usina_entries[0].set("Teste")
                self.fonte_energia_entries[0].set("Eólica")
                self.lat_entries[0].set("-22.890451")
                self.long_entries[0].set("-43.188052")
                self.potencia_entries[0].set("0")
                self.capacidade_reservatorio_entries[0].set("0")
                self.aumentar_fator_entries[0].set(0)
                self.ip_paradas_prog_entries[0].set("2.5")
                self.ip_paradas_nao_prog_entries[0].set("2.5")
                self.tx_risco_curtailment_entries[0].set("0")
                self.tx_degradacao_entries[0].set("0")
                self.tx_depreciacao_contabil_entries[0].set("10")
                self.capex_fontes_entries[0].set("0")
                self.opex_fontes_entries[0].set("0")
                self.pagamento_tustg_entries[0].set("0")
                self.idade_usina_entries[0].set("0")
                self.proj_preco_custo_entries[0].set("0")
                self.geracao_local_entries[0].set(1)

        defaultEnergia()

        ##Adicionei aqui
        def habilitar_pch(event, entry, var):
            opcao_selecionada = var.get()
            if opcao_selecionada == "PCH":
                entry.config(state='normal')
            else:
                entry.delete(0, tk.END)
                entry.config(state='disabled')
        ##ate aqui

        ## Máscaras ##
        #
        def masklat(event, entry, var):
            lat = var.get()
            lat_mask = masks.mask_coordenadas(lat)
            entry.delete(0, tk.END)
            entry.insert(0, lat_mask)
    
        def maskDec(event, entry, var):
            c = var.get()
            c_mask = masks.mask_decimal(c)
            entry.delete(0, tk.END)
            entry.insert(0, c_mask)


        ## Mapa ##
        #
        def atualizar_e_abrir_mapa(i):
            try:
                latitude = float(self.lat_entries[i].get())
                longitude = float(self.long_entries[i].get())
                
                campo = "Erro em Especificação das Fontes"
                subcampo = "Campo Latitude"
                validate_latitude(latitude,subcampo)
                subcampo = "Campo Longitude"
                validate_longitude(longitude,subcampo)

                mapa = folium.Map(location=[latitude, longitude], zoom_start=6)

                folium.Marker([latitude, longitude], tooltip="Localização").add_to(mapa)
                mapa.save('mapa.html')
                webbrowser.open('mapa.html')
            except CoordenadasInvalidasError as e:
                messagebox.showerror(campo, str(e))
                pass
        