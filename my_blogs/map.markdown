# Matlab & Abaqus & Python

-------
## 1. Operate Abaqus with Matlab

Matlab has a lot of command to run other softwares like `dos`,`system`,`!`,`unix`, etc. Here we use the command `dos` as a demo.

	[s,w]=dos('abaqus job=1 inp=RW2.inp user=nam_sn-std.obj int','-echo');

In which the command `dos` means to open the `CMD` in windows, and the following strings is the command you want to run in the `CMD`. `abaqus` is the command to run abaqus command lines. `job=1` means you job's name is '1', `inp=xxxx` is the inp file you want to submit to Abaqus, `user` is the command you need when you have a user defined subroutine file to add in the job session. The `int` means that the log information will show on the screen during calculation which is important because you need the command window to remain rolling so that you can run other commands only when the last calculation finishes. `-echo` means the information will show on the command window of Matlab which will also be stored in the variable 'w'.

Before you start the calculation, several proper .inp files are needed for the stochastic simulation. Here I use Matlab to read the .inp file that have already been built by Abaqus into a 'cell' kind of variable. This 'cell' is large array matrix with string as element. Every line in the file becomes a  string element in the array. What's left is to find out which line you need to change and the location of the commands you want to add on. Then write the changed 'cell' into a new file.

Big discovery today, _the inp file for the Abaqus command need to be more strict in format than the Abaqus cae_, __especially no blank lines inside one session__. But the Abaqus cae can import the wrong inp file as a model.

## 2. Operate Python with Matlab
It's the same as the former one, because the `dos` command can run all the command that runs in the CMD window.

The interesting thing is the Python langurage, the data structure in this langurage is very powerful, the odb file of the Abaqus is also this kind of data structure, that's why Python is very useful in post-processing. Here I use Python to decompose the odb file and take out the displacement and the reaction force.

	from odbAccess import *
	odb = openOdb(path='Job-mc1.odb')

	# 从输出数据库中提取场变量计算结果。
	s2 = odb.steps['Step-2']
	Ux1 = s2.historyRegions['Node RW2-1.48'].historyOutputs['U1'].data

	Fx1 = s2.historyRegions['Node RW2-1.1'].historyOutputs['RF1'].data

	print Ux1
	print Fx1

Then the after code are used in Matlab:
	[s,w]=dos('abaqus python readdata.py >> temp.txt');
The output of CMD will be stored in the _temp.txt_ file and the last two rows will be the displacement and the force.

A problem pops up, because the data in _temp.txt_ has a format below:

> ((0.0, -9840.1611328125), (0.0010000000474974513, -10147.7822265625), (0.0020000000949949026, -10139.9453125),...)

Which Matlab can't read, so I use:

	tem=strrep(ordata,'(','[');
	tem=strrep(tem,')',']');
	tem=strrep(tem,'],','];');
	U=str2num(tem);
to change the buklet so that Matlab can read it as a matrix.
