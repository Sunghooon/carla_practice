# CARLA PRACTICE (on going)

## Introduction
In this repository, I will try simulate object detection with 3D LiDAR sensor. For the simulator, `CARLA Simulator 0.9.9 ver.` will be used. And I'm planning to utilize connection between CARLA and ROS, especially for `ROS melodic`. Guess it will be long-term work for me, hope to be steady with it.


## Prerequisites
* CARLA 0.9.9
* Ubuntu 18.04
* ROS melodic

## Practice

### Launch CARLA simulator server
At `~/CARLA_0.9.9`:

```bash
./CarlaUE4.sh # add -windowed -ResX=N -ResY=N for windowed mode
```
Launching the simulator in server mode, by using `-carla-server` argument, can launch CARLA simulator in **server mode**.

### Connecting Python Client

Launching the client, data will be saved at `_out` folder.
```bash
./client_example.py --autopilot # --images-to-disk
```



Can run `manual_control.py` for GUI interface.


some commands,


export CARLA_ROOT=/home/psx/Documents/CARLA_0.9.10

export PYTHONPATH=$PYTHONPATH:$CARLA_ROOT/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg:$CARLA_ROOT/PythonAPI/carla

source /opt/carla-ros-bridge/melodic/setup.bash 

roslaunch carla_ros_bridge carla_ros_bridge.launch
