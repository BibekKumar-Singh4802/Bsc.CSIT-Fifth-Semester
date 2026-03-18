
# Lab Topic: Single Queue Server System Simulation (M/M/1 Model)
# This program models a single-server queue system using Poisson arrivals and exponential service times.


import simpy
import random

class MM1Queue:
    def __init__(self, env, arrival_rate, service_rate):
        self.env = env
        self.server = simpy.Resource(env, capacity=1)
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate

        # Statistics
        self.total_wait_time = 0
        self.total_system_time = 0
        self.total_customers = 0
        self.server_busy_time = 0
        self.customer_log = []

    def customer_generator(self):
        customer_id = 1
        while True:
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            self.env.process(self.serve_customer(customer_id))
            customer_id += 1

    def serve_customer(self, customer_id):
        arrival_time = self.env.now

        with self.server.request() as request:
            yield request

            service_start = self.env.now
            wait_time = service_start - arrival_time
            self.total_wait_time += wait_time

            service_time = random.expovariate(self.service_rate)
            self.server_busy_time += service_time

            yield self.env.timeout(service_time)
            service_end = self.env.now

            system_time = service_end - arrival_time
            self.total_system_time += system_time
            self.total_customers += 1

            # Store log
            self.customer_log.append(
                (customer_id, arrival_time, service_start, service_end, wait_time, system_time)
            )

# ---------------- USER INPUT ----------------
arrival_rate = float(input("Enter arrival rate λ: "))
service_rate = float(input("Enter service rate μ: "))

# ---------------- SIMULATION SETUP ----------------
SIM_TIME = 100

env = simpy.Environment()
mm1 = MM1Queue(env, arrival_rate, service_rate)
env.process(mm1.customer_generator())
env.run(until=SIM_TIME)

# ---------------- PERFORMANCE METRICS ----------------
λ = arrival_rate
μ = service_rate
ρ = λ / μ

L = λ / (μ - λ)
Lq = ρ * L
W = 1 / (μ - λ)
Wq = ρ * W
P0 = 1 - ρ
server_utilization = ρ * 100
system_stable = "STABLE" if ρ < 1 else "UNSTABLE"

# ---------------- PRINT CUSTOMER LOG ----------------
print("\nCUSTOMER SIMULATION LOG")
print(f"{'ID':<5}{'Arrival':<10}{'Service Start':<15}{'Service End':<12}{'Wq':<8}{'W'}")

for c in mm1.customer_log:
    print(f"{c[0]:<5}{c[1]:<10.2f}{c[2]:<15.2f}{c[3]:<12.2f}{c[4]:<8.2f}{c[5]:.2f}")

# ---------------- PRINT RESULTS ----------------
print("\nSIMULATION RESULTS- Bibek Singh")
print(f"Total customers served   : {mm1.total_customers}")
print(f"Server Utilization       : {server_utilization:.2f}%")

print("\nTHEORETICAL M/M/1 METRICS")
print(f"1. ρ (Server Utilization / Traffic Intensity)   : {ρ:.3f}")
print(f"2. L (Average number of customer in system)     : {L:.3f} customers")
print(f"3. Lq (Average number of customer in queue)     : {Lq:.3f} customers")
print(f"4. W (Average Time in the system)               : {W:.3f} time units")
print(f"5. Wq (Average Waiting time in the queue)       : {Wq:.3f} time units")
print(f"6. P0 (Idle probability)                        : {P0:.3f}")
print(f"7. System Stable?                               : {system_stable}")