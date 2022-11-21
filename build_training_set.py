#!/bin/python3
import os
import shutil
import random

test_one_in =  5
# dataset_dir dataset. This dit contains "meta" and "data"
dataset_dir = "./greggs_data"
# data_dir contains images and yolo syle *.txt files.
data_dir = os.path.join(dataset_dir,"data")
# meta_dir contains meta data.
meta_dir = os.path.join(dataset_dir,"meta")
# build_dir is where the action happens.
build_dir = "./build"
# training_file contains a list of images to train.
training_file = os.path.join(build_dir, "train.txt")
# test_file contains a list of images to test against.
test_file = os.path.join(build_dir, "test.txt")
# data_docker_path is the path docker sees the data.
data_docker_path = "/data"
# obj_names_src is the source file for the class names.
obj_names_src = os.path.join(meta_dir,"obj.names")
# obj_name_build is the path to where the names are in the build directory.
obj_name_build = os.path.join(build_dir, "obj.names")

if not os.path.exists("build"):
    os.makedirs("build")

if not os.path.exists("build/training"):    
    os.makedirs("build/training")

shutil.copyfile(obj_names_src, obj_name_build)
shutil.copyfile("obj.data", os.path.join(build_dir, "obj.data"))
shutil.copyfile("scripts/run_training.sh", os.path.join(build_dir, "run_training.sh"))
shutil.copyfile("scripts/tiny_run_training.sh", os.path.join(build_dir, "tiny_run_training.sh"))
shutil.copyfile("scripts/more_training.sh", os.path.join(build_dir, "more_training.sh"))
shutil.copyfile("scripts/tiny_more_training.sh", os.path.join(build_dir, "tiny_more_training.sh"))
shutil.copyfile("yolo4-greggs.cfg", os.path.join(build_dir, "yolo4-greggs.cfg"))
shutil.copyfile("yolo4-tiny-greggs.cfg", os.path.join(build_dir, "yolo4-tiny-greggs.cfg"))

train_list = []
test_list = []

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
                    test_list.append(docker_file + "\n")
                else:
                    train_list.append(docker_file + "\n")

        elif f.endswith(".txt"):
            pass
        else:
            print("Unexpected file extention in data dir")
            print(os.path.join(dirpath,f))

f_test = open(test_file, "w")
random.shuffle(test_list)
f_test.writelines(test_list)
f_test.close()
f_train = open(training_file, "w")
random.shuffle(train_list)
f_train.writelines(train_list)
f_train.close()




