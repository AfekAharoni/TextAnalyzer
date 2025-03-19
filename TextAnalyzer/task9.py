# ===> Imports <=== 
from typing import Optional, Any
from task1 import *
import json

class SentencesGroups:
    """
    This class represents the sentences groups by shared words in text
    """
    def __init__(self, sentences_file_path: Optional[str] = None, removewords_file_path: Optional[str] = None, processed_data: Optional[str] = None, threshold: Optional[int]=None):
        if processed_data:
            self.__processed_data = extract_processed_data(processed_data)
        else:
            data_processor = TextPreprocessing(sentences_file_path=sentences_file_path, removewords_file_path=removewords_file_path)
            self.__processed_data = data_processor.task1()
        processed_sentences = self.__extract_sentences_from_processed_data()
        self.__sentences, self.__original_sentences = self.__create_dict_for_sentences(processed_sentences)
        self.__threshold = threshold
        self.__graph = self.build_graph()

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
    def sentences(self) -> dict[str, Any]:
        """
        return: The sentences list (without words duplications)
        """
        return self.__sentences
     
    @sentences.setter # Setter
    def sentences(self, sentences: dict[str, Any]):
        """
        :param sentences: A list of sentences (without words duplications)
        """
        self.__sentences = sentences
    
    @property # Getter
    def original_sentences(self) -> dict[str, Any]:
        """
        return: The original sentences list
        """
        return self.__original_sentences
     
    @original_sentences.setter # Setter
    def original_sentences(self, original_sentences: dict[str, Any]):
        """
        :param sentences: The original sentences list
        """
        self.__original_sentences = original_sentences

    @property # Getter
    def threshold(self) -> Optional[int]:
        """
        return: The threshold value
        """
        return self.__threshold
    
    @threshold.setter # Setter
    def threshold(self, threshold: int):
        """
        :param threshold: A threshold value
        """
        self.__threshold = threshold

    @property # Getter
    def graph(self) -> dict:
        """
        return: The graph of sentences
        """
        return self.__graph
     
    @graph.setter # Setter
    def graph(self, graph: dict):
        """
        :param sentences: A sentences graph
        """
        self.__graph = graph
    
    def __extract_sentences_from_processed_data(self) -> list:
        """
        This function extract the sentences from the preprocessed data as received from task 1
        :return: List of Processed Sentences
        """
        data = json.loads(self.__processed_data)      
        extracted_data = data[c.Q1][c.PROCESSED_SENTENCES]
        return extracted_data

    def __create_dict_for_sentences(self, sentences: list) -> tuple[dict[str, Any], dict[str, Any]]:
        """
        This function creates two identical dictionaries for sentences: {sentence: [words of the sentence]}
        :param sentences: list of sentences
        :return: tuple of two identical dictionaries, which each one of them is a key-value pair. key is the sentence and the value is the splitted sentence to words
        """
        dict_of_sentences = dict()
        original_sentences = dict()
        for sentence in sentences:
            sentence_str = c.WHITESPACE.join(sentence)
            dict_of_sentences[sentence_str] = sentence
            original_sentences[sentence_str] = sentence
        return dict_of_sentences, original_sentences

    def build_graph(self) -> dict:
        """
        This function build a graph of sentences, where each node is a sentence
        Sentences are being connected with an edge only if they both have 'threshold' or more common words
        :return: A graph
        """
        graph: dict = dict()
        senctences_list = list(self.sentences.keys())
        for index in range(len(senctences_list)):
            for inner_index in range(index + 1, len(senctences_list)):
                first_sentence, second_sentence = senctences_list[index], senctences_list[inner_index]
                # convert each sentence to a set, ensures that the sentence has no duplication words
                # for example : 1. Harry Potter was here. 2. John the Potter left the city, our only Potter. -> Those two sentences have only one shared word
                first_sentence_words = set(self.sentences[first_sentence]) 
                second_sentence_words = set(self.sentences[second_sentence])
                common_words = sum(1 for word in first_sentence_words if word in second_sentence_words) # sum the number of mutual words
                if common_words >= self.threshold: #type: ignore
                    # add 'edge' to the graph between those sentences
                    if first_sentence not in graph:
                        graph[first_sentence] = []
                    if second_sentence not in graph:
                        graph[second_sentence] = []
                    graph[first_sentence].append(second_sentence)
                    graph[second_sentence].append(first_sentence)
        return graph

    def find_groups(self) -> list:
        """
        This function sort the graph to groups of interconnected nodes - meaning a group where all nodes can reach the other
        The function sort the results by the size of the groups, the smallest group will be the first, and the largest is the last 
        and each group's list of sentences sorted alphabetically
        In addition, if multiple groups are the same length, they ordered alphabetically
        :return: The graph seperated to groups, and sorted
        """
        already_visited = set() # set to ensure that won't be duplications
        sentences_groups = []
        for sentence in self.sentences:
            if sentence not in already_visited:
                group = []
                stack = [sentence]
                while len(stack) > 0:
                    node = stack.pop() # removes the last node in the stack and saves in 'node'
                    if node not in already_visited: # not visited there yet
                        already_visited.add(node)
                        group.append(self.original_sentences[node]) 
                        if node in self.graph:
                            stack.extend([neighbor for neighbor in self.graph[node] if neighbor not in already_visited])
                if group: # ensures that empty group won't enter the groups graph
                    # sort each group alphabetically
                    sentences_groups.append(sorted(group, key=lambda sentence: tuple(sentence)))
        # sort the groups by length, and if multiple groups are the same length, sort alphabetically
        sentences_groups.sort(key=lambda group: (len(group), tuple(group[0]) if group else None)) 
        return sentences_groups

    def task9(self):
        """
        This function returns task 9 output in json format
        :return: Output of graph seperated to groups of interconnected nodes
        """
        groups = self.find_groups()
        output = {c.Q9: {c.GROUP_MATCHES: []}}
        group_counter = 1
        for group in groups:
            output[c.Q9][c.GROUP_MATCHES].append([
                f"{c.GROUP} {group_counter}",
                group
            ])
            group_counter += 1
        return (json.dumps(output, indent=4))
