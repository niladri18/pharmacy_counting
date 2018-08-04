#! Binary search tree class
import sys

__author__ = "Niladri Gomes"
__email__ = "nldrgomeser48@gmail.com"
__date__ = "Aug-03-2018"

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	def add(self,data):
		if data[1] > self.data[1]:
			if self.left:
				self.left.add(data)
			else:
				self.left = Node(data)
		elif data[1] == self.data[1]: 
			if data[0] < self.data[0]:
				if self.left:
					self.left.add(data)
				else:
					self.left = Node(data)
		else:
			if self.right:
				self.right.add(data)
			else:
				self.right = Node(data)
	def inorder(self):
		if self.left:
			yield from self.left.inorder()
		#print(self.data)
		yield self.data
		#return
		if self.right:
			yield from self.right.inorder()
						
				
class BST:
	def __init__(self):
		self.item = None
	
	def add(self,data):
		if self.item:
			self.item.add(data)
		else:
			self.item = Node(data)
			
	
	def inorder(self):
		if self.item:
			yield from self.item.inorder()

			

