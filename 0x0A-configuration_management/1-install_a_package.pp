# Install flask from pip
package { 'Flask':
    ensure   => '2.1.0',
    name     => 'flask',
    provider => 'pip3'
}