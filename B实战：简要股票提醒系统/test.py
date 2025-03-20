# coding:utf-8

def getinfo(anyone):
	anyone.name='A'
	anyone.age='B'
	anyone.color='C'
	anyone.six='D'
	return anyone

class Share(object):
	"""docstring for ClassName"""
	def __init__(self, code):
		self.code = code
		

share=Share('白色')  #实例化

new=getinfo(share)

print(new.six)


