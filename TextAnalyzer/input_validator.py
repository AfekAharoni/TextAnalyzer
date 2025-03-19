# ===> Imports <=== 
import constants as c

def validate_task1(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 1 as dictionary and validate them
    There is 1 option of values to task 1:
        1. Get -s & -n & -r
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if (c.SENTENCES not in kwargs.keys()) or (c.NAMES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()):
        # if one of the following isn't supplied to the task: sentences_file_path, names_file_path, rmovewords_file_path
        print(c.INVALID_ARGUMENTS[c.Q1])
        return False
    if (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.NAMES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str):
        # if the type of the value isn't str as needs to be
        print(c.TYPE_OF_ARGUMENT_INVALID)
        return False
    try:
        # check if can open those files before task 1 do
        try_open_file(kwargs[c.SENTENCES])
    except (FileNotFoundError, PermissionError, IOError, TypeError): 
        print(c.SENTENCES_FILE_INVALID)
        return False
    try:
        try_open_file(kwargs[c.NAMES])
    except (FileNotFoundError, PermissionError, IOError, TypeError): 
        print(c.NAMES_FILE_INVALID)
        return False
    try:
        try_open_file(kwargs[c.UNWANTED_WORDS])
    except (FileNotFoundError, PermissionError, IOError, TypeError): 
        print(c.REMOVEWORDS_FILE_INVALID)
        return False
    return True # If got here, the input is valid

def validate_task2(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 2 as dictionary and validate them
    There are 2 options of values to task 2:
       1. Get --preprocessed & --maxk
       2. Get -s & -r & --maxk
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if kwargs[c.PREPROCESSED] is None: # option 2
        if (c.SENTENCES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()) or (c.MAXK_SEQ not in kwargs.keys()):
            print(c.INVALID_ARGUMENTS[c.Q2])
            return False
        elif (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str):
            # if the type of the value isn't str as needs to be
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        try:
            try_open_file(kwargs[c.SENTENCES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.SENTENCES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.UNWANTED_WORDS])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.REMOVEWORDS_FILE_INVALID)
            return False
        if not number_validation(kwargs[c.MAXK_SEQ]):
            print(c.MAXK_INVALID_INPUT)
            return False
    else: # option 1
        if c.MAXK_SEQ not in kwargs.keys():
            print(c.INVALID_ARGUMENTS[c.Q2])
            return False
        if not number_validation(kwargs[c.MAXK_SEQ]):
            print(c.MAXK_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.PREPROCESSED])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.PREPROCESSED_FILE_INVALID)
            return False
    return True

def validate_task3(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 3 as dictionary and validate them
    There are 2 options of values to task 3:
       1. Get --preprocessed 
       2. Get -s & -r & -n
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if kwargs[c.PREPROCESSED] is None: # option 2
        if (c.SENTENCES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()) or (c.NAMES not in kwargs.keys()):
            print(c.INVALID_ARGUMENTS[c.Q3])
            return False
        elif (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str) or ((type(kwargs[c.NAMES]) != str)):
        # if the type of the value isn't str as needs to be
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        try:
            try_open_file(kwargs[c.SENTENCES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.SENTENCES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.NAMES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.NAMES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.UNWANTED_WORDS])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.REMOVEWORDS_FILE_INVALID)
            return False
    else: # option 1
        if type(kwargs[c.PREPROCESSED])  != str:
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        try:
            try_open_file(kwargs[c.PREPROCESSED])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.PREPROCESSED_FILE_INVALID)
            return False
    return True

def validate_task4(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 4 as dictionary and validate them
    There are 2 options of values to task 4:
        1. Get --preprocessed & --qsek_query_path
        2. Get -s & -r & --qsek_query_path
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if kwargs[c.PREPROCESSED] is None: # option 2
        if (c.SENTENCES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()) or (c.QSEK not in kwargs.keys()):
            print(c.INVALID_ARGUMENTS[c.Q4])
            return False
        elif (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str) or ((type(kwargs[c.QSEK])) != str):
            # if the type of the value isn't str as needs to be
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        try:
            try_open_file(kwargs[c.SENTENCES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.SENTENCES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.QSEK])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.QSEK_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.UNWANTED_WORDS])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.REMOVEWORDS_FILE_INVALID)
            return False
    else: # option 1
        if (type(kwargs[c.PREPROCESSED]) != str) or ((type(kwargs[c.QSEK])) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        try:
            try_open_file(kwargs[c.QSEK])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.QSEK_FILE_INVALID)
            return False 
        try:
            try_open_file(kwargs[c.PREPROCESSED])
        except:
            print(c.PREPROCESSED_FILE_INVALID)
            return False
    return True

