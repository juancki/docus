======================
ROS on GCP with Docker
======================


Google anouced during 2018 a Cloud Robotics Platform (The Robot Report_) that will help compute and process online and offline data. Cloud robotics provide access to:

- Parallel computing of hundreds of machines on the cloud.

- Huge database access and performance.

- And APIs related to Big Data Analysis.

.. _Report: https://therobotreport.com/google-cloud-robotics-platform/

Google advancements in this field are visible in their GitHub repo_, where you can set up the a ROS node in Kubernetes. In this tutorial we will see how to create a GCE instance that has ROS with Docker.

.. _repo: https://github.com/googlecloudrobotics


Docker enviroment to manage ROS instances
=========================================

This tutorial set ups a Google Compute Engine (GCE) instance to be connected to ROS in a custom Virtual Private Cloud (VPC) network.

The following yaml file:

.. literalinclude:: dply-ros.yaml
  :language: yaml

.. literalinclude:: dply-ros.jinja
  :language: jinja

.. figure:: ./SvgFileService.svg
  :name: image's name


