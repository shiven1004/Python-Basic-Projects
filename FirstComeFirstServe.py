# First Come, First Served
def findWaitingTime(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n, bt, wt, tat)
    print("Processes\t" + "Burst time\t" + " Waiting time\t" + "Turn around time")
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print("\t" + str(i + 1) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(wt[i]) + "\t\t\t" + str(tat[i]))

    print("Average waiting time = " + str(total_wt / n))
    print("Average turn around time = " + str(total_tat / n))


if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)

    burst_time = [10, 5, 8]

    findavgTime(processes, n, burst_time)


"""# First Come, First Served using oops
class processes:
    def __init__(self, id, at, bt, ct):
        self.id = id
        self.at = at
        self.bt = bt
        self.ct = ct
        self.tat = self.ct - self.at
        self.wt = self.tat - self.bt

    def get(self):
        print(f"{self.id}\t{self.at}\t{self.bt}\t{self.ct}\t{self.tat}\t{self.wt}")

    def turnaround(self):
        return self.tat

    def waiting(self):
        return self.wt


num = int(input("Enter the Number of Processes:"))
l = []
ct = 0

for i in range(num):

    print(f'Process {i + 1}')
    at = int(input("Enter the Arrival Time:-"))
    bt = int(input("Enter the Burst Time:-"))
    if (len(l) == 0):
        ct = bt
        l.append(processes(i, at, bt, ct))
    else:
        ct += bt
        l.append(processes(i, at, bt, ct))

    print("\n")
avg_tat = 0
avg_wat = 0
print("PID\tAT\tBT\tCT\tTAT\tWT")
for process in l:
    process.get()

for process in l:
    avg_tat += process.turnaround()
    avg_wat += process.waiting()
print(f"Avg_turnaround:{avg_tat / num}\nAvg_Waitingtime:{avg_wat / num}")
"""