def validate_task5(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 5 as dictionary and validate them
    There are 2 options of values to task 5:
        1. Get --preprocessed & --maxk
        2. Get -s & -n & -r & --maxk
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if kwargs[c.PREPROCESSED] is None: # option 2
        if (c.SENTENCES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()) or (c.NAMES not in kwargs.keys()) \
              or (c.MAXK_SEQ not in kwargs.keys()):
            print(c.INVALID_ARGUMENTS[c.Q5])
            return False
        elif (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str) or (type(kwargs[c.NAMES]) != str):
            # if the type of the value isn't str as needs to be
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        if not number_validation(kwargs[c.MAXK_SEQ]):
            print(c.MAXK_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.SENTENCES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.SENTENCES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.NAMES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.NAMES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.UNWANTED_WORDS])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.REMOVEWORDS_FILE_INVALID)
            return False
    else: # option 1
        if (type(kwargs[c.PREPROCESSED]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.MAXK_SEQ]):
            print(c.MAXK_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.PREPROCESSED])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PREPROCESSED_FILE_INVALID)
            return False 
    return True

def validate_task6(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 6 as dictionary and validate them
    There are 2 options of values to task 6:
        1. Get --preprocessed & --windowsize & --threshold
        2. Get -s & -n & -r & --windowsize & --threshold
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if kwargs[c.PREPROCESSED] is None: # option 2
        if (c.SENTENCES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()) or (c.NAMES not in kwargs.keys()) \
              or (c.THRESHOLD not in kwargs.keys()) or (c.WINSIZE not in kwargs.keys()):
            print(c.INVALID_ARGUMENTS[c.Q6])
            return False
        elif (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str) or (type(kwargs[c.NAMES]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.THRESHOLD]):
            print(c.THRESHOLD_INVALID_INPUT)
            return False
        elif not number_validation(kwargs[c.WINSIZE]):
            print(c.WINSIZE_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.SENTENCES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.SENTENCES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.NAMES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.NAMES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.UNWANTED_WORDS])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.REMOVEWORDS_FILE_INVALID)
            return False
        if kwargs[c.WINSIZE] > count_number_of_sentences(kwargs[c.SENTENCES]):
            print(c.WINSIZE_GREATER_THAN_SENTENCES)
            return False
    else: # option 1
        if (type(kwargs[c.PREPROCESSED]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.THRESHOLD]):
            print(c.THRESHOLD_INVALID_INPUT)
            return False
        elif not number_validation(kwargs[c.WINSIZE]):
            print(c.WINSIZE_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.PREPROCESSED])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PREPROCESSED_FILE_INVALID)
            return False 
        if kwargs[c.WINSIZE] > count_number_of_sentences(kwargs[c.SENTENCES]):
            print(c.WINSIZE_GREATER_THAN_SENTENCES)
            return False
    return True

def validate_task7(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 7 as dictionary and validate them
    There are 2 options of values to task 7:
        1. Get --preprocessed & --PAIRS & --maximal_distance
        2. Get -s & -n & -r & --windowsize & --threshold & --pairs & --maximal_distance
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if kwargs[c.PREPROCESSED] is None: # option 2
        if (c.SENTENCES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()) or (c.NAMES not in kwargs.keys()) \
              or (c.THRESHOLD not in kwargs.keys()) or (c.WINSIZE not in kwargs.keys()) \
              or (c.PAIRS not in kwargs.keys()) or (c.MAXDISTANCE not in kwargs.keys()):
            print(c.INVALID_ARGUMENTS[c.Q7])
            return False
        elif (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str) \
            or (type(kwargs[c.NAMES]) != str) or (type(kwargs[c.PAIRS]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.THRESHOLD]):
            print(c.THRESHOLD_INVALID_INPUT)
            return False
        elif not number_validation(kwargs[c.WINSIZE]):
            print(c.WINSIZE_INVALID_INPUT)
            return False
        elif not number_validation(kwargs[c.MAXDISTANCE]):
            print(c.MAXDISTANCE_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.SENTENCES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.SENTENCES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.NAMES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.NAMES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.UNWANTED_WORDS])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.REMOVEWORDS_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.PAIRS])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PAIRS_FILE_INVALID)
            return False
        if kwargs[c.WINSIZE] > count_number_of_sentences(kwargs[c.SENTENCES]):
            print(c.WINSIZE_GREATER_THAN_SENTENCES)
            return False
    else: # option 1
        if (type(kwargs[c.PREPROCESSED]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.MAXDISTANCE]):
            print(c.MAXDISTANCE_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.PAIRS])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PAIRS_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.PREPROCESSED])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PREPROCESSED_FILE_INVALID)
            return False
    return True

