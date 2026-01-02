import pandas as pd
import os
from datetime import datetime

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar_tela()
    print("=== Registro de Ações (Append Mode) ===")
    print("-" * 50)

    # 1. Entrada de Dados
    try:
        ticker = input("Qual o código da ação (ex: VALE3)? ").strip().upper()
        
        qtd_input = input("Quantas ações foram compradas? ")
        quantidade = int(qtd_input)
        
        total_input = input("Qual o valor TOTAL pago (ex: 2500.00)? ").replace(',', '.')
        total_pago = float(total_input)
        
    except ValueError:
        print("\n[ERRO] Valor inválido! Certifique-se de usar números para quantidade e valor.")
        return

    # 2. Cálculos
    preco_medio = total_pago / quantidade
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')

    # 3. Criação do DataFrame com a NOVA linha
    # Atenção: As colunas devem ter o mesmo nome das do arquivo Excel existente
    novo_dado = {
        'Data': [data_atual],
        'Ação': [ticker],
        'Quantidade': [quantidade],
        'Total Pago (R$)': [total_pago],
        'Preço Médio (R$)': [preco_medio]
    }
    df_novo = pd.DataFrame(novo_dado)

    # 4. Exibição na Tela
    print("\n--- Resumo do Lançamento ---")
    print(df_novo.to_string(index=False))
    print("-" * 50)

    # 5. Salvar no Excel (Lógica de Append)
    nome_arquivo = 'XXXX'

    try:
        if os.path.exists(nome_arquivo):
            # CENÁRIO A: Arquivo JÁ EXISTE
            # 1. Lê o arquivo atual
            df_existente = pd.read_excel(nome_arquivo)
            
            # 2. Junta (concatena) o antigo com o novo
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
            
            # 3. Salva tudo de volta no arquivo
            df_final.to_excel(nome_arquivo, index=False)
            print(f"\n[SUCESSO] Nova linha adicionada ao arquivo '{nome_arquivo}'.")
            
        else:
            # CENÁRIO B: Arquivo NÃO EXISTE (cria do zero)
            df_novo.to_excel(nome_arquivo, index=False)
            print(f"\n[SUCESSO] Arquivo '{nome_arquivo}' criado com o primeiro registro.")

    except PermissionError:
        print(f"\n[ERRO CRÍTICO] O arquivo '{nome_arquivo}' está aberto no Excel!")
        print("Por favor, feche o arquivo e tente novamente.")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro inesperado: {e}")

    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()