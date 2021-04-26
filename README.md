<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">BeowulfInstaller</h3>

  <p align="center">
    This project consists in a automatized Beowulf cluster installer with minimal setup.
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
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


This installer was started as a titulation project at Universidad de los Andes.


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
- edit /etc/ssh/sshd_config file and set PermitRootLogin yes
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

- edit the file /etc/ansible hosts according to the hosts example file, groups guineapig and master names must stay the same.
- Run
  ```sh
  ansible-galaxy collection install community.mysql
  ```
  ```sh
  ansible-playbook main.yml
  ```


