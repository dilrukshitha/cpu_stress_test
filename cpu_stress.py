import multiprocessing
import time

def stress_cpu():
    # Stress the CPU by performing continuous calculations
    while True:
        result = 0
        for i in range(1000000):
            result += i

if __name__ == "__main__":
    # Define the number of CPU cores you want to stress (for example, all available cores)
    num_cores = multiprocessing.cpu_count()

    # Create a process for each CPU core
    processes = []
    for i in range(num_cores):
        p = multiprocessing.Process(target=stress_cpu)
        processes.append(p)
        p.start()

    # Run the stress test for 24 hours (86400 seconds)
    time.sleep(86400)

    # Terminate all processes after 24 hours
    for p in processes:
        p.terminate()
