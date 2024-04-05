from Bio.Align import PairwiseAligner
from Bio.pairwise2 import format_alignment

seq1 = 'HEAGAWGHEE'
seq2 = 'PAWHEAE'

aligner = PairwiseAligner()
aligner.mode = 'global'
alignments = aligner.align(seq1, seq2)

for alignment in alignments:
    print(alignment)