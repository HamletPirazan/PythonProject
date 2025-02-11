import re

def count_word_occurrences(text, target_word):
    pattern = r'\b' + re.escape(target_word) + r'\b'
    return len(re.findall(pattern, text, re.IGNORECASE))

print(count_word_occurrences("The quick brown fox jumps over the lazy dog.", "the"))
print(count_word_occurrences("This is a test sentence. This sentence is a test.", "sentence"))
print(count_word_occurrences("Python is a versatile programming language.", "Python"))
print(count_word_occurrences("No matches here.", "word"))