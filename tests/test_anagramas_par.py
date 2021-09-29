from codewars.anagramas_par import anagrama_list, hash


def test_anagrama_list():
    print()
    print(anagrama_list(["abc", "bca", "lucas", "sacul"]))


def test_hash_anagrama_function():
    assert hash("abc") == hash("cba")
