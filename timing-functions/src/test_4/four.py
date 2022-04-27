'''
@file		four.py
@author		Morgan Bergen
@date		April 27 2022
@brief	    this is the implementation details that will test the time complexity of get_entry(0) for ADT linkedList
            by utilizing this class the following will happen
            1.  a linkedList will have inserted 1000 elements into the list
            2.  a record of the time to perform a get_entry at index zero will be allocated to the self.time list built in data structure
            3.  step 1 and 2 will be repeated, increasing the size by 1,000 each time untill the linkedlist has pushed 100,000 times
'''

from linkedlist import LinkedList
import time

class Four:

    '''
    @pre	    constructor must have been called
    @post		member variables will have been initialized to their defaults
                list will start as an empty linkedList
                time and n will start as empty lists
    @param		None
    @raises		None
    @returns	None
    '''
    def __init__(self):
        self.list = LinkedList()
        self.time = []
        self.n = []

    '''
    @pre	    Four() and execute() must have been already called
    @post		p_list will have inserted n many elements onto the list
    @param		p_list, n
    @raises		None
    @returns	None
    '''
    def insert_n(self, p_list, n):
        for i in range(n):
            p_list.insert(i, i)

    '''
    @pre	    Four() must have been already called
    @post		time complexity statistics will be recorded for get_entry(0)
    @param		None
    @raises		None
    @returns	None
    '''
    def execute(self):
        count = 0
        for i in range(100):
            for j in range(1000):
                self.list.insert(0, count)
                count += 1
            print(f"_____________list size = {self.list.size}__________________")
            self.test_get_data_n(self.list, 0)
            print(f"_______________________________________________\n")

    '''
    @pre	    Four() and execute() must have been already called
    @post		time and n will be initialized to the recorded time complexity information
    @param		p_list, n
    @raises		None
    @returns	None
    '''
    def test_get_data_n(self, p_list, n):
        print("beginning the timing code...")
        num_iterations = n
        start_time = time.process_time_ns()

        print(f"get_data at index {num_iterations} = {p_list.get_data(num_iterations)}")

        end_time = time.process_time_ns()
        print(f"total iterations: ", num_iterations)        
        print(f"total time in nano seconds: ", end_time-start_time)
        print(f"total time in seconds: ", self.nanosec_to_sec(end_time-start_time))
        self.time.append(str(end_time-start_time))
        self.n.append(str(self.list.size))

    '''
    @pre	    test_n() must have already been called
    @post		converts nano seconds to seconds
    @param		ns
    @raises		None
    @returns	ns/billion
    '''
    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)

    '''
    @pre	   All methods above must have been called
    @post	   a file will be written into a directory which stores the time complexity statitics
    @param	   file_name
    @raises    None
    @returns   None
    '''
    def generate_statistics(self, file_name):
        f = open(file_name, 'w')
        f.writelines("time in nanoseconds\n")
        for i in range(len(self.time)):
            f.writelines(self.time[i])
            f.writelines("\n")

        f.writelines("\nsize of n\n")
        for i in range(len(self.n)):
            f.writelines(self.n[i])
            f.writelines("\n")
        f.close()