from Bio.Align import PairwiseAligner
from Bio import SeqIO
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <infile>')
    sys.exit(1)

infile = Path(sys.argv[1])
seqs = []
SeqIO.parse(infile, 'fasta')
for record in SeqIO.parse(infile, 'fasta'):
    seqs.append(record)

outfile = Path('assignmentIII_phase2_out.txt')
outfile.unlink(missing_ok=True)
outfile.touch()
aligner = PairwiseAligner()
aligner.mode = 'global'
for seq in seqs:
    alignments = aligner.align(seqs[0].seq, seq.seq)
    print(alignments[0])
    with open(outfile, 'a') as f:
        print(seq.name, file=f)
        print(alignments[0], file=f)
