def find_the_sub_string_b(string_a, n):
    listsubstring = []
    for i in range(0, len(string_a) - (n-1)):
        a = (string_a[i:i+n]).lower()

        listsubstring.append(a)
    maxsubstring = max(listsubstring, key = listsubstring.count)
    return maxsubstring

string_a = "AbcbcaAccbacbabbababcbabcabcabbcabcacabA"
n = 2
Substringmax = find_the_sub_string_b(string_a,n)

string_b = "need one need two need three"
n = 4
Substringmax = find_the_sub_string_b(string_a,n)
