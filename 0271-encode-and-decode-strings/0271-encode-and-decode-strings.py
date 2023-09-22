import base64
class Codec:
    def encode(self, strs: List[str]) -> str:
        result = []
        for st in strs:
            ascii_bytes = st.encode("ascii")
            base64_bytes = base64.b64encode(ascii_bytes)
            base64_string = base64_bytes.decode("ascii")
            result.append(base64_string)
        return ' '.join(result)

        

    def decode(self, s: str) -> List[str]:
        encoded_strs = s.split(' ')
        strs = []
        for base64_string in encoded_strs:
            base64_bytes = base64_string.encode("ascii")
            str_bytes = base64.b64decode(base64_bytes)
            strs.append(str_bytes.decode("ascii"))
        return strs
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))