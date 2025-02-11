def is_palindrome(string):
    reversed_string = string[::-1]
    return True if string == reversed_string else False

print(is_palindrome("somos"))