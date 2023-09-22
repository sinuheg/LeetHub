class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        class Node:
            def __init__(self, freq, val):
                self.next = None
                self.freq = freq
                self.val = val
        def insert_in_order(head, freq, val):
            new_node = Node(freq, val)
            if not head:
                return new_node
            if freq >= head.freq:
                new_node.next = head
                return new_node
            curr = head
            while curr and curr.next:
                if freq >= curr.next.freq:
                    new_node.next = curr.next
                    curr.next = new_node
                    return head
                curr = curr.next
            curr.next = new_node
            return head

        fm = {}
        for num in nums:
            if num not in fm:
                fm[num] = 0
            fm[num] += 1
        ranking = None
        for val,freq in fm.items():
            ranking = insert_in_order(ranking, freq, val)
        result = []
        curr = ranking
        while k > 0 and curr:
            result.append(curr.val)
            k -= 1
            curr = curr.next
        return result


        