from task4 import SearchEngine
import os
import test_contents as content
import constants as c
import tempfile

def test_searchengine_init_with_processed_data():
    """
    Test that SearchEngine correctly initializes when provided a preprocessed_data file path and matches attribute assigned correctly
    Assertions:
        1. Checks if preprocessed_data assigned correctly in the constructor
        2. Checks if matches data well defined
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file, \
                tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_kseq_query_keys_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        temp_kseq_query_keys_file.write(content.KSEQ_QUERY_KEYS)
        temp_kseq_query_keys_file.seek(0)
        search_engine = SearchEngine(preprocessed_data=temp_file.name, kseq_file_path=temp_kseq_query_keys_file.name)
        assert search_engine.matches == content.Q4_MATCHES_RESULT, c.MATCHES_RESULT_INCORRECT
        assert search_engine.processed_data == content.Q1_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_file.name)
    os.remove(temp_kseq_query_keys_file.name)

def test_searchengine_init_without_processed_data():
    """
    Test that SearchEngine correctly initializes when preprocessed_data file path isn't provided
    Assertions:
        1. Checks if matches data well defined 
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_kseq_query_keys_file:
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        temp_kseq_query_keys_file.write(content.KSEQ_QUERY_KEYS)
        temp_kseq_query_keys_file.seek(0)
        search_engine = SearchEngine(sentences_file_path=temp_sentences.name, removewords_file_path=temp_removewords.name, kseq_file_path=temp_kseq_query_keys_file.name)
        assert search_engine.matches == content.Q4_MATCHES_RESULT, c.MATCHES_RESULT_INCORRECT
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_kseq_query_keys_file.name)

def test_task4_final_result_without_preprocessed_data():
    """
    Test that task 4 formats the output in JSON format, without preprocessed data given
    Assertions:
        1. Checks if the output is as expected
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_kseq_query_keys_file:
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        temp_kseq_query_keys_file.write(content.KSEQ_QUERY_KEYS)
        temp_kseq_query_keys_file.seek(0)
        search_engine = SearchEngine(sentences_file_path=temp_sentences.name, removewords_file_path=temp_removewords.name, kseq_file_path=temp_kseq_query_keys_file.name)
        assert search_engine.task4() == content.Q4_FINAL_RESULT, c.TASK4_RESULT_INCORRECT
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_kseq_query_keys_file.name)

def test_kseq_query_keys_with_empty_cells():
    """
    Test that SearchEngine correctly initializes when provided a preprocessed_data file path and matches attribute assigned correctly
    Assertions:
        1. Checks if preprocessed_data assigned correctly in the constructor
        2. Checks if matches data well defined
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file, \
                tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_kseq_query_keys_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        temp_kseq_query_keys_file.write(content.KSEQ_QUERY_KEYS_WITH_EMPTY_CELLS)
        temp_kseq_query_keys_file.seek(0)
        search_engine = SearchEngine(preprocessed_data=temp_file.name, kseq_file_path=temp_kseq_query_keys_file.name)
        assert search_engine.matches == content.Q4_MATCHES_RESULT, c.MATCHES_RESULT_INCORRECT
        assert search_engine.processed_data == content.Q1_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_file.name)
    os.remove(temp_kseq_query_keys_file.name)

def test_setters():
    """
    Test that SearchEngine correctly assign attributes with setters
    Assertions:
        1. Checks if kseq keys data assigned correctly
        2. Checks if sentences data assigned correctly
        3. Checks if unwanted words data assigned correctly
        4. Checks if preprocessed data assigned correctly
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file, \
                tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_kseq_query_keys_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        temp_kseq_query_keys_file.write(content.KSEQ_QUERY_KEYS)
        temp_kseq_query_keys_file.seek(0)
        search_engine = SearchEngine(preprocessed_data=temp_file.name, kseq_file_path=temp_kseq_query_keys_file.name)
        search_engine.kseq_keys = content.KSEQ_QUERY_KEYS_DICT
        assert search_engine.kseq_keys == content.KSEQ_QUERY_KEYS_AFTER_ASSIGNMENT, c.KSEQ_KEYS_INCORRECT_ASSIGN
    os.remove(temp_file.name)
    os.remove(temp_kseq_query_keys_file.name)
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_kseq_query_keys_file:
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        temp_kseq_query_keys_file.write(content.KSEQ_QUERY_KEYS)
        temp_kseq_query_keys_file.seek(0)
        search_engine = SearchEngine(sentences_file_path=temp_sentences.name, removewords_file_path=temp_removewords.name, kseq_file_path=temp_kseq_query_keys_file.name)
        search_engine.sentences = content.Q1_SENTENCES_RESULT
        assert search_engine.sentences == content.Q1_SENTENCES_RESULT, c.SENTENCES_INCORRECT_ASSIGN
        search_engine.unwanted_words = content.Q1_REMOVEWORDS_RESULT
        assert search_engine.unwanted_words == content.Q1_REMOVEWORDS_RESULT, c.UNWANTEDWORDS_INCORRECT_ASSIGN
        search_engine.processed_data = content.Q1_FINAL_RESULT
        assert search_engine.processed_data == content.Q1_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)
    os.remove(temp_kseq_query_keys_file.name)
