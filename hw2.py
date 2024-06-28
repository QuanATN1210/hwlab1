def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    lines = []

    for i in range(size):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4*size - 3, '-'))

    result = "\n".join(lines[::-1] + lines[1:])
    return result

size = int(input())
print(print_rangoli(size))