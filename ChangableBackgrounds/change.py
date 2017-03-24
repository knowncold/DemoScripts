#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands

picdir = 'backgrounds/'
cmd = 'ls ' + picdir
out = commands.getoutput(cmd)
outlist =  out.split('\n')
file_list=[]

file_out = open('xenial.xml','w')
file_out.write(
"""<background>
<starttime>
\t<year>2009</year>
\t<month>08</month>
\t<day>04</day>
\t<hour>00</hour>
\t<minute>00</minute>
\t<second>00</second>
</starttime>
""")

j = 0
static_time = 150.0
transition_time = 3.0
for i in outlist:
    print i
    origin_name = i.split('.')[0]
    extension = i.split('.')[1]
    if ' ' in origin_name:
        origin_name = origin_name[:origin_name.find(' ')]+"\\"+origin_name[origin_name.find(' '):]
    cmd = 'mv '+picdir+origin_name+'.'+extension+' '+picdir+'bgpic'+str(j)+'.'+extension
    file_list.append(picdir+'bgpic'+str(j)+'.'+extension)
    print cmd
    out = commands.getoutput(cmd)
    j += 1
print file_list
print j
for i in range(0,j):
    file_out.write("<static>\n\t<duration>"+str(static_time)+"</duration>\n")
    file_out.write("\t<file>")
    file_out.write("/home/knowncold/Pictures/"+file_list[i])
    file_out.write("</file>\n")
    file_out.write("</static>\n<transition>\n\t<duration>")
    file_out.write(str(transition_time))
    file_out.write("</duration>\n\t<from>")
    file_out.write("/home/knowncold/Pictures/"+file_list[i])
    file_out.write("</from>\n\t")
    file_out.write("<to>")
    if(i==j-1):
        next_file = 0
    else:
        next_file = i+1
    file_out.write("/home/knowncold/Pictures/"+file_list[next_file])
    file_out.write("</to>\n</transition>\n")
file_out.write("</background>")
