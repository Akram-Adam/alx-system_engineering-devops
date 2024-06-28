# kill process killmenow

exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
  onlyif => 'pgrep killmenow',
}
