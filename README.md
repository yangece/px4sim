# px4sim: PX4 flight simulation with MAVROS, QGC, Gazebo

This repo contains instructions and demo code for PX4 flight simulation in ROS Gazebo using MAVROS, QGC. A simple offboard control example is provided. 

## Software installation and configuration

- ROS Docker container and its installed packages
- PX4 configuration:
    - Get px4-autopilot codebase, `git clone https://github.com/PX4/PX4-Autopilot.git --recursive`
    - Run setup bash script, `bash ./PX4-Autopilot/Tools/setup/ubuntu.sh`
    - Manually install kconfig-frontends by building from source
- QGC:QGroundControl 
    - `sudo apt-get install fuse`
    - `sudo apt-get install libpulse-dev`
    - `sudo usermod -a -G dialout $USER`
    - `sudo apt-get remove modemmanager -y`
    - Manually download QGC appimage
        - **Alert** please install version:v4.1.4 (https://github.com/mavlink/qgroundcontrol/releases/download/v4.1.4/QGroundControl.AppImage) or lower, higher version may need to use qt5.15, which is not provided by ubuntu 20.04 LTS offically(5.12 instead)
        - If you wanna use latest QGC, please upgrade your QT manually from qt official site and update env 
- PX4 for gazebo
    - `sudo apt install libgazebo9-dev`
- Build PX4 firmwire from source code
    - Get Firmwire source code `git clone https://github.com/PX4/Firmware.git` 
    - `cd Firmware` 
    - Build firmwire by running `make rostest`  or `make px4_sitl_default`
- Others:
    - `sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y`
    - `pip3 install px4tools`
    - It is highly recommended to install gnome-terminal (or any terminal you like) in container so we can launch multi terminals within the container's shell `.  
    - Remember to save your change in docker by running `docker commit <container_ID> <name>:<tag>`

## Demo steps
1. First, run docker container: 
```
docker exec --user [USER_NAME] -it [CONTAINER_ID] bash
```

use Docker ps command to get CONTAINER_ID

2. Run commands in multipler terminals:
- terminal 1: `roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"`
- terminal 2: launch QGroundControl `yourQGCpath/QGroundControl.AppImage` 
- terminal 3: launch gazebo visual interface `make px4_sitl_default gazebo`
- terminal 4: launch test script, in "px4sim/mavros-demo", run `python3 mission_test.py MC_mission_box.plan` 
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
