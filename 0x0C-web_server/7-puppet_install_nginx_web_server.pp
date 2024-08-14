# File:   7-puppet_install_nginx_web_server.pp
# Author: Akram Adam
# email:  <akramadam050@gmail.com>

# Using Puppet| Install Nginx server, setup and configuration 

class { 'nginx': 
  package_ensure => 'present',
  service_ensure => 'running',
  service_enable => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

nginx::resource::vhost { 'default':
  ensure   => present,
  listen_port => 80,
  www_root => '/var/www/html',
}

file { '/etc/nginx/conf.d/redirect.conf':
  ensure  => file,
  content => 'server {
                listen 80;
                location /redirect_me {
                  return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
                }
              }',
  notify  => Service['nginx'],
}
