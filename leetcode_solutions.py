#Interview
#write down bullet point steps
#implement pseudo code
#implement real code


#Tricks
"""
1. array.insert(i) = array[i:i] = number
2. 2 arrays: nums, nums2
    - Can use zip function to iterate through both at the same time (zip is O(1)
    - for a, b in zip(nums1, nums2)
        print(a, b)
3. Nested array [[1,2,3],[1,2,3].[3,2,4]] can be unwrapped using for loop
    - for a,b,c in array:
        print(a, b, c)
"""

#Count items matching a rule question 1773
class Solution(object):
    """
    You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

    The ith item is said to match the rule if one of the following is true:

    ruleKey == "type" and ruleValue == typei.
    ruleKey == "color" and ruleValue == colori.
    ruleKey == "name" and ruleValue == namei.
    Return the number of items that match the given rule.
    """

    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int

        O(N) time complexity
        O(1) space complexity
        """
        count = 0
        dic = {"type": 0, "color": 1, "name": 2}
        for i in range(len(items)):
            if items[i][dic[ruleKey]] == ruleValue:
                count += 1
        return count

sol = Solution()
print('-- Count items matching a rule--')
print(sol.countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
print('\n\n\n')


#Find Target indices after sorting array question 2089
class Solution(object):
    """
    You are given a 0-indexed integer array nums and a target element target.

    A target index is an index i such that nums[i] == target.

    Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
    """
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Slow Solution
        #O(nlogn) time complexity
        #O(n) space complexity

        ans = []
        nums.sort()
        for count, i in enumerate(nums):
            if i == target:
                ans.append(count)
        return ans

        #Faster Solution
        #O(N) time complexity
        #O(N) space complexity

        index, count = 0, 0
        for i in nums:
            if i < target:
                index += 1
            elif i == target:
                count += 1
        return list(range(index, count+index))
        
sol = Solution()
print('-- Find Target indicies after sorting array--')
print(sol.targetIndices([1,2,5,2,3], target = 2))
print(sol.targetIndices([1,2,5,2,3], target = 5))
print('\n\n\n')

#Create Target array in the given order question 1389
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        arr = []
        for n,i in zip(nums,index): #use zip function to iterate through 2 lists at once
            arr[i:i] = [n] #use slicing so we don't get list out of range index error, replaces insert method
        return arr

#Maximum product of two elements in an Array question 1464
class Solution:
    """
    Given the array of integers nums, you will choose two different
    indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
    """
    def maxProduct(self, nums) -> int:
        """
        O(N) = time complexity
        O(N) = space complexity
        """
        num1 = max(nums)
        nums.remove(num1)
        num2 = max(nums)
        return (num1 - 1) * (num2 - 1)


sol = Solution()
print("--Max Product--")
print(sol.maxProduct([3,4,5,2]))
print(sol.maxProduct([1,5,4,5]))
print('\n\n\n')

#Kth distinct string in an array question 2053
class Solution(object):
    """
    A distinct string is a string that is present only once in an array.

    Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

    Note that the strings are considered in the order in which they appear in the array.

    Input: arr = ["d","b","c","b","c","a"], k = 2
    Output: "a"
    Explanation:
    The only distinct strings in arr are "d" and "a".
    "d" appears 1st, so it is the 1st distinct string.
    "a" appears 2nd, so it is the 2nd distinct string.
    Since k == 2, "a" is returned. 
    """
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str

        O(N) time complexity
        O(1) space complexity
        """
        count = 0
        for i in arr:
            if arr.count(i) == 1: #the trick is to use count method
                count += 1
                if count == k:
                    return i

        return ""

sol = Solution()
print('--Kth distinct string in an array--')
print(sol.kthDistinct(["d","b","c","b","c","a"], k = 2))
print(sol.kthDistinct(["a","b","a"], k=3))
print(sol.kthDistinct(arr = ["aaa","aa","a"], k = 1))
print('\n\n\n')

#Split a string in balanced strings question 1221
class Solution(object):
    """
    Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

    Given a balanced string s, split it into some number of substrings such that:

    Each substring is balanced.
    Return the maximum number of balanced strings you can obtain.
    """
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int

        O(N) linear time complexity
        O(1) Space complexity
        """
        count, balanced_string = 0,0
        for i in s:
            if i == "R":
                count += 1
            elif i == "L":
                count -= 1
            if count == 0:
                balanced_string += 1
        return balanced_string
        
sol = Solution()
print('split a string in balanced strings')
print(sol.balancedStringSplit("RLRLRRRRLLLLRLLR"))
print(sol.balancedStringSplit("LLLLRRRR"))
print('\n\n\n')

#Overlap Intervals question 2623
class Solution(object):
    def overlap(self, intervals, rate, person):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        [[1,7],[2,9],[3,4]]

        Person's A:
        1-2 = 10 dollars
        2-3 = 5 dollars
        3-4 = 3.33 dollars
        4-5 = 5 dollars
        5-6 = 5 dollars
        6-7 = 5 dollars

        28 dollars and 33 cents
        60 dollars
        """
        count = 1
        new_cost = 0
        record = intervals[person]
        intervals.pop(person)
        for integer in range(record[0], record[1]):
            for compare in intervals:
                if integer < compare[1] and integer >= compare[0]:
                    count += 1
            new_cost += rate / count
            count = 1
        print(f"You save {rate * (record[1] - record[0]) - new_cost}")
        return new_cost


