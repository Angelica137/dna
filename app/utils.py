from app.constants import CODON_TO_AMINO_ACID, NUCLEOTIDES


def translate_dna(dna_sequence: str) -> str:
    """
    Translate a DNA sequence into a protein sequence. A codon is a sequence of three DNA nucleotides that
    corresponds to a specific amino acid during protein synthesis.
    :param dna_sequence: the DNA sequence to translate
    :return: the protein sequence
    """

    protein_sequence = ''
    dna_sequence = dna_sequence.upper()
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i + 3]
        if len(codon) != 3:
            return protein_sequence
        try:
            protein_sequence += CODON_TO_AMINO_ACID[codon]
        except KeyError:
            raise ValueError(f'Codon not recognised: {codon}')
    return protein_sequence


def is_valid_dna_sequence(sequence: str) -> bool:
    """
    Check that a DNA sequence contains valid characters
    :param sequence: the DNA sequence to check
    :return: True if ok, False if not
    """

    for nucleotide in sequence.upper():
        if nucleotide not in NUCLEOTIDES:
            return False
    return True
