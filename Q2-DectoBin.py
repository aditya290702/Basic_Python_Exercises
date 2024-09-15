def DtoB(n):


	if (n >= 1):
		DtoB(n // 2)
		print (n % 2)
		

def main():
	n = 5
	x = DtoB(n)
	print (x)

if __name__=="__main__":
	main() 
