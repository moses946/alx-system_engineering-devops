# Install flask from pip
package { 'flask-install':
    ensure   => '2.1.0',
    name     => flask,
    provider => pip3
}