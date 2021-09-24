from codewars.balance_parathenses import balanced, recursive_balanced


def test_balanced_base():
    """
    test base
    :return:
    """

    assert balanced([")"]) == False
    assert balanced(["("]) == False


def test_balanced_cases():
    assert balanced(["(", ")"]) == True
    assert balanced(["(", "("]) == False
    assert balanced([")", ")"]) == False
    assert balanced(["(", ")", "("]) == False
    assert balanced(["(", ")", ")"]) == False


def test_recursive_balanced_base():
    """
    test base
    :return:
    """

    assert recursive_balanced([")"]) == False
    assert recursive_balanced(["("]) == False


def test_recursive_balanced_cases():
    assert recursive_balanced(["(", ")"]) == True
    assert recursive_balanced(["(", "("]) == False
    assert recursive_balanced([")", ")"]) == False
    assert recursive_balanced(["(", ")", "("]) == False
    assert recursive_balanced(["(", ")", ")"]) == False
