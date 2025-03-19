# ===> Imports <=== 
from task1 import *
from typing import Optional
import json
import constants as c

class KSeqCounter:
    """
    This class represents the sequences of words counter of task 2
    """
    def __init__(self, sentences_file_path: Optional[str] = None, names_file_path: Optional[str] = None, removewords_file_path: Optional[str] = None, processed_data: Optional[str] = None):
        if processed_data:
            self.__processed_data = extract_processed_data(processed_data)
        else:
            data_processor = TextPreprocessing(sentences_file_path=sentences_file_path, removewords_file_path=removewords_file_path, people_file_path=names_file_path)
            self.__processed_data = data_processor.task1()

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

    def __kseq_count(self, N: int) -> c.KSeq_count_data_type:
        """
        This function gets a number N and counts every sequence of words for every 1<=k<=N
        For example -> N=3:
            1. Counts how many times each individual word (1-seq) appears in the text. 
            2. Counts how many times each pair of consecutive words (2-seq) appears.
            3. Counts how many times each sequence of three consecutive words (3-seq) appears.
        After comupting all the k-seqs, insert it to a dictionary
        :param N: Positive integer
        :return: Dictionary of all k-seqs (for every 1<=k<=N) for every consecutive words and number of appearence
        """
        data = json.loads(self.processed_data)
        processed_sentences = data[c.Q1][c.PROCESSED_SENTENCES] # using the proccessed data (specific the sentences) from task 1
        sequence_count: c.KSeq_count_data_type = {k: {} for k in range(1, N + 1)} # Initializing a dictionary
        for sentence in processed_sentences: # iterate over each sentence in the processed data, each sentence is represented as a list of words
            for k in range(1, N + 1): # iterate over all sequence lengths 1<=k<=N, for each k - count the occurence of k-length word sequence
                for i in range(len(sentence) - k + 1): # iterate over the words in the current sentences to extract sequences of length k
                    # (len(sentences) - k + 1) -> ensure the function extract only valid sequences that fit within the sentence length
                    sequence = tuple(sentence[i:i + k]) # take a sequence of k consecutive words starting at index i
                    if sequence in sequence_count[k]: # if the sequence is already exists in the k-seq dictionary, add 1 to the count
                        sequence_count[k][sequence] += 1
                    else: # the sequence isn't yet in the k-seq dictionary, initialize it with count 1
                        sequence_count[k][sequence] = 1
        sorted_sequence_count = {k: dict(sorted(sequence_count[k].items())) for k in sequence_count} # lexicographically sort the sequences in each k-seq level  
        return sorted_sequence_count

    def task2(self, N: int) -> str:
        """
        This function returns task 2 output in json format
        :param N: Positive integer
        :return: Output of each k-seq (1<=k<=n) and number of occurences in the processed text
        """
        kseq_count = self.__kseq_count(N) # 'calculate' the data
        output = {
            f"{c.Q2}": {
                f"{N}-Seq Counts": [
                    [
                        f"{k}{c.K_SEQ}",
                        [[
                            " ".join(key),  # merge the list of words to one sentence
                            value
                        ] for key, value in kseq_count[k].items()]
                    ]
                    for k in range(1, N + 1)
                ]
            }
        }
        return json.dumps(output, indent=4)