sol = Solution()
print('--Overlap intervals--')
print(sol.overlap(intervals=[[1, 7], [2, 9], [3, 4]], rate=10, person=0))
print(sol.overlap(intervals=[[1, 6], [4, 8], [3, 9]], rate=6, person=2))
print(sol.overlap(intervals=[[1, 6], [4, 8], [3, 9]], rate=6, person=2))
print(sol.overlap(intervals=[[10, 22], [
      10, 22], [10, 22]], rate=500, person=2))

print(sol.overlap(intervals=[[3, 5], [1, 9], [4, 24]], rate=500, person=2))
print(sol.overlap(intervals=[[3, 5], [1, 9], [
      4, 24], [3, 6], [1, 7]], rate=500, person=2))

print('\n\n\n')

#Percentage of letter in string question 2278
class Solution(object):
    """
    Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent
    """
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int

        O(N) time complexity
        O(1) space complexity
        """
        count = 0
        for char in s:
            if char == letter:
                count += 1
        return f"{int(float(count) / len(s) * 100)}%" #can divide float by int and get float, convert final answer back into into to remove decimals


sol = Solution()
print('--Percentage of letter in string--')
print(sol.percentageLetter('ksdf', 'k'))
print(sol.percentageLetter('IloveNYC', 'Y'))
print('\n\n\n')

#Find Numbers with Even Number of Digits question 1295
class Solution(object):
    """
    Given an array nums of integers, return how many of them contain an even number of digits.
    """
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        O(N) time complexity
        O(1) space complexity
        """
        count = 0
        for i in nums:
            if (len(str(i)) % 2) == 0:
                count += 1
        return count

sol = Solution()
print('--Find numbers with even number of digitts--')
print(sol.findNumbers([12,34423,23423,1,2,2,34,1,4,5,2,34,2,3,2,4234234,232,1,3]))
print(sol.findNumbers([12,3,4,4,44444444444444444444444444444444,4,4,4,2,3]))
print('\n\n\n')


#Find the highest altitude question 1732
class Solution(object):
    """
    There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
    You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i?????????????????? and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
    """
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int

        O(N) run time complexity
        O(1) space time complexity
        """
        maxi = 0
        altitude = 0
        for i in gain:
            altitude += i
            maxi = max(maxi, altitude)
        return maxi

sol = Solution()
print('--Find the Highest Altitude--')
print(sol.largestAltitude([-5,1,15,-7]))
print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))
print('\n\n\n')

#Reverse Words in a String III question 557
class Solution(object):
    """
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

    Example 1:

    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    """
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        
        O(N) time complexity
        O(N) space complexity
        """        
        return ' '.join([word[::-1] for word in s.split(' ')])
        """
        arr = []
        splitted = s.split(' ')
        for i in splitted:
            arr.append(i[::-1])
        return ' '.join(arr)
        """

sol = Solution()
print('reverseWords')
print(sol.reverseWords("there's no place like home"))
print(sol.reverseWords("I need a job desperately"))
print('\n\n\n')

#Richest customer wealth question 1672
class Solution(object):
    """
    You are given an m x n integer grid accounts where accounts[i][j] 
    is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.
    A customer's wealth is the amount of money they have in all their bank accounts. 
    The richest customer is the customer that has the maximum wealth.
    
    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
    """
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        
        O(N) time complexity
        O(1) space complexity
        """
        maxi = 0
        for customer in accounts:
            maxi = max(maxi, sum(customer))
        return maxi

sol = Solution()
print('--Richest Customer Wealth--')
print(sol.maximumWealth([[1,2,3],[3,2,1]]))
print(sol.maximumWealth([[1,5],[7,3],[3,5]]))
print('\n\n\n')


#shuffle the array question 1470
class Solution(object):
    """
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
    
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7] 
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
    """
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        
        O(N) time complexity
        O(1) space complexity
        """
        #Explanation
        Array = [0]*(2*n) #creates an array with 2 times n elements
        list1 = nums[:n]
        list2 = nums[n:]
        #2 pointers
        i = 0 #traverses list1 and list2 at i
        pos = 0#traverses Array at 2i
        while i != n: #the trick is to write the ith item in first list and fth item in second list in one iteration
            Array[pos] = list1[i]
            Array[pos + 1] = list2[i]
            i += 1
            pos += 2
        return Array
    
        #faster method with just 1 variable
        array = [0]*(2*n)
        list1, list2 = nums[:n], nums[n:]
        i = 0
        while i != n:
            array[i*2] = list1[i]
            array[i*2 + 1] = list2[i]
            i += 1
        return array



