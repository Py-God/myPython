import os

for filename in os.listdir():
    if filename.endswith('.rxt'):
        # os.unlink(filename)
        print(filename)

# this is the ideal way to use these delete calls. so it'll print the files you wrote your program to delete
# to prevent accidentally deleting useful files and folders