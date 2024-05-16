# open and close parenthisises, want to know if its valid

# if ) first, then fail
# if ( not mod 2 then fail
# count how many

test_cases = ["(", ")", "()", "(())", ")"]
# close count mantained by open count decrements

def test_string(s):
    open_count = 0
    for i in s:
        if i == "(":
            open_count += 1
        if open_count > 0:
            if i == ")":
                # closed one
                open_count -= 1
    if open_count != 0:
        return False
    return False

for i in test_cases:
    print(int(test_string(i)))
