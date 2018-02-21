import warnings as w

# warning settings
w.simplefilter('always')

# class definition: PRINTER
class printer:

	def __init__(self, papercount = 100):
		if type(papercount) is not int:
			w.warn('Wrong `papercount` datatype, used default value 100.', stacklevel=1)
			papercount = 100
			return

		if papercount > 120:
			w.warn('Sheet overflow on instantiation, used default value 100.', stacklevel=1)
			self._papercount = 100
		else:
			self._papercount = papercount
		
	def get_papercount(self):
		return self._papercount

	def print_papercount(self):
		print (self._papercount)

	def add_paper(self, new_paper):
		if self._papercount + new_paper > 120:
			w.warn('Sheet overflow on adding, added up to max value 120 instead.', stacklevel=1)
			self._papercount = 120
		else:
			self._papercount += new_paper
