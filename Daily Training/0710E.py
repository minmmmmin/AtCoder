S = input().strip()
T = input().strip()

def run_length_encoding(s):
    """Run-length encode the input string s."""
    rle = []
    n = len(s)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1
            count += 1
        rle.append((s[i], count))
        i += 1
    return rle

def can_transform(S, T):
    """Determine if S can be transformed into T by the given rules."""
    rle_s = run_length_encoding(S)
    rle_t = run_length_encoding(T)
    
    # Check if the lengths of the run-length encoded forms are the same
    if len(rle_s) != len(rle_t):
        return "No"
    
    # Check each corresponding tuple in RLE forms
    for (char_s, count_s), (char_t, count_t) in zip(rle_s, rle_t):
        if char_s != char_t:
            return "No"
        if count_s > count_t:
            return "No"
        if count_s < count_t and count_s < 2:
            return "No"
    
    return "Yes"

print(can_transform(S, T))
