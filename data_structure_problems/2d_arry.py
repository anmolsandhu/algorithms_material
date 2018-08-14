

def get_stocks_profit(stocks):

	least = 0
	max_stocks = 0
	for i in range(len(stocks) - 1):
		current_max = 0
		diff_current = 0
		# if stocks[i] < stocks[i+1]:
		# 	diff_current = stocks[i + 1] - stocks[i]
		print "least = ", stocks[least]
		
		diff_old = stocks[i] - stocks[least]
		print stocks[i], "  ", stocks[i + 1]
		print "current diff  =  ", diff_current, " old diff = ", diff_old, "  new least = ", least  
		if diff_current > diff_old:
			current_max = diff_current
		else:
			current_max = diff_old

		if current_max > max_stocks:
			max_stocks = current_max

		if stocks[least] > stocks[i]:
			least = i
		print max_stocks
	return max_stocks

def mod__stocks(prices):

		
	stocks = prices
	least = 0
	max_stocks = 0
	for i in range(len(stocks)):
		current_max = 0
		
		diff_old = stocks[i] - stocks[least]
		
		if stocks[least] > stocks[i]:
			least = i
		
		if diff_old > max_stocks:
			max_stocks = diff_old
				
	return max_stocks




a = [7,1,5,7]
print a
print get_stocks_profit(a)
print mod__stocks(a)

			
		
		
