# train_greggs

Train gregs is a set of scripts to train a yolo (4?) nurel net. At the time of writing the data set is private and referenced through a git submodule to a local server. This project is public for reference only.

# Docker container

Simple scripts are designed to run on a linux system with a basic installation of python3. The training is done in a docker container [BillyBag2/darknet-yolo4-docker](https://github.com/BillyBag2/darknet-yolo4-docker) At the time of writing this was not in a registery but a repository is available to build your own image.

## Prep for first build

[build_training_set.py](build_training_set.py) gathers everything needed into the build director.

## Training

At the time of writing you may need to edit [run_training.sh](scripts\run_training.sh) and [more_training.sh](scripts\more_training.sh).

or [tiny_run_training.sh](scripts\tiny_run_training.sh) or [tiny_more_training.sh](scripts\tiny_more_training.sh).

Run [shell.sh](shell.sh) to start a docker shell. Then run in the docker shell `/build/xxx_training.sh`.

### `[tiny_]run_training.sh`

This script runs the training from the begining. When starting it is recommended that you use a single GPU. If you stop training you can restart by using `[tiny_]more_training.sh`. If you have more than one GPU it is recommended to stop after 1000 interations and then restart with the `[tiny_]more_training.sh` script with two GPUs enabled by editing the script.

### `[tiny_]more_training.sh`

This script continues training from a saved state. It is recomended to stop training after 1000 iterations and restart with all GPUS if you have more than one.

# Example inference

`./darknet detector test /build/obj.data /build/yolo4-tiny-greggs.cfg /build/training/yolo4-tiny-greggs_last.weights /data/chicken\ bake/IMG_2602_frame048.jpg`

# Expected layout

```
greggs_data\data\<class>\
    image_xyz.jpg
    image_xyz.txt
greggs_data\test\<class>\
    image_xyz.jpg
    image_xyz.txt
greggs_data\meta\obj.names
```

# Charts

Charts are created in the docker container in the `~/darknet` directory.
Copy these to /build before exiting the container. Rename them imediately so you can copy the next time you need to without too much hasle. I have not worked out how to keep a chart going from a previous run.

# TODO

* Explain in readme about pre-trained wieghts.
* Copy the chart from the container to build dir.
* Document merging charts.

# References

## darknet

* https://github.com/AlexeyAB/darknet

## Random stuff

* https://github.com/hollance/YOLO-CoreML-MPSNNGraph
* https://www.codeproject.com/script/Content/ViewReadingList.aspx?rlid=33
* https://medium.com/analytics-vidhya/train-a-custom-yolov4-tiny-object-detector-using-google-colab-b58be08c9593
* https://blog.roboflow.com/training-yolov4-on-a-custom-dataset/
* https://github.com/ankits16/CVRecorderFinal/blob/main/converters/YOLOv4toCoreML_Mpieter.ipynb
* https://gist.github.com/TakaoNarikawa/aef13571eec97d78603688eef05b5389



