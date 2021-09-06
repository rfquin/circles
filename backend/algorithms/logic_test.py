'''Testing logic. This will include hard coded data tests. We want to
ensure our algorithms work as expected.

If these tests work, we can expect that the core logic works.
'''

from conditions import *
import pytest


def create_student_3707_COMPA1():
    user = User()
    user.add_program("3707")
    user.add_specialisation("COMPA1")
    return user


def test_no_condition():
    user = create_student_3707_COMPA1()

    no_cond = create_condition(["(", ")"])[0]
    assert no_cond.validate(user) == True

    # Should work even if the user has taken courses already
    user.add_courses({
        "COMP1511": (6, 75),
        "COMP1521": (6, 80)
    })

    assert no_cond.validate(user) == True


def test_course_condition():
    user = create_student_3707_COMPA1()

    single_cond = create_condition(["(", "COMP1511", ")"])[0]
    assert single_cond.validate(user) == False

    user.add_courses({
        "MATH1141": (6, 80)
    })
    assert single_cond.validate(user) == False

    user.add_courses({
        "COMP1511": (6, 80)
    })
    assert single_cond.validate(user) == True


def test_composite_condition_simple():
    '''AND/OR conditions with only course requirements'''
    user = create_student_3707_COMPA1()

    and_cond = create_condition(
        ["(", "COMP1511", "&&", "COMP1521", "&&", "COMP1531", ")"])
    assert and_cond.validate(user) == False

    user.add_courses({
        "COMP1511": (6, 80),
        "COMP1531": (6, None),
        "MATH1141": (6, None)
    })
    assert and_cond.validate(user) == False

    user.add_courses({
        "COMP1521": (6, None)
    })
    assert and_cond.validate(user) == True

    or_cond = create_condition(
        ["(", "MATH1081", "||", "MATH1151", "||", "MATH1241", ")"])
    assert or_cond.validate(user) == False

    user.add_courses({
        "MATH1151": (6, 90),
    })
    assert or_cond.validate(user) == True
