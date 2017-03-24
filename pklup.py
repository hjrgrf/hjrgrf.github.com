# 1. find any new html files in my_blogs
# 2. change the style of the html codes
# 3. update blog_list file
# 4. push to github

import os
import pickle
import re

file_list_new=os.listdir('my_blogs')
new_files=[]
blogs=open('blogs.pkl','r+')
file_list=pickle.load(blogs)
for afile in file_list_new :
    if afile not in file_list :
        new_files.append(afile)
blogs.close()
print new_files

blogs=open('blogs.pkl','r+')
pickle.dump(file_list_new,blogs)
blogs.close()

def findhtml(new_files):
    for new_file in new_files:
        if os.path.isfile(new_file):
            new_blog=new_file
    return new_blog

# new_blog=findhtml(new_files)

# open_new_blog=open(new_blog,'r+')









