class Solution:
    """
    Use non-ASCII character for separator?
    What do I need to not lose information?
    What is encoding? Do we want to compress or
    we only care about safty?
    I mean so many complicated methods exists.
    I have no idea what is appropriate here.

    """


    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s))
            encoded_s += ":"
            encoded_s += s
        return encoded_s
#  5:Hello5:World
    def decode(self, s: str) -> List[str]:
        ans = []
        meta_len = ""
        i = 0
        while i < len(s):
            if s[i] != ":":
                meta_len += s[i]
            else:
                ans.append(s[i + 1 : i + 1 + int(meta_len)])
                i += int(meta_len)
                meta_len = ""
            i += 1
        return ans
                
            
            
