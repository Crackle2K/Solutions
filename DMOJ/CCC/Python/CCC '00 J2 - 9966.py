
numbers = [1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986, 1001, 1111, 1691, 1881, 1961, 6009, 6119, 6699, 6889, 6969, 8008, 8118, 8698, 8888, 8968, 9006, 9116, 9696, 9886, 9966, 10001, 10101, 10801, 11011, 11111, 11811, 16091, 16191, 16891, 18081, 18181, 18881, 19061, 19161, 19861]
# thank you to user 837830 for giving me this list because I do not want to type all of that :(

start, end = int(input()), int(input())
count = 0
for i in range(start, end):
    if i in numbers:
        count += 1

print(count)
