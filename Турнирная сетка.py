import random

list = []
ammount = int(input("Введите число игроков"))
number = 0
while number < ammount:
	player = input("Введите имя игрока")
	list.append(player)
	number += 1

number = 0
table = []
while number < ammount:
	player = random.randint(0, ammount - 1)
	if list[player] not in table:
		player = list[player]
		table.append(player)
		number += 1

i = 0
n = 1

print("Первый тур")
while i < (len(table) - 1):
	print("" + str(n) + ". " + table[i] + " " +  table[i+1])
	i += 2
	n += 1
