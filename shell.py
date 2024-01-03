import dot

while True:
    text = input('dot > ')
    result, error = dot.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(result)
