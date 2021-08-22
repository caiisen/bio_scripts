import gzip
with gzip.open('ht.vcf.gz', 'rt') as input_file:
    format = []
    depth = {}
    for line in input_file:
        if line[0] != '#':
            format = line.split()[9:]
            for sample in format:
                dp = sample.split(':')[2]
                if dp in depth.keys():
                    depth[dp] = depth[dp] + 1
                else:
                    depth[dp] = 0

for key, value in depth.items():
    print(key, value)