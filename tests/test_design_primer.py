from unittest import TestCase

from app.design_primer import design_primer_one, design_primer_two, melting_temp, gen_primes, design_primer_one_temp


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

    def test_return_primer_one__temp_six_nucleotides(self):
        result = design_primer_one_temp('GGCGAGGAGCTG', 20, 25)
        expected = 22
        self.assertEqual(result, expected)
