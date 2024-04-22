#from main_simul import run_main_simulation
from datetime import datetime
import openpyxl
from tkinter import messagebox
import tkinter as tk
from front_loader import LoaderApp


def transform_cert_data(cert_data):
    # Create an ordered list of letters for indexing
    letters = 'ABCDEF'
    # Initialize a dictionary to hold our sublists
    data_by_letter = {letter: [] for letter in letters}

    for key, value in cert_data.items():
        if "criterio" not in key:
            continue
        if value == "1":
            boolean_value = True
        else:
            boolean_value = False
        # Identify the letter in the key and make sure it is uppercase
        letter = key[8].upper()  # Convert to uppercase to match our dictionary keys
        # Convert the value to boolean and append it to the correct sublist
        try:
            data_by_letter[letter].append(boolean_value)
        except KeyError:
            # This block will catch any unexpected letters
            print(f"Unexpected letter found in key: {key}")
            continue

    # Extract the sublists and filter out any empty ones
    certification_entries_data = [data_by_letter[letter] for letter in letters if data_by_letter[letter]]

    return certification_entries_data


def retrieve_annual_ts_data_from_xlsx(workbook_path, number_of_years):
    timeseries_data = list()
    wb = openpyxl.load_workbook(workbook_path)
    sh = wb['dados']
    for i in range(number_of_years):
        timeseries_data.append(sh.cell(2 + i, 2).value)

    return timeseries_data


def retrieve_water_annual_opex(reg_water_electrolyzer_demand, pure_water_electrolyzer_demand,
                               reg_water_price, pure_water_price, water_transport_price,
                               water_distance, h2_average_hour_demand):
    hour_reg_water_electrolyzer_demand = h2_average_hour_demand * reg_water_electrolyzer_demand
    hour_pure_water_electrolyzer_demand = h2_average_hour_demand * pure_water_electrolyzer_demand
    hour_reg_water_cost = hour_reg_water_electrolyzer_demand * reg_water_price
    hour_pure_water_cost = hour_pure_water_electrolyzer_demand * pure_water_price
    transport_costs = water_transport_price * (water_distance / 100) * hour_reg_water_electrolyzer_demand

    hour_water_costs = hour_reg_water_cost + hour_pure_water_cost + transport_costs

    water_annual_opex = hour_water_costs * 8760

    return water_annual_opex