sol = Solution()
print('--shuffle the array--')
print(sol.shuffle([2,5,1,3,4,7], 3))
print(sol.shuffle([4,1,3,5,6,7,8,2,2,3], 5))
print('\n\n\n')



#count the number of consistent strings question 1684
class Solution(object):
    """
    You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
    Return the number of consistent strings in the array words.

    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
    """
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        
        O(N^2) time complexity
        space complexity is O(1)
        """
        length = len(words)
        for word in words:
            for letters in word:
                if letters not in set(allowed):
                    length -= 1
                    break #the trick is to use break as soon as the algo sees a letter that isn't supposed to be there
        return length
                        


sol = Solution()
print('--Count consistent strings--')
print(sol.countConsistentStrings("ab", words = ["ad","bd","aaab","baa","badab"]))
print(sol.countConsistentStrings("cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
print('\n\n\n')

#Counting words with a given prefix question 2185
class Solution(object):
    """
    You are given an array of strings words and a string pref.
    Return the number of strings in words that contain pref as a prefix.
    A prefix of a string s is any leading contiguous substring of s.

    Input: words = ["pay","attention","practice","attend"], pref = "at"
    Output: 2
    Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
    """
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        
        O(N) time complexity
        O(1) space complexity
        """
        count = 0
        length = len(pref)
        for word in words:
            if pref in word[:length]:
                count += 1
        return count


sol = Solution()
print('--Counting words with a given prefix--')
print(sol.prefixCount(["leetcode","win","loops","attend"], pref = "code"))
print(sol.prefixCount(["pay","attention","atmosphere","fachoi"], pref= "at"))
print('\n\n\n')

#Finbonaci number question 509
class Solution(object):
    """
    The Fibonacci numbers, commonly denoted F(n) 
    form a sequence, called the Fibonacci sequence, such that each 
    number is the sum of the two preceding ones, starting from 0 and 1. That is,

    n refers to the index within the fibonnaci sequence
    """
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0, 1]
        if n <= 1:
            return n
        for i in range(1, n):
            ans.append(ans[i] + ans[i - 1])
        return ans[-1]

    def fasterfib(self, n):
        """
        O(N) time complexity
        O(1) Space complexity
        """
        if n <= 1:
            return n
        prev, ans = 0, 1
        for i in range(1, n):
            oldans = ans
            ans += prev
            prev = oldans
        return ans
        #[0,1,1,2,3,5,8,13...]
        

sol = Solution()
print('--fibonacci number--')
print(sol.fib(3))
print(sol.fib(45))
print(sol.fib(5))
print(sol.fib(32))
print(sol.fasterfib(3))
print(sol.fasterfib(45))
print(sol.fasterfib(5))
print(sol.fasterfib(32))
print('\n\n\n')

exit()
#Goal Parser Interpretation Question 1678
class Solution(object):
    """ 
    You own a Goal Parser that can interpret a string command. The command consists of an 
    alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the 
    string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
    Given the string command, return the Goal Parser's interpretation of command.
    """
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        
        O(N) time complexity
        """
        
        return command.replace("()","o").replace("(al)","al")
        #first = command.replace("()", "o")#doesnt actually change command string
        #second = first.replace("(al)","al")
        #return second
        
sol = Solution()
print("--Goal Parser interpretation--")
print(sol.interpret("G()(al)"))
print(sol.interpret("G()()()()()()()()()()()(al)lllllllllllllllllllllllllllllll"))
print('\n\n\n')

#Count Asterisks question 2315
class Solution(object):
    """
    You are given a string s, where every two consecutive vertical bars '|' 
    are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' 
    make a pair, and so forth.
    Return the number of '*' in s, excluding the '*' between each pair of '|'.
    Note that each '|' will belong to exactly one pair.

    """

    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int

        O(N) time complexity
        O(1) space complexity
        """
        count = 0
        barcounter = 0
        for bar in s:
            if bar == "|":
                barcounter += 1
            if barcounter == 0 and bar == "*":
                count += 1
            elif barcounter == 2:
                barcounter = 0
        return count

    def splitcount(self, s): #second solution faster
        """
        18ms, faster than 97.31% of python submissions
        13.3Mb, less than 83.41% of python submissions

        O(N) time complexity
        O(1) space complexity
        """
        splitted = s.split('|')[::2]
        counted = 0
        for section in splitted:
            counted += section.count("*")
        return counted 


sol = Solution()
print("--Count Asterisks--")
print(sol.countAsterisks("l|*e*et|c**o|*de|"))
print('--solution 2--')
print(sol.splitcount("l|*e*et|c**o|*de|"))
print('\n\n\n')


