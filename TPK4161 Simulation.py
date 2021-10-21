import numpy as np

FR = 0.005 # Failure rate
RR = 0.125 # Repair rate

Failure = False # True if machine fails in a given hour
Repair = False # True if machine is repaired in a given hour
MachineWorking = True # True if machine is working in a given hour

FailedHoursPerDay = 0 # Counts the failed hours per day
FailedHoursTotal = 0 # Counts the total failed hours
HoursPerDay = 8
DaysSimulated = 10000 # No. of days simulated

ED = 0 # Expected downtime given by simulation

for i in range(DaysSimulated):
    for j in range(HoursPerDay):
        if MachineWorking == True:
            Failure = np.random.choice([False, True], p=[1-FR,FR])
            if Failure == True:
                FailedHoursPerDay += 1
                MachineWorking = False
        else:
            Repair = np.random.choice([False, True], p=[1-RR,RR])
            if Repair == True:
                MachineWorking = True
            else:
                FailedHoursPerDay += 1
    FailedHoursTotal += FailedHoursPerDay
    FailedHoursPerDay = 0
    MachineWorking = True
 
ED = FailedHoursTotal / (DaysSimulated*HoursPerDay)
print(ED)

    