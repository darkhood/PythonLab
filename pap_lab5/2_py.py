def deco_star(f):
	def inner(message):
		print("*****")
		f(message)
		print("*****")
	return inner
	
def deco_dollar(f):
	def inner(message):
		print("$$$$$")
		f(message)
		print("$$$$$")
	return inner	

'''print("Calling the print_message with stars")
print_message = deco_star(print_message)
print_message("hello")

print("Calling the print_message using dollars and start")
print_message = deco_dollar(deco_star(print_message))
print_message("hello")
'''

@deco_dollar
@deco_star
def print_message(message):
	print(message)
print_message("hello")
