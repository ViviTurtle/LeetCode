class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        current_length = 0
        iterator = 1
        current_characters = dict()
        start_position = 0
        while iterator <= len(s):
            current_char = s[iterator-1:iterator]
            if current_characters.get(current_char) is None:
                current_length = current_length + 1
                current_characters[current_char] = iterator
                iterator += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                iterator = current_characters.get(current_char) + 1
                current_characters.clear()
                current_length = 0
        if current_length > max_length:
            max_length = current_length
        return max_length