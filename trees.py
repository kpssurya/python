

import math
import sys

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def preorder(root):
	if root:
		print(root.data, end = ' ')
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.data, end = ' ')

def inorder(root):
	if root.left != None:
		inorder(root.left)
	print(root.data, end = ' ')
	if root.right != None:
		inorder(root.right)

def levelorder(root):
	q = []
	q.append(root)

	while len(q) != 0:
		node = q.pop(0)
		print(node.data, end = ' ')

		if (node.left != None):
			q.append(node.left)

		if (node.right != None):
			q.append(node.right)

def levelorderTreePrint(root):
	q = []
	q.append(root)

	while True:
		nodes = len(q)
		if nodes == 0:
			break

		while (nodes>0):
			node = q.pop(0)
			print (node.data, end = ' ')

			if (node.left != None):
				q.append(node.left)

			if (node.right != None):
				q.append(node.right)

			nodes = nodes - 1

		print()

def height(root):
	if (root == None):
		return 0
	else:
		lh = height(root.left)
		rh = height(root.right)

		if (lh>rh):
			return lh+1
		else:
			return rh+1


def diameter(root):
	if (root == None):
		return 0

	lh = height(root.left)
	rh = height(root.right)

	ld = diameter(root.left)
	rd = diameter(root.right)

	return max(lh+rh+1, ld, rd)

def isBST(root):
	max = sys.maxsize
	min = -max-1

	return isBSTUtil(root, min, max)


def isBSTUtil(node, min, max):
	if node == None:
		return True

	if (node.data < min or node.data > max):
		return False

	return (isBSTUtil(node.left, min, node.data) and isBSTUtil(node.right, node.data, max))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

bst = TreeNode(4)
bst.left = TreeNode(2)
bst.right = TreeNode(5)
bst.left.left = TreeNode(1)
bst.left.rigth = TreeNode(3)

print ("Pre order traversal of tree")
preorder(root)
print()

print ("postorder order traversal of tree")
postorder(root)
print()

print ("In order traversal of tree")
inorder(root)
print()

print ("Level order traversal of tree")
levelorder(root)
print()

print ("Level order traversal of tree with each level")
levelorderTreePrint(root)
print()

print ("Height of the tree: " + str(height(root)))

print ("Diameter of the tree: " + str(diameter(root)))

print ("Is the tree a BST?: " + str(isBST(root)))
print ("Is the tree a BST?: " + str(isBST(bst)))

