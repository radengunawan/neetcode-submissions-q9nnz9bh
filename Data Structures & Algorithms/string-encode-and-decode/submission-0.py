class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + ':' +s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        start=0

        while start < len(s):
            end = start

            #find s
            while s[end] != ':':
                end +=1
            
            textLength = int(s[start:end])
            decoded_list.append(s[end+1:end+1+textLength])
            start = end + 1 + textLength

        return decoded_list
