
# coding: utf-8

# # Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

# In[1]:


def hash_map(string):
    """Input: String
    Output: Unique hash"""
    char_map = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11,
    'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 
    'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
    'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 
    'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97,'z': 101}
    
    string = string.lower()
    output = 1
    for char in string:
        output *= char_map[char]   
    return output


# In[2]:


def question1(s,t):
    found = False
    
    if len(s) == 0 or len(t) == 0:
        return "Error: Length of input/s must be greater than 0."
    
    elif len(t) > len(s):
        return "Error: Length of t greater than length of s."
    
    else:
        hash_t = hash_map(t) # Calculate the hash of t
        child = s[0:len(t)]  # Get the first substring from s equals to size of t
        hash_child = hash_map(child) # Calculate the hash of first substring of s

        if hash_t == hash_child:  # Check to see if the first susbtring of s has the same hash as t
            found = True
        for i in range(1, len(s) - len(t) + 1): # Keep the sliding window moving forward
            child = s[i:i+len(t)]
            hash_child = (hash_child*hash_map(s[i- 1 + len(t)])) / hash_map(s[i-1]) # Recalculate hash
            if hash_t == hash_child:
                found = True
    return found


# In[3]:


# Test cases
s = "udacity"
t = "ad"
print question1(s, t)
# Should be True

s = "udacity"
t = "ag"
print question1(s, t)
# Should be False

s = ""
t = "ag"
print question1(s, t)
# Should be "Error: Length of input/s must be greater than 0."

s = "udacity"
t = ""
print question1(s, t)
# Should be "Error: Length of input/s must be greater than 0."

s = "udacity"
t = "udacious"
print question1(s, t)
# Should be "Error: Length of t greater than length of s."


# First, we design a function to calculate the unique hash for each string. We keep a sliding window of length t and use the function to calculate the hash of both s and t. If they are the same we have found an anagram. If not we move the sliding window forward one character at a time. This new substring adds one new character and loses one character compared to the previous substring. We update the hash map based on the current substring inside the window and compare it to the hash map of t. 
# We have to iterate through the string at least once. So the time complexity of this algorithm is O(len(s)). The space complexity of this algorithm is constant and hence O(1).
# 
# 

# 
# # Question 2
# Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

# In[4]:


def question2(a):
    """Input: string 
    1) Input should be either all uppercase or lowercase.
    2) Input containing palindromes with spaces in between is not considered palindrome.
    Output: longest palindromic substring"""
    
    start = 0
    max_length = 1
    
    for i in range(1, len(a)): 
        # checking for even palindrome
        lower = i - 1
        upper = i
        while lower >= 0 and upper < len(a) and a[lower] == a[upper]:
            if (upper - lower + 1) > max_length:
                start = lower
                max_length = upper - lower + 1
            lower += -1
            upper += 1
            
        # checking for odd palindrome
        lower = i - 1
        upper = i + 1
        while lower >= 0 and upper < len(a) and a[lower] == a[upper]:
            if (upper - lower + 1) > max_length:
                start = lower
                max_length = upper - lower + 1
            lower += -1
            upper += 1
    
    if max_length > 1:
        return a[start:start + max_length]
    else: 
        return None


# In[5]:


# Test cases
a = 'amoreroma'
print(question2(a))
# Should be amoreoma

a = 'sadracecaradd'
print(question2(a))
# Should be racecar


a = ''
print(question2(a))
# Should be None

a = 'Amore roma'
print(question2(a))
# Should be None


# For each character in the string the program checks for the character before and after that character (in the case of odd palindrome). If they don't match it stops looking. However, if it does match it continues looking to the left and the right. In the worst case, if the string is a single repeated character this process might be repeated for all the characters since each substring is a palindrome. So, the time complexity of this algorithm is O((len(a))^2). This program does not require any extra space, hence the space complexity of this algorithm is O(1)

# # Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
# 
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)], 
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)

# In[6]:


def preprocess_input(G):
    """Input: Adjacency List
    Output: Nodes and List of tuples sorted by their weights"""
    
    nodes = set()
    graph = set()
    
    # Convert adjacency list to set of lists
    for node in G.keys():
        nodes.add(node)
        for vertex in G[node]:
            nodes.add(vertex[0])
            if node < vertex[0]:
                graph.add((node, vertex[0], vertex[1]))
            elif node > vertex[0]:
                graph.add((vertex[0], node, vertex[1]))
    
    # Sort all the edges in increasing order of their weight
    graph = sorted(graph, key = lambda x: x[2])
    return nodes, graph

def find(parent, node):
    """Helper function to find the subset to which node belongs"""
    if parent[node] == node:
        return node
    else:
        return find(parent, parent[node])
    
def union(parent, rank, subset1, subset2):
    """Helper function to do union of two subsets- subset1 and subset2.
    Implements union by rank"""
    subset1 = find(parent, subset1)
    subset2 = find(parent, subset2)
    
    if rank[subset1] > rank[subset2]:
        parent[subset2] = subset1
    elif rank[subset2] > rank[subset1]:
        parent[subset1] = subset2
    else:
        parent[subset1] = subset2
        rank[subset2] += 1
    
