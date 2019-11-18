ROS on GCP
==========

Google anouced during 2018 a Cloud Robotics Platform (The Robot Report_) that will help compute and process online and offline data. Cloud robotics provide access to:

- Parallel computing of hundreds of machines on the cloud.

- Huge database access and performance.

- And APIs related to Big Data Analysis.

.. _Report: https://therobotreport.com/google-cloud-robotics-platform/

AWS' AutoMaker_ already makes possible to deploy Robotic Operating System (ROS) nodes on the cloud with access to developing tools such as speach recognition, simulation environments and premade demo applications ready to modify and addapt to the custom app of the developer.

.. _AutoMaker: https://aws.amazon.com/es/robomaker/

However, as October 2019 Google Cloud Platform does not provide a solution to robotic systems on the cloud.


Docker enviroment to manage ROS instances
=========================================

This tutorial set ups a Google Compute Engine (GCE) instance to be connected to ROS in a custom Virtual Private Cloud (VPC) network.

Glossary
========

- Docker: Containerization tool
- GCE: Virtual Machines.
- VPC: Equivalent of VPN on the cloud.





