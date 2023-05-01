import string

def caesar(text, num):
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[num:] + string.ascii_lowercase[:num])
    return text.translate(cipher)

if __name__ == '__main__':
    text = str(input('Enter text: '))
    num = int(input('Enter Key num: '))
    print('encrypted text : ' + caesar(text, num))
    
