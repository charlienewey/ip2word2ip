#! /usr/bin/env python2

def read_wordlist(path):
    with open(path, "r") as in_file:
        words = [line.rstrip() for line in in_file][0:65536]
        assert len(words) == 65536
    return words

def base256_to_base65536(ip):
    # probably a better way to do this but hey ho
    blocks = [int(block) for block in ip.split(".")]
    num = 0
    for block in blocks:
        num *= 256
        num += (block)

    n = 65536
    digits = []
    if num == 0:
        digits.insert(0, 0)
    while num > 0:
        digits.insert(0, num % n)
        num = num // n

    return digits

def ip_to_words(digits):
    return ".".join([words[d] for d in digits])


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
    for ip in args.ips:
        base65536 = base256_to_base65536(ip)
        print(ip_to_words(base65536))
