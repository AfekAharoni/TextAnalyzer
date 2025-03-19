from task9 import SentencesGroups
import os
import test_contents as content
import constants as c
import tempfile

def test_sentencesgroups_init_with_processed_data():
    """
    Test that SentencesGroups correctly initializes when provided a preprocessed_data file path
    Assertions:
        1. Checks if preprocessed_data assigned correctly in the constructor
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        sentences_groups = SentencesGroups(processed_data=temp_file.name, threshold=3)
        assert sentences_groups.processed_data == content.Q1_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
    os.remove(temp_file.name)

def test_task9_final_result():
    """
    Test that task 9 formats the output in JSON format, without preprocessed data given
    Assertions:
        1. Checks if the output is as expected
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_sentences, \
        tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as temp_removewords:
        temp_sentences.write(content.Q1_SENTENCES_CONTENT)
        temp_sentences.seek(0)
        temp_removewords.write(content.Q1_REMOVEWORDS_CONTENT)
        temp_removewords.seek(0)
        sentences_groups = SentencesGroups(sentences_file_path=temp_sentences.name, removewords_file_path=temp_removewords.name, threshold=1)
        assert sentences_groups.task9() == content.Q9_FINAL_RESULT, c.TASK9_RESULT_INCORRECT
    os.remove(temp_sentences.name)
    os.remove(temp_removewords.name)

def test_setters():
    """
    Test that SentencesGroups correctly assign attributes with setters
    Assertions:
        1. Checks if processed data assigned correctly
        2. Checks if threshold value assigned correctly
        3. Checks if graph data assigned correctly
        4. Checks if sentences data assigned correctly
    """
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        temp_file.write(content.Q1_FINAL_RESULT)
        temp_file.seek(0)
        sentences_groups = SentencesGroups(processed_data=temp_file.name, threshold=2)
        sentences_groups.processed_data = content.Q1_FINAL_RESULT
        assert sentences_groups.processed_data == content.Q1_FINAL_RESULT, c.PROCESSED_DATA_INCORRECT_ASSIGN
        sentences_groups.threshold = 1
        assert sentences_groups.threshold == 1, c.THRESHOLD_INCORRECT_ASSIGN
        sentences_groups.graph = content.Q9_GRAPH
        assert sentences_groups.graph == content.Q9_GRAPH, c.GRAPH_INCORRECT_ASSIGN
        sentences_groups.sentences = content.Q9_SENTENCES
        assert sentences_groups.sentences == content.Q9_SENTENCES, c.SENTENCES_INCORRECT_ASSIGN
        sentences_groups.original_sentences = content.Q9_SENTENCES
        assert sentences_groups.original_sentences == content.Q9_SENTENCES, c.SENTENCES_INCORRECT_ASSIGN
    os.remove(temp_file.name)