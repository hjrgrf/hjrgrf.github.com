# 1. find any new html files in my_blogs
# 2. change the style of the html codes
# 3. update blog_list file
# 4. push to github

import os
import pickle
import re
import shutil

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

# new_files=['ind11.html','image001.png']

def findhtml(new_files):
	for new_file in new_files:
		print new_file
		if os.path.isfile('my_blogs/'+new_file) and new_file.endswith('.html'):
			new_blog=new_file
			break
		else:
			new_blog=0
	return new_blog

new_blog=findhtml(new_files)

print new_blog
if new_blog != 0:
	blog_cont=open('my_blogs/'+new_blog)
	line=blog_cont.readline()
	print line
	line_tag=1
	while line!='' and line!=None and line_tag<12:
		line=blog_cont.readline()
		print line
		line_tag=line_tag+1
		if re.search('<title>(.)*</title>',line):
			print line
			line_sp=re.split('<|>',line)
			line_title=line
			print line_sp[2]
			title_name=line_sp[2]
			

	new_blog_file=open('my_blogs/n_'+new_blog,'w')
	head_file=open('my_blogs/blog_head.html')
	tail_file=open('my_blogs/blog_tail.html')
	line_tag=1
	while line!='' and line!=None and line_tag<4:
		line=head_file.readline()
		new_blog_file.write(line)
		line_tag=line_tag+1

	new_blog_file.write(line_title)

	line=head_file.readline()
	line_tag=line_tag+1
	while line!='' and line!=None and line_tag<17:
		line=head_file.readline()
		new_blog_file.write(line)
		line_tag=line_tag+1


	new_blog_file.write('  <h2 class="project-tagline">'+title_name+'</h2>\n')	


	line=head_file.readline()
	line_tag=line_tag+1
	while line!='' and line!=None and line_tag<22:
		line=head_file.readline()
		new_blog_file.write(line)
		line_tag=line_tag+1



	line_tag=1
	while line!='' and line!=None:
		line=blog_cont.readline()
		if re.search('</body>',line):
			break
		new_blog_file.write(line)
		line_tag=line_tag+1


	line_tag=1
	while line!='' and line!=None:
		line=tail_file.readline()
		new_blog_file.write(line)
		line_tag=line_tag+1



	blog_cont.close()
	new_blog_file.close()
	head_file.close()
	tail_file.close()


	new_title_list=['	  <P>\n','	  <a href="https://hjrgrf.github.io/my_blogs/','">','</a>\n','	  </P>\n']

	b_l=open('my_blogs/blogs_list.html','w')
	b_l_b=open('my_blogs/blogs_list_bk.html')

	line_tag=1
	while line_tag<28:
		line=b_l_b.readline()
		line_tag=line_tag+1
		b_l.write(line)


	b_l.write(new_title_list[0])
	b_l.write(new_title_list[1])
	b_l.write('n_'+new_blog)
	b_l.write(new_title_list[2])
	b_l.write(title_name)
	b_l.write(new_title_list[3])
	b_l.write(new_title_list[4])


	while 1:
		line=b_l_b.readline()
		line_tag=line_tag+1
		if	re.search('</html>',line):
			break
		b_l.write(line)

	b_l.write('</html>')


	b_l.close()
	b_l_b.close()

	shutil.copy('my_blogs/blogs_list.html','my_blogs/blogs_list_bk.html')
	
file_list_new=os.listdir('my_blogs')
blogs=open('blogs.pkl','r+')
pickle.dump(file_list_new,blogs)
blogs.close()