def structure_gen_params(phase_3_data):
    solar_plants_names = list()
    wind_plants_names = list()
    hydro_plants_names = list()

    solar_cap_list = list()
    wind_cap_list = list()
    hydro_cap_list = list()

    solar_coordinates_list = list()
    wind_coordinates_list = list()
    hydro_coordinates_list = list()

    solar_plants_ages_list = list()
    wind_plants_ages_list = list()
    hydro_plants_ages_list = list()

    close_to_electrolyzer_bool_list_solar = list()
    close_to_electrolyzer_bool_list_wind = list()
    close_to_electrolyzer_bool_list_hydro = list()

    degradation_rate_solar_list = list()
    degradation_rate_wind_list = list()
    degradation_rate_hydro_list = list()

    solar_teif_list = list()
    wind_teif_list = list()
    hydro_teif_list = list()

    solar_curtailment_list = list()
    wind_curtailment_list = list()
    hydro_curtailment_list = list()

    solar_ip_list = list()
    wind_ip_list = list()
    hydro_ip_list = list()

    solar_mw_capex_list = list()
    wind_mw_capex_list = list()
    hydro_mw_capex_list = list()

    solar_opex_list = list()
    wind_opex_list = list()
    hydro_opex_list = list()

    solar_tustg_list = list()
    wind_tustg_list = list()
    hydro_tustg_list = list()

    solar_dep_rate_list = list()
    wind_dep_rate_list = list()
    hydro_dep_rate_list = list()

    solar_fixed_cap_factor_list = list()
    wind_fixed_cap_factor_list = list()
    hydro_fixed_cap_factor_list = list()

    plant_reservoir_cap_list = list()

    bool_dict = {0: False, 1: True}

    for generator_data in phase_3_data:
        plant_tech = generator_data['plant_tech']  # OK
        plant_name = generator_data['plant_name']  # OK
        plant_coordinate = (float(generator_data['latitude']), float(generator_data['longitude']))  # OK
        plant_cap = float(generator_data['cap'])  # OK
        plant_reservoir_cap = float(generator_data['reservoir_cap'])  # OK
        plant_fix_cap_factor = bool_dict.get(generator_data['fix_cap_factor'])  # OK
        plant_teip = float(generator_data['teip']) / 100  # OK
        plant_teif = float(generator_data['teif']) / 100  # OK
        plant_curtailment = float(generator_data['curtailment']) / 100  # OK
        plant_degradation_rate = float(generator_data['degradation_rate']) / 100  # OK
        plant_dep_rate = float(generator_data['dep_rate']) / 100  # OK
        plant_capex = float(generator_data['capex']) / plant_cap  # US
        plant_opex = (float(generator_data['opex']) / plant_cap) / 1000  # US
        plant_tustg = float(generator_data['tustg'])  # OK
        plant_close_to = bool_dict.get(generator_data['close_to'])  # OK
        plant_age = int(generator_data['age'])  # OK

        # print('\n')
        # print(plant_tech, type(plant_tech))
        # print(plant_name, type(plant_name))
        # print(plant_coordinate, type(plant_coordinate[0]))
        # print(plant_cap, type(plant_cap))
        # print(plant_reservoir_cap, type(plant_reservoir_cap))
        # print(plant_fix_cap_factor, type(plant_fix_cap_factor))
        # print(plant_teip, type(plant_teip))
        # print(plant_teif, type(plant_teif))
        # print(plant_curtailment, type(plant_curtailment))
        # print(plant_degradation_rate, type(plant_degradation_rate))
        # print(plant_dep_rate, type(plant_dep_rate))
        # print(plant_capex, type(plant_capex))
        # print(plant_opex, type(plant_opex))
        # print(plant_tustg, type(plant_tustg))
        # print(plant_close_to, type(plant_close_to))
        # print(plant_age, type(plant_age))
        # print('\n')

        if plant_tech == 'FV':
            solar_plants_names.append(plant_name)
            solar_cap_list.append(plant_cap)
            solar_coordinates_list.append(plant_coordinate)
            solar_plants_ages_list.append(plant_age)
            close_to_electrolyzer_bool_list_solar.append(plant_close_to)
            degradation_rate_solar_list.append(plant_degradation_rate)
            solar_teif_list.append(plant_teif)
            solar_ip_list.append(plant_teip)
            solar_mw_capex_list.append(plant_capex)
            solar_opex_list.append(plant_opex)
            solar_tustg_list.append(plant_tustg)
            solar_dep_rate_list.append(plant_dep_rate)
            solar_fixed_cap_factor_list.append(plant_fix_cap_factor)
            solar_curtailment_list.append(plant_curtailment)

        elif plant_tech == 'Eólica':
            wind_plants_names.append(plant_name)
            wind_cap_list.append(plant_cap)
            wind_coordinates_list.append(plant_coordinate)
            wind_plants_ages_list.append(plant_age)
            close_to_electrolyzer_bool_list_wind.append(plant_close_to)
            degradation_rate_wind_list.append(plant_degradation_rate)
            wind_teif_list.append(plant_teif)
            wind_ip_list.append(plant_teip)
            wind_mw_capex_list.append(plant_capex)
            wind_opex_list.append(plant_opex)
            wind_tustg_list.append(plant_tustg)
            wind_dep_rate_list.append(plant_dep_rate)
            wind_fixed_cap_factor_list.append(plant_fix_cap_factor)
            wind_curtailment_list.append(plant_curtailment)

        else:
            hydro_plants_names.append(plant_name)
            hydro_cap_list.append(plant_cap)
            hydro_coordinates_list.append(plant_coordinate)
            hydro_plants_ages_list.append(plant_age)
            close_to_electrolyzer_bool_list_hydro.append(plant_close_to)
            degradation_rate_hydro_list.append(plant_degradation_rate)
            hydro_teif_list.append(plant_teif)
            hydro_ip_list.append(plant_teip)
            hydro_mw_capex_list.append(plant_capex)
            hydro_opex_list.append(plant_opex)
            hydro_tustg_list.append(plant_tustg)
            hydro_dep_rate_list.append(plant_dep_rate)
            hydro_fixed_cap_factor_list.append(plant_fix_cap_factor)
            plant_reservoir_cap_list.append(plant_reservoir_cap)
            hydro_curtailment_list.append(plant_curtailment)

    return [solar_plants_names, wind_plants_names, hydro_plants_names, solar_cap_list,
            wind_cap_list, hydro_cap_list, solar_coordinates_list, wind_coordinates_list,
            hydro_coordinates_list, solar_plants_ages_list, wind_plants_ages_list, hydro_plants_ages_list,
            close_to_electrolyzer_bool_list_solar, close_to_electrolyzer_bool_list_wind,
            close_to_electrolyzer_bool_list_hydro, degradation_rate_solar_list,
            degradation_rate_wind_list, degradation_rate_hydro_list, solar_teif_list, wind_teif_list,
            hydro_teif_list, solar_curtailment_list, wind_curtailment_list, hydro_curtailment_list,
            solar_ip_list, wind_ip_list, hydro_ip_list, solar_mw_capex_list,
            wind_mw_capex_list, hydro_mw_capex_list, solar_opex_list, wind_opex_list, hydro_opex_list,
            solar_tustg_list, wind_tustg_list, hydro_tustg_list, solar_dep_rate_list, wind_dep_rate_list,
            hydro_dep_rate_list, solar_fixed_cap_factor_list, wind_fixed_cap_factor_list,
            hydro_fixed_cap_factor_list, plant_reservoir_cap_list]
