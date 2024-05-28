# open and close parentheses, want to know if its valid

test_cases = [
    "(", #0
    ")", #0
    "()", #1
    "(())", #1
    ")", #0
    "(asdasd(sdasdasd)(sd(sd)sds)sdasd)"
]
# close count maintained by open count decrements

#test open close parenthesis
def test_open_close_par(s):
    open_count = 0
    for i in s:
        if i == "(":
            open_count += 1
        if open_count == 0:
            if i == ")":
                return False
        if open_count > 0:
            if i == ")":
                open_count -=1
    if open_count != 0:
        return False
    return True

for i in test_cases:
    print(int(test_open_close_par(i)))
