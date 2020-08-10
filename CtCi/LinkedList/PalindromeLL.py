def is_palindrome(self):
        # Method 1:
        # s = ""
        # p = self.head 
        # while p:
        #     s += p.data
        #     p = p.next
        # return s == s[::-1]

        # Method 2:
        # p = self.head 
        # s = []
        # while p:
        #     s.append(p.data)
        #     p = p.next
        # p = self.head
        # while p:
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.next
        # return True

        # Method 3
        p = self.head 
        q = self.head 
        prev = []
        
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
    
        count = 1

        while count <= i//2 + 1:
            if prev[-count].data != p.data:  # - count is first -1 means the last element , then -2 which means the second last element 
                return False
            p = p.next
            count += 1
        return True

# Example palindromes:
# RACECAR, RADAR

# Example non-palindromes:
# TEST, ABC, HELLO

llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")

llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")

print(llist.is_palindrome())
print(llist_2.is_palindrome())
