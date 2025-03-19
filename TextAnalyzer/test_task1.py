import tempfile
import os
from task1 import *
import test_contents as content
import constants as c


def test_text_preprocessing_init():
    """
    Test the initialization of the TextPreprocessing Class
    Creates temporary CSV files and check that the initlization of the attributes is well-defined
    Assertions:
        1. Checks if 'sentences' file path matches the path inserted, even if None value inserted
        2. Checks if 'removewords' file path matches the path inserted, even if None value inserted
        3. Checks if 'people' file path matches the path inserted, even if None value inserted
        4. Checks if 'sentences' attribute type is dictionary
        5. Checks if 'names' attribute type is list
        6. Checks if 'removewords' attribute type is list
    The temporary CSV files are created for testing only and deleted immediately afterward
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
         tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
            tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_people:
        temp_removewords.write("word\nunwanted_word1\nunwanted_word2\n")
        temp_removewords.seek(0) 
        temp_people.write("Names,Other Names\nAfekito,")
        temp_people.seek(0)
        temp_sentences.write("sentence\nThis is the first test")
        temp_sentences.seek(0)
        # Test people path None
        first_processing = TextPreprocessing(sentences_file_path=temp_sentences.name, removewords_file_path=temp_removewords.name, people_file_path=None)
        assert first_processing._TextPreprocessing__sentences_file_path == temp_sentences.name, c.SENTENCES_PATH_INCORRECT
        assert first_processing._TextPreprocessing__removewords_file_path == temp_removewords.name, c.REMOVEWORDS_PATH_INCORRECT
        assert first_processing._TextPreprocessing__people_file_path is None, c.PEOPLE_PATH_INCORRECT
        assert isinstance(first_processing._TextPreprocessing__sentences, dict), c.SENTENCES_TYPE_INCORRECT
        assert isinstance(first_processing._TextPreprocessing__names, list), c.NAMES_TYPE_INCORRECT
        assert isinstance(first_processing._TextPreprocessing__unwanted_words, list), c.REMOVEWORDS_TYPE_INCORRECT
        # Test sentences path None
        second_processing = TextPreprocessing(sentences_file_path=None, removewords_file_path=temp_removewords.name, people_file_path=temp_people.name)
        assert second_processing._TextPreprocessing__sentences_file_path is None, c.SENTENCES_PATH_INCORRECT
        assert second_processing._TextPreprocessing__removewords_file_path == temp_removewords.name, c.REMOVEWORDS_PATH_INCORRECT
        assert second_processing._TextPreprocessing__people_file_path == temp_people.name, c.PEOPLE_PATH_INCORRECT
        assert isinstance(second_processing._TextPreprocessing__sentences, dict), c.SENTENCES_TYPE_INCORRECT
        assert isinstance(second_processing._TextPreprocessing__names, list), c.NAMES_TYPE_INCORRECT
        assert isinstance(second_processing._TextPreprocessing__unwanted_words, list), c.REMOVEWORDS_TYPE_INCORRECT
        # Test removewords path None
        third_processing = TextPreprocessing(sentences_file_path=temp_sentences.name, removewords_file_path=None, people_file_path=temp_people.name)
        assert third_processing._TextPreprocessing__sentences_file_path == temp_sentences.name, c.SENTENCES_PATH_INCORRECT
        assert third_processing._TextPreprocessing__removewords_file_path is None, c.REMOVEWORDS_PATH_INCORRECT
        assert third_processing._TextPreprocessing__people_file_path == temp_people.name, c.PEOPLE_PATH_INCORRECT
        assert isinstance(third_processing._TextPreprocessing__sentences, dict), c.SENTENCES_TYPE_INCORRECT
        assert isinstance(third_processing._TextPreprocessing__names, list), c.NAMES_TYPE_INCORRECT
        assert isinstance(third_processing._TextPreprocessing__unwanted_words, list), c.REMOVEWORDS_TYPE_INCORRECT
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)

def test_text_preprocessing_attributes():
    """
    Test the initialization and attributes of the TextPreprocessing class
    Creates temporary CSV files contating predifined test data for sentences, name and unwanted words
    Assertions:
        1. Checks if 'sentences' attribute matches the expected sentence list.
        2. Checks if 'names' attribute matches the expected names list.
        3. Check if the 'unwanted_words' attribute matches the expected word list.
    The temporary CSV files are created for testing only and deleted immediately afterward
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
         tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
         tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_people:
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        temp_people.write(content.Q1_PEOPLE_CONTENT)
        temp_people.seek(0)
        text_preprocessing = TextPreprocessing(temp_sentences.name, temp_removewords.name, temp_people.name)
    assert text_preprocessing.sentences == content.Q1_SENTENCES_RESULT, c.SENTENCES_RESULT_INCORRECT
    assert text_preprocessing.names == content.Q1_PEOPLE_RESULT, c.PEOPLE_RESULT_INCORRECT
    assert text_preprocessing.unwanted_words == content.Q1_REMOVEWORDS_RESULT, c.REMOVEWORDS_RESULT_INCORRECT
    unwanted_words_list = ['all', 'the', 'unwanted', 'words']
    text_preprocessing.unwanted_words = unwanted_words_list
    assert text_preprocessing.unwanted_words == unwanted_words_list, c.REMOVE_UNWANTED_WORDS_INCORRECT
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_people.name)

