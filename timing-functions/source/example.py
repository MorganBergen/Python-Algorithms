'''
in this lab we will time various methods from data structures we've made so far
save those times
plot them to see if they match the theoretical expectations
'''

import time

def nanosec_to_sec(ns):
	billion = 1000000000 # one thousand million
	return (ns/billion)


print("beginning the timing code...")
num_iterations = 100000000 # one hundred million
start_time = time.process_time_ns()

# loop that does nothing but repeat, hence the _ variable and the keywork pass
# which just means do nothing

for _ in range(num_iterations):
	pass

end_time = time.process_time_ns()

print(f"total time in nano seconds: ", end_time-start_time)
print(f"total time in seconds: ", nanosec_to_sec(end_time-start_time))
