#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for secret in dir(hidden_4):
        if secret[0] is not '_':
            print(secret)
