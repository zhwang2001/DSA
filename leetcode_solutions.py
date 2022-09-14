#Interview
#write down bullet point steps
#implement pseudo code
#implement real code


#Factorial Calculator
class Factorial:
    def calculator(self, n):
        num = n
        while n != 1:
            num = num * (n - 1)
            n = n - 1
        return num

f = Factorial()
print(f.calculator(5))
print(f.calculator(12))
print(f.calculator(4))
print(f.calculator(56))
print(f.calculator(12))
print(f.calculator(3))

#Factorial Calculator recursive
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n = n - 1)

print(factorial(n = 23))
print(factorial(n = 12))

#Binary tree inorder traversal (recursion)
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root) -> list[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


#Binary tree inroder traversal (iterative) #TODO

#Reverse Linked List
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):#reverse the linked list using a stack
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.head, self.tail = head, head
        stack = [None]
        while self.head != None:
            stack.append(self.head.val)
            self.head = self.head.next
        self.head = self.tail
        while stack[-1] == None:
            self.head.next = stack.pop()
            return self.head
         
class pointerSolution(ListNode):#Reverse linked list using pointers
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        
    def addNode(self, val):
        newnode = ListNode(val)
        if self.size == 0:
            self.head = self.tail = newnode #head and tail are both newnode when first created
        self.size += 1
        self.tail.next = newnode
        self.tail = self.tail.next

    def traverse(self):
        internode = self.head
        while internode != None:
            print(f"{internode.val}->", end = '')
            internode = internode.next
        print(f"\nSize of list is {self.size}")


    def reverse(self):
        """
        Pointers: the variables that reference the object (such as curr) references a state of 
        that object without changing the object itself

        Reverses using 3 pointers without affecting underlying values
        """
        curr = self.head
        prev = None
        while curr != None:
            nxt = curr.next #stores the original state of current.next
            curr.next = prev #changes state,current pointer references previous pointer as next
            prev = curr #previous pointer is not current
            curr = nxt #current pointer is not next pointer
        print('\n\n')
        while prev != None:
            print(f"{prev.val}->", end = '')
            prev = prev.next
        print("\n\n")


ps = pointerSolution()
ps.addNode(23)
ps.addNode(12)
ps.addNode(1)
ps.addNode(45)
ps.addNode(14)
ps.addNode(14)
ps.traverse()
ps.reverse()


#reverse linked list using recursion #Question 206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution_206:
    """
     given the head of a singly linked list, reverse the list, and return the reversed list.
     """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if (not head) or (not head.next):
            return head
        
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return node




class Solution_34(object):
    
    def searchRange(self, nums = list[int], target = int) -> list[int]: 
        """
        Question 34: Find first and last position of element in sorted array
        input: nums = [5, 7, 7, 8, 8,8, 10]
        target = 8
        output = [3,4]
        if None in list return [-1, -1]
        """
        index = [-1, -1]
        if target in nums:
            index[0] = nums.index(target)
            index[1] = len(nums) - nums[::-1].index(target) - 1
        return index


sol = Solution_34()
solution = sol.searchRange(nums = [5, 7, 7, 8, 8, 8, 10],target= 8)
print(solution) 
"""
Explanation:
goal is to take first and last target index within array
we utilize the fact that index method takes first occurance  within the
array, at first this seems like a disadvantage because we need to 
take last as well. However this is good because we can simply
create a new instance of the array by flipping the array using negative step [::-1] and the rest of is obvious
 - keep sending email to ceo until they reply LMAO
"""

class Solution_1: 
    """
    Two Sum Pair problem
    Given an array of integers nums and an integer target return indicies of the two numbers such
    that they add up to target
    
    Input: nums = [2, 7 , 11, 15]
    target = 9
    output = [0, 1]

    best run time: Hash Map
    o(n log n): 2 pointers algorithms
    o(n): Naive implementation
    o(n^2): Brute Force / double for loops
    """
    def naivetwosum(self, nums: list[int], target) -> list[int]:
        index = [None, None]
        for i in nums:
            ans = target - i
            if len(set(nums)) != len(nums): #checks if there are duplicates
                if ans in nums:
                    index[0] = nums.index(i)
                    index[1] = (len(nums) - nums[::-1].index(ans) - 1)#use second duplicate by traversing the list backwards 
                    return index
            elif ans == i: #also can use if ans / ans = 1
                i = nums[(nums.index(i)) + 1 % len(nums)]

            elif ans in nums:
                index[0] = nums.index(i)
                index[1] = nums.index(ans)

sol = Solution_1()
nums = [2, 16, 4, 9, 3, 7, 4, 5]
target = 6
print(sol.naivetwosum(nums, target))

nums = [3, 2, 4]
target = 6
print(sol.naivetwosum(nums, target))

nums = [3, 3, 6, 4] #FIXME
target = 6
print(sol.naivetwosum(nums, target))

nums = [3, 2, 3]
target = 6 
print(sol.naivetwosum(nums, target))

nums = [2, 5, 5, 11]
target = 10 
print(sol.naivetwosum(nums, target))

