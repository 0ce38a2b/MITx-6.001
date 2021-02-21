''''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc'''

s = "abcde"
longest_s = ""
SubString = []
for i in range(len(s)):
    for j in range(len(s)):
        if(i < j):                    # 第一次没注意到的细节
            string_to_check = s[i:j+1]  # 解决最后一个字母问题 ! s[i:j]切片的时候取i 到 j-1
            sflag = True
            for m in range(1, len(string_to_check)):

                if string_to_check[m-1] > string_to_check[m]:
                    sflag = False

            if (sflag == True):
                SubString.append(string_to_check)
# print(SubString)
longest_s = SubString[0]
for element in SubString:
    if (len(element) > len(longest_s)):
          longest_s = element

print("The longest substring in alphabetical order is:" + longest_s)




