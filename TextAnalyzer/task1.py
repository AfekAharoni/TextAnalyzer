# ===> Imports <=== 
import csv
from typing import Optional
import json
import constants as c

class TextPreprocessing:
    """
    This class represent the initial text preprocessing of task 1 
    """
    def __init__(self, sentences_file_path: Optional[str] = None, removewords_file_path: Optional[str] = None, people_file_path: Optional[str] = None) -> None:
        self.__sentences_file_path = sentences_file_path
        self.__people_file_path = people_file_path
        self.__removewords_file_path = removewords_file_path
        self.__sentences: c.Sentences_type = {}
        self.__names: c.Names_type = []
        self.__unwanted_words: c.Unwanted_words_type = []
        self.__load_data() # load the from the files to the attributes (sentences, names, removewords)

    @property # Getter
    def sentences(self) -> c.Sentences_type:
        """
        return: The sentences dictionary of the text preprocessing {number of sentence: sentence seperated to list of words}
        """
        return self.__sentences
     
    @sentences.setter # Setter
    def sentences(self, sentences: c.Sentences_type) -> None:
        """
        :param sentences: A dictionary of sentences
        """
        self.__sentences = sentences
    
    @property # Getter
    def names(self) -> c.Names_type:
        """
        return: The names dictionary of the text preprocessing {name seperated to list of words: other names seperated to list of words}
        """
        return self.__names
     
    @names.setter # Setter
    def names(self, names: c.Names_type) -> None:
        """
        :param names: A list of names
        """
        self.__names = names

    @property # Getter
    def unwanted_words(self) -> c.Unwanted_words_type:
        """
        return: The words to remove list of the text preprocessing
        """
        return self.__unwanted_words
     
    @unwanted_words.setter # Setter
    def unwanted_words(self, unwanted_words: c.Unwanted_words_type) -> None:
        """
        :param remove_words: A list of words to remove
        """
        self.__unwanted_words = unwanted_words

    def __load_data(self) -> None:
        """
        This function loads data from 3 files to the class attributes:
            'sentence_file_path' data -> sentences
            'people_file_path' data -> names
            'removewords_file_path' data -> unwanted_words
        """
        if self.__removewords_file_path is not None:
            self.__unwanted_words = create_unwanted_words_list(self.__removewords_file_path)
        if self.__people_file_path is not None:
            self.__create_names_list()
        if self.__sentences_file_path is not None:
            self.sentences = create_sentences_dict(self.__sentences_file_path, self.unwanted_words)

    def __create_names_list(self):
        """
        This function loads the data from people file path and insert it to the class attribute
        """
        with open(self.__people_file_path, mode = 'r') as people_file:
            content = csv.reader(people_file)
            next(content) # ignore the first row which says the title of the columns
            content = list(content) # convert to list from 'csv.reader' type
            for index in range(len(content)):
                if content[index] != []: # ignore empty lines
                    content[index][c.FIRST_NAME_INDEX] = remove_unwanted_spaces(content[index][c.FIRST_NAME_INDEX])
                    content[index][c.FIRST_NAME_INDEX] = content[index][c.FIRST_NAME_INDEX].split()
                    for inner_index in range(len(content[index][c.FIRST_NAME_INDEX])):
                        # the next section do the following to the first name ('Name'): remove punctiation, change to lowercase letters, remove unwanted words, and split by commas
                        content[index][c.FIRST_NAME_INDEX][inner_index] = remove_punctuation(content[index][c.FIRST_NAME_INDEX][inner_index])
                        content[index][c.FIRST_NAME_INDEX][inner_index] = content[index][c.FIRST_NAME_INDEX][inner_index].lower()
                        content[index][c.FIRST_NAME_INDEX][inner_index] = remove_unwanted_words(content[index][c.FIRST_NAME_INDEX][inner_index], self.unwanted_words)
                    content[index][c.OTHER_NAME_INDEX] = content[index][c.OTHER_NAME_INDEX].split(c.COMMA)                   
                    other_name_list = []
                    for word in content[index][c.OTHER_NAME_INDEX]:
                        if word != "": # if word is not empty
                            word = word.split()
                            if len(word) > 1: # if the other name is like the other name "who lived" -> ['who', 'lived']
                                for inner_index in range(len(word)):
                                    word[inner_index] = word[inner_index].lower()
                                    word[inner_index] = remove_unwanted_words(word[inner_index], self.unwanted_words)
                                # if a word was in the unwanted_word list, the new value will be "", so remove it
                                word = remove_empty_strings_from_list(word)
                                other_name_list.append(word)
                            else: # one other name like 'talented'
                                word = str(word)
                                word = remove_punctuation(word)
                                word = remove_unwanted_spaces(word)
                                word = remove_unwanted_words(word, self.unwanted_words)
                                word = word.lower()
                                if word != "": # if it was unwanted word, it will become ""
                                    other_name_list.append([word])
                    content[index][c.OTHER_NAME_INDEX] = other_name_list
        for index in range(len(content)):
            for inner_index in range(len(content[index])):
                content[index][inner_index] = remove_empty_strings_from_list(content[index][inner_index])
        filtered_content = [name for name in content if name] # remove empty lines
        self.names = filtered_content
        self.__removes_duplication_names()

    def __removes_duplication_names(self):
        """
        This function remove duplication names from the name list
        If after 'cleaning' the names, two people have the same full name, the function keeps the one that appeared first in the file
        """
        already_in_list = [] # saves the names that checked
        for index in range(len(self.names)):
            if self.names[index] != []:
                first_name_list = self.names[index][c.FIRST_NAME_INDEX]
                if first_name_list in already_in_list: # if this name is already in the list, mark it in ""
                    self.names[index][c.FIRST_NAME_INDEX] = ""
                else:
                    already_in_list.append(first_name_list)
        # after mark it by "", now remove it from the list
        for index in range(len(self.names)-1, -1, -1): # run reversed in order to not go out of range (with the del method)
            if self.names[index] != [] and self.names[index][c.FIRST_NAME_INDEX] == "":
                del self.names[index]
    
    def task1(self) -> str:
        """
        This function returns task 1 output in json format
        :return: Output of Processed sentences and names
        """
        output = {
            f"{c.Q1}": {
                "Processed Sentences": list(self.sentences.values()),
                "Processed Names": self.names
            }
        }
        return (json.dumps(output, indent=4))

