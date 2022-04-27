'''
@file		six.py
@author		Morgan Bergen
@date		April 27 2022
@brief	    this is the implementation details that will test the time complexity of printing all elements in the ADT linkedList using get_entry()
            by utilizing this class the following will happen
            1.  a linkedList will have inserted 1000 elements into the list
            2.  a record of the time to perform a print(self.list.size) get_entry at the last index will be allocated to the self.time list built in data structure
            3.  step 1 and 2 will be repeated, increasing the size by 1,000 each time untill the linkedlist has pushed 100,000 times
'''


from linkedlist import LinkedList
import time

class Six:

    '''
    @pre	    constructor must have been called
    @post		member variables will have been initialized to their defaults
                list will start as an empty linkedList
                time_sec, time_nanosec, and n will start as empty lists
    @param		None
    @raises		None
    @returns	None
    '''
    def __init__(self):
        self.list = LinkedList()
        self.time_sec = []
        self.time_nanosec = []
        self.n = []

    '''
    @pre	    Six() must have been already called
    @post		time complexity statistics will be recorded for get_entry(),test_print_n will be called, before each iteration of insert()
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
            print(f"__________________list size = {self.list.size}_______________")
            self.test_print_n(self.list, self.list.size)
            print(f"_______________________________________________\n")

    '''
    @pre	    Six() and execute() must have been already called
    @post		time_sec, time_nanosec, and n will be initialized to the recorded the approropriate complexity information
                this will print out each element onto the consol
    @param		p_list, n
    @raises		None
    @returns	None
    '''
    def test_print_n(self, p_list, n):
        print("beginning the timing code...")
        num_iterations = 10
        start_time = time.process_time_ns()


        for i in range(num_iterations):
            if i == num_iterations - 1:
                print(f"{p_list.get_data(i)} -> • ")
            else:
                print(f"{p_list.get_data(i)} -> ", end="")
    
        end_time = time.process_time_ns()       
        print(f"total time in nano seconds: ", end_time-start_time)
        print(f"total time in seconds: ", self.nanosec_to_sec(end_time-start_time))
        self.time_nanosec.append(str(end_time-start_time))
        self.time_sec.append(str(self.nanosec_to_sec(end_time-start_time)))
        self.n.append(str(num_iterations))


    '''
    @pre	    test_print_n() must have already been called
    @post		converts nano seconds to seconds
    @param		ns
    @raises		None
    @returns	ns/billion
    '''
    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)

    '''
    @pre	   all methods above must have been called
    @post	   a file will be written into a directory which stores the time complexity statitics
    @param	   file_name
    @raises    None
    @returns   None
    '''
    def generate_statistics(self, file_name):
        f = open(file_name, 'w')
        
        f.writelines("time in nano seconds\n")
        for i in range(len(self.time_nanosec)):
            f.writelines(self.time_nanosec[i])
            f.writelines("\n")

        f.writelines("time in seconds\n")
        for i in range(len(self.time_sec)):
            f.writelines(self.time_sec[i])
            f.writelines("\n")

        f.writelines("\nsize of n\n")
        for i in range(len(self.n)):
            f.writelines(self.n[i])
            f.writelines("\n")
        f.close()