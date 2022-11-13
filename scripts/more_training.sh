#!/bin/bash

set -e

# This file is designed to run in the docker container billybag2/darknet-yolo4.
# It expects a /build directory and a /data directory.

# K80 siplified instructions.
# An nvidia K80 appears as two graphics cards.
# Train with one card for 1000 and then stop and switch to two graphics cards.

cd /root/darknet
# Two graphics cards
#./darknet detector train /build/obj.data /build/yolo4-greggs.cfg /build/training/yolo4-greggs_last.weights -dont_show -map -gpus 0,1

# A single graphics card. Use for early training if more than one card.
./darknet detector train /build/obj.data /build/yolo4-greggs.cfg /build/training/yolo4-greggs_last.weights -dont_show -map -gpus 0

