from ex3 import *

def test_concat_list():
    assert concat_list([]) == "", "concat_list 1 test failed"
    print("concat_list test 1 passed")
    assert concat_list(["1","2","3","4","5"]) == "1 2 3 4 5", "concat_list 2 test failed"
    print("concat_list test 2 passed")
    assert concat_list([" "]) == " ", "concat_list 3 test failed"
    print("concat_list test 3 passed")
    assert concat_list(["h", "l", "e", "o"]) == "h l e o", "concat_list 4 " \
                                                           "test failed"
    print("concat_list test 4 passed")
    assert concat_list(["h"]) == "h", "concat_list 5 test failed"
    print("concat_list test 5 passed")
    assert concat_list([]) == "", "concat_list 6 test failed"
    print("concat_list test 6 passed")

def test_maximum():
    assert maximum([1,2,3]) == 3, "maximum 1 test failed"
    print("maximum test 1 passed")
    assert maximum([1.0,2.0,3.0]) == 3.0, "maximum 2 test failed"
    print("maximum test 2 passed")
    assert maximum([0,0,0,0,0]) == 0, "maximum 3 test failed"
    print("maximum test 3 passed")
    assert maximum([10, 10, 10.5]) == 10.5, "maximum 4 test failed"
    print("maximum test 4 passed")
    assert maximum([1,1,1,10, 1,1,1,1, 11]) == 11, "maximum 5 test failed"
    print("maximum test 5 passed")

def test_cyclic():
    assert cyclic([1,2], [2,1]), "cyclic 1 test failed"
    print("cyclic test 1 passed")
    assert cyclic([1,2,3], [3, 1, 2]),"cyclic 2 test failed"
    print("cyclic test 2 passed")
    assert not cyclic([1,3, 2], [1, 2, 3, 4]), "cyclic 3 test failed"
    print("cyclic test 3 passed")
    assert not cyclic([1,2,3,4],[4,4,4]), "cyclic 4 test failed"
    print("cyclic test 4 passed")
    assert cyclic([1], [1]), "cyclic 5 test failed"
    print("cyclic test 5 passed")
    assert cyclic([1, 2], [1, 2]), "cyclic 6 test failed"
    print("cyclic test 6 passed")
    assert cyclic([],[]), "cyclic 7 test failed"
    print("cyclic test 7 passed")
    assert not cyclic([],[1]), "cyclic 8 test failed"
    print("cyclic test 8 passed")


def test_seven_boom():
    assert seven_boom(3) == ["1", "2", "3"], "seven_boom 1 test failed"
    print("seven_boom test 1 passed")
    assert seven_boom(7) == ["1", "2", "3", "4", "5", "6", "boom"], \
        "seven_boom 2 test failed"
    print("seven_boom test 1 passed")
    assert seven_boom(77) == ['1', '2', '3', '4', '5', '6', 'boom', '8',
                              '9', '10', '11', '12', '13', 'boom', '15',
                              '16', 'boom', '18', '19', '20', 'boom', '22',
                              '23', '24', '25', '26', 'boom', 'boom', '29',
                              '30', '31', '32', '33', '34', 'boom', '36',
                              'boom', '38', '39', '40', '41', 'boom', '43',
                              '44', '45', '46', 'boom', '48', 'boom', '50',
                              '51', '52', '53', '54', '55', 'boom', 'boom',
                              '58', '59', '60', '61', '62', 'boom', '64',
                              '65', '66', 'boom', '68', '69', 'boom', 'boom',
                              'boom', 'boom', 'boom', 'boom', 'boom',
                              'boom'], "seven_boom 3 test failed"
    print("seven_boom test 1 passed")

def test_histogram():
    assert histogram(3, []) == [0, 0, 0], "histogram 1 test failed"
    print("histogram test 1 passed")
    assert histogram(3, [0]) == [1, 0, 0], "histogram 2 test failed"
    print("histogram test 2 passed")
    assert histogram(3, [1]) == [0, 1, 0], "histogram 3 test failed"
    print("histogram test 3 passed")
    assert histogram(3, [2]) == [0, 0, 1], "histogram 4 test failed"
    print("histogram test 4 passed")
    assert histogram(4, [3, 2, 3, 1, 3, 2]) == [0, 1, 2, 3], "histogram 5 " \
                                                             "test failed"
    print("histogram test 5 passed")
    assert histogram(5, [3]) == [0, 0, 0, 1, 0], "histogram 6 test failed"
    print("histogram test 6 passed")
    assert histogram(1, [0]) == [1], "histogram 7 test failed"
    print("histogram test 7 passed")


def test_prime_factors():
    assert prime_factors(1) == [], "prime_factors 1 test failed"
    print("prime_factors test 1 passed")
    assert prime_factors(2) == [2], "prime_factors 1 test failed"
    print("prime_factors test 2 passed")
    assert prime_factors(7) == [7], "prime_factors 1 test failed"
    print("prime_factors test 3 passed")
    assert prime_factors(14) == [2, 7], "prime_factors 1 test failed"
    print("prime_factors test 4 passed")
    assert prime_factors(100) == [2, 2, 5, 5], "prime_factors 1 test failed"
    print("prime_factors test 5 passed"),
    assert prime_factors(16) == [2, 2, 2, 2], "prime_factors 1 test failed"
    print("prime_factors test 6 passed")

def test_pairs():
    assert pairs([], 5) == [], "pairs 1 test failed"
    print("pairs test 1 passed")
    assert pairs([4], 5) == [], "pairs 2 test failed"
    print("pairs test 2 passed")
    assert pairs([5], 5) == [], "pairs 3 test failed"
    print("pairs test 3 passed")
    assert pairs([4, 1], 5) == [[4, 1]], "pairs 4 test failed"
    print("pairs test 4 passed")
    assert pairs([1,1,1,1,1,1], 3) == [], "pairs 5 test failed"
    print("pairs test 5 passed")
    assert pairs([1,1,1,1,1,1], 2) == [], "pairs 6 test failed"
    print("pairs test 6 passed")


def main():
    test_concat_list()
    test_maximum()
    test_cyclic()
    test_seven_boom()
    test_histogram()
    test_prime_factors()
    test_pairs()

if __name__ == "__main__":
    main()
