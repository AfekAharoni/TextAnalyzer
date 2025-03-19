# ===> Imports <=== 
from task1 import *
from typing import Optional
import json
import constants as c

class PeopleMentions:
    """
    This class represents the person mentions counter of task 3
    """
    def __init__(self, sentences_file_path: Optional[str] = None, names_file_path: Optional[str] = None, removewords_file_path: Optional[str] = None, preprocessed_data: Optional[str] = None):
        if preprocessed_data:
            self.preprocessed_data = extract_processed_data(preprocessed_data)
        else:
            data_processor = TextPreprocessing(sentences_file_path=sentences_file_path, removewords_file_path=removewords_file_path, people_file_path=names_file_path)
            self.preprocessed_data = data_processor.task1()
    
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

    def count_person_mentions(self) -> dict:
        """
        This function counting every occurence of each person, both name and other names
        Any partial mention of the main name is counted as a person's appearence -> "harry" and "potter" are appearances of "harry potter"
        If only the nickname appears in the text but the primary name doesn't, it is counted under the primary name
        Name with no appearances in the sentences, will not be in the output
        :return: All people mentions
        """
        data = json.loads(self.preprocessed_data) # loads the data from task 1
        # seperate the data to sentences and names
        processed_sentences = data[c.Q1][c.PROCESSED_SENTENCES]
        processed_names = data[c.Q1][c.PROCESSED_NAMES]
        names = dict()
        for name in processed_names:
            all_names_and_othernames = self.__combine_names_and_othernames(name)
            names.update(all_names_and_othernames)
        people_mentions: dict = dict()
        sentences = [c.WHITESPACE.join(sentence) for sentence in processed_sentences] # merge each list of words to sentence
        for name, othernames in names.items():
            for othername in othernames:
                for sentence in sentences:
                    counter = sentence.count(othername)
                    if counter > 0: # if the name appears in the text
                        if name in people_mentions.keys(): # if it's already been in the dict, add this counter
                            people_mentions[name] += counter
                        else: # first insert to the dict
                            people_mentions[name] = counter
        return people_mentions

    def __combine_names_and_othernames(self, name_entry) -> dict:
        """
        This function gets name entry (for example: [['harry', 'potter'], [['lived'], ['undesirable', 'number'], ['chosen'], ['parry', 'otter'], ['chosen'], ['mudbloods', 'friend']]])
        The function returns a dictionary with the following key-value:
            Key: primary name (for example: harry potter)
            Value: all other names merged and primary name seperated to words (for example :  ['harry', 'potter', 'lived', 'undesirable number', 'chosen', 'parry otter', 'chosen', 'mudbloods friend'])
        :param name_entry: A list of all name and other names for a person
        :return: A dictionary of combine name and othernames 
        """
        name = c.WHITESPACE.join(name_entry[0])  # merge the name to a full name
        othernames = [c.WHITESPACE.join(othername) for othername in name_entry[1]]  # merge the other names to a full other name
        return {name: name.split() + othernames} 
    
    def task3(self):
        """
        This function returns task 3 output in json format
        :return: Output of each person and number of mentions in the text
        """
        people_mentions = self.count_person_mentions()
        sorted_people_mentions = dict(sorted(people_mentions.items())) # sort it by alphabetical order
        output = {
            f"{c.Q3}": {
                f"{c.MENTIONS}": [
                    [name, count] for name, count in sorted_people_mentions.items()
                ]
            }
        }
        return (json.dumps(output, indent=4))
