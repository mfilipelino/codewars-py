from codewars.camelcase import to_camel_case


def test_case_basic():
    assert '' == to_camel_case('')


def test_case_simple():
    assert 'theStealthWarrior' == to_camel_case("the-stealth-warrior")
    assert 'TheStealthWarrior' == to_camel_case('The-Stealth-Warrior')
    assert 'ABC' == to_camel_case('A-B-C')

