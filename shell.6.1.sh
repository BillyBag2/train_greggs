#!/bin/bash

docker run -it --rm --gpus all\
 -v `pwd`/build:/build\
 -v `pwd`/greggs_data/data:/data\
 -v `pwd`/greggs_data/test:/test\
 billybag2/darknet-yolo4:c6.1
