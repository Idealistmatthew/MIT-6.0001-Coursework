# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    ## Applying the base case
    if len(sequence) == 1:
        return sequence

    else:
        ## making a list out of the letters
        letter_list = list(sequence)
        ## storing the letter to be concatenated recursively
        concat_letter = letter_list[0]
        ## making a list to store the final permutations
        inductive_permutations = []
        ## removing the frontmost letter from the list
        del letter_list[0]
        ## applying recursion on the function
        sub_permutations = get_permutations(letter_list)
        ## looping through the permutations obtained via recursion
        for permutation in sub_permutations:
            ## loop to add the concat_letter to every possible position within the permutation
            for i in range(len(permutation) + 1):
                ## making the permutation into a list of letters
                new_word_list = list(permutation)
                ## inserting the concat_letter into position i
                new_word_list.insert(i,concat_letter)
                ## join the list to form the permutation
                new_permutation = ''.join(new_word_list)
                ## append the permutation to the final list
                inductive_permutations.append(new_permutation)

    return inductive_permutations

if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
