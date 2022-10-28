import string

from algorithms.task1.search import kmp_search, naive_search, sundays_search
from algorithms.task1.utils import compute, create_csv, generate

if __name__ == "__main__":
    functions = [naive_search, sundays_search, kmp_search]

    # text_len
    create_csv("text_len")
    for _ in range(1):
        dictionary = generate(length=5)
        pattern = generate(length=3)
        for text_len in range(1, 40):
            text = generate(dictionary=dictionary, length=text_len)

            compute(functions=functions, pattern=pattern, text=text, value_name="text_len", value=text_len)

    # dictionary_len
    create_csv("dictionary_len")
    for _ in range(1):
        for dictionary_len in range(1, len(string.ascii_lowercase)):
            dictionary = generate(length=dictionary_len)
            text = generate(dictionary=dictionary, length=100)
            pattern = generate(dictionary=dictionary, length=6)

            compute(functions=functions, pattern=pattern, text=text, value_name="dictionary_len", value=dictionary_len)

    # pattern_len
    create_csv("pattern_len")
    for _ in range(1):
        dictionary = generate(length=5)
        text = generate(dictionary=dictionary, length=50)
        for pattern_len in range(1, 20):
            pattern = generate(dictionary=dictionary, length=pattern_len)

            compute(functions=functions, pattern=pattern, text=text, value_name="pattern_len", value=pattern_len)
