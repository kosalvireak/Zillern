# file_name = 'text.txt'
# file_name = 'from_client_'+ file_name
# file = open(file_name,'x')


file = open('text.txt')

content = file.readlines()
i = 0
while True:
    
    print(content[i])
    i = i + 1
    if content[i-1] == '':
        break
