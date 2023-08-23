import subprocess, time, os, sys

cmd = "./b_ff.sh https://pull-flv-l11-sg01.tiktokcdn.com/stage/stream-2131214190013317163_or4.flv"
args = cmd.split()
process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
for line in process.stdout:
    if "st:1 invalid dropping" in line :
        print(line)
        process.terminate()
