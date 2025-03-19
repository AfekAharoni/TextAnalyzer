#!/usr/bin/env python3
# ===> Imports <=== 
import argparse
import input_validator as validator
from task1 import TextPreprocessing
from task2 import KSeqCounter
from task3 import PeopleMentions
from task4 import SearchEngine
from task5 import PeopleContexts
from task6 import DirectConnections
from task7_task8 import IndirectConnections
from task9 import SentencesGroups
import constants as c
import sys

def readargs(args=None):
    parser = argparse.ArgumentParser(
        prog='Text Analyzer project',
    )
    # General arguments
    parser.add_argument('-t', '--task',
                        help="task number",
                        required=True
                        )
    parser.add_argument('-s', '--sentences',
                        help="Sentence file path",
                        )
    parser.add_argument('-n', '--names',
                        help="Names file path",
                        )
    parser.add_argument('-r', '--removewords',
                        help="Words to remove file path",
                        )
    parser.add_argument('-p', '--preprocessed',
                        help="json with preprocessed data",
                        )
    # Task specific arguments
    parser.add_argument('--maxk',
                        type=int,
                        help="Max k",
                        )
    parser.add_argument('--fixed_length',
                        type=int,
                        help="fixed length to find",
                        )
    parser.add_argument('--windowsize',
                        type=int,
                        help="Window size",
                        )
    parser.add_argument('--pairs',
                        help="json file with list of pairs",
                        )
    parser.add_argument('--threshold',
                        type=int,
                        help="graph connection threshold",
                        )
    parser.add_argument('--maximal_distance',
                        type=int,
                        help="maximal distance between nodes in graph",
                        )

    parser.add_argument('--qsek_query_path',
                        help="json file with query path",
                        )
    return parser.parse_args(args)

def task1_execution(args):
    """
    This function execute task 1, if the arguments are valid, valid arguments:
        1. Sentence input path (-s)
        2. People input path (-n)
        3. Remove Input path (-r)
    :param args: Arguments
    """
    if validator.validate_task1(sentences_file_path = args.sentences, names_file_path = args.names, removewords_file_path = args.removewords):
        text_processor = TextPreprocessing(sentences_file_path=args.sentences, people_file_path=args.names, removewords_file_path=args.removewords)
        output = text_processor.task1()
        print(output)

def task2_execution(args):
    """
    This function execute task 2, if the arguments are valid, valid arguments:
        Option 1:
            1. Preprocessed data as received in task 1 (--preprocessed)
            2. Maximal kseq length to create (--maxk)
        Option 2:
            1. Sentence input path (-s)
            2. Remove Input path (-r)
            3. Maximal kseq length to create (--maxk)
    """
    if validator.validate_task2(sentences_file_path = args.sentences, removewords_file_path = args.removewords, maxk=args.maxk, preprocessed_data = args.preprocessed):
        if args.preprocessed:
            kseq_counter = KSeqCounter(processed_data=args.preprocessed)
            output = kseq_counter.task2(args.maxk)
            print(output)
        elif args.sentences and args.removewords:
            kseq_counter = KSeqCounter(sentences_file_path=args.sentences, removewords_file_path=args.removewords)
            output = kseq_counter.task2(args.maxk)
            print(output)

def task3_execution(args):
    """
    This function execute task 3, if the arguments are valid, valid arguments:
        Option 1:
            1. Preprocessed data as received in task 1 (--preprocessed)
        Option 2:
            1. Sentence input path (-s)
            2. People input path (-n)
            3. Remove input path (-r) 
    """
    if validator.validate_task3(sentences_file_path=args.sentences, removewords_file_path=args.removewords, names_file_path=args.names, preprocessed_data=args.preprocessed):
        people_mentions = PeopleMentions(sentences_file_path = args.sentences, removewords_file_path = args.removewords, names_file_path = args.names, preprocessed_data = args.preprocessed)
        print(people_mentions.task3())

def task4_execution(args):
    """
    This function execute task 4, if the arguments are valid, valid arguments:
        Option 1:
            1. Preprocesed data as received in task 1 (--preprocessed)
            2. Kseq input path (--qsek_query_path)
        Option 2:
            1. Sentences input path (-s)
            2. Remove input path (-r)
            3. Kseq Input path (--qsek_query_path)
    """
    if validator.validate_task4(sentences_file_path=args.sentences, removewords_file_path=args.removewords, qsek_query_path=args.qsek_query_path, preprocessed_data=args.preprocessed):
        search_engine = SearchEngine(sentences_file_path=args.sentences, removewords_file_path=args.removewords, preprocessed_data=args.preprocessed, kseq_file_path=args.qsek_query_path)
        print(search_engine.task4())

def task5_execution(args):
    """
    This function execute task 5, if the arguments are valid, valid arguments:
        Option 1:
            1. Preprocessed data as received in task 1 (--preprocessed)
            2. Length of maximal K-Seq (--maxk)
        Option 2:
            1. Sentences input path (-s)
            2. Names input path (-n)
            3. Remove input path (-r)
            4. Length of maximal K-Seq (--maxk)
    """
    if validator.validate_task5(sentences_file_path=args.sentences, names_file_path=args.names, removewords_file_path=args.removewords, \
                                preprocessed_data=args.preprocessed, maxk=args.maxk):
        people_contexts = PeopleContexts(sentences_file_path=args.sentences, names_file_path=args.names, removewords_file_path=args.removewords, \
                                         preprocessed_data=args.preprocessed, maxk=args.maxk)
        print(people_contexts.task5())

