from algoritmosDeBusca import *

m = 10 #Movimentos aleat�rios
n = 1 #Total de vezes

#Gerar de forma aleat�ria
'''
for j in range(1,m+1):
    temp = []
    for i in range(n):
        ans = busca(j)
        temp.append(ans)
        #print('Movimentos aleat�rios: {} Tempo: {}'.format(i,ans))
    media = ((sum(temp))/n)
    print('Movimentos aleat�rios: {} M�dia: {}'.format(j,media))

print('\nFim da execu��o')
'''

aux = busca(7)
print(aux)