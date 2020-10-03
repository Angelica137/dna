from app.constants import STRAND_MAPPING


def design_primer_one(dna_region: str, primer_length: int):
    """
    Design first primer for the reigion of interest in a given 
    dna sequence and primer length.
    """

    primer_one = dna_region[0: primer_length]
    return primer_one


def design_primer_two(dna_region: str, primer_length: int):
    """
    Design second primer for the reigion of interest in a given 
    dna sequence and primer length.
    """

    primer_two = ''
    primer_prep = dna_region[-primer_length:][::-1]
    for char in primer_prep:
        for key, value in STRAND_MAPPING.items():
            if char == key:
                primer_two += value
    return primer_two


def melting_temp(primer: str):
    """
    Calculate the melting temperature for a given primer.
    """

    primer_length = len(primer)
    count = {
        'A': 0,
        'T': 0,
        'C': 0,
        'G': 0
    }
    for char in primer:
        if char in count:
            count[char] += 1

    if primer_length < 14:
        melting = 2 * (count['A'] + count['T']) + 4 * (count['G'] + count['C'])
    elif primer_length >= 14:
        melting = 64.9 + ((41 * (count['G'] + count['C'] - 16.4)) / (count['A'] + count['T'] + count['G'] + count['C']))
    return round(melting, 1)


def gen_primes(dna_region: str, primer_length: int):
    """
    Generate a pair of primers using one DNA sequence and one length paramater.
    """
    primers = {}
    primer_one = design_primer_one(dna_region, primer_length)
    primer_two = design_primer_two(dna_region, primer_length)
    primers[primer_one] = melting_temp(primer_one)
    primers[primer_two] = melting_temp(primer_two)
    return primers


def design_primer_one_temp(dna_region: str, temp_low: int, temp_high: int):
    """
    Design a group of firs primers using a temperatrure range given by the user.
    Primers must be between 6 and 20 nucleotides.
    """
    first_primers = {}
    primer_length = list(range(6, 21))
    for i in primer_length:
        primer = dna_region[0: i]
        melting_point = melting_temp(primer)
        if (melting_point >= temp_low) and (melting_point <= temp_high):
            first_primers[primer] = melting_point
    return first_primers


def design_primer_two_temp(dna_region: str, temp_low: int, temp_high: int):
    """
    Design a group of second primers using a temperatrure range given by the user.
    Primers must be between 6 and 20 nucleotides.
    """
    second_primers = {}
    primer_length = list(range(6, 21))
    for i in primer_length:
        primer_two = ''
        primer_prep = dna_region[-i:][::-1]
        for char in primer_prep:
            for key, value in STRAND_MAPPING.items():
                if char == key:
                    primer_two += value
        melting_point = melting_temp(primer_two)
        if (melting_point >= temp_low) and (melting_point <= temp_high):
            second_primers[primer_two] = melting_point
    return second_primers
