# Anagram-Generator

This code is an anagram generator that takes an input text from the user and generates all possible anagrams from the text.

An anagram is a word or phrase that is made by rearranging the letters of another word or phrase. For example, the word "listen" can be rearranged to form "silent". Anagram generators are tools that help you find all possible anagrams of a given word or phrase.

You might be wondering, `"Why do I need an anagram generator?"` Well, there are many reasons! For example, anagrams can be a fun way to create new words and phrases, and they can also be used in puzzles and games. Additionally, anagram generators can be useful tools for language learners, as they can help you practice spelling and vocabulary.

By working on this project, you will gain knowledge about how to generate all possible anagrams of a given word or phrase using Python. You will also learn how to filter out meaningful words from the list of anagrams using a Python library called `enchant`. This project will help you build your programming skills, improve your problem-solving abilities, and give you a better understanding of how to use Python to solve real-world problems.

## Functions and Modules

This code has two functions:

# `generate_anagrams(text)`

This function takes an input text and generates all possible anagrams from the text. It uses the `permutation()` function from the `itertools` module to generate all possible combinations of letters in the input text. The generated anagrams are appended to the perms list, duplicates and the original text are removed and the unique permutations are returned as a list.

# `find_meaningful_words(anagrams)`

This function takes a list of anagrams and filters out meaningful words from the list. It uses the `enchant` module to check whether each word in the list is a valid English word or not. If a word is valid, it is added to the `meaningful_words` list. The function then returns the list of meaningful words.

## Task and Hints

# Task 1: Generating Anagrams

Your task is to create a loop that will iterate over the input text using the `permutations()` function from the `itertools` module. You will need to join the iterable elements using the `join()` built-in function and append the generated anagrams to the perms list.

**Hint:** You can use a `for` loop to loop over the permutations of the input text and use the `join()` function to join the iterable elements. Then, you can append the generated anagrams to the perms list.

# Task 2: Filtering Meaningful Words

Your task is to loop over the list of anagrams and filter out meaningful words from the list. You will need to use the `enchant` module to check whether each word in the list is a valid English word or not. If a word is valid, you should append it to the `meaningful_words` list.

**Hint:** You can use a `for` loop to loop over the list of anagrams and use the `check()` function from the `enchant` module to check whether each word is a valid English word or not. If a word is valid, you should append it to the `meaningful_words` list.

## What to do

See the comment inside the `generate_anagrams` function on what to do. Your console should be similar to the attached screenshot below

![image](https://user-images.githubusercontent.com/73473767/222304011-81b1c1ad-d7f1-4419-9e94-2e31e2915db6.png)

## To get started

You will need to install the dependency package provides by Python language bindings for the Enchant spellchecking library.

```pip
pip install pyenchant
```

For more information, visit the project website: http://pyenchant.github.io/pyenchant/. To learn how to use this package, visit the python documentation website: https://pypi.org/project/pyenchant/
