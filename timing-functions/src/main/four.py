from linkedlist import LinkedList
import time

# Operation 4: Linked List get_entry at specifically index 0

class Four:
    def __init__(self):
        self.list = LinkedList()
        self.time = []
        self.n = []

    def insert_n(self, p_list, n):
        for i in range(n):
            p_list.insert(i, i)


    def execute(self):
        count = 0
        for i in range(100):
            for j in range(1000):
                self.list.insert(0, count)
                count += 1
            print(f"_____________list size = {self.list.size}__________________")
            self.test_get_data_n(self.list, 0)
            print(f"_______________________________________________\n")


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

    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)

    def fileIO(self, file_name):
        f = open(file_name, 'w')
        f.writelines("time in nano seconds\n")
        for i in range(len(self.time)):
            f.writelines(self.time[i])
            f.writelines("\n")

        f.writelines("\nsize of n\n")
        for i in range(len(self.n)):
            f.writelines(self.n[i])
            f.writelines("\n")
        f.close()