#Adapted from code by Nikhil Kumar Singh(nickzuck_007) from GeeksForGeeks.org
from Node import Node

def getPathToNodeFromRoot(root, path, key):
    #If the root is undefined, return false
    if root is None:
        return False

    #Append the root node's key to the current path
    path.append(root.nodeKey)

    #If this is the node we're searching for
    if root.nodeKey == key:
        return True

    # Look for the key in the l or r subtrees recursively
    if ((root.l != None and getPathToNodeFromRoot(root.l, path, key))
            or
        (root.r != None and getPathToNodeFromRoot(root.r, path, key))):
        return True

    #Pop the bottom value from the path (erase recursively)
    # return false, as the value has not been found.
    path.pop()
    return False

#Find the lowest common ancestor, or return -1
def findLowestCommonAncestor(root, n1, n2):
    # To store paths to n1 and n2 from the root
    path1 = []
    path2 = []

    #Populate paths with keys
    if (not getPathToNodeFromRoot(root, path1, n1)
            or
        not getPathToNodeFromRoot(root, path2, n2)):
        return -1

    # Compare the paths, find first value between them that differs
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1

    #Determine where paths diverge
    return path1[i - 1]

if __name__ == '__main__':
    root = Node(0)
    root.l = Node(1)
    root.r = Node(2)
    root.l.l = Node(3)
    root.l.r = Node(4)
    root.r.l = Node(5)
    root.r.r = Node(6)
    root.l.l.l = Node(7)
    root.l.l.r = Node(8)
    root.l.r.l = Node(9)
    root.l.r.r = Node(10)
    root.r.l.l = Node(11)
    root.r.l.r = Node(12)
    root.r.r.l = Node(13)
    root.r.r.r = Node(14)

    findLowestCommonAncestor(root, 11, 13)
    findLowestCommonAncestor(root, 9, 10)
    findLowestCommonAncestor(root, 3, 4)
    findLowestCommonAncestor(root, 7, 8)
    findLowestCommonAncestor(root, 11, 12)