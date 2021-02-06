from mapa2 import mapa

lista_fechada = []
atual = []
cidades = {}
cont = 1


def column(matrix, i):
    return [row[i] for row in matrix]


def isfunc(a, b):
  return not set(a).isdisjoint(b)


def expandir(city):
    global atual
    expansao = []

    for i in mapa: 
        if city[0] in i:
            expansao.append(i)

    print('expansao: ', expansao)
    filtro = []
    for i in expansao:
        for j in i[:-1]:
            if type(j) == str:
                if j != city[0]:
                    filtro.append([j, i[2], city[0]])

    print('filtro: ', filtro)
    for i in filtro:
        if i[0] in lista_fechada:
            filtro.remove(i)
    for i in filtro:
        if i[0] in lista_fechada:
            filtro.remove(i)
    print('refiltro: ', filtro)

    for i in filtro:
        c = cidades[city[0]]
        i[1] = i[1] + c[1]
    print('refiltro c/ soma: ', filtro)

    atual = atual + filtro
    print(atual)


def visita(city):
    global lista_fechada, atual, cidades
    print('Visitando: ', city[0])

    is_lista_f = False
    for i in lista_fechada:
        if i == city[0]:
            is_lista_f = True

    if is_lista_f == False:
        lista_fechada.append(city[0])

    existe_cidade = False
    for i in cidades:
        if city[0] == i:
            existe_cidade = True

    if not existe_cidade:
        cidades[city[0]] = [city[0], city[1], city[2]]

    for i in atual:
        if city[0] in i:
            atual.remove(i)


def isObjective(atual, objetivo):
    if atual[0] == objetivo[0]:
        return True
    else:
        return False


def procurar_pai(city):
    global cidades

    return cidades[city[2]]


def procurar_menor():
    global atual
    listtemp = []
    listtemp = column(atual, 1)
    a = min(listtemp)

    ref = ''
    pai = ''
    for i in atual:
        if i[1] == a:
            ref = i[0]
            pai = i[2]

    print(ref, a, pai)
    return [ref, a, pai]


def main(partida):
    global cont
    
    cidades[partida] = [partida, 0, None]
    cidade_inicial = cidades[partida]

    cidades['M'] = ['M', 0, None]
    cidade_final = cidades['M']

    cidade_atual = cidade_inicial
    while True:
        print('===========================')
        print(cont)
        cont = cont + 1
        visita(cidade_atual)
        print('Visitado')
        if not isObjective(cidade_atual, cidade_final):
            print('não é o objetivo')
            expandir(cidade_atual)
            print('expandido')
            proximo, a, pai = procurar_menor()
            cidade_atual = [proximo, a, pai]
            print('lf: ', lista_fechada)
            print('cidades: ', cidades)
        else:
            print('Break')
            break

    cidade_final = cidade_atual

    solucao = []
    solucao.append(cidade_final)

    pai = procurar_pai(cidade_final)
    print('pai: ', pai)
    if pai[2] is not None:
        solucao.append(pai)
        while procurar_pai(pai) != cidade_inicial:
            pai = procurar_pai(pai)
            solucao.append(pai)
        else:
            pai = procurar_pai(pai)
            solucao.append(pai)
    elif pai[2] is None:
        solucao.append(pai)

    solucao.reverse()
    print('\nSoluçao: ', solucao)
    print('Custo: ', cidade_final[1])

    return [solucao, cidade_final[1]]


if __name__ == '__main__':
    main('A')
