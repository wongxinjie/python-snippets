import collections


def find_anagrams(words):
    word_dict = collections.defaultdict(list)
    for s in words:
        word_dict[''.join(sorted(s))].append(s)

    return [s for s in word_dict.values() if len(s) >= 2]


if __name__ == "__main__":
    r = find_anagrams(
        ['debitcard', 'elvis', 'slient', 'badcredit', 'lives',
         'freedom', 'listen'])
    print(r)
