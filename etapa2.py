#etapa2.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import masks
from validations import validate_latitude, validate_longitude, CoordenadasInvalidasError
import folium
import webbrowser    

def criar_etapa2(self,conteudo):

        self.tecnologia_var = tk.StringVar()

        ttk.Label(conteudo, text="1. Demanda:", font=self.fonteB).grid(row=1, column=0, columnspan=5, pady=20, sticky="w")
        botao_restaurar = ttk.Button(conteudo, text="Restaurar", command= lambda: defaultDemanda())
        botao_restaurar.grid(row=1, column=3, pady=20)
        ##alterei aqui
        ttk.Label(conteudo, wraplength=320, text="Produção requerida de H₂ (kg):").grid(row=2, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.demandaH2 = ttk.Entry(conteudo)
        self.demandaH2.grid(row=2, column=3, padx=10, sticky="w")
        self.demandaH2.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Periodicidade da demanda (Horas):").grid(row=3, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.periodicidade_demanda = ttk.Entry(conteudo)
        self.periodicidade_demanda.grid(row=3, column=3, padx=10, sticky="w")
        self.periodicidade_demanda.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=240, text="Localizador do eletrolisador:").grid(row=4, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        ttk.Label(conteudo, text="- Latitude:").grid(row=5, column=1, sticky="w")
        ttk.Label(conteudo, text="- Longitude:").grid(row=6, column=1, sticky="w")

        self.latitude_entry = ttk.Entry(conteudo)
        self.latitude_entry.grid(row=5, column=3, padx=10, sticky="w")
        self.latitude_entry.bind("<KeyRelease>", lambda event: maskEspecificacao(event))
        self.longitude_entry = ttk.Entry(conteudo)
        self.longitude_entry.grid(row=6, column=3, padx=10, sticky="w")
        self.longitude_entry.bind("<KeyRelease>", lambda event: maskEspecificacao(event))
        atualizar_abrir_botao = ttk.Button(conteudo, text="Atualizar e Abrir Mapa", command= lambda:atualizar_e_abrir_mapa())
        atualizar_abrir_botao.grid(row=6, column=4, columnspan=2, pady=20)

        ttk.Label(conteudo, wraplength=320, text="Informar valor de Tust para consumo de energia da rede em horário de ponta ($/kW):").grid(row=7, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.valor_tust_ponta = ttk.Entry(conteudo)
        self.valor_tust_ponta.grid(row=7, column=3, padx=10, sticky="w")
        self.valor_tust_ponta.bind("<KeyRelease>", lambda event: maskEspecificacao(event))
        ttk.Label(conteudo, wraplength=320, text="Informar valor de Tust para consumo de energia da rede em horário fora da ponta ($/kW):").grid(row=8, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.valor_tust_fora_ponta = ttk.Entry(conteudo)
        self.valor_tust_fora_ponta.grid(row=8, column=3, padx=10, sticky="w")
        self.valor_tust_fora_ponta.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, text="2. Eletrolisador:", font=self.fonteB).grid(row=9, column=0, columnspan=5, pady=20, sticky="w")
        botao_restaurar = ttk.Button(conteudo, text="Restaurar", command= lambda:defaultEletrolisador())
        botao_restaurar.grid(row=9, column=3, pady=20)
        
        ttk.Label(conteudo, wraplength=240, text="Tecnologia de eletrólise:").grid(row=10, column=0, pady=6, columnspan=2, padx=20, sticky="w")

        tk.Radiobutton(conteudo, text="PEM", variable=self.tecnologia_var, value="pem", command= lambda:on_tecnologia_changed()).grid(row=10, column=3, columnspan=2, padx=10, sticky="w")
        tk.Radiobutton(conteudo, text="ALK", variable=self.tecnologia_var, value="alk", command= lambda:on_tecnologia_changed()).grid(row=10, column=4, columnspan=2, sticky="w")

        ttk.Label(conteudo, wraplength=320, text="Tamanho comercial do eletrolisador (MW):").grid(row=11, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.tamanho_eletrolisador = ttk.Entry(conteudo)
        self.tamanho_eletrolisador.grid(row=11, column=3, padx=10, sticky="w")
        self.tamanho_eletrolisador.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Informar pressão de saída do eletrolisador (MPa):").grid(row=12, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.pressao_saida_eletrolisador = ttk.Entry(conteudo)
        self.pressao_saida_eletrolisador.grid(row=12, column=3, padx=10, sticky="w")
        self.pressao_saida_eletrolisador.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="CAPEX no eletrolisador ($/kW, CAPEX incluindo purificação):").grid(row=13, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.capex_eletrolisador = ttk.Entry(conteudo)
        self.capex_eletrolisador.grid(row=13, column=3, padx=10, sticky="w")
        self.capex_eletrolisador.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Custos de O&M do eletrolisador+purificador (% do CAPEX do eletrolisador/ano):").grid(row=14, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.custos_om = ttk.Entry(conteudo)
        self.custos_om.grid(row=14, column=3, padx=10, sticky="w")
        self.custos_om.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Vida útil do Stack (anos):").grid(row=15, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.vida_util_stack = ttk.Entry(conteudo)
        self.vida_util_stack.grid(row=15, column=3, padx=10, sticky="w")
        self.vida_util_stack.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Custo de substituição do Stack ($/kW):").grid(row=16, column=0, columnspan=2, pady=6, padx=20, sticky="w")
        self.custo_substituicao_stack = ttk.Entry(conteudo)
        self.custo_substituicao_stack.grid(row=16, column=3, padx=10, sticky="w")
        self.custo_substituicao_stack.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Consumo energético para purificação do H₂ (kWh/kgH₂):").grid(row=17, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.consumo_energetico_purificaco_h2 = ttk.Entry(conteudo)
        self.consumo_energetico_purificaco_h2.grid(row=17, column=3, padx=10, sticky="w")
        self.consumo_energetico_purificaco_h2.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Taxa de degradação do eletrolisador (% a.a):").grid(row=18, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.taxa_degradacao_eletrolisador = ttk.Entry(conteudo)
        self.taxa_degradacao_eletrolisador.grid(row=18, column=3, padx=10, sticky="w")
        self.taxa_degradacao_eletrolisador.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Taxa de depreciação contábil do eletrolisador (% a.a):").grid(row=19, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.taxa_depreciacao_eletrolisador = ttk.Entry(conteudo)
        self.taxa_depreciacao_eletrolisador.grid(row=19, column=3, padx=10, sticky="w")
        self.taxa_depreciacao_eletrolisador.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, text="3. Compressor:", font=self.fonteB).grid(row=20, column=0, columnspan=5, pady=20, sticky="w")
        botao_restaurar = ttk.Button(conteudo, text="Restaurar", command= lambda:defaultCompressor())
        botao_restaurar.grid(row=20, column=3, pady=20)
        
        ttk.Label(conteudo, wraplength=320, text="CAPEX do compressor de referência ($):").grid(row=21, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.capex_compressor = ttk.Entry(conteudo)
        self.capex_compressor.grid(row=21, column=3, padx=10, sticky="w")
        self.capex_compressor.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Potência do compressor de referência (kW):").grid(row=22, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.potencia_compressor = ttk.Entry(conteudo)
        self.potencia_compressor.grid(row=22, column=3, padx=10, sticky="w")
        self.potencia_compressor.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Fator de escala do compressor (%):").grid(row=23, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.fator_escala_compressor = ttk.Entry(conteudo)
        self.fator_escala_compressor.grid(row=23, column=3, padx=10, sticky="w")
        self.fator_escala_compressor.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Custos deO&M do compressor (% do CAPEX do compressor/ano):").grid(row=24, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.custos_om_compressor = ttk.Entry(conteudo)
        self.custos_om_compressor.grid(row=24, column=3, padx=10, sticky="w")
        self.custos_om_compressor.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Eficiência do compressor (%):").grid(row=27, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.eficiencia_compressor = ttk.Entry(conteudo)
        self.eficiencia_compressor.grid(row=27, column=3, padx=10, sticky="w")
        self.eficiencia_compressor.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="Z - Fator de compressibilidade (adimensional):").grid(row=28, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.fator_compressibilidade = ttk.Entry(conteudo)
        self.fator_compressibilidade.grid(row=28, column=3, padx=10, sticky="w")
        self.fator_compressibilidade.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="R - Constante de gases (kJ/(kg*K):").grid(row=29, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.constante_gases = ttk.Entry(conteudo)
        self.constante_gases.grid(row=29, column=3, padx=10, sticky="w")
        self.constante_gases.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="T - Temperatura de entrada (K):").grid(row=30, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.temperatura_entrada = ttk.Entry(conteudo)
        self.temperatura_entrada.grid(row=30, column=3, padx=10, sticky="w")
        self.temperatura_entrada.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="N - Número de estágios de compressão:").grid(row=31, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.numero_estagios_compressao = ttk.Entry(conteudo)
        self.numero_estagios_compressao.grid(row=31, column=3, padx=10, sticky="w")
        self.numero_estagios_compressao.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="ƞ - Eficiência isentrópica de compressão (%):").grid(row=32, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.eficiencia_compressao = ttk.Entry(conteudo)
        self.eficiencia_compressao.grid(row=32, column=3, padx=10, sticky="w")
        self.eficiencia_compressao.bind("<KeyRelease>", lambda event: maskEspecificacao(event))

        ttk.Label(conteudo, wraplength=320, text="ƙ - Razão entre os calores específicos (adimensional):").grid(row=33, column=0, columnspan=2, padx=20, pady=6, sticky="w")
        self.razao_calores = ttk.Entry(conteudo)
        self.razao_calores.grid(row=33, column=3, padx=10, sticky="w")
        self.razao_calores.bind("<KeyRelease>", lambda event: maskEspecificacao(event))


        ##  Interações entre campos ##
        #
        def on_tecnologia_changed():
            selected_option = self.tecnologia_var.get()
            if selected_option == "pem":
                self.tamanho_eletrolisador.delete(0, tk.END)
                self.pressao_saida_eletrolisador.delete(0, tk.END)
                self.capex_eletrolisador.delete(0, tk.END)
                self.custos_om.delete(0, tk.END)
                self.vida_util_stack.delete(0, tk.END)
                self.custo_substituicao_stack.delete(0, tk.END)
                self.consumo_energetico_purificaco_h2.delete(0, tk.END)
                self.taxa_degradacao_eletrolisador.delete(0, tk.END)
                self.taxa_depreciacao_eletrolisador.delete(0, tk.END)
                self.tamanho_eletrolisador.insert(0, "1")
                self.pressao_saida_eletrolisador.insert(0, "3")
                self.capex_eletrolisador.insert(0, "1770")
                self.custos_om.insert(0, "3")
                self.vida_util_stack.insert(0, "7")
                self.custo_substituicao_stack.insert(0, "580")
                self.consumo_energetico_purificaco_h2.insert(0, "0.0013")
                self.consumo_energetico_purificaco_h2.config(state='disabled') ##Aqui
                self.taxa_degradacao_eletrolisador.insert(0, "0.9")
                self.taxa_depreciacao_eletrolisador.insert(0, "9")
            elif selected_option == "alk":
                self.tamanho_eletrolisador.delete(0, tk.END)
                self.pressao_saida_eletrolisador.delete(0, tk.END)
                self.capex_eletrolisador.delete(0, tk.END)
                self.custos_om.delete(0, tk.END)
                self.vida_util_stack.delete(0, tk.END)
                self.custo_substituicao_stack.delete(0, tk.END)
                self.consumo_energetico_purificaco_h2.delete(0, tk.END)
                self.taxa_degradacao_eletrolisador.delete(0, tk.END)
                self.taxa_depreciacao_eletrolisador.delete(0, tk.END)
                self.tamanho_eletrolisador.insert(0, "20")
                self.pressao_saida_eletrolisador.insert(0, "1.5")
                self.capex_eletrolisador.insert(0, "1400")
                self.custos_om.insert(0, "3")
                self.vida_util_stack.insert(0, "7")
                self.custo_substituicao_stack.insert(0, "345")
                ##alterei aqui
                self.consumo_energetico_purificaco_h2.config(state='normal')
                self.consumo_energetico_purificaco_h2.delete(0, tk.END)
                ##ate aqui
                self.consumo_energetico_purificaco_h2.insert(0, "0.0013")
                self.taxa_degradacao_eletrolisador.insert(0, "0.9")
                self.taxa_depreciacao_eletrolisador.insert(0, "9")


        ## Valores Default ##
        #         
        def defaultDemanda():
            self.demandaH2.delete(0, tk.END)
            self.demandaH2.insert(0, "0")
            self.periodicidade_demanda.delete(0, tk.END)
            self.periodicidade_demanda.insert(0, "24")
            self.latitude_entry.delete(0, tk.END)
            self.latitude_entry.insert(0, "-22.890451")
            self.longitude_entry.delete(0, tk.END)
            self.longitude_entry.insert(0, "-43.188052")
            self.valor_tust_ponta.delete(0, tk.END)
            self.valor_tust_ponta.insert(0, "0")
            self.valor_tust_fora_ponta.delete(0, tk.END)
            self.valor_tust_fora_ponta.insert(0, "0")

        def defaultEletrolisador():
            self.tecnologia_var.set("pem")
            self.tamanho_eletrolisador.delete(0, tk.END)
            self.pressao_saida_eletrolisador.delete(0, tk.END)
            self.capex_eletrolisador.delete(0, tk.END)
            self.custos_om.delete(0, tk.END)
            self.vida_util_stack.delete(0, tk.END)
            self.custo_substituicao_stack.delete(0, tk.END)
            self.consumo_energetico_purificaco_h2.delete(0, tk.END)
            self.taxa_degradacao_eletrolisador.delete(0, tk.END)
            self.taxa_depreciacao_eletrolisador.delete(0, tk.END)
            self.tamanho_eletrolisador.insert(0, "1")
            self.pressao_saida_eletrolisador.insert(0, "3")
            self.capex_eletrolisador.insert(0, "1770")
            self.custos_om.insert(0, "3")
            self.vida_util_stack.insert(0, "7")
            self.custo_substituicao_stack.insert(0, "580")
            self.consumo_energetico_purificaco_h2.insert(0, "0.0013")
            self.consumo_energetico_purificaco_h2.config(state='disabled') ##Aqui
            self.taxa_degradacao_eletrolisador.insert(0, "0.9")
            self.taxa_depreciacao_eletrolisador.insert(0, "9")

        def defaultCompressor():
            self.capex_compressor.delete(0, tk.END)
            self.capex_compressor.insert(0, "4656000")
            self.potencia_compressor.delete(0, tk.END)
            self.potencia_compressor.insert(0, "4000")
            self.fator_escala_compressor.delete(0, tk.END)
            self.fator_escala_compressor.insert(0, "80")
            self.custos_om_compressor.delete(0, tk.END)
            self.custos_om_compressor.insert(0, "3")
            self.eficiencia_compressor.delete(0, tk.END)
            self.eficiencia_compressor.insert(0, "95")
            self.fator_compressibilidade.delete(0, tk.END)
            self.fator_compressibilidade.insert(0, "1.027")
            self.constante_gases.delete(0, tk.END)
            self.constante_gases.insert(0, "4.12")
            self.temperatura_entrada.delete(0, tk.END)
            self.temperatura_entrada.insert(0, "293")
            self.numero_estagios_compressao.delete(0, tk.END)
            self.numero_estagios_compressao.insert(0, "3")
            self.eficiencia_compressao.delete(0, tk.END)
            self.eficiencia_compressao.insert(0, "0.8")
            self.razao_calores.delete(0, tk.END)
            self.razao_calores.insert(0, "1.41")
    
        defaultDemanda()
        defaultEletrolisador()
        defaultCompressor()


        ## Máscaras ##
        #
        def maskEspecificacao(event):
            demandaH2 = self.demandaH2.get()
            demandaH2_mask = masks.mask_numeral(demandaH2)
            self.demandaH2.delete(0, tk.END)
            self.demandaH2.insert(0, demandaH2_mask)

            periodicidade_demanda = self.periodicidade_demanda.get()
            periodicidade_demanda_mask = masks.mask_decimal(periodicidade_demanda)
            self.periodicidade_demanda.delete(0, tk.END)
            self.periodicidade_demanda.insert(0, periodicidade_demanda_mask)

            latitude = self.latitude_entry.get()
            latitude_mask = masks.mask_coordenadas(latitude)
            self.latitude_entry.delete(0, tk.END)
            self.latitude_entry.insert(0, latitude_mask)

            longitude = self.longitude_entry.get()
            longitude_mask = masks.mask_coordenadas(longitude)
            self.longitude_entry.delete(0, tk.END)
            self.longitude_entry.insert(0, longitude_mask)

            valor_tust_ponta = self.valor_tust_ponta.get()
            valor_tust_ponta_mask = masks.mask_numeral(valor_tust_ponta)
            self.valor_tust_ponta.delete(0, tk.END)
            self.valor_tust_ponta.insert(0, valor_tust_ponta_mask)

            valor_tust_fora_ponta = self.valor_tust_fora_ponta.get()
            valor_tust_fora_ponta_mask = masks.mask_numeral(valor_tust_fora_ponta)
            self.valor_tust_fora_ponta.delete(0, tk.END)
            self.valor_tust_fora_ponta.insert(0, valor_tust_fora_ponta_mask)

            tamanho_eletrolisador = self.tamanho_eletrolisador.get()
            tamanho_eletrolisador_mask = masks.mask_decimal(tamanho_eletrolisador)
            self.tamanho_eletrolisador.delete(0, tk.END)
            self.tamanho_eletrolisador.insert(0, tamanho_eletrolisador_mask)

            pressao_saida_eletrolisador = self.pressao_saida_eletrolisador.get()
            pressao_saida_eletrolisador_mask = masks.mask_decimal(pressao_saida_eletrolisador)
            self.pressao_saida_eletrolisador.delete(0, tk.END)
            self.pressao_saida_eletrolisador.insert(0, pressao_saida_eletrolisador_mask)

            capex_eletrolisador = self.capex_eletrolisador.get()
            capex_eletrolisador_mask = masks.mask_numeral(capex_eletrolisador)
            self.capex_eletrolisador.delete(0, tk.END)
            self.capex_eletrolisador.insert(0, capex_eletrolisador_mask)

            custos_om = self.custos_om.get()
            custos_om_mask = masks.mask_numeral(custos_om)
            self.custos_om.delete(0, tk.END)
            self.custos_om.insert(0, custos_om_mask)

            vida_util_stack = self.vida_util_stack.get()
            vida_util_stack_mask = masks.mask_numeral(vida_util_stack)
            self.vida_util_stack.delete(0, tk.END)
            self.vida_util_stack.insert(0, vida_util_stack_mask)

            custo_substituicao_stack = self.custo_substituicao_stack.get()
            custo_substituicao_stack_mask = masks.mask_decimal(custo_substituicao_stack)
            self.custo_substituicao_stack.delete(0, tk.END)
            self.custo_substituicao_stack.insert(0, custo_substituicao_stack)

            consumo_energetico_purificaco_h2 = self.consumo_energetico_purificaco_h2.get()
            consumo_energetico_purificaco_h2_mask = masks.mask_decimal(consumo_energetico_purificaco_h2)
            self.consumo_energetico_purificaco_h2.delete(0, tk.END)
            self.consumo_energetico_purificaco_h2.insert(0, consumo_energetico_purificaco_h2_mask)

            taxa_degradacao_eletrolisador = self.taxa_degradacao_eletrolisador.get()
            taxa_degradacao_eletrolisador_mask = masks.mask_decimal(taxa_degradacao_eletrolisador)
            self.taxa_degradacao_eletrolisador.delete(0, tk.END)
            self.taxa_degradacao_eletrolisador.insert(0, taxa_degradacao_eletrolisador_mask)

            taxa_depreciacao_eletrolisador = self.taxa_depreciacao_eletrolisador.get()
            taxa_depreciacao_eletrolisador_mask = masks.mask_decimal(taxa_depreciacao_eletrolisador)
            self.taxa_depreciacao_eletrolisador.delete(0, tk.END)
            self.taxa_depreciacao_eletrolisador.insert(0, taxa_depreciacao_eletrolisador_mask)

            capex_compressor = self.capex_compressor.get()
            capex_compressor_mask = masks.mask_decimal(capex_compressor)
            self.capex_compressor.delete(0, tk.END)
            self.capex_compressor.insert(0, capex_compressor_mask)

            potencia_compressor = self.potencia_compressor.get()
            potencia_compressor_mask = masks.mask_decimal(potencia_compressor)
            self.potencia_compressor.delete(0, tk.END)
            self.potencia_compressor.insert(0, potencia_compressor_mask)

            fator_escala_compressor = self.fator_escala_compressor.get()
            fator_escala_compressor_mask = masks.mask_numeral(fator_escala_compressor)
            self.fator_escala_compressor.delete(0, tk.END)
            self.fator_escala_compressor.insert(0, fator_escala_compressor_mask)

            custos_om_compressor = self.custos_om_compressor.get()
            custos_om_compressor_mask = masks.mask_decimal(custos_om_compressor)
            self.custos_om_compressor.delete(0, tk.END)
            self.custos_om_compressor.insert(0, custos_om_compressor_mask)

            eficiencia_compressor = self.eficiencia_compressor.get()
            eficiencia_compressor_mask = masks.mask_decimal(eficiencia_compressor)
            self.eficiencia_compressor.delete(0, tk.END)
            self.eficiencia_compressor.insert(0, eficiencia_compressor_mask)

            fator_compressibilidade = self.fator_compressibilidade.get()
            fator_compressibilidade_mask = masks.mask_decimal(fator_compressibilidade)
            self.fator_compressibilidade.delete(0, tk.END)
            self.fator_compressibilidade.insert(0, fator_compressibilidade_mask)
            
            constante_gases = self.constante_gases.get()
            constante_gases_mask = masks.mask_decimal(constante_gases)
            self.constante_gases.delete(0, tk.END)
            self.constante_gases.insert(0, constante_gases_mask)

            temperatura_entrada = self.temperatura_entrada.get()
            temperatura_entrada_mask = masks.mask_decimal(temperatura_entrada)
            self.temperatura_entrada.delete(0, tk.END)
            self.temperatura_entrada.insert(0, temperatura_entrada_mask)
            
            numero_estagios_compressao = self.numero_estagios_compressao.get()
            numero_estagios_compressao_mask = masks.mask_numeral(numero_estagios_compressao)
            self.numero_estagios_compressao.delete(0, tk.END)
            self.numero_estagios_compressao.insert(0, numero_estagios_compressao_mask)

            eficiencia_compressao = self.eficiencia_compressao.get()
            eficiencia_compressao_mask = masks.mask_decimal(eficiencia_compressao)
            self.eficiencia_compressao.delete(0, tk.END)
            self.eficiencia_compressao.insert(0, eficiencia_compressao_mask)
            
            razao_calores = self.razao_calores.get()
            razao_calores_mask = masks.mask_decimal(razao_calores)
            self.razao_calores.delete(0, tk.END)
            self.razao_calores.insert(0, razao_calores_mask)


        ## Mapa ##
        #
        def atualizar_e_abrir_mapa():
            global latitude, longitude

            try:    
                # Obtém as coordenadas da latitude e longitude
                latitude = float(self.latitude_entry.get())
                longitude = float(self.longitude_entry.get())

                campo = "Erro em Especificação da Demanda"
                subcampo = "Campo Latitude"
                validate_latitude(latitude,subcampo)
                subcampo = "Campo Longitude"
                validate_longitude(longitude,subcampo)

                # Cria um mapa Folium centrado nas coordenadas especificadas
                mapa = folium.Map(location=[latitude, longitude], zoom_start=6)

                # Adiciona um marcador no mapa nas coordenadas especificadas
                folium.Marker([latitude, longitude], tooltip="Localização").add_to(mapa)

                # Salva o mapa como um arquivo HTML temporário
                mapa.save('mapa.html')

                # Abre o arquivo mapa.html em um navegador
                webbrowser.open('mapa.html')
            except CoordenadasInvalidasError as e:
                messagebox.showerror(campo, str(e))
                pass        




