#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PoseWithCovarianceStamped

class publishGPS(object):

    def __init__(self):
        rospy.loginfo("Initialising GPS publishing")
        self.gps_sub=rospy.Subscriber('/mavros/global_position/global', PoseWithCovarianceStamped, self.callback)
        self.lastMsg=None
        self.gps_pub=rospy.Publisher('/gps/fix', NavSatFix, queue_size=1)
        rospy.sleep(8)
        rospy.loginfo("initialised")
        
    def callback(self, data):
        self.lastMsg=data

    def do_work(self):
        self.splitStrings= str(self.lastMsg).split(",")
        rospy.loginfo(self.splitStrings)
        gpsmsg=NavSatFix()
        gpsmsg.header.stamp = rospy.Time.now()
        gpsmsg.header.frame_id = "gps"
        rospy.loginfo(self.splitStrings[1])
        gpsmsg.latitude=float(self.splitStrings[1][4:])
        gpsmsg.longitude=float(self.splitStrings[2][5:-5])
        self.gps_pub.publish(gpsmsg)

    def run(self):
        r=rospy.Rate(1)
        while not rospy.is_shutdown():
            self.do_work()
            r.sleep()
        
if __name__=='__main__':
    rospy.init_node('pubgps')
    obj=publishGPS()
    obj.run()
