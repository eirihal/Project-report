import numpy as np

FR = 0.005 # failure rate
RR = 0.125 # repair rate

A = np.array([[-FR, FR], [RR, -RR]]) # Transition rate matrix

I = np.array([[1, 0], [0, 1]]) # Identity matrix

P = np.array([1, 0]) # P(0), P is updated through iteration

hours_per_day = 8
minutes_per_day = 8*60
delta = 1 # delta_t, minutes

for i in range(1, minutes_per_day + 1):
    A_d = A * delta
    A_I = A_d + I
    P = np.matmul(P, A_I)

print(P)    