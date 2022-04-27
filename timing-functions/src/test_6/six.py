
from linkedlist import LinkedList
import time

# Operation 6:  Printing all elements in a LinkedList using get_entry

class Six:
    def __init__(self):
        self.list = LinkedList()
        self.time_sec = []
        self.time_nanosec = []
        self.n = []

    def execute(self):
        count = 0
        for i in range(100):
            for j in range(1000):
                self.list.insert(0, count)
                count += 1
            print(f"__________________list size = {self.list.size}_______________")
            self.test_print_n(self.list, self.list.size)
            print(f"_______________________________________________\n")

    def test_print_n(self, p_list, n):
        print("beginning the timing code...")
        num_iterations = n
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

    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)

    def generate_stats(self, file_name):
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