def remove_unwanted_words(sequence: str, unwanted_words: list) -> str:
    """
    This function removes the unwanted words if they appear in the sequence got
    :param sequence: A string to 'clear' from unwanted words
    :return: A new string without the unwanted words
    """
    new_sequence = ""
    sequence_splitted = sequence.split() # split for words
    for word in sequence_splitted:
        if not(word in unwanted_words):
            new_sequence += word
    return new_sequence
    
def remove_empty_strings_from_list(lst_of_strings: list[str]) -> list[str]:
    """
    This function is an helper function, which gets a list of string and remove all of the empty strings from it
    :param lst_of_string: A list of strings
    :return: New list without empty strings
    """
    while "" in lst_of_strings:
        lst_of_strings.remove("")
    return lst_of_strings

def remove_punctuation(sequence: str) -> str:
    """
    This function gets a sequence and 'clean' it from everything that is not letter, number or space
    :param sequence: A sequence
    :return: New sequence without punctuation
    """
    new_sequence = ""
    for char in sequence:
        if char.isalnum() or char.isspace(): # if its a alphabetic letter, a number or a space - add to the new sequence
            new_sequence += char
        else: # 'replace' it with single space
            new_sequence += c.WHITESPACE
    return new_sequence

def remove_unwanted_spaces(sequence: str) -> str:
    """
    This function gets a sequence and 'clean' it from unwanted spaces:
        1. consecutive whitespaces (>1 whitespaces apperaing one after the other), for example: "mr  dunder" -> "mr dunder"
        2. whitespace suffix and prefix (remove whitespaces at the end or beggining of the sequence), for example: "  mr dunder  " -> "mr dunder
    :param sequence: A sequence
    :return: New sequence without unwanted spaces
    """
    new_sequence = ""
    spaced = False # flag which says if the last charachter was space
    for char in sequence:
        if char == c.WHITESPACE:
            # If this char is a whitespace, there are two options:
            # 1. the last char was whitespace too, if so - pass. 
            # 2. the last char wasn't whitespace, if so - add to the new sequence
            if not spaced: 
                new_sequence += char
                spaced = True # added space, so update the flag
        else:
            new_sequence += char
            spaced = False
    return new_sequence.strip() # removes the suffix and prefix whitespaces

def create_unwanted_words_list(removewords_file_path) -> list[str]:
    """
    This function loads the data from the unwanted words file path and insert it to the class attribute
    """
    with open(removewords_file_path, mode = 'r') as removeowrds_file:
        csv_removewords_file = csv.reader(removeowrds_file)
        next(csv_removewords_file) # ignore the first line which is the column name
        temp_removewords = [row for row in csv_removewords_file] # get the content from the file
    return remove_word_list_helper(temp_removewords)

def remove_word_list_helper(lst_to_change: list[list[str]]) -> list[str]:
    """
    This function gets a list of lists of string and makes it list of strings (unwanted words) and lowercase 
    :param lst_to_change: A list needs to be changed to 'flat' list
    :return: A list of strings
    """
    flat_lst = []
    for list in lst_to_change:
        flat_lst.append(remove_unwanted_spaces(list[0]))
    return flat_lst

def create_sentences_dict(sentences_file_path: str, unwanted_words: c.Unwanted_words_type) -> c.Sentences_type:
    """
    This function loads the data from the sentences file path and insert it to the class attribute
    """
    sentences: c.Sentences_type = dict()
    with open(sentences_file_path, mode = 'r', encoding='utf-8') as sentences_file:
        counter = 0
        csv_sentence_file = csv.DictReader(sentences_file)
        for row in csv_sentence_file:
            key = counter
            value = remove_unwanted_spaces(remove_punctuation(row['sentence'])).lower().split()
            # remove the unwanted spaces (consecutive & prefix & suffix), remove punctuation, lowercase, and split to words
            for index in range(len(value)):
                value[index] = remove_unwanted_words(value[index], unwanted_words)
            # if a word was in the unwanted_word list, the new value will be "", so remove it
            value = remove_empty_strings_from_list(value)
            if value != []:
                counter += 1
                sentences[key] = value #type: ignore
    return sentences
    # {counter: sentence} -> for example: {0: 'Hello World!', 1: "Have a good day!"}

def extract_processed_data(processed_data_path: str) -> str:
    with open(processed_data_path, mode = 'r') as f:
        content = f.read()
    return content