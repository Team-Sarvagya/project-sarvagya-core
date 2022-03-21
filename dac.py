import re
import base64
import argparse
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt 



description = "A tool to convert a file (image or video) into an analog signal."

parser = argparse.ArgumentParser(description = description)
parser.add_argument('-f', '--file', type = Path, required = True, help = "Path to input file")
parser.add_argument('-o', '--output', type = Path, required = True, help = "Name of output file")
args = parser.parse_args()

if not args.file.exists():
    raise FileNotFoundError("-f/--file: invalid path specified")



with open(args.file, 'rb') as f:
    data = f.read()

data_b64 = base64.b64encode(data)
decoded = base64.decodebytes(data_b64)
data_binary = "".join(["{:08b}".format(x) for x in decoded])

with open(args.output, 'w') as f:
    f.write(data_binary)



with open(args.output) as f:
    s = f.read()
s_array = [int(i) for i in str(s)]

# plotting the whole data as a PCM wave
# x = np.arange(len(s_array))
# y = s_array

#plotting subpart of data as a PCM wave
x = np.arange(100)
y = s_array[:100]

plt.axhline(y = 0.5, color = 'r', linestyle = '-')
plt.xlabel("Index of bits")
plt.ylabel("Binary values")
plt.title("PCM wave of Binary Data")

plt.step(x, y)
plt.show() 

print("Done!")