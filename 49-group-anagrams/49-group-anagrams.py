class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i) - ord('a')] += 1
            mapper[tuple(count)].append(s) # Tuple - must be non-mutable, defaultdict - bypasses edge case
        return mapper.values()    