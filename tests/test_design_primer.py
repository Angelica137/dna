from unittest import TestCase

from app.design_primer import design_primer_one, design_primer_two


class TestDesginPrimer(TestCase):

    def test_return_primer_one(self):
        result = design_primer_one('GGCGAGGAGCTG', 4)
        expected = 'GGCG'
        self.assertEqual(result, expected)

    def test_return_primer_two(self):
        result = design_primer_two('GGCGAGGAGCTG', 4)
        expected = 'GTCG'
        self.assertEqual(result, expected)