#Sorting the Sentence question 1859
class Solution(object):
    """
    A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.
    A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
    For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
    Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
    """
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        
        time complexity = O(N)
        """
        fea = s.split(' ')
        l = [""] * len(fea)
        for string in (fea):
            l[int(string[-1]) - 1] = string[:-1]
        f = ' '.join(l)
        return f
        
sol = Solution()
print('--find the difference--')
print(sol.sortSentence('this1 be3 could2 good4'))
print('\n\n\n')
    

#Find the difference question 389
class Solution(object):
    """
    You are given two strings s and t.
    String t is generated by random shuffling string s and then add one more letter at a random position.
    Return the letter that was added to t. 
    s = "abcd", t = "abcde"
    """
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        
        O(N) = time complexty
        """
        for letter in t:
            if s.count(letter) != t.count(letter):
                return letter


sol = Solution()
print("--find the difference--")
sol.findTheDifference("abce", "abc")
print('\n\n\n')


#shuffle string question 1528
class Solution(object):
    """
    You are given a string s and an integer array indices of the same length. 
    The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
    Return the shuffled string.

    Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
    output: "leetcode"
    """
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        
        O(N) time complexity
        O(N) space complexity
        """
        l = len(s)*[""] #create k number of arrays
        for i in indices:
            l[i] = s[indices.index(i)]
        return ''.join(l)

sol = Solution()
print('--shuffle string--')
print(sol.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
print(sol.restoreString("abc",[0,1,2]))
print('\n\n\n')

#Maximum Number of Words found in sentences question 2114
class Solution(object):
    """
    A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

    You are given an array of strings sentences, where each sentences[i] represents a single sentence.

    Return the maximum number of words that appear in a single sentence.
    """

    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int

        O(N) time complexity
        O(N) space complexity
        """
        maxi = 0
        for sentence in sentences:
            maxi = max(maxi, len(sentence.split(' ')))
        return maxi


sol = Solution()
print('--most words found--')
print(sol.mostWordsFound(['i love cheese', 'i eat sandwhich', 'birds came from dinosaurs']))
print(sol.mostWordsFound(['time and space complexity of split', 'when will I get an internship', 'pithon']))
print('\n\n\n')



#final value of variable after performing operations question 2011
class Solution(object):
    """
    There is a programming language with only four operations and one variable X:

    ++X and X++ increments the value of the variable X by 1.
    --X and X-- decrements the value of the variable X by 1.
    Initially, the value of X is 0.

    Given an array of strings operations containing a list of operations, 
    return the final value of X after performing all the operations.  
    """
    def finalValueOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        #O(N) slow solution
        #O(1) slow solution

        output = 0
        for string in operations:
            if "--X" == string or "X--" == string:
                output -= 1
            elif "++X" == string or "X++" == string:
                output += 1
        print(output)

        #O(N) slightly faster solution and more pythonic
        #O(1) space compelxity

        dicindex = {"++X" : 1, "X++": 1, "X--":-1, "--X":-1}
        print(sum(dicindex[value] for value in operations))
        
        #O(N) kind of fast solution and also python    
        #O(1) space complexity

        joined = "".join(operations)
        print((joined.count("++") - joined.count("--")))
        

sol = Solution()
print("--find value after operations--")
print(sol.finalValueOperations(["--X","X++","X++"]))
print(sol.finalValueOperations(["++X","X++","X++"]))
print(sol.finalValueOperations(["--X","X--","X--"]))
print('\n\n\n')

#Longest Common Prefix question 14
class Solution(object):
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string
    
    strs = ["flower","flow","flight"]
    """
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        O(N) time complexity solution
        """
        match = 0
        
        for vals in zip(*strs):
            if len(set(vals)) == 1:
                match += 1
            else:
                break
        
        return strs[0][:match]

sol = Solution()
print('--longest common prefix--')
print(sol.longestCommonPrefix(['flower','flow','flight']))
print(sol.longestCommonPrefix(['qualjumcomm','qualcomm','qularavekcomm']))#leetcode didn't write a proper failing test case #FIXME
print(sol.longestCommonPrefix(['wow','sdf','sdfsdfs']))
print('\n\n\n\n\n\n\n\n\n\n')


