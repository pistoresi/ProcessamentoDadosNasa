import re
from prettytable import PrettyTable
import func
import func as HD


table = []
listaHosts=[]
soma=0
contador = 0
list_host = []
lista_dia=[]
x=0

with open('access_log_Jul95', encoding="ISO-8859-1") as file_nasa: #lendo o documento
    for row in file_nasa:
        columns = re.findall(r"(^\S*)|\[(\d{2})|(\".*?\")|(\s\d*\d)", row) #regex
        if len(columns) == 1:
            pass
        elif len(columns) == 5: #percorrendo as colunas/linhas
            hosts = str("".join(x for x in columns[0])).strip()
            listaHosts.append(hosts)
            data = str("".join(x for x in columns[1])).strip()
            requi = str("".join(x for x in columns[2])).strip()
            status = str("".join(x for x in columns[3])).strip()
            byte = int("".join(x for x in columns[4]))
            soma = soma + byte #soma dos bytes do documento

        else: #continuar percorrendo independente do byte
            hosts = str("".join(x for x in columns[0])).strip()
            data = str("".join(x for x in columns[1])).strip()
            requi = str("".join(x for x in columns[2])).strip()
            status = str("".join(x for x in columns[3])).strip()
            byte=0
        table.append([hosts, data, requi, status, byte]) #tabela de colunas após leitura

for row in table: #for para percorrer e devolver os status 404 em hosts unicos e dias com o erro 404
    if row[3] == "404":
        contador += 1
        list_host.append(row[0])
        lista_dia.append(row[1])





print(f"Existem erros totais 404:", contador)
print('===================================================')
print("Quantidade de erros 404 por dia:\n", (HD.GroupTable("dias", "Qtd de erros",HD.groupby(lista_dia))))
print('===================================================')
print(f"Os 5 URLs que mais causaram erro 404:\n", HD.GroupTable("urls","+ causaram erros",{k: v for k, v in sorted(HD.groupby(list_host).items(), key=lambda item:item[1])[-5:]}))
print('===================================================')
print(f"Existem {len(dict.fromkeys(list_host))} hosts únicos")
print('===================================================')
print("A soma de bytes é:", soma)


