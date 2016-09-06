#! /usr/bin/env python2

def read_wordlist(path):
    with open(path, "r") as in_file:
        words = [line.rstrip() for line in in_file][0:65536]
        assert len(words) == 65536
    return words

def words_to_ip(phrase):
    import bisect
    w = phrase.split(".")
    indices = [bisect.bisect_left(words, i) for i in w]
    base256 = [base65536_to_base256(i) for i in indices]
    return ".".join([str(item) for sublist in base256 for item in sublist])

def base65536_to_base256(i):
    q, r = divmod(i, 256)
    return (q, r)


DEFAULT_PATH = "wordlist.txt"
if __name__ == "__main__":
    import sys
    import argparse

    # argument parsing
    p = argparse.ArgumentParser(description="Convert an IP address into a two-word phrase.")
    p.add_argument("--wordlist", dest="path", default=DEFAULT_PATH)
    p.add_argument(dest="ips", nargs="*")
    args = p.parse_args()

    # main logic
    path = args.path
    words = read_wordlist(path)
    for phrase in args.ips:
        print(words_to_ip(phrase))
