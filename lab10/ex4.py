def is_palindrome_recursive(s):
    if not isinstance(s, str):
        return "Помилка: введіть рядок"
    s = ''.join(c.lower() for c in s if c.isalnum())
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

s = input("Введіть рядок: ")
result = is_palindrome_recursive(s)
print("Це паліндром." if result == True else "Це не паліндром." if result == False else result)
