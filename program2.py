def decode_message( s: str, p: str) -> bool:
def match(s: str, p: str, s_index: int, p_index: int) -> bool:
        if s_index == len(s) and p_index == len(p):
     return True
        if p_index == len(p):
            return False
        
        if p[p_index] == '*':
            return match(s, p, s_index, p_index + 1) or \
                   (s_index < len(s) and match(s, p, s_index + 1, p_index))
        
        if s_index < len(s) and (s[s_index] == p[p_index] or p[p_index] == '?'):
            return match(s, p, s_index + 1, p_index + 1)
        
        return False

    return match(s, p, 0, 0)
