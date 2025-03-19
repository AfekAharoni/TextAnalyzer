from task5 import PeopleContexts
import os
import test_contents as content
import constants as c
import tempfile

def test_peoplecontext_init_with_processed_data():
    """
    Test that PeopleContext correctly initializes when provided a preprocessed_data file path
    Assertions:
        1. Checks if preprocessed_data assigned correctly in the constructor
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        people_context = PeopleContexts(preprocessed_data=temp_file.name, maxk=2)
        assert people_context.preprocessed_data == content.Q1_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_file.name)

def test_peoplecontext_init_without_processed_data():
    """
    Test that PeopleContext correctly initializes when preprocessed_data file path isn't provided
    Assertions:
        1. Checks if processed_data assigned correctly in the constructor
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_names:
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        temp_names.write(content.Q1_PEOPLE_CONTENT)
        temp_names.seek(0)
        people_context = PeopleContexts(sentences_file_path=temp_sentences.name, removewords_file_path=temp_removewords.name, names_file_path=temp_names.name, maxk=2)
        assert people_context.preprocessed_data == content.Q1_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_names.name)

def test_task5_final_result():
    """
    Test that task 5 formats the output in JSON format, without preprocessed data given
    Assertions:
        1. Checks if the output is as expected
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        people_context = PeopleContexts(preprocessed_data=temp_file.name, maxk=2)
        assert people_context.task5() == content.Q5_FINAL_RESULT, c.TASK5_RESULT_INCORRECT
    os.remove(temp_file.name)

def test_setters():
    """
    Test that PeopleContext correctly assign attributes with setters
    Assertions:
        1. Checks if sentences data assigned correctly
        2. Checks if unwanted words data assigned correctly
        3. Checks if names data assigned correctly
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        people_context = PeopleContexts(preprocessed_data=temp_file.name, maxk = 2)
        people_context.preprocessed_data = content.Q1_FINAL_RESULT_AS_DICT
        assert people_context.preprocessed_data == content.Q1_FINAL_RESULT_AS_DICT
    os.remove(temp_file.name)
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_names:
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        temp_names.write(content.Q1_PEOPLE_CONTENT)
        temp_names.seek(0)
        people_context = PeopleContexts(sentences_file_path=temp_sentences.name, removewords_file_path=temp_removewords.name, names_file_path=temp_names.name, maxk=2)
        people_context.sentences = content.Q1_SENTENCES_CONTENT
        assert people_context.sentences == content.Q1_SENTENCES_CONTENT, c.SENTENCES_INCORRECT_ASSIGN
        people_context.names = content.Q1_PEOPLE_CONTENT
        assert people_context.names == content.Q1_PEOPLE_CONTENT, c.NAMES_INCORRECT_ASSIGN
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_names.name)
