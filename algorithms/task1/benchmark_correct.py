import string

from algorithms.task1.search import kmp_search, naive_search, python_naive_search, sundays_search
from algorithms.task1.utils import compute, create_csv, generate

if __name__ == "__main__":
    functions = [naive_search, sundays_search, kmp_search, python_naive_search]

    # text_len
    create_csv("text_len")
    for _ in range(10):
        dictionary = generate(length=10)
        pattern = generate(length=6)
        for text_len in (4**i for i in range(4, 30)):
            text = generate(dictionary=dictionary, length=text_len)

            compute(functions=functions, pattern=pattern, text=text, value_name="text_len", value=text_len)

    # dictionary_len
    create_csv("dictionary_len")
    for _ in range(10):
        for dictionary_len in range(2, len(string.ascii_letters), 3):
            dictionary = generate(length=dictionary_len)
            text = generate(dictionary=dictionary, length=200)
            pattern = generate(dictionary=dictionary, length=6)

            compute(functions=functions, pattern=pattern, text=text, value_name="dictionary_len", value=dictionary_len)

    # pattern_len
    create_csv("pattern_len")
    for _ in range(10):
        dictionary = generate(length=12)
        text = generate(dictionary=dictionary, length=500)
        for pattern_len in range(2, 51, 3):
            pattern = generate(dictionary=dictionary, length=pattern_len)

            compute(functions=functions, pattern=pattern, text=text, value_name="pattern_len", value=pattern_len)
