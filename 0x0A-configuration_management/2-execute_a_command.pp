
exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
