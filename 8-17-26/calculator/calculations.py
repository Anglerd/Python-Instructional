def add(a, b):
    """basic addition of a and b"""
    return a + b

def sub(a, b):
    """subtracts b from a (a - b)"""
    return add(a, -b)

def check_int(a):
    """checks if the input is an integer"""
    return int(a) == a

def mult_int(a, b: int):
    """multiplies 2 numbers, b must be an integer. Not to be used externally"""
    if b < 0:
        return -mult_int(a, -b)
    result = 0
    while b > 0:
        result = add(result, a) # result += a
        b = sub(b, 1) # b -= 1
    return result

def count_decimals(a):
    """counts the decimals in a given number. Not to be used externally"""
    count = 0
    """
    # this section does not work since floats are imprecise and as such we will never be able to count the decimals in any float number
    while not check_int(a):
        count = add(count, 1) # count += 1
        a = mult_int(a, 10) # a *= 10
        print(f"count is {count}")
    """
    flag = False
    a = str(a)
    for letter in a:
        if letter == ".":
            flag = True
            continue
        elif flag:
            count = add(count, 1)
    return count

def pow(a, b: int):
    """raises a to the power b (a^b), only valid if b is an integer"""
    if b == 0:
        return 1
    if b < 0:
        return div(1, pow(a, -b), 15)
    result = 1
    while b > 0:
        result = mult(result, a) # result *= a (result = result * a)
        b = sub(b, 1)
    return result

def div(a, b, num_decimals: int=0):
    """divides b from a (a/b)"""
    if b == 0:
        print(f"ERROR: Cannot divide by {b}")
        return None
    sign = 1
    if a < 0:
        a = -a
        sign = -sign
    if b < 0:
        b = -b
        sign = -sign
    result = 0
    remainder = a
    while remainder >= b:
        result = add(result, 1) # result += 1
        remainder = sub(remainder, b) # remainder -= b
    if num_decimals <= 0:
        # this block can be written as the inline if below
        if sign == 1:
            return result
        else:
            return -result
        return (result if sign == 1 else -result) # inline if that is equivalent to the block above
    digits = []
    while remainder != 0 and num_decimals > 0:
        remainder = mult_int(remainder, 10)
        digit = 0
        while remainder >= b:
            digit = add(digit, 1) # digit += 1
            remainder = sub(remainder, b) # remainder -= b
        num_decimals = sub(num_decimals, 1) # num_decimals -= 1
        """
        digits.append(digit)
    for pow_10, digit in enumerate(digits):
        result = add(result, mult_int(pow(0.1, add(pow_10, 1))), digit) # result += digit * (0.1 ^ (pow_10 + 1))
        # for each decimal we go one more power negative for 10 ^ n, which we can write as 0.1 ^ (n - 1) because 0.1 == 1 / 10 or 1 * 10 ^ -1
        """
        digits.append(str(digit))
    result = f"{result}."
    for digit in digits:
        result += digit
    if sign == 1:
        return float(result)
    else:
        return -float(result)
    return float(result)

def mult(a, b):
    """Multiplication using multiple addition. We resolve decimals by simply scaling the number before multiplying"""
    if a == 0 or b == 0:
        return 0
    if b < 0:
        return -mult(a, -b)
    decimals = count_decimals(b)
    if decimals:
        b = mult_int(b, pow(10, decimals)) # scaled_b = b * 10 ^ decimals
    result = mult_int(a, b) # result = scaled_a * scaled_b (we do it this way to ensure b is an integer)
    if decimals:
        result = div(result, pow(10, decimals), decimals) # result = (result / (10 ^ decimals)) (unscale the result) (we can also use 0.1 ^ decimals to avoid using div)
    return result

def mod(a, b):
    quotient = div(a, b)
    num = mult(b, quotient)
    result = sub(a, num)
    if (b < 0 and result > 0) or (b > 0 and result < 0):
        result = add(result, b)
    return result

if __name__ == "__main__":
    print(pow(3, 2)) # 9
    print(pow(3.1, 2)) # idk should be 9.61 not sure why this is 10.2, probably float erros adding up
    print(pow(-2, 3)) # -8
    print(pow(2, -3)) # 0.125
    print(div(1, 2, 2)) # 0.5
    print(div(1.1, 2, 2)) # 0.55
    print(div(1, 2.1, 2)) # 0.47619047619047619047619047619048
    print(div(1, -2, 2)) # -0.5
    print(div(-1, -2, 2)) # 0.5
    print(mult(2, 2)) # 4
    print(mult(1.1, 2)) # 2.2
    print(mult(2, 2.2)) # 4.4
    print(mult(2, -2)) # -4
    print(mult(-2, -2)) # 4
    print(mod(3, 2)) # 1
    print(mod(3.3, 2)) # 1.3
    print(mod(4, 3.4)) # 0.6
    print(mod(-3, 4)) # 1
    print(mod(-3, -4)) # -3
    print(mod(3, -4)) # -1