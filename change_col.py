with open('test.txt', 'r') as input_file:
    words = []
    out = []
    gene_id = []
    test = ''
    for line in input_file:
        words = line.split()
        gene_id = words[3].split('_')
        chr_number = gene_id[1][0:2]
        print(chr_number)
        if chr_number == '00':
            out.append('\t'.join(words))
        else:
            words[0] = gene_id[0] + chr_number + 'G'
            out.append('\t'.join(words))
        print(out)

with open('out.txt', 'w') as output_file:
    output_file.write('\n'.join(out))