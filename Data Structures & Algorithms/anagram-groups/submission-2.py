class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for s in strs:
            anagram_group_id = [0] * 26
            for c in s:
                char_idx = ord(c) - 97
                anagram_group_id[char_idx] = anagram_group_id[char_idx] + 1
            anagram_group_id = tuple(anagram_group_id)
            if anagram_group_id in anagram_groups:
                anagram_groups[anagram_group_id] = anagram_groups[anagram_group_id] + [s]
            else:
                anagram_groups[anagram_group_id] = [s]
        return [res for res in anagram_groups.values()]