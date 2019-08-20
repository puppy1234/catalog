# Catalogs - Udacity 
## gao yuchong - shanghaitech university
### Full Stack Web Development ND
_______________________
## Project Description:
This project aims at creating a catalog website about Starcraft, an interesting RTS game, the items in it introduces the basic concept of the three camps.
* This project explores the basic concept of API and authorization, with which we can find the target information we want in webdevelop.
* I created a database with user,catalog and items,with them to sign in, find items and see them.


## Pre-requisites
* Python 3 [if you are windows download it from this link:https://www.python.org/downloads/ and download python 3.7.2;
if you are a linux user just type in your command line:"sudo apt-get install python3.7 python3.7-dev"]
* Vagrant [download it from here:https://www.vagrantup.com/, after all three tools have been set up]
* VirtualBox 3 [you can download from here:https://www.virtualbox.org/wiki/Download_Old_Builds_5_1, just find the suitable version.]
* VM configuration[you should dowload the configuration fold https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip, unzip it in a newly created fold]
* My Catalog.zip


## Setup
1. cd into the dowloaded vagrant dictionary and put "vagrant up" in your command line.
2. after downloaded the ubuntu system, run "vagrant ssh" to log in
3. put my Catalog dictionary into /vagrant then cd into it
4. run "python database_setup.py" then run "python lotsofitems.py" after seeing "item added", run "python project.py"
5. open your browser, type in localhost::8000 to see my web page.

*After these, you can login to edit or delete items or just see through what i have in it.