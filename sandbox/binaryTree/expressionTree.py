class ExpressionTree:
	# builds an expression tree for the expression string.
	def __init__(self, expStr):
		self._expTree = None
		self._buildTree(expStr)
	
	# evaluates the expression tree and returns the resulting value.
	def evaluate(self, varMap):
		return self._evalTree(self._expTree, varMap)

	# returns a string representation of the expression tree.
	def __str__(self):
		return self._buildString(self._expTree)
