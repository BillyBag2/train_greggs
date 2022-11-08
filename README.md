# train_greggs

Train gregs is a set of scripts to train a yolo (4?) nurel net. At the time of writing the data set is private and referenced through a git submodule to a local server. This project is public for reference only.

# Docker container

Basic scripts are designed to run on a linux system with a basic installation of python3. The tarining is done in a docker container [BillyBag2/darknet-yolo4-docker](https://github.com/BillyBag2/darknet-yolo4-docker) At the time of writing this was not in a registery but a repository is available to build your own image.

# Scripts

## Prep for first build

[build_training_set.py](build_training_set.py) gathers everything needed into the build director.

## training (WIP)
The intention is to run the docker container with the local directories mounted in the container as /build /data 