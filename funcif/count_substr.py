# Exercise 3.35. Count substrings: This is extension of Exercise 3.34: count how many times certain string appears
# in another string, e.g., function returns 2 when called w/DNA string 'ACGTTACGGAACG' & substring 'ACG'. 
# Hint: For each match of 1st character of substring in main string, check if next n characters in main string
# matches substring, where n is length of substring. Use slices like s to pick out a substring of s.

def count_substr(dna, substr):
    i = 0
    for p in xrange(len(dna)):
        if dna[p] == substr[0]:
            if dna[p:p + len(substr)] == substr:
                i += 1
    return i

dna = 'ATATGCGGATACCTATA'
substr = 'ATA'
print count_substr(dna, substr)

"""
OUTPUT:

bash-3.2$ python count_substr.py
3

"""