def try_open_file(filename: str):
    """
    This function gets a filename and tries to open it, if can't raise an exception
    :param filename: A filename
    """
    try:
        file = open(filename, 'r')
        file.close()
    except (FileNotFoundError, PermissionError, IOError, TypeError) as e:
        raise e

def number_validation(number: int) -> bool:
    """
    This function gets a number and check if it's an itenger, and if it's positive
    :param number: a number (threshold, windows_size, maxk or maximal_distance)
    :return: True if valid, False else
    """
    if type(number) != int:
        return False
    if number < 0:
        return False
    return True

def count_number_of_sentences(sentences_path: str) -> int:
    """
    This function gets a sentences file path and return the number of sentences (lines)
    :param sentences_path: Path of sentences file
    :return: Number of sentences in the file (lines)
    """
    with open(sentences_path, mode = 'r') as f:
        counter = len(f.readlines())
    return counter

# ==> EXTENSIONS <==

def validate_task8(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 8 as dictionary and validate them
    There are 2 options of values to task 8:
        1. Get --preprocessed & --pairs & --fixed_length
        2. Get -s & -n & -r & --windowsize & --threshold & --pairs & --fixed_length
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if kwargs[c.PREPROCESSED] is None: # option 2
        if (c.SENTENCES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()) or (c.NAMES not in kwargs.keys()) \
              or (c.THRESHOLD not in kwargs.keys()) or (c.WINSIZE not in kwargs.keys()) \
              or (c.PAIRS not in kwargs.keys()) or (c.FIXED_LEN not in kwargs.keys()):
            print(c.INVALID_ARGUMENTS[c.Q8])
            return False
        elif (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str) \
            or (type(kwargs[c.NAMES]) != str) or (type(kwargs[c.PAIRS]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.THRESHOLD]):
            print(c.THRESHOLD_INVALID_INPUT)
            return False
        elif not number_validation(kwargs[c.WINSIZE]):
            print(c.WINSIZE_INVALID_INPUT)
            return False
        elif not number_validation(kwargs[c.FIXED_LEN]):
            print(c.FIXEDLEN_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.SENTENCES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.SENTENCES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.NAMES])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.NAMES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.UNWANTED_WORDS])
        except (FileNotFoundError, PermissionError, IOError, TypeError): 
            print(c.REMOVEWORDS_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.PAIRS])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PAIRS_FILE_INVALID)
            return False
        if kwargs[c.WINSIZE] > count_number_of_sentences(kwargs[c.SENTENCES]):
            print(c.WINSIZE_GREATER_THAN_SENTENCES)
            return False
    else: # option 1
        if (type(kwargs[c.PREPROCESSED]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.FIXED_LEN]):
            print(c.FIXEDLEN_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.PAIRS])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PAIRS_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.PREPROCESSED])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PREPROCESSED_FILE_INVALID)
            return False
    return True

def validate_task9(**kwargs) -> bool:
    """
    This function gets all the arguments given to task 9 as dictionary and validate them
    There are 2 options of values to task 8:
        1. Get --preprocessed & --threshold
        2. Get -s & -r & --threshold
    :param **kwargs: Dictionary of arguments
    :return: True if valid, False else
    """
    if kwargs[c.PREPROCESSED] is None: # option 2
        if (c.SENTENCES not in kwargs.keys()) or (c.UNWANTED_WORDS not in kwargs.keys()) or (c.THRESHOLD not in kwargs.keys()):
            print(c.INVALID_ARGUMENTS[c.Q9])
            return False
        elif (type(kwargs[c.SENTENCES]) != str) or (type(kwargs[c.UNWANTED_WORDS]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.THRESHOLD]) or kwargs[c.THRESHOLD] == 0:
            print(c.THRESHOLD_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.SENTENCES])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.SENTENCES_FILE_INVALID)
            return False
        try:
            try_open_file(kwargs[c.UNWANTED_WORDS])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.REMOVEWORDS_FILE_INVALID)
            return False
    else: # option 1
        if (type(kwargs[c.PREPROCESSED]) != str):
            print(c.TYPE_OF_ARGUMENT_INVALID)
            return False
        elif not number_validation(kwargs[c.THRESHOLD]) or kwargs[c.THRESHOLD] == 0:
            print(c.THRESHOLD_INVALID_INPUT)
            return False
        try:
            try_open_file(kwargs[c.PREPROCESSED])
        except (FileNotFoundError, PermissionError, IOError, TypeError):
            print(c.PREPROCESSED_FILE_INVALID)
            return False
    return True