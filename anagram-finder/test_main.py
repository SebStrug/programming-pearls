from main import sign_words, sort_signed_words, squash_signed_words


def test_sign_words():
    words_list = ["pans", "pots", "opt", "snap", "stop", "tops"]
    words_gen = iter(words_list)
    expected_res = [
        ("anps", "pans"),
        ("opst", "pots"),
        ("opt", "opt"),
        ("anps", "snap"),
        ("opst", "stop"),
        ("opst", "tops"),
    ]

    res = sign_words(words_gen)
    print(res)
    assert len(res) == len(expected_res)
    assert all([a == b for a, b in zip(res, expected_res)])


def test_sort_signed_words():
    signed_words = [
        ("anps", "pans"),
        ("opst", "pots"),
        ("opt", "opt"),
        ("anps", "snap"),
        ("opst", "stop"),
        ("opst", "tops"),
    ]

    expected_res = [
        ("anps", "pans"),
        ("anps", "snap"),
        ("opst", "pots"),
        ("opst", "stop"),
        ("opst", "tops"),
        ("opt", "opt"),
    ]
    res = sort_signed_words(signed_words)
    assert len(res) == len(expected_res)
    assert all([a == b for a, b in zip(res, expected_res)])


def test_squash_signed_words():
    signed_words = [
        ("anps", "pans"),
        ("anps", "snap"),
        ("opst", "pots"),
        ("opst", "stop"),
        ("opst", "tops"),
        ("opt", "opt"),
    ]

    expected_res = {
        'anps': ['pans', 'snap'],
        'opst': ['pots', 'stop', 'tops'],
        'opt': ['opt']
    }
    res = squash_signed_words(signed_words)
    assert dict(res) == expected_res
