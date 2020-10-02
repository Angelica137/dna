def design_primer(dna_region: str, primer_length: int):
		"""
		Design two primers for the reigion of interest in a given 
		dna sequence
		"""

		primer_one = dna_region[0: primer_length]
		return primer_one
