# SSH ESSENTIALS

This project contains the basics of using ssh to connect to servers.
The most common way of connecting to a remote Linux server is through SSH.SSH stands for Secure Shell and provides a safe and secure way of executing commands, making changes, and configuring services remotely. When you connect through SSH, you log in using an account that exists on the remote server.

## About 

Along with this project, there is an Ubuntu server that will be connected to while running the bash scripts. To access the server, you have to use the RSA key if authorized.

## Tasks

#### Use a private key
Use ssh to connect to the server using the private key `~/.ssh/school` with the user `ubuntu`.

#### Create an SSH key pair
Bash script that creates an RSA key pair stored in the file `school`, with `4096` bits and protected with a passphrase `betty`.

#### Client configuration file
An ssh-client_configuration file that is configured to refuse password authentication and uses the private key `~/.ssh/school`

#### Client configuration file (with Puppet)
Apply client configuration using Puppet.

