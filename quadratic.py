# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = b ** 2 - 4 * a * c

    if discriminante < 0:
        return "( )"
    elif discriminante == 0:
        r = (-b) / (2 * a)
        return f"({r})"
    else:
        raiz_disc = discriminante ** 0.5
        r1 = (-b + raiz_disc) / (2 * a)
        r2 = (-b - raiz_disc) / (2 * a)
        return f"({r1}, {r2})"

def value_y(a, b, c, x):
    return a * x ** 2 + b* x + c

def to_string(a, b, c):
    resultado = "f(x) = "

    if a != 0:
        resultado += f"{a} * X^2"

    if b != 0:
        if resultado != "f(x) = ":
            resultado += " + "
        resultado += f"{b} * X"

    if c != 0:
        if resultado != "f(x) = ":
            resultado += " + "
        resultado += f"{c}"

    if resultado == "f(x) = ":
        resultado += "0"

    return resultado


def derivation(a, b, c):
    resultado = "f'(x) = "

    coef = 2 * a

    if coef != 0:
        resultado += f"{coef} * X"

    if b != 0:
        if resultado != "f'(x) = ":
            resultado += " + "
        resultado += f"{b}"

    # Si todo es 0
    if resultado == "f'(x) = ":
        resultado += "0"

    return resultado
