def is_credit_card_valid(n):
	if n % 2 == 0:
		print("Failed")
		return False 
	return (sum([int(str(n)[el]) for el in range(0, len(str(n)), 2)]) + sum([sum([int(i) for i in str(2*int(str(n)[el]))]) for el in range(1, len(str(n)), 2)])) % 10  == 0

print(is_credit_card_valid(79927398713))
