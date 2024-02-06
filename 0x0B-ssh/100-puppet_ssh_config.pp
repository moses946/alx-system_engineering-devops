# Puppet file that creates a client config file for ssh.

file { "/etc/ssh/ssh_config":
	ensure => file,
	content => "
		Host *
		   IdentityFile ~/.ssh/school
		   PasswordAuthentication no
	",
}
