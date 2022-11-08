#!/bin/bash

set -e

# This file is designed to run in the docker container billybag2/darknet-yolo4.
# It expects a /build directory and a /data directory.

cd /root/darknet
./darknet detector train /build/obj.data /build/yolo4-greggs.cfg /build/training/yolo4-greggs_last.weights -dont_show -map
