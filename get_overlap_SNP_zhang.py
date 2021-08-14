import gzip

with gzip.open('406cannabis.jc.vcf.gz', 'rt') as input_file:
    jc = set()
    for line in input_file:
        if line[0] != '#':
            print(line.strip().split()[0:2])
            jc.add('-'.join(line.strip().split()[0:5]))
print('jc finish')

with gzip.open('406cannabis.ht.vcf.gz', 'rt') as input_file:
    with open('ol.vcf', 'w') as output_file:
        for line in input_file:
            if line[0] == '#':
                output_file.write(line)
            else:
                if '-'.join(line.strip().split()[0:5]) in jc:
                    output_file.write(line)

'''
    ht = []
    ht_header = []
    for line in input_file:
        if line[0] == '#':
            ht_header.append(line)
        else:
            ht.append(line.strip().split())
print('ht finish')

overlap = []
for i in ht:
    for j in jc:
        if i[0:5] == j[0:5]:
            overlap.append(i)

with open('406cannabis.ol.vcf', 'wt') as output_file:
    for i in ht_header:
        output_file.write(i)
    for i in overlap:
        output_file.write('\t'.join(i) + '\n')
'''