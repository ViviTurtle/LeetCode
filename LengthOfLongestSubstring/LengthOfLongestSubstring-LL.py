class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        current_characters = dict()
        start_position = 0
        for iterator, character in enumerate(s, 1):
            #If character in dictionary Or while loop is exiting
            if current_characters.get(character) and current_characters.get(character) > start_position:
                    start_position = current_characters.get(character)
            current_length = iterator - start_position
            if current_length > max_length:
                max_length = current_length
            current_characters[character] = iterator
        return max_length