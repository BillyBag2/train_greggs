#!/bin/bash

set -e

# This file is designed to run in the docker container billybag2/darknet-yolo4.
# It expects a /build directory and a /data directory.

cd /root/darknet
./darknet detector train /build/obj.data /build/yolo4-tiny-greggs.cfg /build/yolov4-tiny.conv.29 -dont_show -map -iou_thresh 0.75
