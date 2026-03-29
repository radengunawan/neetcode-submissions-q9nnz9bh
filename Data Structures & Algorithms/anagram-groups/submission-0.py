class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = {}

        for i in range (len(strs)):
            sorted_word = ''.join(sorted(strs[i]))

            if sorted_word not in anagram_groups:
                anagram_groups[sorted_word] = []

            anagram_groups[sorted_word].append(strs[i])

        return list(anagram_groups.values())
        