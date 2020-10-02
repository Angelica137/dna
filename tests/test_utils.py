from unittest import TestCase

from app.utils import translate_dna, is_valid_dna_sequence


class TestTranslateDNA(TestCase):

    def test_unknown_codon(self):
        with self.assertRaises(ValueError):
            translate_dna('ACGXACGG')

    def test_lower_case(self):
        result = translate_dna('acgCACtca')
        expected = 'THS'
        self.assertEqual(result, expected)

    def test_not_multiple_of_three(self):
        result = translate_dna('acgCACtc')
        expected = 'TH'
        self.assertEqual(result, expected)

    def test_translation_ends_at_stop_codon(self):
        result = translate_dna('acgTAGtc')
        expected = 'T*'
        self.assertEqual(result, expected)

        result = translate_dna('TAA')
        expected = '_'
        self.assertEqual(result, expected)

        result = translate_dna('ACGCACTATGAGTGA')
        expected = 'THYE_'
        self.assertEqual(result, expected)


class TestIsValidDNASequence(TestCase):

    def test_empty_sequence(self):
        self.assertTrue(is_valid_dna_sequence(''))

    def test_not_ok(self):
        self.assertFalse(is_valid_dna_sequence('ACGTAXCC'))

    def test_ok(self):
        self.assertTrue(is_valid_dna_sequence('ACGTAG'))

    def test_ok_lowercase(self):
        self.assertTrue(is_valid_dna_sequence('ACGtagG'))
