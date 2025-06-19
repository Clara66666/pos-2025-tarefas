from xml.dom.minidom import parse

def carregar_cardapio(arquivo):
    doc = parse(arquivo)
    pratos = doc.getElementsByTagName("prato")
    
    cardapio = {}
    for prato in pratos:
        id_prato = prato.getAttribute("id")
        nome = prato.getElementsByTagName("nome")[0].firstChild.data
        
        
        descricao = prato.getElementsByTagName("descricao")[0].firstChild.data
        
        ingredientes = prato.getElementsByTagName("ingrediente")
        lista_ingredientes = [ing.firstChild.data for ing in ingredientes]
        
        preco = prato.getElementsByTagName("preco")[0].firstChild.data
        calorias = prato.getElementsByTagName("calorias")[0].firstChild.data
        tempo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.data
        
        
        cardapio[id_prato] = {
            "nome": nome,
            "descricao": descricao,
            "ingredientes": lista_ingredientes,
            "preco": preco,
            "calorias": calorias,
            "tempoPreparo": tempo
        }
    return cardapio

def mostrar_menu(cardapio):
    print("===== MENU =====")
    for id_prato, dados in cardapio.items():
        print(f"{id_prato} - {dados['nome']}")
    print("================")

def mostrar_detalhes(cardapio, id_prato):
    if id_prato in cardapio:
        dados = cardapio[id_prato]
        print(f"Nome: {dados['nome']}")
        print(f"Descrição: {dados['descricao']}")
        print(f"Ingredientes: {', '.join(dados['ingredientes'])}")
        print(f"Preço: {dados['preco']}")
        print(f"Calorias: {dados['calorias']}")
        print(f"Tempo de preparo: {dados['tempoPreparo']}")
    else:
        print("Prato não encontrado. Tente novamente.")

def main():
    arquivo_xml = "cardapio.xml" 
    cardapio = carregar_cardapio(arquivo_xml)
    
    while True:
        mostrar_menu(cardapio)
        escolha = input("Digite o ID do prato para ver detalhes (ou 'sair' para encerrar): ").strip()
        if escolha.lower() == "sair":
            print("Até mais!")
            break
        mostrar_detalhes(cardapio, escolha)
        print()

if __name__ == "__main__":
    main()
