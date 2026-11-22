class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach:
        1. Count the frequency of each number and store them in a dict
        2. Store the keys of the numbers with the highest frequency in a list
        3. Use a while loop to iterate through the dictionary to find the k most frequent
        4. Return the list
        Time complexity = O(K * N)
        Space Complexity = O(N)
        """
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        ans = []
        while len(ans) < k:
            mostfreq = 0
            for key, val in count.items():
                if mostfreq < val:
                    mostfreq = val
                    maxKey = key
            ans.append(maxKey)
            count[maxKey] = 0

        return ans