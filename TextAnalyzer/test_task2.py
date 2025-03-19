import tempfile
import os
from task2 import KSeqCounter
import test_contents as content
import constants as c
import json

def test_kseqcounter_init_with_processed_data():
    """
    Test that KSeqCounter correctly initializes when provided a preprocessed_data file path
    Assertions:
        1. Checks if preprocessed_data assigned correctly in the constructor
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0) 
        counter = KSeqCounter(processed_data=temp_file.name)
    assert json.loads(counter.processed_data) == json.loads(content.Q1_FINAL_RESULT), c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_file.name)

def test_kseq_count():
    """
    Test the function __kseq_count for counting sequences of words correctly
    Aseertions:
        1. Checks if the counter counts as expected
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        counter = KSeqCounter(processed_data=temp_file.name)
    kseq_result = counter._KSeqCounter__kseq_count(2)
    assert kseq_result == content.KSEQCOUNTER_RESULT, c.KSEQ_RESULTS_INCORRECT
    os.remove(temp_file.name)

def test_preprocessed_data_assignment():
    """
    Check that the assignment of preprocessed attribute is well-defined
    """
    counter = KSeqCounter()
    counter.processed_data = content.Q1_FINAL_RESULT
    assert content.Q1_FINAL_RESULT == counter.processed_data, c.PROCESSED_DATA_INCORRECT_ASSIGN

def test_task2_final_result_with_preprocessed_data():
    """
    Test that task2 correctly formats the output in JSON format, with preprocessed data given
    Assertions:
        1. Check if the output is as expected
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        counter = KSeqCounter(processed_data=temp_file.name)
        output_json = counter.task2(2)
        assert output_json == content.Q2_FINAL_RESULT, c.TASK2_RESULT_INCORRECT

def test_task2_final_result_without_preprocessed_data():
    """
    Test that task 2 formats the output in JSON format, without preprocessed data given
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
        counter = KSeqCounter(sentences_file_path=temp_sentences.name, names_file_path=temp_people.name, removewords_file_path=temp_removewords.name)
        output_json = counter.task2(2)
        assert output_json == content.Q2_FINAL_RESULT, c.TASK2_RESULT_INCORRECT
