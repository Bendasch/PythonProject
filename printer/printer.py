import warnings as w

# warning settings
w.simplefilter('always')

# class definition: PRINTER
class printer:

	attributes = [	['papercount',	'printername']	,
					['int',			'str']			]

	def __init__(self, printername = 'printer', papercount = 100):
		if type(papercount) is not int:
			w.warn('Wrong `papercount` datatype, used default value 100.', stacklevel=1)
			self._papercount  = 100
		elif papercount > 120:
			w.warn('Sheet overflow on instantiation, used default value 100.', stacklevel=1)
			self._papercount  = 100
		else:
			self._papercount  = papercount

		if type(printername) is not str:
			w.warn('Wrong `printername` datatype, used default value `printer`.', stacklevel=1)
			self._printername = 'printer'
		else:
			self._printername = printername

		return


	def get_papercount(self):
		return self._papercount

	def get_printername(self):
		return self._printername

	def print_papercount(self):
		print (self._papercount)

	def print_printername(self):
		print (self._printername)

	def add_paper(self, new_paper):
		if self._papercount + new_paper > 120:
			w.warn('Sheet overflow on adding, added up to max value 120 instead.', stacklevel=1)
			self._papercount = 120
		else:
			self._papercount += new_paper

	def change_printername(self, printername):
		if type(printername) is not str:
			w.warn('Wrong `printername` datatype, couldn`t change name.', stacklevel=1)
			return
		else:
			self._printername = printername
