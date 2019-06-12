from algoritmosDeBusca import *

m = 10 #Movimentos aleatórios
n = 1 #Total de vezes

#Gerar de forma aleatória
'''
for j in range(1,m+1):
    temp = []
    for i in range(n):
        ans = busca(j)
        temp.append(ans)
        #print('Movimentos aleatórios: {} Tempo: {}'.format(i,ans))
    media = ((sum(temp))/n)
    print('Movimentos aleatórios: {} Média: {}'.format(j,media))

print('\nFim da execução')
'''

aux = busca(7)
print(aux)