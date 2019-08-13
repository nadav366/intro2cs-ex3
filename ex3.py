def input_list():
    """
    A function that accepts a string input into list (empty string to stop)
    :return: List value, input strinf list
    """
    inp_list = []
    one_inp = input()  # first input
    while one_inp is not "":  # Receiving input up to an empty string
        inp_list.append(one_inp)
        one_inp = input()
    return inp_list


def concat_list(str_list):
    """
    A function that concatenates a string list into a single string,
     with spaces between the strings.
    :param str_list: List value, list of strings
    :return: String value, The entire list is connected to one string.
    """
    tot_str = ""
    for index in range(len(str_list) - 1):  # All string, except last
        tot_str += str_list[index] + " "  # Add cell and space
    tot_str += str_list[len(str_list) - 1]  # Adds the last cell
    return tot_str



def maximum(num_list):
    """
    A function that receives a list of numbers and returns the maximum
    :param num_list: List value, List of numbers
    :return: Numeric value, the maximum
    """
    if len(num_list) == 0:  # empty list
        return None

    bigger = num_list[0]
    for index in range(1, len(num_list)):
        if num_list[index] > bigger:
            bigger = num_list[index]
    return bigger


def move(lst1, lst2, i):
    """
    A function that accepts lists and a number, and checks whether
    the lists are the same list that is moved by the number
    :param lst1: List value, List of numbers
    :param lst2: List value, List of numbers
    :param i: Numeric value, How much to move
    :return: Boolean value, if the lists are the same but moved by the number
    """
    for place in range(len(lst1)):
        if lst1[place] != lst2[(place+i) % len(lst1)]:
            return False
    return True


def cyclic(lst1, lst2):
    """
    A function that accepts two lists of numbers and
     checks whether they are moving one another
    :param lst1: List value, List of numbers
    :param lst2: List value, List of numbers
    :return: Boolean value, if the lists are the same but moved by some number
    """
    # Check whether the lists are the same length or empty
    if len(lst1) != len(lst2):
        return False
    if len(lst1) == 0:
        return True

    for i in range(len(lst1)):  # Goes through all the sliding options
        if move(lst1, lst2, i):
            return True
    return False


BAD_NUM = 7


def seven_boom(num):
    """
    A function that receives a number and returns the
     results of the game seven boom up to it
    :param num: Int valueS
    :return: List value, List of strings, game results
    """
    lst = []
    for index in range(num):
        # Checking "bad" cases
        if (index + 1) % BAD_NUM == 0 or str(BAD_NUM) in str(index + 1):
            lst.append("boom")
        else:
            lst.append(str(index + 1))
    return lst


def histogram(n, num_list):
    """
    A function that receives an n number and a list of
    numbers and returns a list with the number of times
    each number to n is listed
    :param n: Int value, The range of numbers
    :param num_list: List value, List of numbers
    :return: List value, List of numbers, How many times each number appear
    """
    count_list = [0] * n  # List with n zeros
    for index in range(len(num_list)):
        count_list[num_list[index]] += 1
    return count_list


def prime_factors(num):
    """
    A function that decomposes each number into its primes factors
    :param num: Int value
    :return: List value, List of numbers, the decomposes of the number
    """
    factors_lst = []
    for index in range(2, num + 1):
        if num % index == 0:  # Checks whether the index divides the number
            factors_lst.append(index)  # Adds the index to the list
            factors_lst += prime_factors(num // index)  # Checks the decomposition-
            # of the number divided by the index and adds it to the list
            break
    return factors_lst


def cartesian(lst1, lst2):
    """
    A function that calculates the Cartesian product between two lists
    :param lst1: List value
    :param lst2: List value
    :return: List value, With lists of pairs, which are cartesian multiples
    """
    tot_lst = []
    for cell2 in lst2:
        for cell1 in lst1:
            tot_lst.append([cell1, cell2])
    return tot_lst


def pairs(num_list, n):
    """
    A function that receives a list of numbers, and a n number
    returns a list with number pairs from the list whose sum is n
    :param num_list: List value, List of numbers
    :param n: Int value
    :return: List value, With lists of pairs, Whose sum is n
    """
    pair_lst = []
    for i1 in range(len(num_list)):  # Passes all the numbers in the list
        for i2 in range(i1 + 1, len(num_list)):  # all the numbers from i1 onwards
            if num_list[i1] + num_list[i2] == n:
                pair_lst.append([num_list[i1], num_list[i2]])
    return pair_lst


print(concat_list([]))