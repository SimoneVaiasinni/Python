#   open() returns a file object.  open(filename, mode).
#   'r' when the file will only be read, 
#   'w' for only writing 
#   'a' opens the file for appending,
#   'r+' opens the file for both reading and writing,
#   'b' appended to the mode opens the file in binary mode
File = open("file.txt" , 'rb+')
File.write(b'0123456789abcdef')

print(File.seek(5))    # Go to the 6th byte in the file
print(File.read(5))     

File.close()


#It is good practice to use the with keyword when dealing with file objects.
#The advantage is that the file is properly closed after its suite finishes, 
#   even if an exception is raised at some point. 
#Using with is also much shorter than writing equivalent try-finally blocks: 
#   is good practice to use the with keyword when dealing with file objects.
with open('file.txt', 'r') as f:
    read_file = f.read()
    print(read_file)

# ============= Saving structured data with json ============ #
import json
json.dumps([1, 'simple', 'list'])