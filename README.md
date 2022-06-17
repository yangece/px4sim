# px4sim: PX4 flight simulation with MAVROS, QGC, Gazebo

This repo contains instructions and demo code for PX4 flight simulation in ROS Gazebo using MAVROS, QGC. A simple offboard control example is provided. 

## Software installation and configuration

- ROS Docker container and its installed packages
- PX4 configuration:
    - git clone https://github.com/PX4/PX4-Autopilot.git --recursive
    - bash ./PX4-Autopilot/Tools/setup/ubuntu.sh
    - manually install kconfig-frontends by building from source
- QGC:
    - sudo apt-get install fuse
    - sudo apt-get install libpulse-dev
    - sudo usermod -a -G dialout $USER
    - sudo apt-get remove modemmanager -y
- PX4 for gazebo
    - sudo apt install libgazebo9-dev
- others:
    - sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y
    - pip3 install px4tools

## Demo steps
1. First, run docker container: 
```
docker exec --user [USER_NAME] -it [CONTAINER_ID] bash
```

use Docker ps command to get CONTAINER_ID

2. Run commands in multipler terminals:
- terminal 1: roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"
- terminal 2: ./QGroundControl.AppImage
- terminal 3: sudo make px4_sitl_default gazebo
- terminal 4: python3 mission_test.py MC_mission_box.plan
- terminal 5: rqt

Note that you need to turn on the Xserver for all users by typing "xhost +" on terminal 3 and/or others.

3. for Mavros diagnostics
```
rostopic echo /diagnostics -n1
```

TODO: https://github.com/Jaeyoung-Lim/mavros_controllers

## References:

1. https://gaas.gitbook.io/guide/software-realization-build-your-own-autonomous-drone/build-your-own-autonomous-drone-e01-offboard-control-and-gazebo-simulation
2. https://www.youtube.com/watch?v=rxt0aBnBeJI
