# Docker

* Go to https://docs.docker.com/engine/install/ubuntu/.
* Operating system requirements are checked. <br>
  `$ cat /etc/*release*`
* Any old versions of Docker will be deleted. <br>
  `$ sudo apt-get remove docker docker-engine docker.io containerd runc`
* Update the apt package index and install packages to allow apt to use a repository over HTTPS:<br>
  `$ sudo apt-get update`
  `$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release`
* Add Docker’s official GPG key:<br>
  `$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg`
* Use the following command to set up the stable repository. To add the nightly or test repository, 
  add the word nightly or test (or both) after the word stable in the commands below. 
  Learn about nightly and test channels.<br>
  ` echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
* Update the apt package index, and install the latest version of Docker Engine and containerd.<br>
  `$ sudo apt-get update`
  `$ sudo apt-get install docker-ce docker-ce-cli containerd.io`
* Verify that Docker Engine is installed correctly by running the hello-world image.<br>
  `sudo docker run hello-world`
* The Docker version and installed are checked.<br>
  `$ sudo docker version`
  
  👉 For more detail: https://docs.docker.com/engine/install/ubuntu/
