""" data_read = open ('01.txt', 'r')
data_write = open ('02.txt', 'a')

for line in data_read:
    i = 0
    while i < len(line):
        if line[i] == '1':
            data_write.writelines('\n')
            data_write.writelines(line)
            break
        else:
            data_write.writelines('\n')
            data_write.writelines('nothing to write')
        i += 1 """

n = 20

