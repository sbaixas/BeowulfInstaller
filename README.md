

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">BeowulfInstaller</h3>

  <p align="center">
    This project consists in a automatized Beowulf cluster installer with minimal setup.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This installer was started as a titulation project at Universidad de los Andes de Chile.


### Built With

* <a href="https://slurm.schedmd.com/documentation.html">Slurm</a> []()
* <a href="https://pmix.github.io/">PMix</a> []()
* <a href="https://www.open-mpi.org/">OpenMPI</a> []()
* <a href="https://www.beegfs.io/">BeeGFS</a> []()
* <a href="https://www.ansible.com/">Ansible</a> []()


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

At least 4 computers capable of running Ubuntu 20.04.0 interconnected via ethernet with a switch or router.

One of the computers will act as a control node, the rest will be divided into metadata storage and compute nodes.

### Installation

1. Install <a href="http://old-releases.ubuntu.com/releases/20.04.0/">Ubuntu 20.04 LTS Beta</a> on all the nodes. (It is not working with the 20.04.02 due to kernel changes).


2. Set a static ip address in all nodes and then restart the network
3. In all nodes but the control node do the following:
- Set a root user password and run the following commands:
  ```sh
  sudo apt update
  
  ```sh
  sudo apt install ssh
  ```
- Edit /etc/ssh/sshd_config file and set PermitRootLogin yes
- Run
  ```sh
  sudo service sshd restart
  ```
4.- In the control node do the following:

- Clone this repository and cd into the repo folder
- Run
  ```sh
  sudo apt install ansible
  ```
- For each node
  ```sh
  ssh-copy-id root@[ip_address]
  ```
  where ip_address is the static ip previously set for each node.

- Edit the file /etc/ansible hosts according to the hosts example file, groups guineapig and master names must stay the same.
- Run
  ```sh
  ansible-galaxy collection install community.mysql
  ```
  ```sh
  ansible-playbook main.yml
  ```


