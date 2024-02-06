class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm = {}
        for char in t:
            if char in hm:
                hm[char] -= 1
            else:
                hm[char] = -1
        left = 0
        right = 0
        min_window = ""
        while right < len(s):
            to_add = s[right]
            if to_add in hm:
                hm[to_add] += 1
            min_window = self.get_min_window(min_window, hm, left, right, s)
            
            # remove from left
            while left < right:
                to_remove = s[left]
                if to_remove in hm:
                    if hm[to_remove] > 0:
                        hm[to_remove] -= 1
                        left += 1
                    else:
                        break
                else:
                    left += 1
            min_window = self.get_min_window(min_window, hm, left, right, s)
            right +=1
        return min_window
    
    def get_min_window(self, min_window, hm, left, right, s):
        if hm:
            for char in hm:
                if hm[char] < 0:
                    return min_window
            this_window = s[left:right+1]
            if min_window == "":
                return this_window
            return this_window if len(this_window) < len(min_window) else min_window
        else: 
            return min_window
