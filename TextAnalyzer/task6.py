# ===> Imports <=== 
from typing import Optional
from task1 import *
import json
import constants as c

class DirectConnections:
    """
    This class represents the direct connections between people
    """
    def __init__(self,  windowsize: Optional[int], threshold: Optional[int], sentences_file_path: Optional[str] = None, removewords_file_path: Optional[str] = None, 
                 names_file_path: Optional[str] = None, preprocessed_data: Optional[str] = None):
        if preprocessed_data:
            self.__preprocessed_data = extract_processed_data(preprocessed_data)
        else:
            data_processor = TextPreprocessing(sentences_file_path=sentences_file_path, removewords_file_path=removewords_file_path, people_file_path=names_file_path)
            self.__preprocessed_data = data_processor.task1()
        self.__window_size = windowsize
        self.__threshold = threshold
        self.__names = self.__extract_data_from_processed_data(c.PROCESSED_NAMES)
        self.__sentences = self.__extract_data_from_processed_data(c.PROCESSED_SENTENCES)

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
    
    @property # Getter
    def window_size(self) -> Optional[int]:
        """
        :return: The windows size
        """
        return self.__window_size
     
    @window_size.setter # Setter
    def window_size(self, window_size: int):
        """
        :param window_size: Window size
        """
        self.__window_size = window_size
    
    @property # Getter
    def threshold(self) -> Optional[int]:
        """
        :return: The threshold value used for the calculation
        """
        return self.__threshold
     
    @threshold.setter # Setter
    def threshold(self, threshold: int):
        """
        :param threshold: The threshold value
        """
        self.__threshold = threshold
    
    def __extract_data_from_processed_data(self, type_of_data: str) -> list:
        """
        This function extract the data (sentences or names) from the preprocessed data as received from task 1
        :param type_of_data: Type of data need to be extracted (Processed Sentences or Processed Names)
        :return: List of Processed Sentences or List of Processed Names
        """
        data = json.loads(self.preprocessed_data)        
        extracted_data = data[c.Q1][type_of_data]
        return extracted_data

    def __create_sentence_windows(self) -> list:
        """
        This functions create all the windows for window_size attribute of the object
        :return: A list of lists, which each inner list is a sentence seperated to words
        """
        windows = []
        for i in range(len(self.sentences) - self.window_size + 1):# type: ignore
             # run all over the sentences until the window_size can be fit in
            window = self.sentences[i: i + self.window_size] #type: ignore
            # window_size length of sentences (aka window)
            windows.append(window)
        return windows

    def __find_person_mentions_in_window(self, window: list) -> set:
        """
        This function find person mentions in a single window
        :param window: A window of sentences (list of lists, each inner-list is a sentence seperated to words)
        :return: A set of all people mentioned in this windows
        """
        people_mentioned = set() # set because the order isn't necessary at this point, and to ensures there is no duplications
        for sentence in window:
            sentence_merged = c.WHITESPACE.join(sentence) # make the sentence (list of words) to one string
            # ^ will make the search for each other name easier 
            for name in self.names:
                primary_name = name[c.FIRST_NAME_INDEX] # extract the primary name
                other_names = name[c.OTHER_NAME_INDEX] # extract the other names 
                primary_name_found = False # an helper flag
                for word in primary_name: 
                # for the primary name ['harry', 'potter'], search 'harry' and search 'potter' seperated
                    if word in sentence:
                        primary_name_found = True
                        break # already found, don't need to continue running on this sentence
                if primary_name_found:
                    people_mentioned.add(c.WHITESPACE.join(primary_name)) # add the primary name to the people mentioned
                for other_name in other_names: 
                # for the other names: [['lived'], ['undesirable', 'number'], ['chosen'], ['parry', 'otter']]
                # search 'lived', 'undesirable number', 'chosen', 'parry otter'
                    other_name_merged = c.WHITESPACE.join(other_name) # merge each other name to one string
                    if other_name_merged in sentence_merged:
                        people_mentioned.add(c.WHITESPACE.join(primary_name)) # add the primary name of this other name to the people mentioned
        return people_mentioned

    def calculate_direct_connections(self) -> list:
        """
        This function calculate the direct connections in the data given
        The function returns pairs of people, like a graph, where:
            1. Nodes represent the persons from the people list
            2. Edge first_person(*), second_person(@) exists if C(*@)>=t, where C(*@) is their mutual appearance count
                (number of windows in which they are connected), and t is provided as the threshold parameter
        :return: List of edges making up the graph 
        """
        connections_count: dict = dict() # a dictionary of {(first_person, second_person), mutual appearance count}
        windows = self.__create_sentence_windows() # all of the windows, with the size of window_size attribute of the object
        for window in windows:
            people_mentioned = self.__find_person_mentions_in_window(window)
            sorted_people_mentioned: list = sorted(people_mentioned) # convert from set to a sorted list
            for index in range(len(sorted_people_mentioned)):
                # the next section of the code is for calculate the number of mutual appearances of each two people
                first_person = sorted_people_mentioned[index] 
                for inner_index in range(index + 1, len(sorted_people_mentioned)):
                    second_person = sorted_people_mentioned[inner_index]
                    # the reason of the type selection of 'both_together' is because dictionary values (two people names)
                    # should be immutable. list, for example, won't work because it's mutable
                    both_together = (first_person, second_person) 
                    if both_together in connections_count:
                        # already have direct connection, add one to the counter
                        connections_count[both_together] += 1
                    else:
                        # initialize their counter in the dictionary to one
                        connections_count[both_together] = 1
        connections = [list(both_together) for both_together, count in connections_count.items() if count >= self.threshold] 
        sorted_connections = sorted(connections, key=lambda pair: (pair[0], pair[1]))
        # alphabethical sort of two people in each 'pair' in conntections
        return sorted_connections

    def task6(self):
        """
        This function returns task 6 output in json format
        :return: Output of each pair of people that appears in the same window_size window in the sentences given, 
                at lease threshold times
        """
        direct_connections = self.calculate_direct_connections()
        output = {
            f"{c.Q6}": {
                f"{c.PAIR_MATCHES}": [
                    [pair[0].split(), pair[1].split()] for pair in direct_connections
                ]
            }
        }
        return (json.dumps(output, indent=4))
