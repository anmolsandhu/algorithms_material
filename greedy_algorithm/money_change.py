


coin_val = [1,5,10]

def min_coins(money):
	if money < 0:
		return 

	current_money = money

	flag = True
	coins = {10:0, 1:0, 5:0}

	while current_money > 0:

		if (current_money - 10) >= 0:
			current_money = current_money - 10
			coins[10] += 1
		elif (current_money - 5) >= 0:
			current_money = current_money - 5
			coins[5] += 1
		elif (current_money - 1) >= 0:
			current_money = current_money - 1
			coins[1] += 1

		# if current_money == 0:
		# 	flag = False

	return coins


print min_coins(997)
