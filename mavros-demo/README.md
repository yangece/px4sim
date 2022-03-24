# UAV flight simulation with MAVROS, Gazebo, PX4, RViz, QGC

1. Docker environment

    see instructions in the docker-ros github repo for building and running the Docker container.

2. Steps

    - run docker container:
	```
    bash run.sh
    ```


    - open another terminal, "docker ps" to see the docker container id, then

    ```
    docker exec -it --user <user_name> <container_id> bash
    ```

   repeat to open more terminals to connect to the same docker container

    - on terminal 1:

    ```
    roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"
    ```

    - on terminal 2:

    ```
    sudo usermod -aG dialout $USER
    sudo apt-get remove modemmanager -y (not necessary in noetic)
    ./QGroundControl.AppImage
    ```

    - on terminal 3:

    first, turn on x11:
    ```
    xhost +
    ```

    then, go to px4 directory: px4/PX4-
    ```
    sudo make px4_sitl_default gazebo
    ```

    - on terminal 4:

    go to mavros-demo directory: 
    ```
    python3 mission_test.py MC_mission_box.plan
    ```

    - on terminal 5:

    open rqt or rviz

3. offboard control development

    go to ros_wc directory (ROS workspace directory for dev inside docker container)
    offboard control demo example in offb directory

    - run rviz:
    ```
    rosrun rviz rviz
    ```

    add topics, and then
    save as offb.rviz file

    make a rviz launch file, offb.rviz, save in launch/ directory

    - build offb package
    ```
    catkin_make
    source devel/setup.bash
    ```

    - run rviz launch file:
    ```
    roslaunch offb rviz.launch
    ```

4. other issues

    - gazebo REST issue: [Err] [REST.cc:205] Error in REST request:
    https://answers.gazebosim.org//question/25030/gazebo-error-restcc205-error-in-rest-request/



