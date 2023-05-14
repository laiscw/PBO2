print('lais Cakrawati\n210511002\nT121A(R1)\n')
import os

try:
    os.mkdir('/mydirectory')
except OSError as e:
    print("Failed to create directory: ", e)