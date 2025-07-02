import xml.etree.ElementTree as ET
import json
import os


pasta = "parsers"
xml_path = os.path.join(pasta, "imobiliaria.xml")
json_path = os.path.join(pasta, "imobiliaria.json")


def xml_para_dict(elemento):
    dicionario = {}
    for filho in elemento:
        
        if len(filho):
            valor = xml_para_dict(filho)
        else:
            valor = filho.text

        
        if filho.tag in dicionario:
            if isinstance(dicionario[filho.tag], list):
                dicionario[filho.tag].append(valor)
            else:
                dicionario[filho.tag] = [dicionario[filho.tag], valor]
        else:
            dicionario[filho.tag] = valor
    return dicionario


tree = ET.parse(xml_path)
root = tree.getroot()


lista_imoveis = []

for imovel in root.findall('imovel'):
    lista_imoveis.append(xml_para_dict(imovel))


with open(json_path, "w", encoding="utf-8") as f:
    json.dump(lista_imoveis, f, ensure_ascii=False, indent=4)

print("Arquivo JSON gerado com sucesso!")