def process_output(mst):
    """Input: A list of lists
    Output: Adjacency list"""
    adjacency_list = {}
    for node1, node2, w in mst:
        if node1 in adjacency_list:
            adjacency_list[node1].append((node2, w))
        else:
            adjacency_list[node1] = [(node2, w)]
    return adjacency_list 

def question3(G):
    mst = [] # Store the Minimum Spanning Tree obtained from Graph
    
    # Preprocess the graph as list of tuples sorted by their weights
    nodes, graph = preprocess_input(G)
    # print graph
    
    # Initialize the parent of node as node itself and rank as 0
    parent = {}
    rank = {}
    
    for node in nodes:
        parent[node] = node
        rank[node] = 0
    
    for edge in graph:
        
        # Pick the edge with smallest weight and 
        # find the subset to which each node in the edge belongs
        node1,node2,w = edge
        subset1 = find(parent, node1)
        subset2 = find(parent, node2)
        
        # If including this edge doesn't form a cycle include it in the minimum spannining tree (mst)
        if subset1 != subset2:
            mst.append([node1, node2, w])
            union(parent, rank, subset1, subset2)
        # If including this edge results in cycle, discard it.
    return process_output(mst)


# In[7]:


# Test cases
G = {}
print(question3(G)) 
# Should be {}

G = {'B': [('A', 2)]}
print(question3(G)) 
# Should be {'A': [('B', 2)]}

G = {'A': [('B', 10), ('C', 6), ('D', 5)],
      'B': [('D', 15), ('A', 10)], 
      'C': [('D', 4), ('A', 6)]}
print(question3(G)) 
# Should be {'A': [('D', 5), ('B', 10)], 'C': [('D', 4)]}


# I used Kruskal's algorithm to solve this problem.
# 
# 1. Sort all the edges in increasing order of their weight.
# 2. Iterate through each edge starting from the one with the smallest weight (Greedy Algorithm).
# 3. If it does not form a cycle include it, else discard it. To detect cycles, I used a disjoint-set data structure (Union&Find) to keep track of which vertices are in which subsets.
# 
# The default sorting of edges in Python takes O(ElogE). We iterate through each edge once O(E) and apply find-union algorithm which can take at most O(logV). Hence the time complexity of this algorithm is O(ElogE) + O(ElogV). The space complexity of this algorithm is O(E + V).
# 
# E is the number of edges in the graph and V is the number of vertices.

# # Question 4
# Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be
# 
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.

# In[8]:


def preprocess_input(M):
    """Input: Matrix,
    Output: Adjacency List representing a graph"""
    
    from collections import defaultdict
    G = defaultdict(list)
    
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 1:
                G[i].append(j)
    return G

def question4(T, r, n1, n2):
    """Finds Least Common Ancestor of Binary Search Tree recursively."""
    
    # Convert matrix to adjacency list
    G = preprocess_input(T)
    
    if len(T) == 0:
        return "Empty Tree"
    
    if (n1 > len(T) or n2 > len(T)):
        return "One or both of the nodes not present in Tree."
    
    # If root is greater than both the nodes look to the left of the root.
    if (r > n1 and r > n2):
        return question4(G[r][0])
    
    # If root is smaller than both the nodes look to the right of the root.
    if (r < n1 and r < n2):
        return question4(G[r][1])
    
    # If root is in between node1 (n1) and node2 (n1) return root.
    return r


# In[9]:


# Test cases
print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
# Should be 3

print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          20,
          20)
# Should be "One or both of the nodes not present in Tree."

print question4([],
          3,
          1,
          4)
# Should be Empty Tree


# I have used the properties of Binary Search Tree (BST) to recursively traverse the tree. If the root is greater than both the nodes, then we look to the left of the root for LCA (Least Common Ancestor). If the root is smaller than both the nodes look to the right of the root for LCA. If the root is in the middle of two nodes, then the root is the LCA.
# 
# The time complexity of above solution is O(h) where h is the height of the tree. Also, the above function makes recursive calls hence requires O(h) extra space.

# # Question 5
# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
# 
# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# In[10]:


# A Node object contains the item and a reference to the next Node
class Node(object): 
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Linked List    
class linked_list(object):
    def __init__(self):
        self.head = None
        
    def add(self, item): 
        """Add a new item to the linked list."""
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        
    def length(self):
        """Returns the length of linked list."""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    
def question5(ll, m):
    """Find the element in a singly linked list that's m elements from the end."""
    if ll.length() == 0:
        return "Error: Empty linked list."
    elif m < ll.length():
        current = ll.head
        for i in range(ll.length() -m):
            current = current.next
        return current.data
    return "Error: Length of m greater than length of linked list."


# In[11]:


# Test cases
ll = linked_list()
ll.add(90)
ll.add(80)
ll.add(70)
ll.add(60)
ll.add(50)
ll.add(40)
ll.add(30)
ll.add(20)
ll.add(10)

print question5(ll, 4)
# Should be 60

print question5(ll, 13)
# Should be Error: Length of m greater than length of linked list.

ll = linked_list()
print question5(ll, 4)


# The above solution implements a technique called linked list traversal in which we systematically visit each node. We start a pointer at the first node in the list and as we visit each node, we move the pointer to the next node. In the worst case, we have to traverse all the way to the end of the singly linked list and hence the worst case time complexity is O(len(ll)). Here the space complexity is O(1), since we are not creating any additional list other than input linked list.
