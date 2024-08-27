"""
User Guide:
----------
1. Inherit Logger (no need to initialize)
2. Add following logs:
	- error using the attribute :		errorMessage
	- warnings using the attribute :	warningMessage
	- information using the attribute :	fyiMessage
3. Print logs using:
	- print(Logger.errorMessage)
	- print(Logger.warningMessage)
	- print(Logger.fyiMessage)
	- print(Logger.logs) 				# this print all error/warnings/fyi message in their respective orders.

For further use-case visit ./userLogger.py
"""

class Logger(object):

	_errors : str = []
	_errorIndex: int = 0
	_warnings: str = []
	__warningIndex: int = 0
	_fyi: str = []
	_fyiIndex: int = 0
	_logs: str = []

	@property
	def logs(self):
		return "\n".join(map(str, self._logs))
 
	@property
	def errorMessage(self):
		return "\n".join(map(str, self._errors))

	@errorMessage.setter
	def errorMessage(self, msg):
		self._errorIndex += 1
		self._errors.append(f"[Error: {self._errorIndex}] " + msg)
		self._logs.append(f"[Error: {self._errorIndex}] " + msg)
		
	@property
	def warningMessage(self):
		return "\n".join(map(str, self._warnings))

	@warningMessage.setter
	def warningMessage(self, msg):
		self.__warningIndex += 1
		self._warnings.append(f"[Warning: {self.__warningIndex}] " + msg)
		self._logs.append(f"[Warning: {self.__warningIndex}] " + msg)

	@property
	def fyiMessage(self):
		return "\n".join(map(str, self._fyi))

	@warningMessage.setter
	def fyiMessage(self, msg):
		self._fyiIndex += 1
		self._fyi.append(f"[FYI: {self._fyiIndex}	] " + msg)
		self._logs.append(f"[FYI: {self._fyiIndex}] " + msg)
			

if __name__ == "__main__":
	logger = Logger()
	logger.warningMessage = f"Division not possible,  !" 
	print(logger.warningMessage)
	# OR
	print(logger.logs)