def test_text_preprocessing_final_output():
    """
    Test task 1 final results
    Creates temporary CSV files contating predifined test data for sentences, name and unwanted words
    Assertions:
        1. Checks if the output mathces the expected task 1 output
    The temporary CSV files are created for testing only and deleted immediately afterward
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
         tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
         tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_people:
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        temp_people.write(content.Q1_PEOPLE_CONTENT)
        temp_people.seek(0)
        text_preprocessing = TextPreprocessing(temp_sentences.name, temp_removewords.name, temp_people.name)
        assert text_preprocessing.task1() == content.Q1_FINAL_RESULT, c.TASK1_RESULT_INCORRECT
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_people.name)

def test_remove_unwanted_words_from_string():
    """
    Test the remove_unwanted_words function to ensure it correctly removes unwanted words 
    Assertions:
        1. Checks if 'remove_unwanted_words' from task1.py file removes exactly the word it needs to
    """
    assert remove_unwanted_words("Programming", ["Programmer", "ing"]) == "Programming", c.REMOVE_UNWANTED_WORDS_INCORRECT
    assert remove_unwanted_words("Hello!", ["world"]) == "Hello!", c.REMOVE_UNWANTED_WORDS_INCORRECT
    assert remove_unwanted_words("Test", ["not in the sentence"]) == "Test", c.REMOVE_UNWANTED_WORDS_INCORRECT
    assert remove_unwanted_words("delete all words", ["delete", "all", "words"]) == "", c.REMOVE_UNWANTED_WORDS_INCORRECT
    assert remove_unwanted_words("", ["any"]) == "", c.REMOVE_UNWANTED_WORDS_INCORRECT
    assert remove_unwanted_words("Same", []) == "Same", c.REMOVE_UNWANTED_WORDS_INCORRECT

def test_remove_empty_strings_from_list():
    """
    Test the remove_empty_strings_from_list function to ensure it correctly removes all empty strings
    Assertions:
        1. Checks if 'remove_empty_strings_from_list' from task1.py file clears all the empty strings from the list
    """
    assert remove_empty_strings_from_list(["hello", "", "world", "", "Python"]) == ["hello", "world", "Python"], c.REMOVE_EMPTY_STRINGS_FROM_LIST_INCORRECT
    assert remove_empty_strings_from_list(["", "", "", ""]) == [], c.REMOVE_EMPTY_STRINGS_FROM_LIST_INCORRECT
    assert remove_empty_strings_from_list(["a", "b", "c"]) == ["a", "b", "c"], c.REMOVE_EMPTY_STRINGS_FROM_LIST_INCORRECT
    assert remove_empty_strings_from_list([]) == [], c.REMOVE_EMPTY_STRINGS_FROM_LIST_INCORRECT
    assert remove_empty_strings_from_list([" ", "", "   ", "word"]) == [" ", "   ", "word"], c.REMOVE_EMPTY_STRINGS_FROM_LIST_INCORRECT
    assert remove_empty_strings_from_list(["", "keep", "", "", "this", "", "words"]) == ["keep", "this", "words"], c.REMOVE_EMPTY_STRINGS_FROM_LIST_INCORRECT

def test_remove_punctuation():
    """
    Test the remove_punctuation function to ensure it correctly removes punctuation
    Assertions:
        1. Checks if 'remove_punctuation' from task1.py file clears a string from everything that isn't letter, number or space
    """
    assert remove_punctuation("Hello, world!") == "Hello  world ", c.REMOVE_PUNCTUATION_FROM_STRING_INCORRECT
    assert remove_punctuation("This project is so!!! fun!!") == "This project is so    fun  ", c.REMOVE_PUNCTUATION_FROM_STRING_INCORRECT
    assert remove_punctuation("Price: $100.50") == "Price   100 50", c.REMOVE_PUNCTUATION_FROM_STRING_INCORRECT
    assert remove_punctuation("Keep the same") == "Keep the same", c.REMOVE_PUNCTUATION_FROM_STRING_INCORRECT
    assert remove_punctuation("") == "", c.REMOVE_PUNCTUATION_FROM_STRING_INCORRECT
    assert remove_punctuation("!@#$%^&*()") == "          ", c.REMOVE_PUNCTUATION_FROM_STRING_INCORRECT
    assert remove_punctuation("Hello\nworld\t!") == "Hello\nworld\t ", c.REMOVE_PUNCTUATION_FROM_STRING_INCORRECT

def test_remove_unwanted_spaces():
    """
    Test the remove_unwanted_spaces function to ensure it correctly cleans unwanted spaces
    Assertions:
        1. Checks if 'remove_unwanted_spaces' from task1.py file clears all the unwanted spaces from a string, including duplications, suffix and prefix
    """
    assert remove_unwanted_spaces("Hello    world!") == "Hello world!", c.REMOVE_UNWANTED_SPACES_INCORRECT
    assert remove_unwanted_spaces("   Afekito   ") == "Afekito", c.REMOVE_UNWANTED_SPACES_INCORRECT
    assert remove_unwanted_spaces("  Multiple   spaces here   ") == "Multiple spaces here", c.REMOVE_UNWANTED_SPACES_INCORRECT
    assert remove_unwanted_spaces("Word") == "Word", c.REMOVE_UNWANTED_SPACES_INCORRECT
    assert remove_unwanted_spaces("     ") == "", c.REMOVE_UNWANTED_SPACES_INCORRECT
    assert remove_unwanted_spaces("NoSpacesHere") == "NoSpacesHere", c.REMOVE_UNWANTED_SPACES_INCORRECT
    assert remove_unwanted_spaces("\nHello\tWorld\n") == "Hello\tWorld", c.REMOVE_UNWANTED_SPACES_INCORRECT
    assert remove_unwanted_spaces("Hello \t World \n") == "Hello \t World", c.REMOVE_UNWANTED_SPACES_INCORRECT
    long_text = "  This   is   a   long   text  with     many   spaces   "
    expected_result = "This is a long text with many spaces"
    assert remove_unwanted_spaces(long_text) == expected_result, c.REMOVE_UNWANTED_SPACES_INCORRECT

def test_remove_duplication_names():
    """
    Test the remove_duplication_names function to ensure it correctly cleans duplications of names from names list
    Assertions:
        1. Checks if 'remove_duplication_names' from task1.py file clears all the duplication names from names list
    """
    text_processing = TextPreprocessing()
    text_processing.names = [
        [['Spongebob'], [['bob'], ['pineapple']]],  # first occurrence -> should be kept
        [['Spongebob'], [['bob'], ['squarepants']]],  # duplicated -> should be removed
        [['Patrick'], [['star']]],  # 
        [['Spongebob'], [['chef'], ['krabby']]],  # duplicated -> should be removed
        [['Sandy'], [['cheeks']]],  
    ]
    text_processing._TextPreprocessing__removes_duplication_names()
    expected_output = [
        [['Spongebob'], [['bob'], ['pineapple']]], 
        [['Patrick'], [['star']]],  
        [['Sandy'], [['cheeks']]],  
    ]
    assert text_processing.names == expected_output, c.REMOVE_DUPLICATED_NAMES_INCORRECT