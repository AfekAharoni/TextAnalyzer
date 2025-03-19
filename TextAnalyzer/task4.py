# ===> Imports <=== 
from task1 import *
from typing import Optional
import json
import constants as c

class SearchEngine:
    """
    This class represents the basic search engine functionallity of task 4
    """
    def __init__(self, sentences_file_path: Optional[str] = None, removewords_file_path: Optional[str] = None, preprocessed_data: Optional[str] = None, kseq_file_path: Optional[str] = None):
        self.__kseq_file_path = kseq_file_path
        self.__kseq_keys = self.__create_kseq_list()
        if preprocessed_data:
            self.__processed_data = extract_processed_data(preprocessed_data)
            temp_sentences = self.__extract_sentences_from_processed_data(self.__processed_data)
        else:
            self.__unwanted_words = create_unwanted_words_list(removewords_file_path)
            temp_sentences = create_sentences_dict(sentences_file_path, self.__unwanted_words) #type: ignore
        self.__sentences = dict()
        for counter, sentence in temp_sentences.items():
            self.__sentences[counter] = self.__merge_words_to_sentence(sentence)
        self.__matches: c.Matches_type  = dict()
        self.__create_match_of_kseq_to_sentences() # {K-seq: [all sentences the k-seq appears in]}
        # for example: {"hello world": ["hello world have a good day", "console.writeline(hello world) was my first line"]}

    @property # Getter
    def processed_data(self) -> str:
        """
        return: The proccessed data
        """
        return self.__processed_data
    
    @processed_data.setter # Setter
    def processed_data(self, processed_data: str):
        """
        :param processed_data: Processed data to set as attribute
        """
        self.__processed_data = processed_data

    @property # Getter
    def unwanted_words(self) -> c.Unwanted_words_type:
        """
        return: The words to remove list of the text preprocessing
        """
        return self.__unwanted_words
     
    @unwanted_words.setter # Setter
    def unwanted_words(self, unwanted_words: c.Unwanted_words_type):
        """
        :param remove_words: A list of words to remove
        """
        self.__unwanted_words = unwanted_words

    @property # Getter
    def sentences(self) -> c.Sentences_type:
        """
        return: The sentences dictionary of the text preprocessing {number of sentence: sentence}
        """
        return self.__sentences
     
    @sentences.setter # Setter
    def sentences(self, sentences: c.Sentences_type):
        """
        :param sentences: A dictionary of sentences
        """
        self.__sentences = sentences

    @property # Getter
    def matches(self) -> c.Matches_type:
        """
        return: A dictionary of k-seq and sentences {K-seq: [sentences the k-seq appears in]}
        """
        return self.__matches
     
    @matches.setter # Setter
    def matches(self, matches: c.Matches_type):
        """
        :param matches: A dictionary of matches for each k-seq (key)
        """
        self.__matches = matches
    
    @property # Getter
    def kseq_keys(self):
        """
        return: A list of k-seqs got from K-Seq json file
        """
        return self.__kseq_keys
     
    @kseq_keys.setter # Setter
    def kseq_keys(self, kseq_keys):
        """
        :param kseq_keys: A list of K-Seq from K-Seq json file
        """
        self.__kseq_keys = kseq_keys

    def __create_kseq_list(self) -> c.KSeq_type:
        """
        This function create K-Seq list from the kseq_file_path got to the object
        The function 'cleans' the K-seqs from punctuation, suffix & prefix whitespaces, duplication of whitespaces, lowercase all the letters and remove the unwanted words
        :return: All K-Seq keys after cleaning, as a list of strings
        """
        with open(self.__kseq_file_path, mode = 'r', encoding='utf-8') as kseq_file: #type: ignore
            data_reader = kseq_file.read()
        data = json.loads(data_reader)
        kseq_keys = data[c.KEYS]
        for key in kseq_keys:
            for index in range(len(key)):
                key[index] = remove_unwanted_spaces(remove_punctuation(key[index])).lower()
        while c.EMPTY_LIST in kseq_keys: # Remove [""] if there is in the list
            kseq_keys.remove(c.EMPTY_LIST)
        for index in range(len(kseq_keys)):
            kseq_keys[index] = c.WHITESPACE.join(kseq_keys[index]) # Merge words to one sentence
            kseq_keys[index] = remove_unwanted_spaces(kseq_keys[index]) # Remove again spaces, if there is after the merge
        kseq_keys = list(set(kseq_keys)) # By converting to set, it removes the duplications, and then re-convert to list
        while "" in kseq_keys: # If empty is still in the kseq_keys, remove it
            kseq_keys.remove("")
        return kseq_keys

    def __extract_sentences_from_processed_data(self, processed_data: str) -> c.Sentences_type:
        """
        This function gets the processed data as received from task 1, and extract the sentences from it
        :param processed_data: The data as received from task 1
        :return: A dictionary of sentences {counter: sentence}, For example: {0: "first sentence", 1: "second sentence"}
        """
        data = json.loads(processed_data)
        sentences = data[c.Q1][c.PROCESSED_SENTENCES]
        sentences_dict = dict()
        counter = 0
        for row in sentences:
            key = counter
            sentences_dict[key] = row
            counter += 1
        return sentences_dict

    def __merge_words_to_sentence(self, lst_of_words):
        """
        This function gets list of words and merge it to one sentence
        :param lst_of_words: A list of words
        :return: A sentence containing the names from the list
        """
        return c.WHITESPACE.join(lst_of_words)

    def __create_match_of_kseq_to_sentences(self):
        """
        This function set as SearchEngine attribute the match of each K-Seq to sentences
        """
        matches = dict()
        for sentence in self.sentences.values():
            for key in self.kseq_keys:
                if key in sentence: 
                    if key in matches.keys(): # This key already in the matches keys (was in one of the previous sentences)
                        matches[key].append(sentence)
                    else: # Initalize it in the dictionary
                        matches[key] = [sentence]
        matches = dict(sorted(matches.items())) # Sort the matches by the keys (K-Seqs)
        for key, sentences in matches.items():
            matches[key] = sorted(sentences, key = lambda sentence: sentence.split()) # Sort the values for each key (Sentences)
        matches = {key: value for key, value in matches.items() if key != ""} # Remove empty strings from sentences
        self.matches = matches

    def __extract_sentences_for_kseq(self, kseq: str) -> list[str]:
        """
        This function gets a K-Seq and extract the sentences that match to this KSeq from the dictionary
        :param kseq: A KSeq
        :return: List of sentences that match to the KSeq given
        """
        return self.matches[kseq] 
        # Run time O(1) for each KSeq, because accessing a specific key in a dictionary in python is performed in constant time due to hash table

    def task4(self):
        """
        This function returns task 4 output in json format
        :return: Output of each K-Seq and sentences the the K-Seq appears in 
        """
        output = {f"{c.Q4}": {f"{c.MATCHES}": []}}
        for kseq in self.matches.keys():
            formatted_sentences = []
            sentences = self.__extract_sentences_for_kseq(kseq) # O(1) for each KSeq
            for sentence in sentences:
                words_list = sentence.split()
                formatted_sentences.append(words_list)
            output[f"{c.Q4}"][f"{c.MATCHES}"].append([kseq, formatted_sentences])
        return (json.dumps(output, indent=4))
