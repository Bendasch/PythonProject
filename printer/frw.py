def create_instance( modname, classname, data ):
	module = __import__(modname)
	classobj = getattr(module, classname)
	instance = classobj(data)
	return instance