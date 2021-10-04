from codewars.stack.evaluate_postfix import evaluate_post_fix


def test_stack_exaluate_post_fix():
    assert evaluate_post_fix("12+") == 3
    assert evaluate_post_fix("15*") == 5
    assert evaluate_post_fix("42/") == 2
    assert evaluate_post_fix("42/4*") == 8
    assert evaluate_post_fix("921*-8-4+") == 3
    assert evaluate_post_fix("642/+") == 8
