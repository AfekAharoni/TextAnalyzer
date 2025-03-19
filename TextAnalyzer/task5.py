# ===> Imports <=== 
from typing import Optional
from task1 import *
import json
import constants as c

class PeopleContexts:
    """
    This class represents the context of people and associated k-seqs of them
    """
    def __init__(self, maxk: int, sentences_file_path: Optional[str] = None, removewords_file_path: Optional[str] = None, names_file_path: Optional[str] = None, preprocessed_data: Optional[str] = None):
        if preprocessed_data:
            self.__preprocessed_data = extract_processed_data(preprocessed_data)
        else:
            data_processor = TextPreprocessing(sentences_file_path=sentences_file_path, removewords_file_path=removewords_file_path, people_file_path=names_file_path)
            self.__preprocessed_data = data_processor.task1()
        self.__sentences = self.__extract_data_from_processed_data(c.PROCESSED_SENTENCES)
        names = self.__extract_data_from_processed_data(c.PROCESSED_NAMES)
        self.__names = self.__formatting_names(names)
        self.__max_kseq_length = maxk
        self.find_names_in_sentences()

    @property # Getter
    def preprocessed_data(self) -> str:
        """
        return: The proccessed data
        """
        return self.__preprocessed_data

    @preprocessed_data.setter # Setter
    def preprocessed_data(self, preprocessed_data: str):
        """
        :param processed_data: Processed data to set as attribute
        """
        self.__preprocessed_data = preprocessed_data

    @property # Getter
    def sentences(self) -> list:
        """
        return: The sentences dictionary of the text preprocessing {number of sentence: sentence}
        """
        return self.__sentences
     
    @sentences.setter # Setter
    def sentences(self, sentences: list):
        """
        :param sentences: A dictionary of sentences
        """
        self.__sentences = sentences

    @property # Getter
    def names(self) -> list:
        """
        return: The names dictionary of the text preprocessing {name seperated to list of words: other names seperated to list of words}
        """
        return self.__names
     
    @names.setter # Setter
    def names(self, names: list):
        """
        :param names: A list of names
        """
        self.__names = names

    def __extract_data_from_processed_data(self, type_of_data: str) -> list:
        """
        This function extract the data (sentences or names) from the preprocessed data as received from task 1
        :param type_of_data: Type of data need to be extracted (Processed Sentences or Processed Names)
        :return: List of Processed Sentences or List of Processed Names
        """
        data = json.loads(self.preprocessed_data)        
        extracted_data = data[c.Q1][type_of_data]
        return extracted_data

    def __formatting_names(self, names: list) -> list:
        """
        This function get names and change the format of it (merge other names to 'sentence')
        For Example: [['harry', 'potter'], [['lived'], ['undesirable', 'number']]
        -> [['harry potter', 'harry', 'potter', 'lived', 'undesirable number']]
        :param names: List of names
        :return: List of names in new format [[PrimaryName, PrimaryName Seperated, Other Names Seperated]]
        """
        flat_names = []
        for name in names:
            primary_name = name[c.FIRST_NAME_INDEX]
            other_names = [c.WHITESPACE.join(other_name) for other_name in name[c.OTHER_NAME_INDEX]]
            flat_entry = [c.WHITESPACE.join(primary_name)] +  primary_name + other_names
            flat_names.append(flat_entry)
        return flat_names

    def find_names_in_sentences(self) -> dict:
        """
        This function search for names in the sentences of the PeopleContexts object
        The function creates a dictionary of names and combinations of maximum 'maxk' of each sentence the name appears in
        :return: Dictionary in the following format:
             {Primary Name: All combinations of maximum 'maxk' of each sentence the name (or other names) appears in}
        """
        all_sentences_for_names = dict()
        for name in self.names:
            combinations_per_name = self.search_for_name_in_sentences(name)
            all_sentences_for_names.update(combinations_per_name) # add to the dictionary
        sorted_by_name = dict(sorted(all_sentences_for_names.items())) # alphabetical sort by the names of the dictionary (keys)
        sorted_by_combinations = dict()
        for name, combinations in sorted_by_name.items(): 
            sorted_by_combinations[name] = sorted(combinations, key = lambda sentence: c.WHITESPACE.join(sentence))
            # alphabetical sort by the sentences of the key (values)
        remove_no_combinations = dict()
        for name, combinations in sorted_by_combinations.items():
            if combinations != []: # remove name without combinations found
                remove_no_combinations[name] = combinations
        return remove_no_combinations

    def search_for_name_in_sentences(self, name: list) -> dict:
        """
        This function gets a name and returns all the combination of maximum 'maxk' for each sentence the name (or the other name) appears in
        :param name: List of name [Primary Name, Primary Name Seperated, Other Names Seperated]
        :return: Dictionary in the following format:
            {Primary Name:  All combinations of maximum 'maxk' of each sentence the name (or other names) appears in}
        """
        combinations_per_name = []
        primary_name = name[c.FIRST_NAME_INDEX]
        for sentence in self.sentences:
            for part_of_name in name: 
                if part_of_name in sentence: 
                    for k in range(1, self.__max_kseq_length + 1): # for every 1<=K<=N (N=max_kseq_length)
                        for index in range(len(sentence) - k + 1):
                            kseq = sentence[index: index + k] # a single combination of the sentence the name appears in
                            if kseq not in combinations_per_name: # ensures that there will be not duplications in the combinations
                                combinations_per_name.append(kseq)
        return {primary_name: combinations_per_name}
            
    def task5(self):
        """
        This function returns task 5 output in json format
        :return: Output of each person in the People file identify the sentences in which they are mentioned, and for each 1<=k<=maxk
        that, the k-seqs that make up these sentences, along with the k-seq's number of appearances in these sentences
        """
        output = {
            f"{c.Q5}": {
                f"{c.PERSON_CONTEXT}": []
            }
        }
        all_sentences_for_names = self.find_names_in_sentences()
        for name, combinations in all_sentences_for_names.items():
            output[f"{c.Q5}"][f"{c.PERSON_CONTEXT}"].append([name, combinations])
        return (json.dumps(output, indent=4))
