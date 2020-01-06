========================================
Ubuntu 18.04 LTS on GCP for ROS with GUI
========================================


In this tutorial we will cover the script I created to make your own ROS development enviroment in a GCP instance. And then, connect to it using Google's Remote Desktop.

In the turorial *Debian 9 docker ROS on GCP* we used the metadata information of the ``start-up`` script which allows for simple interface to execute commands in a bash format.

In this case, we are going to use the ``.cloud-init`` metedata yaml (documentation_) to set multiple things:

- Set run commands to be executed on the creation only.
- Sources of the packages to download the packages.
- The packages that we want to download.

The files to perform the installation ``chromotium.cloud-init`` and ``create-desktop.bash`` are in the github repo https://github.com/juancki/ros-docker-gcp/tree/master/gce-ros-ubuntu. 

Lauch instance
..............
Execute this file you will create the instance:

.. code-block:: bash

   chmod +x create-desktop.bash
   ./create-desktop.bash full

You will see that the GCE instance is being launched in the console.  

Connect Remote-desktop
......................

- On the GCP Cloud Shell we connect to the newly created instance and wait for the initialization to finish.:

.. code-block:: bash

   gcloud compute ssh desktop-full -- journalctl -f --identifier=cloud-init

- Then, open this link in your browser: http://goto.google.com/crd-auth

- Once accepted permissions copy the command and remember to add a name to the end of the command such as ``desktop-full``. Paste it into the terminal and press enter.

- Then go to Chrome Remote Desktop client in your browser:  https://remotedesktop.google.com

- Open a terminal an run, to set up bash:

.. code-block:: bash

  echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
  source ~/.bashrc

There your are, it should be good to go.

The rest of the article is the explanation behind the values set.

create-desktop.bash
-------------------
Starting for the easiest part, this file only contains one command. This ``gcloud`` command is to create a GCE instance with Ubuntu 18.04 LTS image with 4 cores and 15GB of RAM, 200GB of SSD disk and with the ``user-data`` from the file ``chomoting.cloud-init``.

.. literalinclude:: create-desktop.bash
  :language: bash
  :caption: create-desktop.bash
 

The cost of this instance is is related to the instance type_ that in this case is set to ``n1-standard-4`` but can have multple cores and the size of the disk which is 200GB.


chomoting.cloud-init
....................

This file describes in a cloud-standarized way to set up the instance. In this case we have added the sources and packages required to install ROS Melodic.

Shown ahead, this file has a first commented part to show the instructions to setup the machine and to connect with remotedesktop.

The second part shows 5 sections:

- bootcmd: excuted early in the initialization process.
- apt_sources: The source of the packages for debian based distros.
- packages: excuted on the start.
- write_files: We create and set content of the following files.
- runcmd: List of string that will be executed near the end of the process. 

cloud-init: bootcmd:
--------------------
We set up the keys of the sources to be able to get the index of the packages.

Particularely, ``- curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | apt-key add - >/dev/null`` sets the key for ROS packages.

cloud-init: apt_sources:
------------------------
Then we add all the sources that will be necessary to locate the packages that we want to install.

In this case we set the sources for:  ROS, Docker and some Google Toos such as logging, monitoring and remote-desktop.

We also the source of the ros packages in the ``ros-latest.list`` file under the ``/etc/apt/sources.list.d`` folder.

.. code-block:: yaml

        - source: "deb http://packages.ros.org/ros/ubuntu bionic main"
          filename: ros-latest.list


cloud-init: packages:
---------------------
The actual packages that we would install using ``apt install``. We include the packages included in the ROS Melodic installation_.


cloud-init: write_files:
------------------------
In this section, we set up the basic files for apt, remote-desktop and docker.


cloud-init: runcmd:
-------------------
Finally the services are launch, PyCharm/Eclipse installed and ROS' rosdep initialized.

.. literalinclude:: chromoting.cloud-init
  :language: yaml
  :caption: chromoting.cloud-init


Hacking with cloud-init
-----------------------
As we have seen this file is structured to easily see the most fundamental parts of the packages installed in a cloud instance. To modify the file, I strongly suggest using the logs of the ``cloud-init`` operation: ``/var/log/cloud-init-output.log`` and ``/var/log/cloud-init.log``.



.. _documentation: https://cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance
.. _type: https://cloud.google.com/compute/docs/machine-types
.. _cloud-init-doc: https://cloudinit.readthedocs.io/en/latest/topics/hacking.html
.. _installation: http://wiki.ros.org/melodic/Installation/Ubuntu
