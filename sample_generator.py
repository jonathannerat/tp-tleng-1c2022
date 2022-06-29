from parser import PTypeBool, PTypeFloat, PTypeInt, PTypeString

class SampleGenerator:
	def __init__(self, typedefs):
		self.typedefs = typedefs

	def generate(self):
		def type_resolver(identifier):
			if not isinstance(identifier, str):
				return identifier

			if identifier == 'bool':
				return PTypeBool()
			elif identifier == 'float64':
				return PTypeFloat()
			elif identifier == 'int':
				return PTypeInt()
			elif identifier == 'string':
				return PTypeString()

			typedefs_that_match = [
				typedef for typedef in self.typedefs if typedef.name == identifier
			]
			return type_resolver(typedefs_that_match[0].type)
			
		return type_resolver(self.typedefs[0].type).random_value(type_resolver)
