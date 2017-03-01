complements = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
        }

def to_rna(dna):
    try:
        rna = [complements[n] for n in dna]
        return ''.join(rna)
    except KeyError:
        return ''
