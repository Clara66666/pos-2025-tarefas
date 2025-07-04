import json

def mostrar_menu(imoveis):
    print("\nLista de imóveis:")
    for i, imovel in enumerate(imoveis):
        print(f"{i} - {imovel.get('descricao', 'Sem descrição')}")

def mostrar_detalhes(imovel):
    print("\nDetalhes do imóvel:")
    print(f"Descrição: {imovel.get('descricao')}")

    proprietario = imovel.get('proprietario', {})
    nome = proprietario.get('nome', 'Não informado')
    email = proprietario.get('email', 'Não informado')
    telefones = proprietario.get('telefone')
    if isinstance(telefones, list):
        tel_str = ", ".join(telefones)
    else:
        tel_str = telefones or "Não informado"

    print(f"Proprietário: {nome}")
    print(f"E-mail: {email}")
    print(f"Telefones: {tel_str}")

    endereco = imovel.get('endereco', {})
    rua = endereco.get('rua', 'Desconhecida')
    numero = endereco.get('numero', 's/n')
    bairro = endereco.get('bairro', '')
    cidade = endereco.get('cidade', '')
    print(f"Endereço: {rua}, {numero}, {bairro} - {cidade}")

    caracteristicas = imovel.get('caracteristicas', {})
    tamanho = caracteristicas.get('tamanho', '?')
    quartos = caracteristicas.get('numQuartos', '?')
    banheiros = caracteristicas.get('numBanheiros', '?')
    print(f"Tamanho: {tamanho} m²")
    print(f"Quartos: {quartos}")
    print(f"Banheiros: {banheiros}")

    valor = imovel.get('valor', 'Não informado')
    print(f"Valor: R$ {valor}")
    print()

def main():
    try:
        with open("parsers/imobiliaria.json", "r", encoding="utf-8") as f:
            imoveis = json.load(f)
    except FileNotFoundError:
        print("Arquivo JSON não encontrado.")
        return

    while True:
        mostrar_menu(imoveis)
        escolha = input("\nDigite o ID do imóvel (ou 'sair' para encerrar): ").strip()

        if escolha.lower() == "sair":
            break
        if not escolha.isdigit():
            print("Por favor, digite um número válido.")
            continue

        idx = int(escolha)
        if 0 <= idx < len(imoveis):
            mostrar_detalhes(imoveis[idx])
        else:
            print("ID fora do intervalo.")

if __name__ == "__main__":
    main()

