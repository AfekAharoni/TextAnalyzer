from task3 import PeopleMentions
import os
import test_contents as content
import constants as c
import json
import tempfile

def test_peoplementions_init_with_processed_data():
    """
    Test that PeopleMentions correctly initializes when provided a preprocessed_data file path
    Assertions:
        1. Checks if preprocessed_data assigned correctly in the constructor
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0) 
        counter = PeopleMentions(preprocessed_data=temp_file.name)
    assert json.loads(counter.preprocessed_data) == json.loads(content.Q1_FINAL_RESULT), c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_file.name)

def test_count_person_mentions():
    """
    Test that the person mentions counter works correctly
    Assertions:
        1. Checks if People Mentions counter return what expected
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
        people_mentions = PeopleMentions(sentences_file_path=temp_sentences.name, names_file_path=temp_people.name, removewords_file_path=temp_removewords.name)
        output = people_mentions.count_person_mentions()
        assert output == content.PEOPLE_MENTIONS_COUNTER, c.PEOPLE_MENTIONS_INCOREECT
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_people.name)

def test_task3_final_result_with_preprocessed_data():
    """
    Test that task 3 correctly formats the output in JSON format, with preprocessed data given
    Assertions:
        1. Check if the output is as expected
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        counter = PeopleMentions(preprocessed_data=temp_file.name)
        output_json = counter.task3()
        assert output_json == content.Q3_FINAL_RESULT, c.TASK3_RESULT_INCORRECT
    os.remove(temp_file.name)

def test_task3_final_result_without_preprocessed_data():
    """
    Test that task 3 formats the output in JSON format, without preprocessed data given
    Assertions:
        1. Checks if the output is as expected
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
        counter = PeopleMentions(sentences_file_path=temp_sentences.name, names_file_path=temp_people.name, removewords_file_path=temp_removewords.name)
        output_json = counter.task3()
        assert output_json == content.Q3_FINAL_RESULT, c.TASK3_RESULT_INCORRECT
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_people.name)
