class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None

    def nextNode(self):
        return self.next
    
    def __str__(self):
        return f'this is {self.data}'

class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        currentNode = self.head

        while currentNode.nextNode() != None:
            count = count + 1
            currentNode = currentNode.nextNode()

        return count

    def __getitem__(self, position):
        listLength = self.__len__()
        count = 0
        currentNode = self.head

        #Positive index
        if position >= 0 and position <= listLength:
            while count < position:
                currentNode = currentNode.nextNode()
                count = count+1

            return currentNode
        
        #negative index
        elif position < 0:
            stepsToTake = listLength + 1 + position

            while count < stepsToTake:

                currentNode = currentNode.nextNode()
                count = count+1

            return currentNode    


node1 = Node('Node 1')
node2 = Node('Node 2')
node3 = Node('Node 3')
node4 = Node('Node 4')
node5 = Node('Node 5')
node6 = Node('Node 6')
node7 = Node('Node 7')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

llist1 = LinkedList()
llist1.head = node1

#print(len(llist1))
print(llist1[7])