times = (
    'Heat', 'Celtics', 'Bucks', '76ers', 'Raptors', 'Bulls', 'Nets', 'Hawks', 'Cavaliers', 'Hornerts'
)
print("==--"*20)
print(f'Times da Conferência Leste- NBA:\n{times}')

num = input('Digite o nome de um time: ')
while num not in times:
    num = input('Digite um time corretamente!!!\n')

print("==--"*20)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print("==--"*20)
print(f'Os 4 últimos colocados: {times[-4:]}')
print("==--"*20)
print(f'Ordem alfabética dos times:\n{sorted(times)}')
print("==--"*20)
print(f'O time {num} está na posição: {times.index(num)+1}')