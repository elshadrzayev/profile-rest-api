# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 config.vm.box = "ubuntu/bionic64"
 config.vm.box_version = "~> 20200304.0.0"

#connect your local host to server
 config.vm.network "forwarded_port", guest: 8000, host: 8000

#this is how you run scripts when you first create a server
 config.vm.provision "shell", inline: <<-SHELL
 #disable autoupdate to avoid a conflict with below autoupdate when you first run it
   systemctl disable apt-daily.service
   systemctl disable apt-daily.timer
 #update local repository with all local packages so we can install pyhton3 -venv zip
   sudo apt-get update
   sudo apt-get install -y python3-venv zip
 #here it says python3 instead of our default python version
   touch /home/vagrant/.bash_aliases
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
 SHELL
end
