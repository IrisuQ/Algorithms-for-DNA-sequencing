def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    print ("!!!")
    return genome

genome = readGenome('lambda_virus.fa')

def match_naive(p, t):
    # occurrencs = []
    occur = -1
    for i in range(len(t)-len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
                break
        if match:
            occur = i
            break
    print (occur)
    return occur

def reverseComplement(s):
	complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N'}    # N -> ATCG
	t = ''
	for base in s:
		t = complement[base]+t
	return t

def match_naive_2mm(p, t):
    occur = -1
    print (len(t))
    for i in range(len(t)-len(p) + 1):
        match = True
        mm = 0
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                if mm < 2:
                    mm += 1
                else:
                    match = False
                    break
        if match:
            occur = i
            break
    print (occur)
    return occur


# rev = reverseComplement('AGTCGA')
# occur1 = match_naive_2mm('AGGAGGTT', genome)
# occur2 = match_naive(rev, genome)
# print (occur1+occur2)


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filedname) as fh:
		while True:
			fh.readline()
			seq = fh.readline().rstrip()
			fh.readline()
			qual = fh.readline().rstrip()
			if len(seq) == 0:
				break
			sequences.append(seq)
			qualities.append(quual)
	return sequences, qualities

seq, qual = readFastq('hw1.fastq')

