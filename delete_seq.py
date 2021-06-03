with open ('subject.fasta', 'r') as subject_file:
    subject = {}
    for line in subject_file:
        if '>' in line:
            seq_name = line.strip().strip('>')
            subject[seq_name] = []
        else:
            subject[seq_name].append(line.strip())
    for key, value in subject.items():
        subject[key] = ''.join(value)

with open ('query.list', 'r') as query_file:
    out = {}
    for line in query_file:
        if line.strip() in subject:
            del subject[line.strip()]

with open ('query.fasta', 'w') as out_file:
    for key, value in subject.items():
        out_file.write('>' + key + '\n')
        out_file.write(value + '\n')