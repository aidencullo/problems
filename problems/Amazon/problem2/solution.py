def distinct_words(password):
    n = len(password)
    passwords = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            reversed_password = password[:i] + password[i:j][::-1] + password[j:]
            if not reversed_password in passwords:
                passwords.add(reversed_password)
    return len(passwords)


def distinct_words(password):
    n = len(password)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if password[i] != password[j]:
                count += 1
    return count + 1
