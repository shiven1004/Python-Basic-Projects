# Round Robin Scheduling Algorithm

def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0
    # Keep traversing processes in round robin manner until all of them are not done.
    while (1):
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum

                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break


def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n
    findWaitingTime(processes, n, bt, wt, quantum)
    findTurnAroundTime(processes, n, bt, wt, tat)

    print("Processes\tBurst Time\t\tWaiting Time\t\tTurn Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print("\t", i + 1, "\t\t\t", bt[i], "\t\t\t", wt[i], "\t\t\t", tat[i])

    print("\nAverage Waiting Time = %.5f" % (total_wt / n))
    print("\nAverage Turn Around Time = %.5f" % (total_tat / n))

if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)
    burst_time = [10, 5, 8]
    quantum = 2
    findavgTime(processes, n, burst_time, quantum)
