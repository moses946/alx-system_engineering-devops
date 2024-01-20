# Configuration Management

## About 

This project contains a set of tasks to familiarize with basic syntax of puppet configuration management.

As a broader subject, configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management.

## Requirements

* All files should be intepreted on Ubuntu
* All files should end with a newline.
* A README.md should be present at the root of the project folder.
* All puppet manifests must pass puppet-lint.
* All manifests must start with a comment explaining what the manifest does.

## Tasks

#### Create a file.

Using puppet, create a file in /tmp

* File path is /tmp/school
* File permision is 0744
* File owner is www-data
* File group is www-data
* File contains I love Puppet

#### Install a package

Using puppet, install flask from pip3

* Flask version must be 2.1.0


#### Execute a command

Using puppet, create a manifest that kills a process named killmenow.

* Use the exec Puppet resource.
* Use pkill to end process.