def reverse(words: str) -> str:
    words_split = words.split(" ")
    print(words_split)
    words_reversed = words_split[::-1]

    result = " ".join(words_reversed)

    return result



print(reverse("Hamlet geu"))
print(reverse("Hello World!"))
print(reverse("Python is fun"))