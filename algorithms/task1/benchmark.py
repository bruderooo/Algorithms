import csv
import string
from time import perf_counter_ns

from algorithms.task1.search import kmp_search, naive_search, python_naive_search, sundays_search
from algorithms.task1.utils import generate

ALL_SIGNS = string.ascii_letters + string.digits + string.whitespace


if __name__ == "__main__":
    functions = [naive_search, sundays_search, kmp_search, python_naive_search]

    with open("wyniki.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["count", "pattern_len", "text_len", "dictionary_len", "function", "time[ns]"])

    for _ in range(15):
        for dictionary_len in range(4, 18):
            dictionary = ALL_SIGNS[:dictionary_len]

            for text_len in range(100, 1000, 50):
                text = generate(dictionary=dictionary, length=text_len)

                for pattern_len in range(5, 12):
                    pattern = generate(dictionary=dictionary, length=pattern_len)

                    for func in functions:
                        start_time = perf_counter_ns()
                        count = func(text=text, pattern=pattern)
                        end_time = perf_counter_ns()

                        with open("wyniki.csv", "a", newline="") as f:
                            writer = csv.writer(f)
                            writer.writerow(
                                (count, pattern_len, text_len, dictionary_len, func.__name__, end_time - start_time)
                            )
