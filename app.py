import pandas as pd
import os, sys

sys.tracebacklimit = 0


renomeaNomesFamilias = [
        {"formento_qtd_fam_benef_indinegas_i" : "indigenas"},
        {"formento_qtd_fam_benef_quilombolas_i" : "quilombolas"},
        {"formento_qtd_fam_benef_ciganas_i" : "ciganas"},
        {"formento_qtd_fam_benef_comun_terreiro_i ":"terreiro"},
        {"formento_qtd_fam_benef_extrativistas_i":"extrativistas"},
        {"formento_qtd_fam_benef_pescadores_artesanais_i": "pescadores"},
        {"formento_qtd_fam_benef_ribeirinhas_i": "ribeirinhas"},
        {"formento_qtd_fam_benef_agrilcultores_familiares_i": "agricultores_familiares"},
        {"formento_qtd_fam_benef_assentados_ref_agraria_i": "assentados_ref_agr"},
        {"formento_qtd_fam_benef_acampados_rurais_i": "acampados_rurais"},
        {"formento_qtd_fam_benef_credito_fundiario_i": "credito_fundiario"},
        {"formento_qtd_fam_benef_atingidas_empr_infra_i": "atingidas_empr_infra"},
        {"formento_qtd_fam_benef_presos_sist_carcerario_i": "presos_sist_carcerario"},
        {"formento_qtd_fam_benef_catadores_material_reciclado_i": "catadores_reciclagem"},
        {"formento_qtd_total_familias_benef_":"total"}
        ]

def analisaDados(ano):
    df = pd.read_csv(f"dados/{ano}.csv")
    # soma = df['2']
    df = df.drop("codigo_ibge", axis=1)
    df = df.drop("anomes_s", axis=1)

    for i in renomeaNomesFamilias:
        df = df.rename(columns=i)

    df_total = df.sum()
    print(df_total)

    df_total.to_csv(f'resultado_analise/{ano}.csv')

if __name__ == "__main__":
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print("Relatório de Famílias atendidas pelo Programa Fomento Rural, por Grupo Populacional Tradicional e Específico (GPTE)")
        ano = input("\n[2012 - 2022] | Digite o ano que queira analisar: ")
        analisaDados(ano)
        input("Pressione qualquer tecla | Para sair digite ctrl+c")
        