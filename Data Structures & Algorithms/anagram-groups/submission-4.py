class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        buckets = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(word)
        return list(buckets.values())


