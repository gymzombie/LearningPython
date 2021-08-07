
import re
# TODO: Upgrade this from a list of one-liners to just straight "make a test file with all the tests in it"

regex = r"[Tt]est\.assert_equals\((?P<function>[\w]+)\((?P<orig_test>[\'\"\w\d\s\,\#]+)\)\,[\s]+(?P<success_criteria>[\'\"\w\d\s\,\#]+)\)"

# Add tests from kata here
test_str = ('  test.assert_equals(count_deaf_rats("~O~O~O~O P"), 0) \
    test.assert_equals(count_deaf_rats("P O~ O~ ~O O~"), 1) \
    test.assert_equals(count_deaf_rats("~O~O~O~OP~O~OO~"), 2) \
            ')


def convert_test(test_val):
    matches = re.search(regex, test_str)
    function = matches.group('function')
    orig_test = matches.group('orig_test')
    success_criteria = matches.group('success_criteria')

    pass


print(convert_test(test_str))
