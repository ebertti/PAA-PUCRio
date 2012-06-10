#-*- coding: utf-8 -*-

A, B, C, D, E, F, G, H, I, J, K, L, M = range(0, 13)

grafo = [
    [B, C, F], # A
    [A], # B
    [A, G], # C
    [F, E], # D
    [F, D, G], # E
    [A, E], # F
    [C, E, H, J, L], # G
    [G, I], # H
    [H], # I
    [G, L, M, K], # J
    [J], #K
    [G, J, M], #L
    [L, J] # m
]

visitado = []
separadores = []
articulacao = []
baixo = []
now = 0


def separador(v):
    separadores[v] += 1

def profundidade(v):
    global now
    now += 1
    visitado[v] = now
    minimo = now

    for w in grafo[v]:
        if not visitado[w]:
            profundidade(w)
            if baixo[w] >= visitado[v]:
                separador(v)
            if baixo[w] < minimo:
                minimo = baixo[w]
        else:
            minimo = min(minimo, visitado[w])
        baixo[v] = minimo

def caminhamento():
    #zerando
    for i in range(0, len(grafo)):
        visitado.append(0)
        separadores.append(0)
        baixo.append(0)

    for i in range(0, len(grafo)):
        if not visitado[i]:
            profundidade(i)

            if separadores[i] > 1:
                articulacao.append(i)
def main():
    caminhamento()
    print articulacao
    print visitado
    print separadores
    print baixo
    print now
if __name__ == '__main__':
    main()
  