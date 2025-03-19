# ===> Imports <=== 
from typing import Optional
from task6 import DirectConnections
from task1 import *
import json
import constants as c

class IndirectConnections:
    """
    This class represents the indirect connections between people in the graph
    """
    def __init__(self, sentences_file_path: Optional[str] = None, removewords_file_path: Optional[str] = None, 
                 names_file_path: Optional[str] = None, pairs_file_path: Optional[str] = None, maximal_distance: Optional[int] = None, 
                 windowsize: Optional[int] = None, threshold: Optional[int] = None, 
                   preprocessed_data: Optional[str] = None, fixed_length: Optional[int] = None):
        if preprocessed_data:
            self.__preprocessed_data = extract_processed_data(preprocessed_data)
        else:
            direct_connections = DirectConnections(sentences_file_path=sentences_file_path, removewords_file_path=removewords_file_path, 
                                                    names_file_path=names_file_path, windowsize=windowsize,
                                                    threshold=threshold)
            self.__preprocessed_data = direct_connections.task6()
        self.__maximal_distance = maximal_distance
        self.__fixed_length = fixed_length # Extension: Task 8
        self.__people_connections_data = self.__read_file(pairs_file_path)
    
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
    def people_connections_data(self) -> str:
        """
        :return: People connections data
        """
        return self.__people_connections_data

    @people_connections_data.setter # Setter
    def people_connections_data(self, people_connections_data: str):
        """
        :return: People connections data to set as attribute
        """
        self.__people_connections_data = people_connections_data
    
    @property # Getter
    def maximal_distance(self) -> Optional[int]:
        """
        :return: The maximal distance allowed
        """
        return self.__maximal_distance

    @maximal_distance.setter # Setter
    def maximal_distance(self, maximal_distance: int):
        """
        :param maximal_distance: The maximal distance allowed to set as attribute
        """
        self.__maximal_distance = maximal_distance 

    def __read_file(self, file_path) -> str:
        """
        This function gets a file path and returns the file content as string
        :param file_path: A file path
        :return: File content
        """
        with open(file_path, mode = 'r') as f:
            content = f.read()
        return content

    def __extract_data_from_file(self, type_of_data: str) -> list:
        """
        This function extract the data (Pair Matches or People Connections) 
            1. type_of_data can be 'Pair Matches', in this case, the function returns list of the pair matches as received in 
                the processed data of task 6
            2. type_of_data can be 'keys', in this case, the function returns the list of the people connections need to be
                checked in task 7
        :param type_of_data: Type of data need to be extracted (Pair Matches or keys)
        :return: List of Pair Matches or List of keys
        """
        if type_of_data == c.PAIR_MATCHES:
            data = json.loads(self.preprocessed_data)     
            extracted_data = data[c.Q6][c.PAIR_MATCHES]
        else: # type_of_data == KEYS
            data = json.loads(self.people_connections_data)
            extracted_data = data[c.KEYS]
        return extracted_data

    def __create_neighbors_dict(self, pairs: list) -> dict:
        """
        This function creates a dictionary from the list of the direct connections
        :param pairs: List of direct connections
        :return: A dictionary of neighbors {person: [list of all neighbors (edges)]}
        """
        neighbors_dict: dict = dict()
        for pair in pairs:
            first_person = c.WHITESPACE.join(pair[c.FIRST_PERSON_INDEX])
            second_person = c.WHITESPACE.join(pair[c.SECOND_PERSON_INDEX])
            # if one of those people not in the dictionary, initalize a list for him
            if first_person not in neighbors_dict:
                neighbors_dict[first_person] = []
            if second_person not in neighbors_dict:
                neighbors_dict[second_person] = []
            # these two are a pair, so add them for each other neighbors
            neighbors_dict[first_person].append(second_person)
            neighbors_dict[second_person].append(first_person)
        return neighbors_dict
    
    def __check_if_pair_connected(self, neighbors_dict: dict, first_person: str, second_person: str, maximal_distance: int) -> bool:
        """
        This function checks if two people are connected within the maximal distance 
        :param neighbors_dict: The neighbors list of the graph {person: [list of all neighbors (edges)]}
        :param first_person: First person primary name
        :param second_person: Second person primary name
        :param maximal_distance: The maximum distance allowed
        :return: True if connected within the maximal distance, False else
        """
        queue = []
        # The queue data structure is a list of tuples, when the first element in the tuple is
        # the person name and the second element is the distance from the first person
        # [(Name, distance)]
        queue.append((first_person, 0)) # first defaultive value
        already_visited = set() # set to ensure that won't be duplications
        while len(queue) > 0: 
            currect_person, distance = queue[0]
            del queue[0] # delete from the queue, because this iteration is running over this preson
            if currect_person == second_person: # so there is a connection between first_person and second_person within the maximal distance
                return True
            if distance < maximal_distance: # can continue to run
                if currect_person in neighbors_dict: # so maybe there will be another edge to continue with
                    neighbors = neighbors_dict[currect_person]
                    for neighbor in neighbors: 
                        if neighbor not in already_visited: # if didn't visited this 'node'
                            already_visited.add(neighbor) # next iteration will visit this 'node', so add to the visited
                            queue.append((neighbor, distance + 1)) # append so the next iteration will run over this neighbor
        return False

    def task7(self):
        """
        This function returns task 7 output in json format
        :return: Output of list of person-pairs whether they both are connected by any path in the 
            graph. Even if they're not directly connected, they could still be linked through one or more
            intermediate people (friends or friends-of-friends)
        """
        pairs_to_check = self.__extract_data_from_file(c.KEYS)
        direct_pairs = self.__extract_data_from_file(c.PAIR_MATCHES)
        neighbors_dict = self.__create_neighbors_dict(direct_pairs)
        results = []
        for pair in pairs_to_check:
            first_person, second_person = sorted(pair) # sort alphabetically
            is_connected = self.__check_if_pair_connected(neighbors_dict, first_person, second_person, self.maximal_distance)
            results.append([first_person, second_person, is_connected])
        results = sorted(results, key=lambda names:(names[c.FIRST_PERSON_INDEX], names[c.SECOND_PERSON_INDEX]))
        output = {c.Q7: {c.PAIR_MATCHES: results}}
        return ((json.dumps(output, indent=4)))

    # ===> Extension: Task 8 <===
    @property # Getter
    def fixed_length(self) -> Optional[int]:
        """
        :return: The fixed length of a path
        """
        return self.__fixed_length

    @fixed_length.setter # Setter
    def fixed_length(self, fixed_length: int):
        """
        :param fixed_length: The fixed length of a path
        """
        self.__fixed_length = fixed_length

    def __check_if_pair_connected_by_fixed_length(self, neighbors_dict: dict, first_person: str, second_person: str, fixed_length: int, already_visited: Optional[set] = None) -> bool:
        """
        This function checks if two people are connected in fixed_length length of path
        :param neighbors_dict: The neighbors list of the graph {person: [list of all neighbors (edges)]}
        :param first_person: First person primary name
        :param second_person: Second person primary name
        :param fixed_length: The fixed length needed to check path between those two people
        :return: True if connected in exactly fixed_length, False else
        """        
        if already_visited is None: # first time running in the recursive for this pair (first_person, second_person)
            already_visited = set()
        if first_person == second_person and fixed_length == 0: 
            # first_person and second_person are connected by a path in extacly 'fixed_length' length of path
            return True
        if fixed_length == 0 or first_person not in neighbors_dict:
            # if got to the fixed_length length of path or this person has no links (a leaf in the graph)
            return False
        already_visited.add(first_person) 
        for neighbor in neighbors_dict[first_person]: # check for every linked node for this person
            if neighbor not in already_visited: # not visited yet, so check for this path
                if self.__check_if_pair_connected_by_fixed_length(neighbors_dict, neighbor, second_person, fixed_length - 1, already_visited):
                    # there is a connection
                    return True
        return False # if got here, there is no connection in fixed_length from first_person to second_person

    def task8(self):
        """
        This function returns task 8 output in json format
        :return: Output of list of person-pairs whether they both are connected by any path in the 
            graph in fixed-length parameter given. Even if they're not directly connected, they could still be linked through one or more
            intermediate people (friends or friends-of-friends)
        """
        pairs_to_check = self.__extract_data_from_file(c.KEYS)
        direct_pairs = self.__extract_data_from_file(c.PAIR_MATCHES)
        neighbors_dict = self.__create_neighbors_dict(direct_pairs)
        results = []
        for pair in pairs_to_check:
            first_person, second_person = sorted(pair) # sort alphabetically
            is_connected = self.__check_if_pair_connected_by_fixed_length(neighbors_dict, first_person, second_person, self.fixed_length)
            results.append([first_person, second_person, is_connected])
        results = sorted(results, key=lambda names:(names[c.FIRST_PERSON_INDEX], names[c.SECOND_PERSON_INDEX]))
        output = {c.Q8: {c.PAIR_MATCHES: results}}
        return ((json.dumps(output, indent=4)))       
