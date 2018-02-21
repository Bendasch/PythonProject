import frw
import warnings

display_warnings = True
printers = []
caught_warnings = []
k = 1
while k<4:
	papercount = k*50
	printer_name = 'printer_' + str(k)
	with warnings.catch_warnings(record=True) as w:
		# warning settings
		warnings.simplefilter('always')
		# Trigger a warning.
		instx = frw.create_instance('printer', 'printer', 'x')	
		inst = frw.create_instance('printer', 'printer', papercount)
		inst.add_paper(50)
		if len(w) >= 1 and display_warnings:
			for warning in w:
				print ('*** ' + str(warning.message))
				print (' >  ' + str(warning.filename) + \
						', line ' + str(warning.lineno) + '!\n')

	printers.append([printer_name, inst])
	k+=1

for item in printers:
	print (item[0] + ' has ' + str(item[1].get_papercount()) + ' sheets.')
