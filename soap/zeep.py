from soap.zeep import Client

wsdl = 'http://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL'

client = Client(wsdl=wsdl)

numero = int(input("Digite um número inteiro: "))

resultado = client.service.NumberToWords(ubiNum=numero)

print("Número por extenso em inglês:", resultado)
