# Text Analyzer Project / Afek Aharoni / afek.aharoni / 214143414

![Text Analyzer](https://github.com/AfekAharoni/TextAnalyzer/blob/main/TextAnalyzer/Logo.png?raw=true)

## Extensions:

* Extension 8 - Checking for fixed-length paths between people in a graph, without repeating nodes, to see if a specific path length exists.

* Extension 9 - A text analysis algorithm clusters sentences using a graph based on shared words, with sorting and runtime analysis.

Task 8 extends functionallity to determine whether two people are connected by a fixed-length path in a connection graph. The input includes a JSON file with a list of connected pairs and an integer K representing the exact path length to check. The path cannot contain repeated nodes (no loops). The output is a list of name pairs with a bollean value indicating whether a path of length K exists between them. Additionally, runtime analysis is conducted to evaluate the impact of different K values on performance.

Task 9 focuses on grouping sentences based on shared words by constructing a graph where each sentence is a node, and an edge is created between two sentences if they share a minumim number of words (as defined by threshold). The algorithm builds the graph and clusters sentences into group of interconnected nodes, meaning each sentence in a group is connected to at least one other sentence. The groups are sorted first by size (smallest to largest) and then alphabetically if multiple groups have the same size. The output is a JSON-formatted list of sentences groups, showing which sentences are connected.

## Design

During the project, several critical decisions were made to ensure efficiency, high performance and maintainabillity of the code. The main decisions focudes on selecting data structures, organizing the code, and optimizing searches and computations.

1. A dictionary was chosen over alternatives such as list or custom data structures. This decision was based on several factors. Dictionaries allow fast access to sentences using a unique key, making lookup and comparisons more efficient without requiring a full list scan. (Task 1)

2. Using a queue was preferred over recursion or simple arrays for managing searches. BFS (Breadth-First Search), as I explained in the video, requires a queue to efficiently manage connection layers, ensuring systematic exploration. The queue based approach prevents redundant searches and enhances the overall efficiency of detecting connections between people in the dataset. (Task 7 & Task 8)

3. Using sets to identify common words between sentences was chosen to improve efficiency. This approach allows checking shared words in constant time instead of the quadratic complexity associated with comparing words one by one. This significantly optimizes performance when dealing with large text datasets. (Task 9)

4. Searching for KSeq occurrences was optimized to O(1) complexity for each lookup. By using a dictionary to store the KSeq mappings to sentences, I ensure that retrieving the sentences associated with a given KSeq is done in constant time. This significantly improves the efficiency of the search process compared to iterating over a list. (Task 4)

5. A dedicated constants file was utilized to store predefined values such as attribute names, output messages, and error messages (for testing). This approach ensured consistency across all tasks and minimized hardcoded strings throughout the project. By centralizing these values, updates and modifications could be efficiently managed without requiring extensive code changes.

6. A separate validation module was implemented to check input parameters before executing each task. This validation process ensures that:
   a. Required file paths existed and were accessible.
   b. Numerical parameters such as threshold and sequence lengths were within the acceptable ranges.
   c. Proper argument types were provided, preventing runtime errors.

The design choices in the project were made with a balance between computational efficiency and code readability. Choosing appropriate data structures for each task contributed to improving algorithm performance and handling large data volumes optimally.
