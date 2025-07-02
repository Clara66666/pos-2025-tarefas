import json
import os

def mostrar_menu(imoveis):
    print("LISTA DE IMÓVEIS")
    for i, imovel in enumerate(imoveis):
        descricao = imovel.get('descricao', 'Sem descrição')
        print(f"{i} - {descricao}")
    

def mostrar_detalhes(imovel):
    print(" DETALHES DO IMÓVEL")
    for chave, valor in imovel.items():
        
        if isinstance(valor, dict):
            print(f"{chave.capitalize()}:")
            for subchave, subvalor in valor.items():
               
                if isinstance(subvalor, list):
                    print(f"  {subchave}:")
                    for item in subvalor:
                        print(f"    - {item}")
                else:
                    print(f"  {subchave}: {subvalor}")
       
        elif isinstance(valor, list):
            print(f"{chave.capitalize()}:")
            for item in valor:
                print(f"  - {item}")
        else:
            print(f"{chave.capitalize()}: {valor}")
   

def main():
    pasta = "parsers"
    json_path = os.path.join(pasta, "imobiliaria.json")

    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            imoveis = json.load(f)
    except FileNotFoundError:
        print(f"Arquivo {json_path} não encontrado. Execute primeiro o script que gera o JSON.")
        return

    while True:
        mostrar_menu(imoveis)
        escolha = input("Digite o ID do imóvel para ver detalhes (ou 'sair' para encerrar): ").strip()

        if escolha.lower() == 'sair':
            print("Programa encerrado. Até mais!")
            break

        if not escolha.isdigit():
            print("Por favor, digite um número válido ou 'sair'.")
            continue

        idx = int(escolha)

        if 0 <= idx < len(imoveis):
            mostrar_detalhes(imoveis[idx])
        else:
            print("ID inválido. Tente novamente.")

if __name__ == "__main__":
    main()
