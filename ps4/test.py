VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

def build_transpose_dict(vowels_permutation):
    '''
    vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to an
    uppercase and lowercase letter, respectively. Vowels are shuffled
    according to vowels_permutation. The first letter in vowels_permutation
    corresponds to a, the second to e, and so on in the order a, e, i, o, u.
    The consonants remain the same. The dictionary should have 52
    keys of all the uppercase letters and all the lowercase letters.

    Example: When input "eaiuo":
    Mapping is a->e, e->a, i->i, o->u, u->o
    and "Hello World!" maps to "Hallu Wurld!"

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    lower_vowel_permutation = list(vowels_permutation)
    upper_vowel_permutation = list(vowels_permutation.upper())
    transpose_dict = {}
    lower_vowel_list = list(VOWELS_LOWER)
    upper_vowel_list = list(VOWELS_UPPER)
    lower_consonants_list = list(CONSONANTS_LOWER)
    upper_consonants_list = list(CONSONANTS_UPPER)
    for i in range(len(lower_vowel_list)):
        transpose_dict[lower_vowel_list[i]] = lower_vowel_permutation[i]
        transpose_dict[upper_vowel_list[i]] = upper_vowel_permutation[i]
    for j in range(len(lower_consonants_list)):
        transpose_dict[lower_consonants_list[j]] = lower_consonants_list[j]
        transpose_dict[upper_consonants_list[j]] = upper_consonants_list[j]
    return transpose_dict

print(build_transpose_dict('eaiou'))
