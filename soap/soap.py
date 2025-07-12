import requests
from xml.dom import minidom

URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"


def make_soap_request(function_name, body_content):
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": f"http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso/{function_name}"
    }
    body = f"""
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            {body_content}
        </soap:Body>
    </soap:Envelope>
    """
    response = requests.post(URL, data=body.strip(), headers=headers)
    return response.text



def get_currency_by_country_code(country_code):
    body_content = f"""
    <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
        <sCountryISOCode>{country_code}</sCountryISOCode>
    </CountryCurrency>
    """
    xml_response = make_soap_request("CountryCurrency", body_content)
    dom = minidom.parseString(xml_response)
    currency = dom.getElementsByTagName("m:sName")[0].firstChild.nodeValue
    print(f"Moeda de {country_code}: {currency}")

def get_country_name_by_iso_code(country_code):
    body_content = f"""
    <CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
        <sCountryISOCode>{country_code}</sCountryISOCode>
    </CountryName>
    """
    xml_response = make_soap_request("CountryName", body_content)
    dom = minidom.parseString(xml_response)
    name = dom.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue
    print(f"Nome do país {country_code}: {name}")

def get_capital_by_country_code(country_code):
    body_content = f"""
    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
        <sCountryISOCode>{country_code}</sCountryISOCode>
    </CapitalCity>
    """
    xml_response = make_soap_request("CapitalCity", body_content)
    dom = minidom.parseString(xml_response)
    capital = dom.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue
    print(f"Capital de {country_code}: {capital}")



def main():
    print("Escolha uma opção:")
    print("1 - Buscar moeda por código do país")
    print("2 - Buscar nome do país por código ISO")
    print("3 - Buscar capital por código do país")

    choice = input("Digite a opção desejada (1-3): ")
    country_code = input("Digite o código ISO do país (ex: BR, US, FR): ").upper()

    if choice == '1':
        get_currency_by_country_code(country_code)
    elif choice == '2':
        get_country_name_by_iso_code(country_code)
    elif choice == '3':
        get_capital_by_country_code(country_code)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
