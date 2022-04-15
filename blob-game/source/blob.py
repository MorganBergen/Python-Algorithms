
from map import Map

class Blob:
	
	def __init__(self):
		self.name = "blob"
		map = Map()
		map.run()
		map.printMap()
		rows = map.num_rows
		cols = map.num_cols
		start_row = map.start_row
		start_col = map.start_col
		map_copy = map.map
	
	def change(self, row):
		if row == 0:
			print(row)
			return 0
		else:
			print(row)
			return self.change(row-1)


	def destory(self, r, c):
		map_copy
