



def add(self, entry):
	
	if self._root == None:
		self._root = BNode(entry)
	
	elif self._root.entry < entry: # check to add right
		if self._root._right == None:
			self._root._right = BNode(entry)
		else:
			self._rec_add(entry, self._root.right)
			
	elif self._root.entry > entry: # check to add left
		if self._root._left == None:
			self._root._left = BNode(entry)
		else:
			self._rec_add(entry, self._root.left)
	else:
		raise RuntimeError('No Duplicates Allowed')

def _rec_add(self, entry, cur_node):
	
	if cur_node == None:
	
		self.cur_node = BNode(entry)
	
	else:
		if cur_node.entry < entry:
		
			if cur_node.right == None:
				cur_node._right = BNode(entry)
			else:
				self._rec_add(entry, cur_node.right)
		elif cur_node.entry > entry:
			if cur_node.left == None:
				cur_node._left = BNode(entry)
			else:
				self._rec_add(entry, cur_node.left)
		else:
		
		raise RuntimeError("no duplicates allowed")
