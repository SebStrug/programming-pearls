"""Implement an Anagram Program

From 2.8 of Programming Pearls (2nd ed.) by Jon Bentley
"""

from typing import Iterator, Tuple, List, Dict
from pathlib import Path
from collections import defaultdict
from operator import itemgetter
import argparse


def load_words() -> Iterator[str]:
    """Iterate through words that do not contain punctuation
    or numbers.

    Words file from https://github.com/dwyl/english-words
    """
    fname = Path(__file__).parent / "words_alpha.txt"
    for word in fname.open("r"):
        yield word.strip()


def sign_words(words: Iterator[str]) -> Tuple[str, str]:
    """Sign words, the signature is the sorted word.
    Store in a sorted dictionary

    Args:
        Iterator that provides words

    Returns:
        Set of <sorted word>:<original word> tuples, sorted
        by the first element in each tuple (i.e. sorted word)
    """
    signed_words = []
    while True:
        try:
            word = next(words)
        except StopIteration:
            break
        else:
            signature = "".join(sorted(word))
            signed_words.append((signature, word))
    return signed_words


def sort_signed_words(signed_words: Tuple[str, str]) -> Tuple[str, str]:
    """Sort the set of signature-word tuples by the signature

    Order of the second words is irrelevant.
    """
    signed_words.sort(key=itemgetter(0))
    return signed_words


def squash_signed_words(
    signed_words: Tuple[str, str]
) -> Dict[str, List[str]]:
    """Given a set of <signatures>:<words> sorted by signature
    combine all the signatures to produce a list of each original
    word next to the signatures

    Args:
        Set of of <signatures><original-word>, sorted by signature

    Returns:
        Dictionary of <signature>:<list-of-associated-words>
    """
    squashed_words = defaultdict(list)

    current_signature = signed_words[0][0]
    for signature, word in signed_words:
        squashed_words[signature].append(word)
        if signature != current_signature:
            current_signature = signature
    return squashed_words


def get_parsed_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Find all anagrams of a word')
    parser.add_argument('--word', dest='word', type=str,
                        help='word to get anagrams for')
    return parser


def main():
    # Turn list of English words into dict of <signature>:<list-of-associated-words>
    words = load_words()
    signed_words = sign_words(words)
    # Guard by closing the dictionary
    words.close()
    sorted_words = sort_signed_words(signed_words)
    squashed_words = squash_signed_words(sorted_words)

    # Given an input word, return the anagrams of said word.
    parser = get_parsed_args()
    args = parser.parse_args()
    sorted_input_word = ''.join(sorted(args.word))
    print(squashed_words.get(sorted_input_word))


if __name__ == "__main__":
    main()