def task6_execution(args):
    """
    This function execute task 6, if the arguments are valid, valid arguments:
        Option 1:
            1. Preprocessed data as received in task 1 (--preprocessed)
            2. Window size (--windowsize)
            3. Threshold value (--threshold)
        Option 2:
            1. Sentences input path (-s)
            2. Names input path (-n)
            3. Remove input path (-r)
            4. Window size (--windowsize)
            5. Threshold value (--threshold)    
    """
    if validator.validate_task6(sentences_file_path=args.sentences, names_file_path=args.names, removewords_file_path=args.removewords, \
                                preprocessed_data=args.preprocessed, threshold=args.threshold, windowsize=args.windowsize):
        direct_conntections = DirectConnections(sentences_file_path=args.sentences, names_file_path=args.names, removewords_file_path=args.removewords, \
                                preprocessed_data=args.preprocessed, threshold=args.threshold, windowsize=args.windowsize)
        print(direct_conntections.task6())
    
def task7_execution(args):
    """
    This function execute task 7, if the arguments are valid, valid arguments:
        Option 1:
            1. Preprocessed data as received in task 6 (--preprocessed)
            2. People connections path (--pairs)
            3. Maximal distance value (--maximal_distance)
        Option 2:
            1. Sentences input path (-s)
            2. Names input path (-n)
            3. Remove input path (-r)
            4. Window size (--windowsize)
            5. Threshold value (--threshold)    
            6. People connections path (--pairs)
            7. Maximal distance value (--maximal_distance)
    """
    if validator.validate_task7(sentences_file_path = args.sentences, names_file_path = args.names, removewords_file_path = args.removewords, \
                                preprocessed_data = args.preprocessed, threshold = args.threshold, windowsize = args.windowsize, \
                                    pairs_file_path = args.pairs, maximal_distance = args.maximal_distance):
        indirect_connections = IndirectConnections(sentences_file_path = args.sentences, names_file_path = args.names, removewords_file_path = args.removewords, \
                                preprocessed_data = args.preprocessed, threshold = args.threshold, windowsize = args.windowsize, \
                                    pairs_file_path = args.pairs, maximal_distance = args.maximal_distance)
        print(indirect_connections.task7())

# ==> EXTENSIONS <==

def task8_execution(args): 
    """
    This function execute task 8, if the arguments are valid, valid arguments:
        Option 1:
            1. Preprocessed data as received in task 6 (--preprocessed)
            2. People connections path (--pairs)
            3. Fixed length value (--fixed_length)
        Option 2:
            1. Sentences input path (-s)
            2. Names input path (-n)
            3. Remove input path (-r)
            4. Window size (--windowsize)
            5. Threshold value (--threshold)    
            6. People connections path (--pairs)
            7. Fixed length value (--fixed_length)
    """
    if validator.validate_task8(sentences_file_path = args.sentences, names_file_path = args.names, removewords_file_path = args.removewords, \
                                preprocessed_data = args.preprocessed, threshold = args.threshold, windowsize = args.windowsize, \
                                    pairs_file_path = args.pairs, fixed_length = args.fixed_length):
        indirect_connections = IndirectConnections(sentences_file_path = args.sentences, names_file_path = args.names, removewords_file_path = args.removewords, \
                                preprocessed_data = args.preprocessed, threshold = args.threshold, windowsize = args.windowsize, \
                                    pairs_file_path = args.pairs, fixed_length = args.fixed_length)
        print(indirect_connections.task8())

def task9_execution(args):
    """
    This function execute task 9, if the arguments are valid, valid arguments:
        Option 1:
            1. Preprocessed data as received in task 1 (--preprocessed)
            2. Threshold value (--threshold)
        Option 2:
            1. Sentences input path (-s)
            2. Remove input path (-r)
            3. Threshold value (--threshold)
    """
    if validator.validate_task9(sentences_file_path = args.sentences, removewords_file_path = args.removewords, \
                                preprocessed_data = args.preprocessed, threshold = args.threshold):
        sentences_groups = SentencesGroups(sentences_file_path=args.sentences, removewords_file_path=args.removewords, \
                                           processed_data=args.preprocessed, threshold=args.threshold)
        print(sentences_groups.task9())

def main():
    args = readargs(sys.argv[1:]) # first index is the name of the file (main.py), not relevant
    if args.task == "1":
        task1_execution(args)
    elif args.task == "2":
        task2_execution(args)
    elif args.task == "3":
        task3_execution(args)
    elif args.task == "4":
        task4_execution(args)
    elif args.task == "5":
        task5_execution(args)
    elif args.task == "6":
        task6_execution(args)
    elif args.task == "7":
        task7_execution(args)
    elif args.task == "8":
        task8_execution(args)
    elif args.task == "9":
        task9_execution(args)
    else:
        print(c.TASK_NUM_INVALID)

if __name__=="__main__":
    main()