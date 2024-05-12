def node(word): # Creates a new node
    return {'word': word, 'left': None, 'right': None, 'height': 1}


def get_height(node):  # Returns tree height

    if node is None:
        return 0
    
    return node['height']


def update_height(node): # Changes tree height after node insertion

    node['height'] = 1 + max(get_height(node['left']), get_height(node['right']))


def subtree_difference(node):  # Returns balance factor of the tree
    if node is None:
        return 0
    
    return get_height(node['left']) - get_height(node['right'])


def rotate_left(y): # Left-left rotation

    if y is None or y['right'] is None:
        return y

    x = y['right']

    y['right'] = x['left']
    x['left'] = y

    update_height(y)
    update_height(x)

    return x


def rotate_right(x): # Right-right rotation

    if x is None or x['left'] is None:
        return x

    y = x['left']

    x['left'] = y['right']
    y['right'] = x

    update_height(x)
    update_height(y)

    return y


def insert_node(root, key): # Node insertion
    '''Inserts value in the tree and corrects imbalances (if any).

    Keyword Arguments:
    root -- starting node
    key -- the value to be inserted'''

    if root is None:
        return node(key)

    if key[0] < root['word'][0]:
        root['left'] = insert_node(root['left'], key)

    else:
        root['right'] = insert_node(root['right'], key)

    update_height(root)

    balance = subtree_difference(root)
    
    # Left-left imbalance

    if balance > 1 and key[0] < root['left']['word'][0]:
        
        return rotate_right(root)

    # Right-right imbalance

    if balance < -1 and key[0] > root['right']['word'][0]:

        return rotate_left(root)

    # Right-left imbalance

    if balance < -1 and key[0] < root['right']['word'][0]:

        root['right'] = rotate_right(root['right'])
        return rotate_left(root)

    # Left-right imbalance

    if balance > 1 and key[0] > root['left']['word'][0]:

        root['left'] = rotate_left(root['left'])
        return rotate_right(root)
    return root


def test_avl():
    '''Testcase'''

    root = None
    # words = ['apple', 'banana', 'cake', 'beetroot', 'normal']
    words = ["monkey", 'zebra', 'octpus']
    for word in words:
        root = insert_node(root, word)
    print(root)
