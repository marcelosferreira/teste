import json

def enviar_formulario(self):

        cert_types = {"energia_fornecida": 1, "hidrgenio_produzido": 0}
        cert_type = cert_types.get(self.certif_var.get())
        cert_types_det = {"24 7 CFE (Carbon Free Energy)": 1, "RED - Renewable Energy Directive": 1, "Low Carbon Hydrogen Standart": 2, "CHPS - Clean Hydrogen Production Standart": 3, "Outro": 4}
        cert_type_det = cert_types_det.get(self.op_certfic_var.get())
        eebms = {"Mensal":"Month", "Semanal":"Week", "Horária": "Hour", "A cada 30 min": "30_min"}
        eebm = eebms.get(self.menu_balanco_energia.get())
        bidding_zone_limits = {"SIN": 0, "Subsistema": 1, "Distância (Informar valor)":-1}
        bidding_zone_limit = bidding_zone_limits.get(self.menu_limite_bidding_zone.get())
        eams = {"Mensal":"Month", "Semanal":"Week", "Horária": "Hour", "A cada 30 min": "30_min"}
        eam = eams.get(self.periodicidade_checagens_menu.get())
        emissions_fronts = {"Até a produção": 0, "Até a entrega": 1}
        emissions_front = emissions_fronts.get(self.menu_fronteira_analise.get())
        emission_factors_crits = {"Somente combustão": 0, "Combustão + Upstream": 1}
        emission_factors_crit = emission_factors_crits.get(self.menu_criterio_fator_emissão_hidrogenio.get())

        def coletar_dados_etapa3():
            dados_etapa3 = []
            for i in range(20):
                if (self.selecionar_entries[i].get()=="1"):
                    dados_linha = {
                        "nome_usina": self.nome_usina_entries[i].get(),
                        "fonte_energia": self.fonte_energia_entries[i].get(),
                        "latitude": self.lat_entries[i].get(),
                        "longitude": self.long_entries[i].get(),
                        "potencia": self.potencia_entries[i].get(),
                        "capacidade_reservatorio": self.capacidade_reservatorio_entries[i].get(),
                        "aumentar_fator": self.aumentar_fator_entries[i].get(),
                        "ip_paradas_programadas": self.ip_paradas_prog_entries[i].get(),
                        "ip_paradas_nao_programadas": self.ip_paradas_nao_prog_entries[i].get(),
                        "tx_risco_curtailment": self.tx_risco_curtailment_entries[i].get(),
                        "tx_degradacao": self.tx_degradacao_entries[i].get(),
                        "tx_depreciacao_contabil": self.tx_depreciacao_contabil_entries[i].get(),
                        "capex_fontes": self.capex_fontes_entries[i].get(),
                        "opex_fontes": self.opex_fontes_entries[i].get(),
                        "pagamento_tustg": self.pagamento_tustg_entries[i].get(),
                        "geracao_local": self.geracao_local_entries[i].get(),
                        "idade_usina": self.idade_usina_entries[i].get(),
                        "proj_preco_custo": self.proj_preco_custo_entries[i].get(),
                        "prev_geracao": self.prev_geracao_entries[i].get(),
                        "custo_preco_energia": self.custo_preco_energia_entries[i].get()
                    }
                    dados_etapa3.append(dados_linha)

            return dados_etapa3


        form = {
            #ETAPA1
            "cert_type": cert_type, 
            "cert_type_det": cert_type_det,
            "min_renewable_part_24_7":self.part_minima.get(),
            "ci_with_upstream": self.limite_intensidade.get(),
            "min_renewable_part": self.limite_particiapacao.get(),
            "eebm": eebm,
            "bidding_zone_limit": bidding_zone_limit,
            "bidding_zone_limit_dist": self.limite_bidding_zone_distancia.get(),
            "power_plants_adic_lim": self.limite_adicionalidade.get(),
            "cert_emissions_limit": self.limite_emissoes_cadeira_producao.get(),
            "eam": eam,
            "emissions_front": emissions_front,
            "emissions_imat": self.imaterialidade.get(),
            "emission_factors_crit": emission_factors_crit,
            "cert_pressure": self.padrao_pressao_hidrogenio.get(),
            "cert_purity": self.padrao_pureza.get(),
            #Abaixo somente as variáveis da tela
            "criterioA_intensidade_carbono": self.criterioA_intensidade_carbono.get(),
            "criterioA_participacao_minima": self.criterioA_part_minima.get(),
            "criterioA_contratacao_planta_temporal": self.criterioA_contratacao_planta_temporal.get(),
            "criterioA_contratacao_planta_espacial": self.criterioA_contratacao_planta_espacial.get(),
            "criterioA_contratacao_planta_adicionalidade": self.criterioA_contratacao_planta_adicionalidade.get(),
            "criterioB_intensidade_carbono": self.criterioB_intensidade_carbono.get(),
            "criterioB_participacao_minima": self.criterioB_part_minima.get(),
            "criterioB_contratacao_planta_temporal": self.criterioB_contratacao_planta_temporal.get(),
            "criterioB_contratacao_planta_espacial": self.criterioB_contratacao_planta_espacial.get(),
            "criterioB_contratacao_planta_adicionalidade": self.criterioB_contratacao_planta_adicionalidade.get(),
            "criterioC_intensidade_carbono": self.criterioC_intensidade_carbono.get(),
            "criterioC_participacao_minima": self.criterioC_part_minima.get(),
            "criterioC_contratacao_planta_temporal": self.criterioC_contratacao_planta_temporal.get(),
            "criterioC_contratacao_planta_espacial": self.criterioC_contratacao_planta_espacial.get(),
            "criterioC_contratacao_planta_adicionalidade": self.criterioC_contratacao_planta_adicionalidade.get(),
            "criterioD_intensidade_carbono": self.criterioD_intensidade_carbono.get(),
            "criterioD_participacao_minima": self.criterioD_part_minima.get(),
            "criterioD_contratacao_planta_temporal": self.criterioD_contratacao_planta_temporal.get(),
            "criterioD_contratacao_planta_espacial": self.criterioD_contratacao_planta_espacial.get(),
            "criterioD_contratacao_planta_adicionalidade": self.criterioD_contratacao_planta_adicionalidade.get(),
            "criterioE_intensidade_carbono": self.criterioE_intensidade_carbono.get(),
            "criterioE_participacao_minima": self.criterioE_part_minima.get(),
            "criterioE_contratacao_planta_temporal": self.criterioE_contratacao_planta_temporal.get(),
            "criterioE_contratacao_planta_espacial": self.criterioE_contratacao_planta_espacial.get(),
            "criterioE_contratacao_planta_adicionalidade": self.criterioE_contratacao_planta_adicionalidade.get(),
            "criterioF_intensidade_carbono": self.criterioF_intensidade_carbono.get(),
            "criterioF_participacao_minima": self.criterioF_part_minima.get(),
            "criterioF_contratacao_planta_temporal": self.criterioF_contratacao_planta_temporal.get(),
            "criterioF_contratacao_planta_espacial": self.criterioF_contratacao_planta_espacial.get(),
            "criterioF_contratacao_planta_adicionalidade": self.criterioF_contratacao_planta_adicionalidade.get(),
            #ETAPA2
            "demanda_H2": self.demandaH2.get(),
            "periodicidade_demanda": self.periodicidade_demanda.get(),
            "latitude": self.latitude_entry.get(),
            "longitude": self.longitude_entry.get(),
            "valor_tust_ponta": self.valor_tust_ponta.get(),
            "valor_tust_fora_ponta": self.valor_tust_fora_ponta.get(),
            "tecnologia_eletrólise": self.tecnologia_var.get(),
            "tamanho_eletrolisador": self.tamanho_eletrolisador.get(),
            "pressao_saida_eletrolisador": self.pressao_saida_eletrolisador.get(),
            "capex_eletrolisador": self.capex_eletrolisador.get(),
            "custos_om": self.custos_om.get(),
            "vida_util_stack": self.vida_util_stack.get(),
            "custo_substituicao_stack": self.custo_substituicao_stack.get(),
            "consumo_energetico_purificaco_h2": self.consumo_energetico_purificaco_h2.get(),
            "taxa_degradacao_eletrolisador": self.taxa_degradacao_eletrolisador.get(),
            "taxa_depreciacao_eletrolisador": self.taxa_depreciacao_eletrolisador.get(),
            "capex_compressor": self.capex_compressor.get(),
            "potencia_compressor": self.potencia_compressor.get(),
            "fator_escala_compressor": self.fator_escala_compressor.get(),
            "custos_om_compressor": self.custos_om_compressor.get(),
            "eficiencia_compressor": self.eficiencia_compressor.get(),
            "fator_compressibilidade": self.fator_compressibilidade.get(),
            "constante_gases": self.constante_gases.get(),
            "temperatura_entrada": self.temperatura_entrada.get(),
            "numero_estagios_compressao": self.numero_estagios_compressao.get(),
            "eficiencia_compressao": self.eficiencia_compressao.get(),
            "razao_calores": self.razao_calores.get(),
            #ETAPA3
            "Etapa3": coletar_dados_etapa3(),
            #ETAPA4
            "utiliza_baterias": self.baterias_var.get(),
            "tecnologia_baterias": self.tecbaterias_var.get(),
            "capex_bateria": self.capex_bateria.get(),
            "custos_om_bateria": self.custos_om_bateria.get(),
            "custos_substituicao_baterias": self.custos_substituicao_baterias.get(),
            "capacidade_baterias": self.capacidade_baterias.get(),
            "capacidade_descarregamento": self.capacidade_descarregamento.get(),
            "capacidade_carregamento": self.capacidade_carregamento.get(),
            "eficiencia_carga_bateria": self.eficiencia_carga_bateria.get(),
            "eficiencia_descarga_bateria": self.eficiencia_descarga_bateria.get(),
            "ciclos": self.ciclos.get(),
            "taxa_depreciacao_contabil_bateria": self.taxa_depreciacao_contabil_bateria.get(),
            #ETAPA5
            "horizonte_projeto": self.horizonteprojeto.get(),
            "participacao_capital_proprio": self.partcaptaproprio.get(),
            "custo_capital_proprio": self.custocapitalproprio.get(),
            "tipo_amortizacao": self.tipoamortizacao_var.get(),
            "periodo_financiamento": self.periodofuncionamento.get(),
            "taxa_juros_real_financiamento": self.txjurosreal.get(),
            "periodo_carencia": self.periodocarencia.get(),
            "custos_administrativos_projeto": self.custosprojeto.get(),
            "pis_confins": self.pisconfins.get(),
            "icms": self.icms.get(),
            "imposto_renda_contribuicao_social": self.impostorenda.get(),
            "venda_oxigenio": self.vendaoxigenio_var.get(),
            "taxa_producao_oxigenio": self.taxaprodoxigenio.get(),
            "preco_venda_oxigenio": self.precovendaoxigenio.get(),
            "taxa_aumento_preco_oxigenio": self.taxaaumentooxigenio.get(),
            "demanda_agua_eletrolisador": self.demandaagua.get(),
            "demanda_agua_processo_eletrolisador": self.demandaaguaeletro.get(),
            "preco_agua_pura": self.precoaguapura.get(),
            "preco_agua_processo": self.precoaguaproc.get(),
            "preco_transporte_agua": self.precotranspagua.get(),
            "distancia_eletrolisador_fonte_agua": self.disteletrolisadorfonte.get(),
            "taxa_aumento_anual_custos_agua": self.taxaaumentoanual.get(),
            "precificacao_carbono": self.precificacaocarbono.get(),
            "aumento_preco_carbono": self.aumentoprecocarbono.get(),
            "valor_referencia_emissoes_producao_reforma_vapor": self.valoremissoesprod.get(),
            "preco_aquisicao_energia_rede": self.precoaquisicaoenergia.get(),
            "possibilidade_venda_excedente_energia_rede": self.possibilidadevendaexcedente_var.get(),
            "preco_venda_excedente_energia_rede": self.precovendaenergia.get(),
            "custo_construcao_novas_linhas_transmissao": self.custorelativonovaslinhas.get(),
            "fator_emissao_rede": self.fator_emissao_var.get(),
            "projecao_participacao_renovaveis_rede": self.proj_esperada_var.get(),
            }

        json_string = json.dumps(form, indent=2)
        print(json_string)
        nome = "form.json"

        with open(nome, 'w') as arquivo:
            json.dump(form, arquivo, indent=2)

        print("Dados salvos como", nome)


