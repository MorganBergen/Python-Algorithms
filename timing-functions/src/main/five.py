from linkedlist import LinkedList
import time

# Operation 5: Linked List get_entry at specifically the last index

class Five:
    def __init__(self):
        self.list = LinkedList()
        self.time = []
        self.n = []

    def execute(self):
        for i in range(100):
            n = (i+1)*1000
            self.insert_n(self.list, n)
            print(f"inserted {self.list.size} nodes to the list")
            print(f"__________________________________________")
            self.test_get_data_n(self.list, (self.list.size - 1))
            print(f"__________________________________________")
            print(f"list size = {self.list.size}")
            self.list = LinkedList()
            print('\n')

    def test_get_data_n(self, p_list, n):
        print("beginning the timing code...")
        num_iterations = n
        start_time = time.process_time_ns()

        print(f"get_data at index {num_iterations} = {p_list.get_data(num_iterations)}")

        end_time = time.process_time_ns()
        print(f"total iterations: ", num_iterations)        
        print(f"total time in nano seconds: ", end_time-start_time)
        print(f"total time in seconds: ", self.nanosec_to_sec(end_time-start_time))
        self.time.append(str(self.nanosec_to_sec(end_time-start_time)))
        self.n.append(str(num_iterations))

    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)

    def insert_n(self, p_list, n):
        for i in range(n):
            p_list.insert(i, i)

    def fileIO(self, file_name):
        f = open(file_name, 'w')
        f.writelines("time in seconds\n")
        for i in range(len(self.time)):
            f.writelines(self.time[i])
            f.writelines("\n")

        f.writelines("\nsize of n\n")
        for i in range(len(self.n)):
            f.writelines(self.n[i])
            f.writelines("\n")
        f.close()