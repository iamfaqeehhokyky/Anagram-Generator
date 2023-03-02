import enchant
from itertools import permutations


def generate_anagrams(text):
    """
    Generate anagrams from input text
    """
    # Generate all permutations of the input text
    perms = []

    """Task 1:"""
    # Create a loop to loop over the input text using the permutation function from the itertools module
    # The permutations will split each words into a chunk of letters, so you may want to join the iterable elements
    # using the join() python built-in function.
    # Append this inside the perms list above.
    # Write your code for the first task beneath this line

    # Write your code for the first task above this line

    # Remove duplicates and the original text
    unique_perms = set(perms)
    unique_perms.remove(text)

    # Return the unique permutations as a list
    return list(unique_perms)


def find_meaningful_words(anagrams):
    """
    Filter out meaningful words from list of anagrams
    """
    # Initialize dictionary
    d = enchant.Dict("en_US")

    # Loop over list of anagrams and add meaningful words to new list
    meaningful_words = []
    for word in anagrams:
        if d.check(word):
            meaningful_words.append(word)

    # Return list of meaningful words
    return meaningful_words


# Test the functions with some input text
text = input("Enter a word to see it's anagram: ").lower()
anagrams = generate_anagrams(text)
meaningful_words = find_meaningful_words(anagrams)
print()
print()
print(f"Anagrams of '{text}': {anagrams}")
print()
print()
print(f"Meaningful words from anagrams: {meaningful_words}")
