import os
import re

wrkdir = "/Users/xinba/Downloads"
seqs = []
for fn in os.listdir(wrkdir):
    if fn.endswith(".html"):
        with open(os.path.join(wrkdir, fn), 'r') as fin:
            for line in fin:
                seqs.extend(re.findall(r'<td>([A|T|G|C|N]+)</td>', line))
print(seqs)
