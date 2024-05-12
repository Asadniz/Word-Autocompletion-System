from AVL_tree import *

def filereading(inp):
    '''Reading and removing 2-letter words from corpus.

    Keyword Arguments:
    inp: The input corpus to be processed.'''

    # File reading

    with open(inp) as f:
        words = f.readlines()

    words = words[0]
    words = words.split()
    relevance_list = []

    for i in range(len(words)):
        words[i] = words[i].rstrip()

    # Removing all 2-letter words from the dataset

    for i in range(len(words)):
        if len(words[i]) >= 3:
            relevance_list.append(words[i])

    return relevance_list


def transfer(tree, corpus):
    '''Creating an AVL tree of the corpus.

    Keyword Arguments:
    tree -- the tree (default empty)
    corpus -- the data to make the tree of''' 

    lst = []
    for i in corpus:
        if i not in lst:
            lst.append(i)
            frequency = corpus.count(i)
            tree = insert_node(tree, (i, frequency))

    # Returns an AVL tree with a tuple node value, each tuple stores a word and its frequency.

    return tree


corpus = filereading('Corpus1.txt')  # dataset

# Creating an AVL tree of the corpus

tree = transfer(None, corpus)

suggestions = []

def prefix_matching(node, prefix, suggestions):
    '''Finding words with the given prefix.
    
    Keyword Arguments:
    node -- current node traversed in the tree
    prefix -- the string word is compared with
    suggestions -- list in which the word is added
    '''

    # Selecting last written word/prefix

    spaces = 0
    for space in range(len(prefix)):

        if prefix[space] == " ":

            spaces += 1

    if spaces > 0:

        prefix = prefix.split()
        prefix = prefix[spaces:]
        prefix = "".join(prefix)

    if node is None:
        return

    # Check if the word starts with prefix

    if node['word'][0].startswith(prefix):

        if node['word'][0] not in suggestions:

            suggestions.append(node['word'])

    # Tree traversal

    prefix_matching(node['left'], prefix,  suggestions)

    prefix_matching(node['right'], prefix,  suggestions)

    n = len(suggestions)

    # Sorting the words

    for i in range(n):

        for j in range(0, n-i-1):

            if suggestions[j] < suggestions[j+1]:

                suggestions[j], suggestions[j + 1] = suggestions[j+1], suggestions[j]

    # Getting the best 3 suggestions

    suggestions = suggestions[:3]

    # Fetching the words

    for i in range(len(suggestions)):

        suggestions[i] = suggestions[i][0]

    # Returns a list of the best 3 suggestions

    return suggestions