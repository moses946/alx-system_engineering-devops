<h3 align="center">Networking basics #1</h3>
---

<p align="center"> This project contains solutions to quizzes for networking basics for the ALX Software Engineering course.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

The focus of this project is to solve basic networking questions after meeting the following learning objectives:
    
    What is localhost/127.0.0.1
    What is 0.0.0.0
    What is /etc/hosts
    How to display your machine’s active network interfaces

## 🎈 Usage <a name="usage"></a>

Clone the repository to your machine.
Files ``0-change_your_home_IP`` and  ``1-show_attached_IPs`` are executable.

The file ``0-change_your_home_IP`` configures a machine to resolve ``localhost`` to ``127.0.0.2`` and ``facebook.com`` to ``8.8.8.8``

```
 ./0-change_your_home_IP
```

<strong> ❗ Be sure to revert changes to the hosts file after running this file.</strong>

To Display all active IPv4 IPs on your machine run:
```
./1-show_attached_IPs
```

To have your local machine listen on port 98 on localhost:

```
./100-port_listening_on_localohost
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Bash](https://www.gnu.org/software/bash/)

## ✍️ Authors <a name = "authors"></a>

- [@mosesmwai](https://github.com/moses946) - Initial work