#Defranging an IP address question 1108
class Solution(object):
    """
    Given a valid (ipv4) ip address, return a defranged version
    of that IP address, A defranged IP address replaces every period
    "." with "[.]"
    """
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str

        O(n) time complexity of join and split
        Auxillary space complexity
        """
        return '[.]'.join(address.split('.'))


print("--defranging an ip address--")
print(Solution().defangIPaddr('1.1.2.3.4.5'))
print(Solution().defangIPaddr('1.2.2.3.4.6'))
print('\n\n\n')

#reverise string question 344
class Solution(object):
    """
    Write a function that reverses a string. The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.
    """
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]#the trick is to assign the first position, the last number, and so on
        return s


sol = Solution()
print(sol.reverseString(['h','e','l','l','o']))
print(sol.reverseString(['j','o','h','n','s','o','n']))
print('\n\n\n')


#Happy number question 202
class Solution(object):
    """
    Starting with any positive integer, 
    replace the number by the sum of the
    squares of its digits.
    Repeat the process until the number equals 1 (where 
    it will stay), or it loops endlessly in a 
    cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    """
    count = 0
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0 
        self.count += 1
        for i in str(n):
            sum += int(i)**2
        if sum == 1:
            return True
        elif self.count == 50:
            return False
        return self.isHappy(sum)

sol = Solution()
print(sol.isHappy(n = 19))
print(sol.isHappy(n = 23))
print(sol.isHappy(n = 12))
print(sol.isHappy(n = 133))
print('\n\n\n')
#diagnoal difference HACKERRANK day 2

class Solution(object):
    """
    Given a 3x3 square matrix, calculate the absolute difference between the sums of its diagonals.

    For example, the square matrix  is shown below:

    1 2 3
    4 5 6
    9 8 9     
    """
    def diagonalDifference(self, *arr):
        """
        time complexity = O(N)
        Space complexity = O(1)
        """
        sum1 = 0
        sum2 = 0
        l_index = 0
        r_index = -1 
        for i in range(len(arr)):
            sum1 += arr[i][l_index]
            l_index += 1
            sum2 += arr[i][r_index]
            r_index -= 1
        subtracted = abs(sum1 - sum2)
        return subtracted


sol = Solution()
print(sol.diagonalDifference([1,2,3],[4,4,6],[7,8,9]))
print(sol.diagonalDifference((1,2,3),(3,1,6),(1,8,3)))
print(sol.diagonalDifference((1,3,2),(4,4,6),(7,8,9)))
print(sol.diagonalDifference((1,1,0),(4,9,6),(4,8,2)))
print(sol.diagonalDifference((1,6,3),(4,4,6),(7,8,9)))
print(sol.diagonalDifference((1,8,2),(4,2,6),(2,8,5)))

#Intersection of 2 arrays question 349
class Solution(object):
    """
    Given two integer arrays nums1 and nums2, return an array 
    of their intersection. Each element in the result must be 
    unique and you may return the result in any order.
    """
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        time complexity: O(N)
        """
        common = set()
        for integer in nums1:
            if integer in nums2:
                common.add(integer)
        return common

print('--intersection of two arrays--')
sol = Solution()
print(sol.intersection([2,3,4,1,2], [2,3,4,4]))
print(sol.intersection([1,2,2,1], [1,1]))
print(sol.intersection([1,4,5,6,7,8,2,3,4,2], [9,9,2,4,6,8,2,4,5,7,1,5,7]))
print('\n\n\n')


#Longest Continuous Increase subsequence question 674
class Solution(object):
    """
    Given an unsorted array of integers nums, return the length 
    of the longest continuous increasing subsequence (i.e. 
    subarray). The subsequence must be strictly increasing.

    A continuous increasing subsequence is defined by two 
    indices l and r (l < r) such that it is [nums[l], nums[l 
    + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums
    [i] < nums[i + 1].
    """
    
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Explanation:
        use sliding window / kadane's algorithm

        trick:
        1. have a variable that resets to 1 everytime
        the current number is less than previous

        2. have another variable that stores the maximum
        value after iterating through the entire array

        Time complexity = O(N)
        Space complexity = O(1)
        """
        maxi = 1
        counter = 1 #init at 1, stores temporary count maxi = 1 #init at 1, stores absolute count
        length = len(nums)
        for integer in range(1, length):
            if nums[integer] > nums[integer - 1]: #start at second number in array compare to previous
                counter += 1
                if maxi < counter:
                    maxi = counter
            else:
                counter = 1
        return maxi


sol = Solution()
print("--longest continuous inreasing substring--")
print(sol.findLengthOfLCIS([2,3,5,3,6,7,9]))
print(sol.findLengthOfLCIS([1,3,5,7,4,2,4,3,4,5,6,7,8,9,10]))
print(sol.findLengthOfLCIS([1,4,5,6,8,0,2,4,5,2,3,4,1,2]))
print("\n\n\n")

#Find the Difference of Two Arrays question 2215
class Solution(object):
    """
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
    Note that the integers in the lists may be returned in any order.   
    """
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        
        Explanation:

        if im subtracting nums2 from nums1, it will immedialty discard
        all values from nums2 and discard duplicate values that appeared in both nums1 and nums2
        """

        return [list(set(nums1) - set(nums2)), list(set(nums2)-set(nums1))]


        
sol = Solution()
print("--Find Difference between 2 arrays--")
print(sol.findDifference([1,2,3,4], [2,3,4,5])) #returns [[1],[5]]
print(sol.findDifference([2,5,6,7], [1,2,7,6])) #returns [[5], [1]]
print('\n\n\n')



