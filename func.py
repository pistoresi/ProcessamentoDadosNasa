from prettytable import PrettyTable


def groupby(lista): #agrupando os resultados devidos
    hd = {}
    for row in lista:
        if row not in hd:
            hd[row] = 0
        hd[row] += 1
    return hd

def GroupTable (t, t1, t2):
    A = PrettyTable([t,t1])
    for key, val in t2.items():
        A.add_row([key, val])
    return A

