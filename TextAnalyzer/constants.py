# ===> Imports <=== 
from typing import Union, Tuple
# ===> Questions <===
Q1 = "Question 1"
Q2 = "Question 2"
Q3 = "Question 3"
Q4 = "Question 4"
Q5 = "Question 5"
Q6 = "Question 6"
Q7 = "Question 7"
Q8 = "Question 8"
Q9 = "Question 9"
# ==> Attribute names <===
SENTENCES = 'sentences_file_path'
NAMES = 'names_file_path'
UNWANTED_WORDS = 'removewords_file_path'
PREPROCESSED = "preprocessed_data"
MAXK_SEQ = 'maxk'
QSEK = "qsek_query_path"
THRESHOLD = "threshold"
WINSIZE = "windowsize"
PAIRS = "pairs_file_path"
MAXDISTANCE = "maximal_distance"
FIXED_LEN = "fixed_length"
# ===> Constant Indexes <===
FIRST_NAME_INDEX = 0
OTHER_NAME_INDEX = 1
FIRST_PERSON_INDEX = 0
SECOND_PERSON_INDEX = 1
# ===> Output Messages <===
PROCESSED_SENTENCES = "Processed Sentences"
K_SEQ = "_seq"
PROCESSED_NAMES = "Processed Names"
MENTIONS = "Name Mentions"
KEYS = "keys"
MATCHES = "K-Seq Matches"
PERSON_CONTEXT = "Person Contexts and K-Seqs"
PAIR_MATCHES = "Pair Matches"
GROUP_MATCHES = "group Matches"
GROUP = "Group"
# ===> Constant Signs <===
WHITESPACE = " "
COMMA = ","
NEXT_LINE = "\n"
EMPTY_LIST = [""]
# ===> Types <===
Sentences_type = dict[int, list[int]]
Names_type = list[Union[list[str], str]]
Unwanted_words_type = list[str]
KSeq_count_data_type = dict[int, dict[Tuple[str, ...], int]]
Matches_type = dict[str, list[str]]
KSeq_type = list[str]
# ===> Informative Invalid Input Messages <===
INVALID_ARGUMENTS = {
    Q1: "Invalid input for Task 1. Expected arguments:\n"
         "-s <Sentence file path>\n"
         "-n <Names file path>\n"
         "-r <Words to remove file path>",
    
    Q2: "Invalid input for Task 2. Expected arguments:\n"
         "Option 1:\n"
         "  --preprocessed <JSON file with preprocessed data>\n"
         "  --maxk <Max k-sequence length>\n"
         "Option 2:\n"
         "  -s <Sentence file path>\n"
         "  -r <Words to remove file path>\n"
         "  --maxk <Max k-sequence length>",

    Q3: "Invalid input for Task 3. Expected arguments:\n"
         "Option 1:\n"
         "  --preprocessed <JSON file with preprocessed data>\n"
         "Option 2:\n"
         "  -s <Sentence file path>\n"
         "  -n <Names file path>\n"
         "  -r <Words to remove file path>",

    Q4: "Invalid input for Task 4. Expected arguments:\n"
         "Option 1:\n"
         "  --preprocessed <JSON file with preprocessed data>\n"
         "  --qsek_query_path <JSON file with query sequences>\n"
         "Option 2:\n"
         "  -s <Sentence file path>\n"
         "  -r <Words to remove file path>\n"
         "  --qsek_query_path <JSON file with query sequences>",

    Q5: "Invalid input for Task 5. Expected arguments:\n"
         "Option 1:\n"
         "  --preprocessed <JSON file with preprocessed data>\n"
         "  --maxk <Max k-sequence length>\n"
         "Option 2:\n"
         "  -s <Sentence file path>\n"
         "  -n <Names file path>\n"
         "  -r <Words to remove file path>\n"
         "  --maxk <Max k-sequence length>",

    Q6: "Invalid input for Task 6. Expected arguments:\n"
         "Option 1:\n"
         "  --preprocessed <JSON file with preprocessed data>\n"
         "  --windowsize <Window size>\n"
         "  --threshold <Threshold value>\n"
         "Option 2:\n"
         "  -s <Sentence file path>\n"
         "  -n <Names file path>\n"
         "  -r <Words to remove file path>\n"
         "  --windowsize <Window size>\n"
         "  --threshold <Threshold value>",

    Q7: "Invalid input for Task 7. Expected arguments:\n"
         "Option 1:\n"
         "  --preprocessed <JSON file with preprocessed data>\n"
         "  --pairs <JSON file with list of pairs>\n"
         "  --maximal_distance <Maximal distance>\n"
         "Option 2:\n"
         "  -s <Sentence file path>\n"
         "  -n <Names file path>\n"
         "  -r <Words to remove file path>\n"
         "  --windowsize <Window size>\n"
         "  --threshold <Threshold value>\n"
         "  --pairs <JSON file with list of pairs>\n"
         "  --maximal_distance <Maximal distance>",

    Q8: "Invalid input for Task 8. Expected arguments:\n"
         "Option 1:\n"
         "  --preprocessed <JSON file with preprocessed data>\n"
         "  --pairs <JSON file with list of pairs>\n"
         "  --fixed_length <Fixed length>\n"
         "Option 2:\n"
         "  -s <Sentence file path>\n"
         "  -n <Names file path>\n"
         "  -r <Words to remove file path>\n"
         "  --windowsize <Window size>\n"
         "  --threshold <Threshold value>\n"
         "  --pairs <JSON file with list of pairs>\n"
         "  --fixed_length <Fixed length>",

    Q9: "Invalid input for Task 9. Expected arguments:\n"
         "Option 1:\n"
         "  --preprocessed <JSON file with preprocessed data>\n"
         "  --threshold <Threshold value>\n"
         "Option 2:\n"
         "  -s <Sentence file path>\n"
         "  -r <Words to remove file path>\n"
         "  --threshold <Threshold value>"
}
SENTENCES_FILE_INVALID = "Can't open this sentences file!"
NAMES_FILE_INVALID = "Can't open this names file!"
REMOVEWORDS_FILE_INVALID = "Can't open this remove words file!"
PREPROCESSED_FILE_INVALID = "Can't open this preprocessed file!"
QSEK_FILE_INVALID = "Can't open this qsek file!"
PAIRS_FILE_INVALID = "Can't open this pairs file!"
TYPE_OF_ARGUMENT_INVALID = "One of the argument's type is invalid!"
MAXK_INVALID_INPUT = "MAXK invalid input!"
THRESHOLD_INVALID_INPUT = "Threshold invalid input!"
WINSIZE_INVALID_INPUT = "Winsize invalid input!"
MAXDISTANCE_INVALID_INPUT = "Maxdistance invalid input!"
FIXEDLEN_INVALID_INPUT = "Fixed length invalid input!"
WINSIZE_GREATER_THAN_SENTENCES = "Winsize can't be greater then the sentences number!"
TASK_NUM_INVALID = "Tasks Number can be 1-9 only!"
# ===> Tests Assertions Informative Error Messages <===
SENTENCES_PATH_INCORRECT = "Sentences file path is incorrect!"
REMOVEWORDS_PATH_INCORRECT = "Remove words file path is incorrect!"
PEOPLE_PATH_INCORRECT = "People file path is incorrect!"
SENTENCES_TYPE_INCORRECT = "Sentences attribute should be a dictionary!"
NAMES_TYPE_INCORRECT = "Names attribute should be a list!"
REMOVEWORDS_TYPE_INCORRECT = "Unwanted words attribute should be a list!"
PEOPLE_RESULT_INCORRECT = "Names result isn't correct!"
SENTENCES_RESULT_INCORRECT = "Sentences result isn't correct!"
REMOVEWORDS_RESULT_INCORRECT = "Remove words result isn't correct!"
TASK1_RESULT_INCORRECT = "Final result of task 1 isn't correct!"
REMOVE_UNWANTED_WORDS_INCORRECT = "The sequence isn't match what expected!"
REMOVE_EMPTY_STRINGS_FROM_LIST_INCORRECT = "There is more empty string in the list!"
REMOVE_PUNCTUATION_FROM_STRING_INCORRECT = "Expected punctuation removal result is incorrect!"
REMOVE_UNWANTED_SPACES_INCORRECT = "Expected spaces removal result is incorrect!"
REMOVE_DUPLICATED_NAMES_INCORRECT = "Didn't remove duplicated names correctly!"
PROCESSED_DATA_INCORRECT_ASSIGN = "Processed data wasn't correctly assigned!"
KSEQ_RESULTS_INCORRECT = "KSeqCounter didn't return the expected value!"
TASK2_RESULT_INCORRECT = "Final result of task 2 isn't correct!"
PEOPLE_MENTIONS_INCOREECT = "People Mentions count return unexpected value!"
TASK3_RESULT_INCORRECT = "Final result of task 3 isn't correct!"
MATCHES_RESULT_INCORRECT = "Matches result of task 4 isn't correct!"
KSEQ_KEYS_INCORRECT_ASSIGN = "Kseq keys data wasn't correctly assigned!"
SENTENCES_INCORRECT_ASSIGN = "Sentences data wasn't correctly assigned!"
UNWANTEDWORDS_INCORRECT_ASSIGN = "Unwanted words data wasn't correctly assigned!"
NAMES_INCORRECT_ASSIGN = "Names data wasn't correctly assigned!"
TASK4_RESULT_INCORRECT = "Final result of task 4 isn't correct!"
TASK5_RESULT_INCORRECT = "Final result of task 5 isn't correct!"
WINDOWSIZE_INCORRECT_ASSIGN = "Window size data wasn't correctly assigned!"
THRESHOLD_INCORRECT_ASSIGN = "Threshold data wasn't correctly assigned!"
TASK6_RESULT_INCORRECT = "Final result of task 6 isn't correct!"
FIXED_LENGTH_INCORRECT_ASSIGN = "Fixed length data wasn't correctly assigned!"
PAIRS_INCORRECT_ASSIGN = "Pairs data wasn't correctly assigned!"
MAXIMAL_DISTANCE_INCORRECT_ASSIGN = "Maximal distance data wasn't correctly assigned!"
TASK7_RESULT_INCORRECT = "Final result of task 7 isn't correct!"
TASK8_RESULT_INCORRECT = "Final result of task 8 isn't correct!"
IS_PAIR_CONNECTED_INCORRECT = "Unexpected result from is_pair_connected function!"
GRAPH_INCORRECT_ASSIGN = "Graph data wasn't correctly assigned!"
TASK9_RESULT_INCORRECT = "Final result of task 9 isn't correct!"
