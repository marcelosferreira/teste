#etapa4.py
import tkinter as tk
from tkinter import ttk
import masks

def criar_etapa4(self,etapa4):

        self.baterias_var = tk.StringVar()
        self.tecbaterias_var = tk.StringVar()

        ttk.Label(etapa4, text="Especificação da Tecnologia de armazenamento",font=self.fonte).grid(row=0, column=0, columnspan=4, sticky="w")

        ttk.Label(etapa4, text="O projeto utiliza baterias?").grid(row=1, column=0, padx=20, pady=6, sticky="w")
        tk.Radiobutton(etapa4, text="Sim", variable=self.baterias_var, value="sim", command= lambda:on_op_baterias_changed()).grid(row=1, column=1, columnspan=2, padx=10, sticky="w")
        tk.Radiobutton(etapa4, text="Não", variable=self.baterias_var, value="nao", command= lambda:on_op_baterias_changed()).grid(row=1, column=2, columnspan=2, sticky="w")
        
        ttk.Label(etapa4, text="Selecionar tipo de tecnologia de baterias:").grid(row=3, column=0, padx=20, pady=6, sticky="w")
        tk.Radiobutton(etapa4, text="Lítio                ", variable=self.tecbaterias_var, value="litio", command= lambda:on_op_tec_baterias_changed()).grid(row=3, column=1, padx=10, sticky="w")
        tk.Radiobutton(etapa4, text="Chumbo-Ácido                ", variable=self.tecbaterias_var, value="chumbo_acido", command=lambda:on_op_tec_baterias_changed()).grid(row=3, column=2, sticky="w")
        tk.Radiobutton(etapa4, text="Sódio                ", variable=self.tecbaterias_var, value="sodio", command=lambda:on_op_tec_baterias_changed()).grid(row=3, column=3, padx=10, sticky="w")
        tk.Radiobutton(etapa4, text="Outra                ", variable=self.tecbaterias_var, value="outra", command=lambda:on_op_tec_baterias_changed()).grid(row=3, column=4, sticky="w")

        ttk.Label(etapa4, text="CAPEX bateria: ($/kW)").grid(row=4, column=0, padx=20, pady=6, sticky="w")
        self.capex_bateria = ttk.Entry(etapa4)
        self.capex_bateria.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.capex_bateria.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Custos de O&M bateria ($/(kW*ano)):").grid(row=5, column=0, padx=20, pady=6, sticky="w")
        self.custos_om_bateria = ttk.Entry(etapa4)
        self.custos_om_bateria.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.custos_om_bateria.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Custos de substituição das baterias (% CAPEX bateria):").grid(row=6, column=0, padx=20, pady=6, sticky="w")
        self.custos_substituicao_baterias = ttk.Entry(etapa4)
        self.custos_substituicao_baterias.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        self.custos_substituicao_baterias.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Capacidade de referência das baterias (MWh):").grid(row=7, column=0, padx=20, pady=6, sticky="w")
        self.capacidade_baterias = ttk.Entry(etapa4)
        self.capacidade_baterias.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        self.capacidade_baterias.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Capacidade de descarregamento (% da capacidade de armazenamento):").grid(row=8, column=0, padx=20, pady=6, sticky="w")
        self.capacidade_descarregamento = ttk.Entry(etapa4)
        self.capacidade_descarregamento.grid(row=8, column=1, padx=10, pady=5, sticky="w")
        self.capacidade_descarregamento.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Capacidade de carregamento (% da capacidade de armazenamento):").grid(row=9, column=0, padx=20, pady=6, sticky="w")
        self.capacidade_carregamento = ttk.Entry(etapa4)
        self.capacidade_carregamento.grid(row=9, column=1, padx=10, pady=5, sticky="w")
        self.capacidade_carregamento.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Eficiência de carga da bateria (%):").grid(row=10, column=0, padx=20, pady=6, sticky="w")
        self.eficiencia_carga_bateria = ttk.Entry(etapa4)
        self.eficiencia_carga_bateria.grid(row=10, column=1, padx=10, pady=5, sticky="w")
        self.eficiencia_carga_bateria.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Eficiência de descarga da bateria (%):").grid(row=11, column=0, padx=20, pady=6, sticky="w")
        self.eficiencia_descarga_bateria = ttk.Entry(etapa4)
        self.eficiencia_descarga_bateria.grid(row=11, column=1, padx=10, pady=5, sticky="w")
        self.eficiencia_descarga_bateria.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Ciclos (ciclos):").grid(row=12, column=0, padx=20, pady=6, sticky="w")
        self.ciclos = ttk.Entry(etapa4)
        self.ciclos.grid(row=12, column=1, padx=10, pady=5, sticky="w")
        self.ciclos.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))

        ttk.Label(etapa4, text="Taxa de depreciação contábil da bateria (%a.a):").grid(row=13, column=0, padx=20, pady=6, sticky="w")
        self.taxa_depreciacao_contabil_bateria = ttk.Entry(etapa4)
        self.taxa_depreciacao_contabil_bateria.grid(row=13, column=1, padx=10, pady=5, sticky="w")
        self.taxa_depreciacao_contabil_bateria.bind("<KeyRelease>", lambda event: maskTecnologiaBaterias(event))


        ## Valores Default ##
        #         
        def defaultTecnologia():
            self.baterias_var.set("sim")
            self.tecbaterias_var.set("litio")
            self.capex_bateria.delete(0, tk.END)
            self.capex_bateria.insert(0, "150")
            self.custos_om_bateria.delete(0, tk.END)
            self.custos_om_bateria.insert(0, "30")
            self.custos_substituicao_baterias.delete(0, tk.END)
            self.custos_substituicao_baterias.insert(0, "90")
            self.capacidade_baterias.delete(0, tk.END)
            self.capacidade_baterias.insert(0, "1")
            self.capacidade_descarregamento.delete(0, tk.END)
            self.capacidade_descarregamento.insert(0, "1")
            self.capacidade_carregamento.delete(0, tk.END)
            self.capacidade_carregamento.insert(0, "1")
            self.eficiencia_carga_bateria.delete(0, tk.END)
            self.eficiencia_carga_bateria.insert(0, "90")
            self.eficiencia_descarga_bateria.delete(0, tk.END)
            self.eficiencia_descarga_bateria.insert(0, "90")
            self.ciclos.delete(0, tk.END)
            self.ciclos.insert(0, "2000")
            self.taxa_depreciacao_contabil_bateria.delete(0, tk.END)
            self.taxa_depreciacao_contabil_bateria.insert(0, "10")


        ##  Interações entre campos ##
        #
        def on_op_baterias_changed():
            selected_option = self.baterias_var.get()
            if selected_option == "sim":
                self.capex_bateria.config(state=tk.NORMAL)
                self.custos_om_bateria.config(state=tk.NORMAL)
                self.custos_substituicao_baterias.config(state=tk.NORMAL)
                self.capacidade_baterias.config(state=tk.NORMAL)
                self.capacidade_descarregamento.config(state=tk.NORMAL)
                self.capacidade_carregamento.config(state=tk.NORMAL)
                self.eficiencia_carga_bateria.config(state=tk.NORMAL)
                self.eficiencia_descarga_bateria.config(state=tk.NORMAL)
                self.ciclos.config(state=tk.NORMAL)
                self.taxa_depreciacao_contabil_bateria.config(state=tk.NORMAL)
                defaultTecnologia()
            elif selected_option == "nao":
                self.capex_bateria.delete(0, tk.END)
                self.capex_bateria.config(state=tk.DISABLED)
                self.custos_om_bateria.delete(0, tk.END)
                self.custos_om_bateria.config(state=tk.DISABLED)
                self.custos_substituicao_baterias.delete(0, tk.END)
                self.custos_substituicao_baterias.config(state=tk.DISABLED)
                self.capacidade_baterias.delete(0, tk.END)
                self.capacidade_baterias.config(state=tk.DISABLED)
                self.capacidade_descarregamento.delete(0, tk.END)
                self.capacidade_descarregamento.config(state=tk.DISABLED)
                self.capacidade_carregamento.delete(0, tk.END)
                self.capacidade_carregamento.config(state=tk.DISABLED)
                self.eficiencia_carga_bateria.delete(0, tk.END)
                self.eficiencia_carga_bateria.config(state=tk.DISABLED)
                self.eficiencia_descarga_bateria.delete(0, tk.END)
                self.eficiencia_descarga_bateria.config(state=tk.DISABLED)
                self.ciclos.delete(0, tk.END)
                self.ciclos.config(state=tk.DISABLED)
                self.taxa_depreciacao_contabil_bateria.delete(0, tk.END)
                self.taxa_depreciacao_contabil_bateria.config(state=tk.DISABLED)

        def on_op_tec_baterias_changed():
            selected_option = self.tecbaterias_var.get()
            if selected_option == "litio":
                self.capex_bateria.delete(0, tk.END)
                self.capex_bateria.insert(0, "150")
                self.custos_om_bateria.delete(0, tk.END)
                self.custos_om_bateria.insert(0, "30")
                self.custos_substituicao_baterias.delete(0, tk.END)
                self.custos_substituicao_baterias.insert(0, "90")
                self.capacidade_baterias.delete(0, tk.END)
                self.capacidade_baterias.insert(0, "1")
                self.capacidade_descarregamento.delete(0, tk.END)
                self.capacidade_descarregamento.insert(0, "1")
                self.capacidade_carregamento.delete(0, tk.END)
                self.capacidade_carregamento.insert(0, "1")
                self.eficiencia_carga_bateria.delete(0, tk.END)
                self.eficiencia_carga_bateria.insert(0, "90")
                self.eficiencia_descarga_bateria.delete(0, tk.END)
                self.eficiencia_descarga_bateria.insert(0, "90")
                self.ciclos.delete(0, tk.END)
                self.ciclos.insert(0, "2000")
                self.taxa_depreciacao_contabil_bateria.delete(0, tk.END)
                self.taxa_depreciacao_contabil_bateria.insert(0, "10")
            elif selected_option == "chumbo_acido":
                self.capex_bateria.delete(0, tk.END)
                self.capex_bateria.insert(0, "129.7")
                self.custos_om_bateria.delete(0, tk.END)
                self.custos_om_bateria.insert(0, "8.42")
                self.custos_substituicao_baterias.delete(0, tk.END)
                self.custos_substituicao_baterias.insert(0, "104.4")
                self.capacidade_baterias.delete(0, tk.END)
                self.capacidade_baterias.insert(0, "40")
                self.capacidade_descarregamento.delete(0, tk.END)
                self.capacidade_descarregamento.insert(0, "12")
                self.capacidade_carregamento.delete(0, tk.END)
                self.capacidade_carregamento.insert(0, "20")
                self.eficiencia_carga_bateria.delete(0, tk.END)
                self.eficiencia_carga_bateria.insert(0, "65")
                self.eficiencia_descarga_bateria.delete(0, tk.END)
                self.eficiencia_descarga_bateria.insert(0, "70")
                self.ciclos.delete(0, tk.END)
                self.ciclos.insert(0, "2000")
                self.taxa_depreciacao_contabil_bateria.delete(0, tk.END)
                self.taxa_depreciacao_contabil_bateria.insert(0, "0")
            elif selected_option == "sodio":
                self.capex_bateria.delete(0, tk.END)
                self.capex_bateria.insert(0, "300")
                self.custos_om_bateria.delete(0, tk.END)
                self.custos_om_bateria.insert(0, "6.5")
                self.custos_substituicao_baterias.delete(0, tk.END)
                self.custos_substituicao_baterias.insert(0, "0")
                self.capacidade_baterias.delete(0, tk.END)
                self.capacidade_baterias.insert(0, "34")
                self.capacidade_descarregamento.delete(0, tk.END)
                self.capacidade_descarregamento.insert(0, "0")
                self.capacidade_carregamento.delete(0, tk.END)
                self.capacidade_carregamento.insert(0, "7")
                self.eficiencia_carga_bateria.delete(0, tk.END)
                self.eficiencia_carga_bateria.insert(0, "90")
                self.eficiencia_descarga_bateria.delete(0, tk.END)
                self.eficiencia_descarga_bateria.insert(0, "75")
                self.ciclos.delete(0, tk.END)
                self.ciclos.insert(0, "3500")
                self.taxa_depreciacao_contabil_bateria.delete(0, tk.END)
                self.taxa_depreciacao_contabil_bateria.insert(0, "0")
                #Alterei aqui, comentei tudo 
            # elif selected_option == "outra":
            #     self.capex_bateria.delete(0, tk.END)
            #     self.custos_om_bateria.delete(0, tk.END)
            #     self.custos_substituicao_baterias.delete(0, tk.END)
            #     self.capacidade_baterias.delete(0, tk.END)
            #     self.capacidade_descarregamento.delete(0, tk.END)
            #     self.capacidade_carregamento.delete(0, tk.END)
            #     self.eficiencia_carga_bateria.delete(0, tk.END)
            #     self.eficiencia_descarga_bateria.delete(0, tk.END)
            #     self.ciclos.delete(0, tk.END)
            #     self.taxa_depreciacao_contabil_bateria.delete(0, tk.END)
        
        defaultTecnologia()


        ## Máscaras ##
        #
        def maskTecnologiaBaterias(event):
        
            capex_bateria = self.capex_bateria.get()
            capex_bateria_mask = masks.mask_decimal(capex_bateria)
            self.capex_bateria.delete(0, tk.END)
            self.capex_bateria.insert(0, capex_bateria_mask)
            
            custos_om_bateria = self.custos_om_bateria.get()
            custos_om_bateria_mask = masks.mask_decimal(custos_om_bateria)
            self.custos_om_bateria.delete(0, tk.END)
            self.custos_om_bateria.insert(0, custos_om_bateria_mask)
            
            custos_substituicao_baterias = self.custos_substituicao_baterias.get()
            custos_substituicao_baterias_mask = masks.mask_decimal(custos_substituicao_baterias)
            self.custos_substituicao_baterias.delete(0, tk.END)
            self.custos_substituicao_baterias.insert(0, custos_substituicao_baterias_mask)

            capacidade_baterias = self.capacidade_baterias.get()
            capacidade_baterias_mask = masks.mask_decimal(capacidade_baterias)
            self.capacidade_baterias.delete(0, tk.END)
            self.capacidade_baterias.insert(0, capacidade_baterias_mask)        

            capacidade_descarregamento = self.capacidade_descarregamento.get()
            capacidade_descarregamento_mask = masks.mask_decimal(capacidade_descarregamento)
            self.capacidade_descarregamento.delete(0, tk.END)
            self.capacidade_descarregamento.insert(0, capacidade_descarregamento_mask)
            
            capacidade_carregamento = self.capacidade_carregamento.get()
            capacidade_carregamento_mask = masks.mask_decimal(capacidade_carregamento)
            self.capacidade_carregamento.delete(0, tk.END)
            self.capacidade_carregamento.insert(0, capacidade_carregamento_mask)

            eficiencia_carga_bateria = self.eficiencia_carga_bateria.get()
            eficiencia_carga_bateria_mask = masks.mask_decimal(eficiencia_carga_bateria)
            self.eficiencia_carga_bateria.delete(0, tk.END)
            self.eficiencia_carga_bateria.insert(0, eficiencia_carga_bateria_mask)

            eficiencia_descarga_bateria = self.eficiencia_descarga_bateria.get()
            eficiencia_descarga_bateria_mask = masks.mask_decimal(eficiencia_descarga_bateria)
            self.eficiencia_descarga_bateria.delete(0, tk.END)
            self.eficiencia_descarga_bateria.insert(0, eficiencia_descarga_bateria_mask)
            
            ciclos = self.ciclos.get()
            ciclos_mask = masks.mask_numeral(ciclos)
            self.ciclos.delete(0, tk.END)
            self.ciclos.insert(0, ciclos_mask)

            taxa_depreciacao_contabil_bateria = self.taxa_depreciacao_contabil_bateria.get()
            taxa_depreciacao_contabil_bateria_mask = masks.mask_decimal(taxa_depreciacao_contabil_bateria)
            self.taxa_depreciacao_contabil_bateria.delete(0, tk.END)
            self.taxa_depreciacao_contabil_bateria.insert(0, taxa_depreciacao_contabil_bateria_mask)

            capex_bateria = self.capex_bateria.get()
            capex_bateria_mask = masks.mask_numeral(capex_bateria)
            self.capex_bateria.delete(0, tk.END)
            self.capex_bateria.insert(0, capex_bateria_mask)
