"""
Write a Program which takes a path of "txt" file and check each line of file if any line is found duplicate then it should be removed and file must be get updated
"""



lines_seen = set() # holds lines already seen
print("Please Give me a path of File which has to modify - ")
t = str(input())

#input =/storage/emulated/0/download/Email.txt

with open(t,"r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            lines_seen.add(i)
    f.truncate()
print("File Updated Successfully..!!!")