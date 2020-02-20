import datetime

def data(data_atual,data_desejada):
    dias = data_atual-data_desejada
    return dias

data_atual = datetime.date(year = 2020,month = 2,day = 20)
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))    
ano = int(input('Digite o ano: '))
data_desejada = datetime.date(ano,mes,dia)

quant_dias = data(data_atual,data_desejada)
print(quant_dias)