# # file_name = 'text.txt'
# # file_name = 'from_client_'+ file_name
# # file = open(file_name,'x')


# file = open('text.txt')

# content = file.readlines()
# i = 0
# while True:
    
#     print(content[i])
#     i = i + 1
#     if content[i-1] == '':
#         break


f = open("Light sensor.txt","r")
end_of_file = f.readline()
for x in f:
    res = x.split()
    val = (str(res[0]), str(res[1]))
    print(val)
    if not end_of_file:
        break