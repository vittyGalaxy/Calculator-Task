import re

class MyParser():
	def __init__(self):
		pass

	def solve(self, expression):
		expression_array = re.findall(r'\(|\)|\d+|\+|\-|\*|\/', expression)
		return expression_array



def main():
	parser = MyParser()
	expression_1 = "51+23"
	print(parser.solve(expression_1))
	
	expression_2 = "(51+23)"
	print(parser.solve(expression_2))

if __name__ == '__main__':
 	main()
		