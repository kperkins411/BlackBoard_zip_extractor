#get a list of files
from glob import glob
import os
import subprocess

# the parent directory where I'm running the eclipse C++ project
eclipse_project_dir = "/home/keith/eclipse-workspace/Proj1_410_solution/"
where_student_files_are_dir = "/home/keith/Desktop/410/"
script_output_results = "stdout.txt"

filelist = glob(where_student_files_are_dir + "*.cpp")
# filelist.sort()

#redirect output
out = open(script_output_results,"w")
for file in filelist:
    #bb format is   Project1_00767120_attempt_2017-09-15-19-05-17_utilities
    #2nd group is student id
    delims = file.split("_")
    student_id = "-----------------------------------FOR_STUDENT_" + delims[1]+"-----------------------------------------"

    #remove results and utilities
    cmds = "echo " + student_id + ";rm " + eclipse_project_dir + "results.txt;rm " + eclipse_project_dir + "utilities.cpp"
    # cmds = "rm "+ proj_dir +"results.txt;rm "+ proj_dir +"utilities.cpp"

    process = subprocess.Popen(cmds,shell=True,  stdout=out,stderr=out)
    process.wait()

    #copy in student utilities.cpp
    cmds = "cp " + file +" " + eclipse_project_dir + "utilities.cpp"
    process = subprocess.Popen(cmds, shell=True, stdout=out,stderr=out)
    process.wait()

    #you can comment out the following lines, set a breakpoint on above process.wait
    # then step through this program to breakpoint
    # and then debug student code in eclipse
    cmds = "cd " + eclipse_project_dir + ";cd ./Debug;make clean;make;cd ..;./Debug/Proj1_410_solution"
    process = subprocess.Popen(cmds, shell=True, stdout=out,stderr=out)
    process.wait()

out.close

