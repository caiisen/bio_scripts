with open('blast.result', 'r') as input_file:
    seq = {}
    for line in input_file:
        if line.split()[0] in seq.keys():
            seq[line.split()[0]] = seq[line.split()[0]] + 1
        else:
            seq[line.split()[0]] = 1

SCG = []
for key, value in seq.items():
    if value == 1:
        SCG.append(key)
print(SCG)

with open('CsLZ.gff', 'r') as input_file:
    with open('out.bed', 'w') as output_file:
        for line in input_file:
            if line.split()[2] == 'mRNA':
                if line.split()[-1].split(';')[0][3:] in SCG:
                    output_file.write(line.split()[0] + '\t')
                    output_file.write('\t'.join(line.split()[3:5]) + '\n')
