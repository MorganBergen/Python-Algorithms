def breadthFirstTrav(bintree):
	# create a queue and add the root node to it
	Queue q
	q.enqueue(bintree)
	
	# visit each node in the tree
	while not q.is_empty():
		# remove the next node from the queue and visit it.
		node = q.dequeue()
		print(node.data)
	
	# add the two children to the queue
	if node.left is not None:
		q.enqueue(node.left)
	if node.right is not None:
		q.enqueue(node.right)