##AQUI
def open_loader():
    root = tk.Tk()
    loader = LoaderApp(root)
    root.mainloop()

def enviar_formulario(self):

    open_loader()
##ATE AQUI

    cert_types = {"energia_fornecida": 1, "hidrgenio_produzido": 0}
    cert_type = cert_types.get(self.certif_var.get())
    cert_types_det = {"24 7 CFE (Carbon Free Energy)": 1, "RED - Renewable Energy Directive": 1,
                      "Low Carbon Hydrogen Standart": 2,
                      "CHPS - Clean Hydrogen Production Standart": 3, "Outro": 4}
    cert_type_det = cert_types_det.get(self.op_certfic_var.get())
    eebms = {"Mensal": "Month", "Semanal": "Week", "Horária": "Hour", "A cada 30 min": "Hour"}
    eebm = eebms.get(self.menu_balanco_energia.get())
    bidding_zone_limits = {"SIN": 0, "Subsistema": 1, "Distância (Informar valor)": -1}
    bidding_zone_limit = self.menu_limite_bidding_zone.get()
    eams = {"Mensal": "Month", "Semanal": "Week", "Horária": "Hour", "A cada 30 min": "30_min"}
    eam = eams.get(self.periodicidade_checagens_menu.get())
    emissions_fronts = {"Até a produção": False, "Até a entrega": True}
    emissions_front_delivery = emissions_fronts.get(self.menu_fronteira_analise.get())
    emission_factors_crits = {"Somente combustão": False, "Combustão + Upstream": True}
    full_chain = emission_factors_crits.get(self.menu_criterio_fator_emissão_hidrogenio.get())
    renewability_approval_period = self.periodo_validade_aprovacao.get()

    def coletar_dados_etapa3():
        dados_etapa3 = []
        for i in range(20):
            if (self.selecionar_entries[i].get() == "1"):
                dados_linha = {
                    "plant_name": self.nome_usina_entries[i].get(),
                    "plant_tech": self.fonte_energia_entries[i].get(),
                    "latitude": self.lat_entries[i].get(),
                    "longitude": self.long_entries[i].get(),
                    "cap": self.potencia_entries[i].get(),
                    "reservoir_cap": self.capacidade_reservatorio_entries[i].get(),
                    "fix_cap_factor": self.aumentar_fator_entries[i].get(),
                    "teip": self.ip_paradas_prog_entries[i].get(),
                    "teif": self.ip_paradas_nao_prog_entries[i].get(),
                    "curtailment": self.tx_risco_curtailment_entries[i].get(),
                    "degradation_rate": self.tx_degradacao_entries[i].get(),
                    "dep_rate": self.tx_depreciacao_contabil_entries[i].get(),
                    "capex": self.capex_fontes_entries[i].get(),
                    "opex": self.opex_fontes_entries[i].get(),
                    "tustg": self.pagamento_tustg_entries[i].get(),
                    "close_to": self.geracao_local_entries[i].get(),
                    "age": self.idade_usina_entries[i].get(),
                    "proj_preco_custo": self.proj_preco_custo_entries[i].get(),
                    "prev_geracao": self.prev_geracao_entries[i].get(),
                    "custo_preco_energia": self.custo_preco_energia_entries[i].get()
                }
                dados_etapa3.append(dados_linha)

        return dados_etapa3

    max_distance_locality_form = self.limite_bidding_zone_distancia.get()
    if max_distance_locality_form == '':
        max_distance_locality_form = 0

    form = {
        # ETAPA1
        "cert_type": cert_type,
        "cert_type_det": cert_type_det,
        "min_renewable_part_24_7": self.part_minima.get(),
        "allowed_grid_carbon_intensity": float(self.limite_intensidade.get()),  # OK
        "min_renewability": float(self.limite_particiapacao.get()) / 100,  # OK
        "eebm": eebm,  # OK
        "bidding_zone_limit": bidding_zone_limit,  # OK
        "max_distance_locality": max_distance_locality_form,  # OK
        "plants_max_age": float(self.limite_adicionalidade.get()),  # OK
        "cert_emissions_limit": float(self.limite_emissoes_cadeira_producao.get()),  # OK
        "eam": eebm,  # OK
        "emissions_front_delivery": emissions_front_delivery,  # OK
        "emissions_imat": self.imaterialidade.get(),  # IN
        "full_chain": full_chain,  # OK
        "renewability_approval_period": int(renewability_approval_period),  # OK
        "cert_pressure": self.padrao_pressao_hidrogenio.get(),  # IN
        "purity_level": self.padrao_pureza.get(),  # IN
        # Abaixo somente as variáveis da tela
        "criterioA_intensidade_carbono": self.criterioA_intensidade_carbono.get(),  # OK
        "criterioA_participacao_minima": self.criterioA_part_minima.get(),  # OK
        "criterioA_contratacao_planta_temporal": self.criterioA_contratacao_planta_temporal.get(),  # OK
        "criterioA_contratacao_planta_espacial": self.criterioA_contratacao_planta_espacial.get(),  # OK
        "criterioA_contratacao_planta_adicionalidade": self.criterioA_contratacao_planta_adicionalidade.get(),  # OK
        "criterioB_intensidade_carbono": self.criterioB_intensidade_carbono.get(),  # OK
        "criterioB_participacao_minima": self.criterioB_part_minima.get(),  # OK
        "criterioB_contratacao_planta_temporal": self.criterioB_contratacao_planta_temporal.get(),  # OK
        "criterioB_contratacao_planta_espacial": self.criterioB_contratacao_planta_espacial.get(),  # OK
        "criterioB_contratacao_planta_adicionalidade": self.criterioB_contratacao_planta_adicionalidade.get(),  # OK
        "criterioC_intensidade_carbono": self.criterioC_intensidade_carbono.get(),  # OK
        "criterioC_participacao_minima": self.criterioC_part_minima.get(),  # OK
        "criterioC_contratacao_planta_temporal": self.criterioC_contratacao_planta_temporal.get(),  # OK
        "criterioC_contratacao_planta_espacial": self.criterioC_contratacao_planta_espacial.get(),  # OK
        "criterioC_contratacao_planta_adicionalidade": self.criterioC_contratacao_planta_adicionalidade.get(),  # OK
        "criterioD_intensidade_carbono": self.criterioD_intensidade_carbono.get(),  # OK
        "criterioD_participacao_minima": self.criterioD_part_minima.get(),  # OK
        "criterioD_contratacao_planta_temporal": self.criterioD_contratacao_planta_temporal.get(),  # OK
        "criterioD_contratacao_planta_espacial": self.criterioD_contratacao_planta_espacial.get(),  # OK
        "criterioD_contratacao_planta_adicionalidade": self.criterioD_contratacao_planta_adicionalidade.get(),  # OK
        "criterioE_intensidade_carbono": self.criterioE_intensidade_carbono.get(),  # OK
        "criterioE_participacao_minima": self.criterioE_part_minima.get(),  # OK
        "criterioE_contratacao_planta_temporal": self.criterioE_contratacao_planta_temporal.get(),  # OK
        "criterioE_contratacao_planta_espacial": self.criterioE_contratacao_planta_espacial.get(),  # OK
        "criterioE_contratacao_planta_adicionalidade": self.criterioE_contratacao_planta_adicionalidade.get(),  # OK
        "criterioF_intensidade_carbono": self.criterioF_intensidade_carbono.get(),  # OK
        "criterioF_participacao_minima": self.criterioF_part_minima.get(),  # OK
        "criterioF_contratacao_planta_temporal": self.criterioF_contratacao_planta_temporal.get(),  # OK
        "criterioF_contratacao_planta_espacial": self.criterioF_contratacao_planta_espacial.get(),  # OK
        "criterioF_contratacao_planta_adicionalidade": self.criterioF_contratacao_planta_adicionalidade.get(),  # OK
        # ETAPA2
        "h2_periodic_demand": float(self.demandaH2.get()),  # OK
        "demand_hours": int(self.periodicidade_demanda.get()),  # OK
        "electrolyzer_latitude": float(self.latitude_entry.get()),  # US OK
        "electrolyzer_longitude": float(self.longitude_entry.get()),  # US OK
        "tustc_p": float(self.valor_tust_ponta.get()),  # OK
        "tustc_op": float(self.valor_tust_fora_ponta.get()),  # OK
        "electrolyzer_technology": (self.tecnologia_var.get()).upper,  # OK
        "scale_of_operation": float(self.tamanho_eletrolisador.get()),  # OK
        "compressor_pin": float(self.pressao_saida_eletrolisador.get()),  # OK
        "electrolyzer_mw_capex": float(self.capex_eletrolisador.get()) * 1000,  # OK
        "electrolyzer_opex_percentage": float(self.custos_om.get()) / 100,  # US OK
        "number_of_years_before_stack_change": int(self.vida_util_stack.get()),  # OK
        "stack_substitution_cost": float(self.custo_substituicao_stack.get()) * 1000,  # US OK
        "consumo_energetico_purificaco_h2": self.consumo_energetico_purificaco_h2.get(),  # IN
        "electrolyzer_degradation_rate": float(self.taxa_degradacao_eletrolisador.get()) / 100,  # OK
        "dep_rate_electrolyzer": float(self.taxa_depreciacao_eletrolisador.get()) / 100,  # OK
        "ref_compressor_capex": float(self.capex_compressor.get()),  # US OK
        "ref_compressor_cap": float(self.potencia_compressor.get()),  # US OK
        "fator_escala_compressor": self.fator_escala_compressor.get(),  # IN
        "compressor_om": float(self.custos_om_compressor.get()),  # US OK
        "compressor_efficiency": float(self.eficiencia_compressor.get()) / 100,  # OK
        "compressor_compressibility_factor": float(self.fator_compressibilidade.get()),  # OK
        "compressor_gas_constant": float(self.constante_gases.get()),  # OK
        "compressor_entry_temp": float(self.temperatura_entrada.get()),  # OK
        "compressor_number_of_stages": float(self.numero_estagios_compressao.get()),  # OK
        "compressor_isentropic_eff": float(self.eficiencia_compressao.get()),  # OK
        "compressor_heat_ratio": float(self.razao_calores.get()),  # OK
        # ETAPA3
        "Etapa3": coletar_dados_etapa3(),  # OK
        # ETAPA4
        "batteries_usage": self.baterias_var.get(),  # US OK
        "tecnologia_baterias": self.tecbaterias_var.get(),  # OK
        "batteries_mw_capex": float(self.capex_bateria.get()) * 1000,  # OK
        "batteries_opex": float(self.custos_om_bateria.get()),  # OK
        "custos_substituicao_baterias": self.custos_substituicao_baterias.get(),  # IN
        "capacidade_baterias": self.capacidade_baterias.get(),  # IN
        "discharge_capacity_batteries": float(self.capacidade_descarregamento.get()),  # OK
        "charge_capacity_batteries": float(self.capacidade_carregamento.get()),  # OK
        "batteries_charge_efficiency": float(self.eficiencia_carga_bateria.get()) / 100,  # OK
        "batteries_discharge_efficiency": float(self.eficiencia_descarga_bateria.get()) / 100,  # OK
        "ciclos": self.ciclos.get(),  # IN
        "dep_rate_batteries": float(self.taxa_depreciacao_contabil_bateria.get()) / 100,  # OK
        # ETAPA5
        "number_of_years": int(self.horizonteprojeto.get()),  # OK
        "equity_part": float(self.partcaptaproprio.get()) / 100,  # OK
        "equity_cost": float(self.custocapitalproprio.get()) / 100,  # OK
        "amortization_type": self.tipoamortizacao_var.get(),  # OK
        "financing_period": int(self.periodofuncionamento.get()),  # OK
        "interest_rate": float(self.txjurosreal.get()) / 100,  # OK
        "grace_period": int(self.periodocarencia.get()),  # OK
        "managing_opex": float(self.custosprojeto.get()),  # OK
        "pis_cofins_rate": float(self.pisconfins.get()) / 100,  # OK
        "icms_rate": float(self.icms.get()) / 100,  # OK
        "income_tax_and_cssl_rate": float(self.impostorenda.get()) / 100,  # OK
        "venda_oxigenio": self.vendaoxigenio_var.get(),  # IN
        "taxa_producao_oxigenio": self.taxaprodoxigenio.get(),  # IN
        "preco_venda_oxigenio": self.precovendaoxigenio.get(),  # IN
        "taxa_aumento_preco_oxigenio": self.taxaaumentooxigenio.get(),  # IN
        "pure_water_electrolyzer_demand": float(self.demandaagua.get()),  # US OK
        "reg_water_electrolyzer_demand": float(self.demandaaguaeletro.get()),  # US OK
        "pure_water_price": float(self.precoaguapura.get()),  # US OK
        "reg_water_price": float(self.precoaguaproc.get()),  # US OK
        "water_transport_price": float(self.precotranspagua.get()),  # US OK
        "water_distance": float(self.disteletrolisadorfonte.get()),  # US OK
        "taxa_aumento_anual_custos_agua": self.taxaaumentoanual.get(),  # IN
        "precificacao_carbono": self.precificacaocarbono.get(),  # IN
        "aumento_preco_carbono": self.aumentoprecocarbono.get(),  # IN
        "valor_referencia_emissoes_producao_reforma_vapor": self.valoremissoesprod.get(),  # IN
        "price_of_energy_bought_acl": float(self.precoaquisicaoenergia.get()),  # OK
        "possibilidade_venda_excedente_energia_rede": self.possibilidadevendaexcedente_var.get(),  # US
        "pld_spot": float(self.precovendaenergia.get()),  # OK
        "grid_additional_costs": float(self.custorelativonovaslinhas.get()),  # OK
        "grid_carbon_emission_file_path": self.fator_emissao_var.get(),  # US OK
        "grid_renewables_part_list_file_path": self.proj_esperada_var.get(),  # US OK
    }

    for key, value in form.items():
        print(f"{key}: {type(value)}, {value}")

    # json_string = json.dumps(form, indent=2)
    # print(json_string)
    nome = "form.json"

    # with open(nome, 'w') as arquivo:
    #     json.dump(form, arquivo, indent=2)

    print("Dados salvos como", nome)

    certification_entries_data = transform_cert_data(form)

    print(certification_entries_data)

    structured_data = structure_gen_params(form['Etapa3'])

    solar_plants_names = structured_data[0]
    wind_plants_names = structured_data[1]
    hydro_plants_names = structured_data[2]

    solar_cap_list = structured_data[3]
    wind_cap_list = structured_data[4]
    hydro_cap_list = structured_data[5]

    solar_coordinates_list = structured_data[6]
    wind_coordinates_list = structured_data[7]
    hydro_coordinates_list = structured_data[8]

    solar_plants_ages_list = structured_data[9]
    wind_plants_ages_list = structured_data[10]
    hydro_plants_ages_list = structured_data[11]

    close_to_electrolyzer_bool_list_solar = structured_data[12]
    close_to_electrolyzer_bool_list_wind = structured_data[13]
    close_to_electrolyzer_bool_list_hydro = structured_data[14]

    degradation_rate_solar_list = structured_data[15]
    degradation_rate_wind_list = structured_data[16]
    degradation_rate_hydro_list = structured_data[17]

    solar_teif_list = structured_data[18]
    wind_teif_list = structured_data[19]
    hydro_teif_list = structured_data[20]

    solar_curtailment_list = structured_data[21]
    wind_curtailment_list = structured_data[22]
    hydro_curtailment_list = structured_data[23]

    solar_ip_list = structured_data[24]
    wind_ip_list = structured_data[25]
    hydro_ip_list = structured_data[26]

    solar_mw_capex_list = structured_data[27]
    wind_mw_capex_list = structured_data[28]
    hydro_mw_capex_list = structured_data[29]

    solar_opex_list = structured_data[30]
    wind_opex_list = structured_data[31]
    hydro_opex_list = structured_data[32]

    solar_tustg_list = structured_data[33]
    wind_tustg_list = structured_data[34]
    hydro_tustg_list = structured_data[35]

    solar_dep_rate_list = structured_data[36]
    wind_dep_rate_list = structured_data[37]
    hydro_dep_rate_list = structured_data[38]

    solar_fixed_cap_factor_list = structured_data[39]
    wind_fixed_cap_factor_list = structured_data[40]
    hydro_fixed_cap_factor_list = structured_data[41]

    plant_reservoir_cap_list = structured_data[42]

    first_year = datetime.now().year

    number_of_years = form['number_of_years']
    h2_periodic_demand = form['h2_periodic_demand']
    demand_hours = form['demand_hours']
    electrolyzer_coordinate = (form['electrolyzer_latitude'], form['electrolyzer_longitude'])
    dep_rate_electrolyzer = form['dep_rate_electrolyzer']
    electrolyzer_technology = form['electrolyzer_technology']
    scale_of_operation = form['scale_of_operation']
    electrolyzer_degradation_rate = form['electrolyzer_degradation_rate']
    number_of_years_before_stack_change = form['number_of_years_before_stack_change']
    stack_substitution_cost_percentage = form['stack_substitution_cost'] / form['electrolyzer_mw_capex']
    electrolyzer_mw_capex = form['electrolyzer_mw_capex']
    grid_additional_costs = form['grid_additional_costs']
    electrolyzer_opex = (form['electrolyzer_opex_percentage'] * electrolyzer_mw_capex) / 1000
    water_annual_opex = retrieve_water_annual_opex(form['reg_water_electrolyzer_demand'],
                                                   form['pure_water_electrolyzer_demand'],
                                                   form['reg_water_price'], form['pure_water_price'],
                                                   form['water_transport_price'], form['water_distance'],
                                                   h2_periodic_demand / demand_hours)
    managing_opex = form['managing_opex']
    purity_level = form['purity_level']
    exit_pressure = form['cert_pressure']
    purifier_consumptions_params = None
    infrastructure_capex = 0
    dep_rate_infrastructure = 0.1
    compressor_mw_capex = (form['ref_compressor_capex'] / form['ref_compressor_cap']) / 1000
    compressor_opex = (form['compressor_om'] * compressor_mw_capex) / 1000
    compressor_pin = form['compressor_pin']
    compressor_pout = 10
    dep_rate_compressor = 0.1
    compressor_efficiency = form['compressor_efficiency']
    compressor_compressibility_factor = form['compressor_compressibility_factor']
    compressor_gas_constant = form['compressor_gas_constant']
    compressor_entry_temp = form['compressor_entry_temp']
    compressor_number_of_stages = form['compressor_number_of_stages']
    compressor_isentropic_eff = form['compressor_isentropic_eff']
    compressor_heat_ratio = form['compressor_heat_ratio']
    batteries_usage_bool_dict = {'sim': True, 'não': False}
    batteries_usage = batteries_usage_bool_dict.get(form['batteries_usage'])
    batteries_mw_capex = form['batteries_mw_capex']
    batteries_opex = form['batteries_opex']
    charge_capacity_batteries = form['charge_capacity_batteries']
    discharge_capacity_batteries = form['discharge_capacity_batteries']
    batteries_charge_efficiency = form['batteries_charge_efficiency']
    batteries_discharge_efficiency = form['batteries_discharge_efficiency']
    dep_rate_batteries = form['dep_rate_batteries']
    equity_part = form['equity_part']
    equity_cost = form['equity_cost']
    amortization_type = form['amortization_type']
    financing_period = form['financing_period']
    interest_rate = form['interest_rate']
    grace_period = form['grace_period']
    price_of_energy_bought_acl = form['price_of_energy_bought_acl']
    pld_spot = form['pld_spot']
    pis_cofins_rate = form['pis_cofins_rate']
    icms_rate = form['icms_rate']
    income_tax_and_cssl_rate = form['income_tax_and_cssl_rate']
    tustc_p = form['tustc_p']
    tustc_op = form['tustc_op']
    grid_allowed_bool = True
    consider_upstream_emissions = True
    grid_carbon_emission_file_path = form['grid_carbon_emission_file_path']
    grid_carbon_emission_factor_list = retrieve_annual_ts_data_from_xlsx(grid_carbon_emission_file_path,
                                                                         number_of_years)
    allowed_grid_carbon_intensity = form['allowed_grid_carbon_intensity']
    min_renewability = form['min_renewability']
    grid_renewables_part_list_file_path = form['grid_renewables_part_list_file_path']
    grid_renewables_part_list = retrieve_annual_ts_data_from_xlsx(grid_renewables_part_list_file_path,
                                                                  number_of_years)
    max_distance_locality = form['max_distance_locality']
    plants_max_age = form['plants_max_age']

    # run_main_simulation(first_year, number_of_years, solar_plants_names, wind_plants_names, hydro_plants_names,
    #                     solar_cap_list, wind_cap_list, hydro_cap_list, solar_coordinates_list, wind_coordinates_list,
    #                     hydro_coordinates_list, solar_plants_ages_list, wind_plants_ages_list, hydro_plants_ages_list,
    #                     close_to_electrolyzer_bool_list_solar, close_to_electrolyzer_bool_list_wind,
    #                     close_to_electrolyzer_bool_list_hydro, degradation_rate_solar_list,
    #                     degradation_rate_wind_list, degradation_rate_hydro_list, solar_teif_list, wind_teif_list,
    #                     hydro_teif_list, solar_ip_list, wind_ip_list, hydro_ip_list, solar_mw_capex_list,
    #                     wind_mw_capex_list, hydro_mw_capex_list, solar_opex_list, wind_opex_list, hydro_opex_list,
    #                     solar_tustg_list, wind_tustg_list, hydro_tustg_list, solar_dep_rate_list, wind_dep_rate_list,
    #                     hydro_dep_rate_list, solar_fixed_cap_factor_list, wind_fixed_cap_factor_list,
    #                     hydro_fixed_cap_factor_list, plant_reservoir_cap_list, h2_periodic_demand,
    #                     demand_hours, electrolyzer_coordinate, dep_rate_electrolyzer, electrolyzer_technology,
    #                     scale_of_operation, electrolyzer_degradation_rate, number_of_years_before_stack_change,
    #                     stack_substitution_cost_percentage, electrolyzer_mw_capex, grid_additional_costs,
    #                     electrolyzer_opex, water_annual_opex, managing_opex, purity_level, exit_pressure,
    #                     purifier_consumptions_params, infrastructure_capex, dep_rate_infrastructure,
    #                     compressor_mw_capex, compressor_opex, compressor_pin, compressor_pout, dep_rate_compressor,
    #                     compressor_efficiency, compressor_compressibility_factor, compressor_gas_constant,
    #                     compressor_entry_temp, compressor_number_of_stages, compressor_isentropic_eff,
    #                     compressor_heat_ratio, batteries_usage, batteries_mw_capex, batteries_opex,
    #                     charge_capacity_batteries, discharge_capacity_batteries, batteries_charge_efficiency,
    #                     batteries_discharge_efficiency, dep_rate_batteries, equity_part, equity_cost,
    #                     amortization_type, financing_period, interest_rate, grace_period, price_of_energy_bought_acl,
    #                     pld_spot, pis_cofins_rate, icms_rate, income_tax_and_cssl_rate, tustc_p, tustc_op,
    #                     eebm, eam, emissions_front_delivery, full_chain, grid_allowed_bool,
    #                     consider_upstream_emissions, certification_entries_data, grid_carbon_emission_factor_list,
    #                     allowed_grid_carbon_intensity, min_renewability, grid_renewables_part_list,
    #                     renewability_approval_period, bidding_zone_limit, max_distance_locality, plants_max_age)

    # messagebox.showinfo("Simulações concluídas", "Todas as simulações foram concluídas com sucesso.")

