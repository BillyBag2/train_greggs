#!/bin/bash

docker run --rm --gpus all -v `pwd`/build:/build -v `pwd`/greggs_data/data:/data billybag2/darknet-yolo4 

