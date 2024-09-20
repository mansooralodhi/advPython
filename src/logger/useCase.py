from logger import Logger


class useCase(Logger):
    
	def add(self):
		self.fyiMessage = f"Adding not possible !"
		self.fyiMessage = f"Adding 000  not possible !"
      
	def multiply(self):
		self.fyiMessage = f"Multiplication not possible !"
		self.fyiMessage = f"Multiplication -1 not possible !"

	def divide(self):
		try:
			_  = 1 / 0
		except Exception as e:
			self.errorMessage = f"Division not possible,  {e}!"
		try:
			_  = b / 0.2
		except Exception as e:
			self.warningMessage = f"Division not possible,  {e}!"


if __name__ == "__main__":
	logger = useCase()
	logger.add()
	logger.divide()
	logger.multiply()
	# print(logger.logs)
	logfile = '/'.join(__file__.split("\\")[:-1]) + '/logs.txt'
	print(logfile)
	logger.writeLogs(logfile, append=True, position='top')

