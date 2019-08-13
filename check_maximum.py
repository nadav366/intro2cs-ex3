from ex3 import maximum


def test():
    """
    Test for the maximum function
    Prints a result for each test, and a general result - is everything okay
    :return: Boolean value, if the test succeeded
    """
    flag = True

    if maximum([]) is not None:
        print("test 1 is fail")
        flag = False
    else:
        print("test 1 is OK")

    if maximum([2, 5]) != 5:
        print("test 2 is fail")
        flag = False
    else:
        print("test 2 is OK")

    if maximum([-65, -32, -73]) != -32:
        print("test 3 is fail")
        flag = False
    else:
        print("test 3 is OK")

    if maximum([1.00087, 1.001, 0.000015]) != 1.001:
        print("test 4 is fail")
        flag = False
    else:
        print("test 4 is OK")

    if maximum([-34, 0.1, 54, 99.9, -15.4]) != 99.9:
        print("test 5 is fail")
        flag = False
    else:
        print("test 5 is OK")

    if maximum([0, 0, 0]) != 0:
        print("test 6 is fail")
        flag = False
    else:
        print("test 6 is OK")

    if flag:  # Check if everything is all right
        print("The test succeeded")
    else:
        print("The test fail")

    return flag


if __name__ == '__main__':
    """
    main function
    """
    test()
