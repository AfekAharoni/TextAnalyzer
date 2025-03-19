from task7_task8 import IndirectConnections
import os
import test_contents as content
import constants as c
import tempfile

def test_indirectconnections_init_with_processed_data():
    """
    Test that IndirectConnections correctly initializes when provided a preprocessed_data file path
    Assertions:
        1. Checks if preprocessed_data assigned correctly in the constructor
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_pairs:
        temp_file.write(content.Q6_FINAL_RESULT)
        temp_file.seek(0)
        temp_pairs.write(content.PEOPLE_CONNECTIONS)
        temp_pairs.seek(0)
        indirect_connections = IndirectConnections(preprocessed_data=temp_file.name, pairs_file_path=temp_pairs.name, windowsize=3, threshold=3, maximal_distance=2)
        assert indirect_connections.preprocessed_data == content.Q6_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_file.name)

def test_task7_final_result():
    """
    Test that task 7 formats the output in JSON format, with preprocessed data given
    Assertions:
        1. Checks if the output is as expected
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_pairs:
        temp_file.write(content.Q6_FINAL_RESULT)
        temp_file.seek(0)
        temp_pairs.write(content.PEOPLE_CONNECTIONS)
        temp_pairs.seek(0)
        indirect_connections = IndirectConnections(preprocessed_data=temp_file.name, pairs_file_path=temp_pairs.name, maximal_distance=2)
        assert indirect_connections.task7() == content.Q7_FINAL_RESULT, c.TASK7_RESULT_INCORRECT
    os.remove(temp_file.name)
    os.remove(temp_pairs.name)

def test_task8_final_result():
    """
    Test that task 8 formats the output in JSON format, with preprocessed data given
    Assertions:
        1. Checks if the output is as expected
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_pairs:
        temp_file.write(content.Q6_FINAL_RESULT)
        temp_file.seek(0)
        temp_pairs.write(content.PEOPLE_CONNECTIONS)
        temp_pairs.seek(0)
        indirect_connections = IndirectConnections(preprocessed_data=temp_file.name, pairs_file_path=temp_pairs.name, fixed_length=1)
        assert indirect_connections.task8() == content.Q8_FINAL_RESULT, c.TASK8_RESULT_INCORRECT
    os.remove(temp_file.name)
    os.remove(temp_pairs.name)
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_people, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
            tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords, \
                tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_pairs:
        temp_people.write(content.Q1_PEOPLE_CONTENT)
        temp_people.seek(0)
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        temp_pairs.write(content.PEOPLE_CONNECTIONS)
        temp_pairs.seek(0)
        indirect_connections = IndirectConnections(sentences_file_path=temp_sentences.name, removewords_file_path=temp_removewords.name, names_file_path=temp_people.name, pairs_file_path=temp_pairs.name, windowsize=3, threshold=2, fixed_length=2)
        assert indirect_connections.task8() == content.Q8_FINAL_RESULT_WITH_CONNECTION, c.TASK8_RESULT_INCORRECT
    os.remove(temp_people.name)
    os.remove(temp_pairs.name)
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)

def test_setters():
    """
    Test that InirectConnections correctly assign attributes with setters
    Assertions:
        1. Checks if processed data assigned correctly
        2. Checks if fixed length data assigned correctly
        3. Checks if maximal distance data assigned correctly
        4. Checks if pairs data assigned correctly
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file, \
                tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_pairs:
        temp_file.write(content.Q6_FINAL_RESULT)
        temp_file.seek(0)
        temp_pairs.write(content.PEOPLE_CONNECTIONS)
        temp_pairs.seek(0)
        indirect_connections = IndirectConnections(preprocessed_data=temp_file.name, pairs_file_path=temp_pairs.name, fixed_length=1)
        indirect_connections.preprocessed_data = content.Q6_FINAL_RESULT
        assert indirect_connections.preprocessed_data == content.Q6_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
        indirect_connections.fixed_length = 3
        assert indirect_connections.fixed_length == 3, c.FIXED_LENGTH_INCORRECT_ASSIGN
        indirect_connections.people_connections_data = content.PEOPLE_CONNECTIONS_AS_DICT
        assert indirect_connections.people_connections_data == content.PEOPLE_CONNECTIONS_AS_DICT, c.PAIRS_INCORRECT_ASSIGN
        indirect_connections.maximal_distance = 5
        assert indirect_connections.maximal_distance == 5, c.MAXIMAL_DISTANCE_INCORRECT_ASSIGN
    os.remove(temp_file.name)
    os.remove(temp_pairs.name)

def test_if_pair_connected():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file, \
                tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_pairs:
        temp_file.write(content.Q6_FINAL_RESULT)
        temp_file.seek(0)
        temp_pairs.write(content.PEOPLE_CONNECTIONS)
        temp_pairs.seek(0)
        indirect_connections = IndirectConnections(preprocessed_data=temp_file.name, pairs_file_path=temp_pairs.name, fixed_length=2)
        assert indirect_connections._IndirectConnections__check_if_pair_connected(content.NEIGHBORS_DICT, content.FIRST_PERSON, content.SECOND_PERSON, maximal_distance=2), c.IS_PAIR_CONNECTED_INCORRECT
    os.remove(temp_file.name)
    os.remove(temp_pairs.name)