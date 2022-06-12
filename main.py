import requests

def bid():
    
    r = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    info_dolar = r.json()['USDBRL']
    return float(info_dolar['bid'])
    #Apenas retornará a cotação ATUAL!

print(bid())


def infos():
    
    r = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    info_dolar = r.json()['USDBRL']
    info = ''
    for i in info_dolar:
        
        if i == "create_date" or i == 'codein':
            continue
            
        info += f"\n{str(i).capitalize()}: {str(info_dolar[i])}"
    return info
    
    #Retornará principais informações

print(infos())
