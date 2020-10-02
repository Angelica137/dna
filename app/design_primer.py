from app.constants import STRAND_MAPPING


def design_primer_one(dna_region: str, primer_length: int):
		"""
		Design first primer for the reigion of interest in a given 
		dna sequence
		"""

		primer_one = dna_region[0: primer_length]
		return primer_one


def design_primer_two(dna_region: str, primer_length: int):
		"""
		Design second primer for the reigion of interest in a given 
		dna sequence
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
		Calculate the melting temperature for a given primer
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
				melting = 2 * (count.get('A') + count.get('T')) + 4 * (count.get('G') + count.get('C'))
		elif primer_length >= 14:
				melting = ((64.9 + 41) * (count.get('G') + count.get('C')) - 16.4) / (count.get('A') + count.get('T') + count.get('G') + count.get('C'))
		return melting
