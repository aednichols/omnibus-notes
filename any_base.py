#!/usr/bin/python

# I started solving the cryptopals.com challenges, and it slipped my mind in the first challenge that
# "base64 encoding" is not the same as converting to base 64. So, I ended up with this correct but so
# far useless converter between arbitrary bases, that I shall save for future use

domain = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/' # up to base-64

# 0xab = 10101011 = 1+2+8+32+128 = 171

def any_base( input, input_base, output_base):
	base10 = 0
	
	for (position, character) in enumerate(reversed(input)):
		base10 += (input_base ** position) * domain.index(character)

	output = ""

	while base10 > 0:
		multiplier = base10 / output_base
		remainder  = base10 % output_base
		
		output = domain[remainder] + output
		
		base10 = multiplier	

	return output


print any_base("1111", 2, 10)