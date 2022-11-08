#!/bin/python3
import os
import shutil

test_one_in =  5
data_dir = "./greggs_data/data"
meta_dir = "./greggs_data/meta"
build_dir = "./build"
training_file = os.path.join(build_dir, "train.txt")
test_file = os.path.join(build_dir, "test.txt")
data_docker_path = "/data"

obj_names_src = os.path.join(meta_dir,"obj.names")
obj_name_build = os.path.join(build_dir, "obj.names")

if not os.path.exists("build"):
    os.makedirs("build")

if not os.path.exists("build/training"):    
    os.makedirs("build/training")

shutil.copyfile(obj_names_src, obj_name_build)
shutil.copyfile("obj.data", os.path.join(build_dir, "obj.data"))
shutil.copyfile("scripts/run_training.sh", os.path.join(build_dir, "run_training.sh"))
shutil.copyfile("scripts/more_training.sh", os.path.join(build_dir, "more_training.sh"))
shutil.copyfile("yolo4-greggs.cfg", os.path.join(build_dir, "yolo4-greggs.cfg"))

f_test = open(test_file, "w")
f_train = open(training_file, "w")

one_in = 0
for dirpath, dnames, fnames in os.walk(data_dir):
    for f in fnames:
        if f.endswith(".jpg") or  f.endswith(".jpeg"):
            text_file = os.path.join(dirpath,os.path.splitext(f)[0] + ".txt")
            if os.path.exists(text_file):
                one_in = one_in + 1
                local_path = os.path.relpath(dirpath, "./greggs_data/data/")
                docker_path = os.path.join(data_docker_path, local_path)
                docker_file = os.path.join(docker_path,f)
                if one_in >= test_one_in:
                    one_in = 0;
                    target = f_test
                else:
                    target = f_train
                target.write(docker_file + "\n")

        elif f.endswith(".txt"):
            pass
        else:
            print("Unexpected file extention in data dir")
            print(os.path.join(dirpath,f))
f_train.close()
f_test.close()



