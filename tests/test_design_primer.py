from unittest import TestCase

from app.design_primer import design_primer_one, design_primer_two, melting_temp, gen_primes, design_primer_one_temp, design_primer_two_temp


class TestDesginPrimer(TestCase):

    def test_return_primer_one(self):
        result = design_primer_one('GGCGAGGAGCTG', 4)
        expected = 'GGCG'
        self.assertEqual(result, expected)

    def test_return_primer_two(self):
        result = design_primer_two('GGCGAGGAGCTG', 4)
        expected = 'CAGC'
        self.assertEqual(result, expected)

    def test_return_melting_temp_less_14(self):
        result = melting_temp('AACC')
        expected = 12
        self.assertEqual(result, expected)

    def test_return_melting_temp_greater_14(self):
        result = melting_temp('ATAGGCTACATTGCA')
        expected = 36.5
        self.assertEqual(result, expected)

    def test_return_both_primers_and_tem(self):
        result = gen_primes('GGCGAGGAGCTG', 4)
        expected = {
            'GGCG': 16,
            'CAGC': 14
        }
        self.assertEqual(result, expected)

    def test_return_primer_one__temp_small_range(self):
        result = design_primer_one_temp('GGCGAGGAGCTG', 20, 25)
        expected = {'GGCGAG': 22}
        self.assertEqual(result, expected)

    def test_return_primer_one__temp_larger_range(self):
        result = design_primer_one_temp('GGCGAGGAGCTG', 20, 60)
        expected = {
            'GGCGAG': 22,
            'GGCGAGG': 26,
            'GGCGAGGA': 28,
            'GGCGAGGAG': 32,
            'GGCGAGGAGC': 36,
            'GGCGAGGAGCT': 38,
            'GGCGAGGAGCTG': 42
        }
        self.assertEqual(result, expected)

    def test_return_primer_one__temp_larger_strand(self):
        result = design_primer_one_temp('ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCCTGACCTACGGCGTGCAGTGCTTCAGCCGCTACCCCGACCACATGAAGCAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCACCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAG', 20, 40)
        expected = {
            'ATGGTGA': 20,
            'ATGGTGAG': 24,
            'ATGGTGAGC': 28,
            'ATGGTGAGCA': 30,
            'ATGGTGAGCAA': 32,
            'ATGGTGAGCAAG': 36,
            'ATGGTGAGCAAGG': 40
        }
        self.assertEqual(result, expected)

    def test_return_primer_two__temp_small_range(self):
        result = design_primer_two_temp('GGCGAGGAGCTG', 20, 25)
        expected = {'CAGCTC': 20, 'CAGCTCC': 24}
        self.assertEqual(result, expected)

    def test_return_primer_two__temp_larger_strand(self):
        result = design_primer_two_temp('ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCCTGACCTACGGCGTGCAGTGCTTCAGCCGCTACCCCGACCACATGAAGCAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCACCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAG', 1, 20)
        expected = {
            'CTTGTA': 16,
            'CTTGTAC': 20
        }
        self.assertEqual(result, expected)
