from .convert_codewars_test_to_pytest import convert_test


def test_spaghetti():
    assert convert_test("Test.assert_equals(pig_latin(\"spaghetti\"), \"aghettispay\")") == \
           "assert pig_latin(\"Spaghetti\") == \"aghettispay\""

def test_piglatin_map():
    assert convert_test("Test.assert_equals(pig_latin(\"map\"), \"apmay\")") == \
            "assert pig_latin(\"map\") == \"apmay\""

def test_piglatin_sentence1():
    assert convert_test("Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')") == \
            "assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'"




Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')

Test.assert_equals(pig_latin("egg"), "eggway")




