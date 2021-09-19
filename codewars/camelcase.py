def to_camel_case(text):
    result = []
    upper = False
    for c in text:

        if upper:
            c = c.upper()
            upper = False

        if c == '-' or c == '_':
            upper = True
        else:
            result.append(c)

    return ''.join(result)

