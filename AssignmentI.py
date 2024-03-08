import sys
import numpy as np
from Bio import SeqIO
from pathlib import Path

if len(sys.argv) != 5:
    print(f'Usage: {sys.argv[0]} <seq_length> <n_mutations> <mutation_rate> <outfile>')
    sys.exit(1)

l,m,p,outfile = sys.argv[1:]

mapping = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}
map_seq = lambda x: ''.join([mapping[i] for i in x])

rng = np.random.RandomState(0)
seq = rng.randint(0, 4, l)

n_bases_to_change = int(np.floor(p * l)) if p*l >= 1 else 1
n_bases_to_change

seqs = [seq]
bases_changed_str = ['']
for i in range(m):
    seqs.append(seq.copy())
    bases_to_change = np.random.choice(l, n_bases_to_change, replace=False)
    bases_changed_str.append(np.array2string(bases_to_change, separator=', ')[1:-1])
    seqs[-1][bases_to_change] = np.random.randint(0, 4, n_bases_to_change)

records = [SeqIO.SeqRecord(seq=map_seq(seq), id=f'S{i}', description=b) for i, (seq, b) in enumerate(zip(seqs[1:], bases_changed_str))]
SeqIO.write(records, Path(outfile).open('w'), 'fasta')
# %%