#Valid Anagram question 242
class Solution(object):
    """
    #NOTE  
    #this question doesn't require an oxford dictionary as we don't have to check if the 
    #anagram word is a real word, we can just assume if the letters are the same in both strings after sorting,
    #then it's an anagram

    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = [i for i in s]
        s2 =[f for f in t]
        return sorted(s1) == sorted(s2)
    
        #This solution is faster
        #return collections.Counter(s)==collections.Counter(t)

sol = Solution()
print("--Valid Anagram--")
sol.isAnagram(s = "anagram", t = "nagaram") #True
sol.isAnagram(s = "rat", t = "fat") #False
print('\n\n\n')


#Contains Duplicate question 217
class Solution(object):
    """
    Given an integer array nums, return true if any value appears at 
    least twice in the array, and return false if every element is distinct.
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))


sol = Solution()
print('--Contains Duplicate--')
print(sol.containsDuplicate([1,2,3,1]))
print(sol.containsDuplicate([2,3,4,4,4,4,4,4,2,3]))
print(sol.containsDuplicate([2,3,1,6,8,5,4,1,9,9,9,9,9]))
print(sol.containsDuplicate([1,2,3,4,2,1,4,1,1]))
print(sol.containsDuplicate([1,4,5,6,8,9,2,0,0]))
print('\n\n\n')

#plus one question 66
class Solution(object):
    """
    You are given a large integer represented as an integer array digits, 
    where each digits[i] is the ith digit of the integer. The digits are 
    ordered from most significant to least significant in left-to-right order. 
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        for i in digits:
            s += (str(i))
        finished = str(int(s) + 1)
        return finished
        answer = []
        for i in finsihed:
            answer.append(i)
        return answer

sol = Solution()
print('--Plus One--')
print(sol.plusOne([9,9,9]))
print(sol.plusOne([4,9,1]))
print(sol.plusOne([4,9,9]))

#remove element question 27

class Solution:
    """
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
    """
    def removeElement(self, nums, val):
        """
        type nums: List[int]
        type val: int
        rtype: int
        """
        while val in nums:
            nums.remove(val)
        return nums



sol = Solution()
print('--Remove Element--')
print(sol.removeElement([2,3,4,2,1,4], 2))
print(sol.removeElement([2,3,3,2,1,3], 3))

#Rotate Array problem 189
class Solution:
    """
    Given an array, rotate the array to the right by k steps where k is non negative

    Leetcode won't accept this answer even though it's right
    """
    def rotate(self, nums, k):
        """
        type nums: List[int]
        type k: int
        rtype: None (modify nums)
        """
        for i in range(k):
            nums.insert(0, nums.pop())
            print(nums)
        if len(nums) > 50000: #lol
            sliced = nums[:(k*-1)]
            nums = nums[(k*-1):]
            nums.extend(sliced)
            print(nums)


sol = Solution()
print('--rotate array--')
sol.rotate([1,2,3,4,5,6,7], 3)
sol.rotate([1,2], 3)
#sol.rotate([2,3,4,5,1,2,3,4,1,2,3,1,2,3,1,2,3,1,3,1,12,12,12,12,12,141,1515,15], 92000)
print('\n\n\n')


#Find Duplicate Number question 287
class Solution:
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.

    """
    #Methods used

    #tortoise and hare cycle detection algorithm
    #sorting
    #Set storage
    #negatives

    #best time complexity and space complexity
    ##  tortoise and hare algorithm

    def twopointerfindDuplicate(self, nums):

            """
            :type nums: List[int]
            :rtype: int
            
            Constraints:
            Can't use extra space, can't modify nums
            
            2 variables tortoise and hare: O(1) constant space complexity
            O(n) time complexity where n is the number of nodes
            
            pigeon hole principle = we have n distinct values /containers and n + 1 values then there will be a duplicate 

            when not using linked list, the values in the array dictate the next index
            """
            tortoise = hare = nums[0] #start 1 first index

            while True: #continue until cycle is found, in this case we can always assume a cycle exists
                tortoise = nums[tortoise]
                hare = nums[nums[hare]]
                if tortoise == hare:
                    break
            tortoise = nums[0]

            while tortoise != hare: #we continue until the next index nums[tortoise] is equal to duplicate number (2)
                tortoise = nums[tortoise]
                hare = nums[hare]#both tortoise and hare must travel at same speed now
            return tortoise #we don't return num[tortoise] because we return the index of the answer which in the case
            # of [1,3,4,2,2] would be 3 which is wrong, instead we return tortoise or hare because it's indecies num[3] and num[4] both 
            #return 2

    

    #breaking constraints
    ##  sorting
    def sortingfindDuplicate(self, nums):
        nums.sort()
        for integer in range(len(nums)):
            if nums[integer] == nums[integer - 1]:
                return integer

    #iterate through list and record already visited numbers
    ##  set storage
    def setfindDuplicate(self, nums):
        seen = set()
        for integer in nums:
            if integer in seen: return integer
            seen.add(integer)

    #negatives
    def negativemarkfindDuplicate(self, nums):
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate


