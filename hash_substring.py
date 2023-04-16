# python3

def read_input():
    choice = input().rstrip()
    if choice == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif choice == 'F':
        file_name = input()
        try:
            with open('./tests/' + file_name, 'r') as file:
                pattern = file.readline().rstrip()
                text = file.readline().rstrip()
        except Exception as ex:
            print('File not found', str(ex))
            return
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    if len(pattern) > len(text):
        return occurrences
    
    base = 256
    prime_modulus = 101
    b = pow(base, len(pattern) - 1)

    p_hash = 0
    t_hash = 0

    for i in range(len(pattern)):
        p_hash = (base * p_hash + ord(pattern[i])) % prime_modulus
        t_hash = (base * t_hash + ord(text[i])) % prime_modulus

    for i in range(len(text) - len(pattern) + 1):
        if p_hash == t_hash:
            if text[i:i + len(pattern)] == pattern:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            t_hash = (base * (t_hash - ord(text[i]) * b) + ord(text[i + len(pattern)])) % prime_modulus

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

