import os, time
path_name = input("Please input your file name")
with open(path_name + ".py", "a") as outf:
    outf.write("#! python3\n##0\n## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000\n##  0              00     0  0         0           00             00       0      0    0      0   0          0\n##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000\n##    0            00     0  0         0          0  0            00       0      0    0      0   0              0\n##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000\n##\n## authors = Monkeyboy2805")
print("Created file")
time.sleep(5)