nums = [1,1,1,1,1,1,4,1,1,7,1,1,1]
target = 11 
print(sol.naivetwosum(nums, target))

#NOTE
""" 
the above solution was obtained using trial and error, 
debugging, brute forcing test cases and a lot of conditional
statements. The answer could never been obtained first try
. The best way to solve the question is by using hashmap
"""


#store values in set
#use a pointer



class treeNode:
    def __init__(self, val: None):
        self.val = val
        self.right = None
        self.left = None


class Solution_104:
    def maxdepth(self, val):
        self.depth = 0
        newnode = treeNode(val = val)
        if newnode.val == None:
            self.root, self.val = newnode
        """give the root of a binary tree return its maximum depth"""
        self.pointer = newnode
        while self.pointer.left or self.pointer.right != None:
            if data < self.val:
                if self.left == None:
                    self.pointer.left = newnode
                    self.pointer.right = None
                self.depth += 1
                print(f"degree of tree is now {self.degree}")
            elif data > self.val:
                if self.right == None:
                    self.pointer.right = newnode
                    self.pointer.left = None
                self.depth += 1
                print(f"degree of tree is now {self.degree}")

            else:
                raise Exception("valus must not match values of parent node")
        self.pointer = self.root


#sol = Solution_104()
#sol.maxdepth(23)

class TreeNode:#FIXME
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution_701:
    def insertIntoBST(self, root, data):
            """
            1. If the root is null, we create a new node with a value of val and return it
            2. if the root is not null we check the value of the root with the value of val. If 
            th val is less than the root we call the function recursively and pass the left child of the 
            root as the new root if the val is greater than teh root we call the function recursively and pass
            the right child of the root as the new root
            3. We return the root after updating the left or right child of the root
            """
            if root == None:
                root = TreeNode(data)
                return root
            if root.val > data:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.right = self.insertIntoBST(root.right, val)
            return root


class Solution: #FIXME
    def lengthOfLonfgestSubstring(self, s: str) -> int:
        print('lol') 


class Solution_125:
    """A phrase is a palindrome if, after converting all uppercase
    letters into lowercase letters and removing all non-alphanumeric characters, it
    reads the same forward and backward. Alphanumeric characters include letters and numbers

    use isalnum() to check if the string contains alpha or numeric characters
    one method replaces isalpha and isnumeric
    use .lower to remove capital letters

    return True if is palindrome else return False
    """
    def isPalindrome(self, s: str) -> bool:
        pal_checker = []
        for letter in s:
            if letter.isalnum():
                pal_checker.append(letter.lower())
                
        if pal_checker[::-1] == pal_checker:
            return True
            print("it's a palindrome")
        return False
        print("it's not a palindrome")

sol = Solution_125()
print(sol.isPalindrome(s = 'racecar'))
print(sol.isPalindrome(s = 'sdfsdff'))
print(sol.isPalindrome(s = '23 sdf SSS fds 32'))
print(sol.isPalindrome(s = ':23 SDFADF  sfd SD FDDF'))




"""
Tricks:
(len(list) - list[::-1].index(item) - 1): [obtain last index through traversing list backwards, good for pair problems]
self.head = (list[index] + 1) % len (list) [circular indexer to find the next index without raising errors
self.tail = (list[index] + len(list)) % len(list) [circular indexer to find tail within queue

class Node:
   # "For implementation in stacks, queues, deques and the circular variations of the previous 3"
    def __init__(self, data):
        self.data = data #stores the data for the nodes
        self.next = next #actually returns the next address within queue or deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
    #"traverse allows us to show the linked list in its entirety"
        self.head = None
        self.tail = None
        self.size = 0


   def traverse(self, ind, display: true):
      #display  = show entire linked list
      if self.isempty():
          print("linked list has no nodes")

      internode = self.head
      elif display == True:
          while self.head != None:
              print(internode.data, '->', end = ' ')
      for i in range(ind):
          internode = internode.next 
      print(f'{internode.data} at index{ind}')
      return internode
"""

# Sequential/linear: Queues, Stacks, Deques, Linked Lists, Arrays
# Hierachal: Trees, Graphs




#Github and Git cheatsheat

#git clone (clone git repositorye
#git commit (commit changes locally to git directory)
#git push (push changes to remote repository such as git)
#git pull (pull changes from remote repository to local git directory) #git add (force track new files / changes)
#git init (initialize local directory)
#git add <filename> (tracks file and adds to staging area)
#git add . tracks all files
#git status (status of uncommited and tracked files)
#git stage (staging area after using git add to start tracking file)
#git revert (revert changes)
#git diff --ours
#git diff --theirs
#git show
#git revert
#gitk (GUI application for git)
#git blame <filename> (check the changes to a specific file)

#git config user.name "zhwang822" (local configuration)
#git config user.email "jameszihao.wang@mail.utoronto.ca" (local configuration)
#git config --global user.name "zhwang2001" (global configuration)
#git config --global user.email "zhwang2001@gmail.com" (global configuration)
#git config --list (shows all configurations)
#git config --list --show-origin (show origin flag)

