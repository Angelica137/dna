from flask import Blueprint, request
from werkzeug.exceptions import UnprocessableEntity

from app.utils import translate_dna, is_valid_dna_sequence
from app.design_primer import gen_primes

design_tools_api = Blueprint('design-tools', __name__)


@design_tools_api.route('/translate', methods=['POST'])
def translate():
    data = request.json
    dna_sequence = data['dna_sequence']

    if not is_valid_dna_sequence(dna_sequence):
        raise UnprocessableEntity('DNA character not recognised')

    try:
        protein_sequence = translate_dna(dna_sequence)
    except ValueError as exception:
        raise UnprocessableEntity(str(exception))

    return protein_sequence


@design_tools_api.route('/primer', methods=['POST'])
def primer():
    data = request.json
    dna_region = data['dna_region', 'primer_length']

    if not is_valid_dna_sequence(dna_region):
        raise UnprocessableEntity('DNA character not recognised')

    try:
        generate_primes = gen_primes(dna_region, primer_length)
    except ValueError as exception:
        raise UnprocessableEntity(str(exception))

    return generate_primes