sol = Solution()
print('--find the duplicate using floyd tortoise and hare cycle detection algorithm--')
print(sol.twopointerfindDuplicate([1,3,4,2,2]))
print(sol.twopointerfindDuplicate([1,3,4,2,2, 5]))

print('--find the duplicate using set--')
print(sol.setfindDuplicate([1,3,4,2,2]))
print(sol.setfindDuplicate([1,3,4,2,2, 5]))

print('--find the duplicate using negative mark--')
print(sol.negativemarkfindDuplicate([1,3,4,2,2]))
print(sol.negativemarkfindDuplicate([1,3,4,2,2, 5]))

print('--find the duplicate using sorting method--')
print(sol.sortingfindDuplicate([1,3,4,2,2]))
print(sol.sortingfindDuplicate([1,3,4,2,2, 5]))
print('\n\n\n')





#Missing Number question 268
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        run time complexity = O(n)
        
        Given an array nums containing n distinct numbers in the range [0, n], 
        return the only number in the range that is missing from the array.
        """
        nums.sort() #must be sorted
        length = len(nums)
        for i in range(length):
            if 0 not in nums: #written to pass this test case [0]
                return 0
            elif nums[i] == nums[-1]: #if we end up getting to last number in list then the missing number can only be number after last
                return nums[-1] + 1
            elif nums[i] + 1 != nums[i + 1]: #check if the current number + 1 == 2nd number
                return nums[i] + 1

sol = Solution()
print('--Missing number--')
print(sol.missingNumber([0, 1, 3]))
print(sol.missingNumber([0, 2, 1]))
print(sol.missingNumber([0, 1, 2]))
print(sol.missingNumber([1]))
print(sol.missingNumber([0]))
print('\n\n\n')




#single number question 136 and single number 2 question 136
class Solution(object):
    def searchInsert(self, nums):
        """
        given a non empty array of integers
        find the element that appears only once when all other
        elements appear twice

        O(n) time complexity

        trick: use python "in" keyword if the current index
        is in the list behind us or infront of us

        takes advantage of the fact that slicing out of range
        of the list will return an empty list instead of an index
        error
        """
        
        for count, integer in enumerate(nums):
            if integer in nums[count + 1:] or integer in nums[:count]: #checks if there are duplicates of the current index behind or infront of it
                continue
            else:
                return integer

sol = Solution()
print('--single number--')
print(sol.searchInsert(nums = [2,2,1,1,3,5,3]))
print(sol.searchInsert(nums = [2, 3, 4,4,3, 1, 1]))
print(sol.searchInsert(nums = [2, 3, 4,4, 3, 2,1]))
print(sol.searchInsert(nums = [2,2, 3, 4,4,4, 3,3, 2,1])) #also works for single number if 3 duplicate list
print('\n\n\n')


#single number 3 question 260
class Solution(object):
    def singleNumber(self, nums):
        """
        this time there are 2 numbers in the array that don't have duplicate
        numbers, return the 2 numbers in this format [x, y]
        
        constant space complexity
        O(n) time complexity

        trick is to check behind and after current index to check for duplicates
        """
        #NOTE: try with not in to isolate for non duplicates immediatly
        for count, integer in enumerate(nums):
            if integer in nums[count + 1:] or integer in nums[:count]:
                continue
            else:
                nums.remove(integer)
                nums.insert(0, integer)
        return nums[:2]

sol = Solution()
print('--single number 3--')
print(sol.singleNumber([0,1,1,2]))
print(sol.singleNumber([1,2,1,3,2,5]))
print('\n\n\n')



#Search insert position question 35:
class Solution(object):
    def searchInsert(self, nums, target):
        """
        type nums: list[int]
        type target: int

        problem:
        return the target index within the list
        if the target not in the list return index of where target should be

        single pointer implementation
        """
        n = 0
        while n != len(nums): #we don't do len(nums) - 1 because of [1] target 0 testcase
            if target == nums[n]:
                return n
            elif nums[n] > target:
                return n
            elif target > nums[-1]:#special case where the number must be appended to rear [1,3,5,6] target = 7 | previous condition wouldn't #   return correct number
                return len(nums)
            n += 1

sol = Solution()
print("--Search Insert--")
print(sol.searchInsert([23,45, 65,95], 54))
print('\n\n\n')

#Find the pivot index question 724
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for count, i in enumerate(nums):
            rightsum = S - nums[count] - leftsum 
            if leftsum == rightsum:
                return count
            leftsum += i
        return -1


sol = Solution()
print("--Pivot index--")
print(sol.pivotIndex([2,3,4,5,0]))
print(sol.pivotIndex([2,3,4,5,2]))
print('\n\n\n')


#best time to buy and sell stock 2 question 122
class Solution(object):
    def maxProfit(self, prices: list):
        """
        can buy and sell multiple times within array
        """
        profit = 0
        for i in range(1, len(prices)):#starting at 1 is better than 0
            difference = prices[i] - prices[i - 1] #by making our pointer the current value and not the next we avoid indexing outside of array
            if difference > 0:
                profit += difference 
        return profit

sol = Solution()
print('--maxprofit--')
print(sol.maxProfit([2,3,5,2,8,9]))
print('\n\n\n')




#length of the last word question 58
class Solution(object): #FIXME
    def lengthOfLastWord(self, s:str) -> int:
        """
        given string s, return the length of the last word
        (not a good solution becuase fails testcase below)
        """
        string_list = []
        for string in s[::-1].strip(' '):
            if string == ' ':
                return len(string_list) - 1
        if ' ' not in string_list[0]:
            return len(string_list)
        if len(string_list) == 1:
            return 1



sol = Solution()
print(sol.lengthOfLastWord('hougaloug'))
print(sol.lengthOfLastWord('fs sdff sdsdfs sdd '))

#remove duplicates from array
class Solution(object):
    def removeduplicate(self, arr: []) -> list:
        new_list = []
        for i in arr:
            if i not in new_list:
                new_list.append(i)
        return new_list

sol = Solution()
print('--remove duplicates--')
print(sol.removeduplicate([2,3,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
print(sol.removeduplicate([2,5,6,12,33,12,12,12,99999,5,5]))
print('\n\n\n')


#Palindrome's with numbers question 9
class Solution(object):
    def numpalindrome(self, n: int) -> bool:
        str_list = []
        for num in str(n):
            str_list.append(num)
        if str_list[::-1] == str_list:
            return True
        return False


sol = Solution()
print('--Palindrome Number--')
print(sol.numpalindrome(n = 123))
print(sol.numpalindrome(n = 23))
print(sol.numpalindrome(n = 442244))
print(sol.numpalindrome(n = 441112211144))
print(sol.numpalindrome(n = 45))
print('\n\n\n')

#Valid parentheses question 20
class Solution(object):
    def isvalid(self, s) -> bool:
        """
        the trick is to only append the lefty to the stack
        if the index of righty matches index of lefty than pop stack
        if len(list) == 0 then return True
        """
        lefty = '{[('
        righty = '}])'
        stack = []
        for bracket in s:
            if bracket in lefty:
                stack.append(bracket)
            elif bracket in righty:
               if len(stack) == 0:#this is for a testcase where only one right  bracket is presented
                   return False
               elif righty.index(bracket) != lefty.index(stack.pop()):
                   return False
        return True if len(stack) == 0 else False #return len(stack) == 0 #return True if stack is empty ONLY CASE WE RETURN TRUE IS IF STACK IS EMPTY, ALL OTHER CASES ARE FALSE

print('--Valid Parentheses--')     
sol = Solution()
print(sol.isvalid('{234234234}'))
print(sol.isvalid('{[]}()'))
print(sol.isvalid(')'))
print(sol.isvalid('([{{]}))))'))
print('\n\n\n')

#maximum subarray:
#Explanation
"""
use Kadane's algorithm
if the sum is negative then make sum = 0
there is a variable that keep tracks of the maximum so far
"""
class Solution_53:
    """
    Given an integer array nums, find the contiguous 
    subarray (containing at least one number) 
    which has the largest sum and return its sum.
    """
        

    def maxSubArray(self, nums) -> int:
        cursum, maxsum = 0, min(nums)
        for integer in nums:
            maxsum += integer
            if cursum < 0:
                cursum = 0
            if cursum < 0:#do not use elif
                cursum = 0
        print(maxsum,"\n")
                

sol = Solution_53()
sol.maxSubArray([2, -3, 4, 1, 14, 2])


#Best time to buy and sell a stock question 121:
class Solution_121:
    def maxProfit(self, prices) -> int:
        """You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        
        Takes advantage of the fact that we don't have to record the exact locations of where we buy and sell
        but simply record the maximum profit obtained so far as we interate through the array
        """
                
        #o(n) run time
        #o(1) space complexity
        left, right = 0, 1
        profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1
        print(profit)

sol = Solution_121()
sol.maxProfit([23, 34, 12, 2, 57, 90])
sol.maxProfit([2,4, 1])
sol.maxProfit([3, 4, 5])

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
    def reverseList(self, head):
        
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


#make a new repositoy and push to main
#echo "# sdfsdf" >> README.md
#git init
#git add Readme.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/zhwang2001/sdfsdf.git
#git push -u origin main

#push existing repository from command line
#git remote add origin https://github.com/zhwang2001/sdfsdf.git
#git branch -M main
#git push -u origin main


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