#git commit -m "initial commit"
#git remote set-url origin git@github.com:zhwang822/machine_learning.git
#git push -u origin master
#git remote add origin https:// link 
#git rm -r name (remove folder / do it recursively)
#git rm -f name (remove file)
#git mv <old file name> <new file name>

#LARGE DATASETS ARE UPLOADED THROUGH GIT LFS
#1. remove all large files from repository
#2. git lfs install
#3. git lfs track "*.csv" #track all csv files
#4. git add .
#5. add back large files
#6. git add .
#7. git commit -m
#8. git push origin master



#GitBash
# $ls -la #list all files
# $touch <file> #create new file
# $git commit -am (commit all modified and delted files except for non tracked files)
# echo "Hello git!" > hello.git (insert Hello git! into hello.git file) (can be used with .gitignore
# mkdir file (make a non special directory in current directory) 
# rmdir (remove directory)
# mv (move directory)
# git branch -a
# git checkout
# echo "todo.txt" >> .gitignore (add files from directory into .gitignore so they won't appear in repository
# git log (shows logs of commits)

#branching
#git branch (current branch)
#git checkout/switch (switch branches)
#git merge <branch> merge current branch with <branch>



begging


#Vim Cheatsheat

"""
:q = #quit
:e filename.py = load file
:w filename.py = save file
:synatax on/off = turn on or off
:wq save and close
/ search a word
:dd delete line
:yy yank a line

'"*yy or "+yy' for copy to system keyboard
'"*p or "+p' for paste from system keyboard

:p used to yank a word
:3dd delete 3 lines
:set number
:set no number = set no number line
:q! = dont save
a = append
x = delete

:!interpreter filename.py run program
+p = paste
y = copy the selected text to keyboard
yy copy current line

d$ (also add number to beginning to delete more lines)
de delete until end of line
dw delete until beggining of word
diw delete entire word

colorscheme + space + tab = change color

control w, s = split horizontally
control w, j or k go to top or bottom window

H = first line of current screen
M = middle line of current screen
L = last line of current screen



d$ (also add number to beginning to delete more lines)
de delete until end of line
dw delete until beggining of word


colorscheme + space + tab = change color

control w, s = split horizontally
control w, j or k go to top or bottom window

control w, r rotate
:vsplit filename.py split vertically or vsp filename.py
:vs filename.py split vertically 
sp filename.py split horizonatally

Navigation:

control d = move 1/2 page down
control u = move 1/2  page up
control e = moves screen up 1 line
control y = moves screen down 1 line
control b = moves screen up one page 
control f = moves screen down one page



[[ = beginning of page
]] = end of page
shift { = move a couple of lines up
sfhit } = move a couple of lines down

control shift ] does something
control ww goes through all windows
:terminal opens terminal


disable mouse in vim
vertical resize 30
resize 30
control v > = select block and indent

:Sex = file explorer
:Sex! = file explorer vertical
:Explore = file explorer

dj = delete 2 lines
fa (finds first occurence of a), ; finds next occurence
control G to find out information about the page
/ = search + <Enter> --> n to find next occurent N to find previous
? = search backwards
fa (finds first occurence of a), ; finds next occurence
control G to find out information about the page

o = start a new line after and enter insert mode
shift o = start a new line before and enter insert mode
^ = go to first non blank character on line
$ = go to end of current line
0 = go to beginning of current line

:help key-notation
create a new window using control w v
set nohlsearch = turn off search highliting
use f and daw to (caw used to delete entire word + insert mode)

ddkp = move line up
ddp = move line down

ci(bracket type) if cursor within the bracket or brace can delete its contnet
ca deletes everything but inner contents

>> indent
<< outdent


g; go to last cursor location
/word/ go to first occurence of word


w = go to first character in line, also used to go through list by first word

control o = jump back to the previous positoin
control i = jump to next position

use s or r to replace text
press j to join
shift # to select all words under cursor

#COMBINATIONS
shift A = go to end of line and insert mode (use with enter to move to next line fast
shift I = go to beginning of line and insert mode

shift V = whole line highlighting visual mode
v = single character highlting (used in conjunction with w or b or 5 enter)
j = add on to other keys for more functionality
>
dj = 2 lines down or 2yy
shift v j 1 line down

#HORITZONTAL DOMINATION:
f[word] = find word on line, use ; to navigate forward, , to navigate backwards 
#use shift f for traversing string backwards
t[word] = just before word, use ; to navigate forward, , to navigate backward
#use shift t for traversiing string backwards

uC
#VERTICAL DOMINATION
10 o jj = 10 enters down
shift j = remove blank spaces

#VIMRC
vim $MYVIMRC
e $MYVIMRC
:so (to refresh changes) (debugger)
set cursorline
set cursorcolumn
vimrc configuration guide how to customize your vim code editor with mappings vim script
hilight Cursorcolumn ctermbg = blue cterm = red
hilight Cursorline ctermbg = blue cterm = red

zz: save and close
G = go to end of page
:b <filename> go to file
:ls use ls in vim command
:pwd = current directory
"""






