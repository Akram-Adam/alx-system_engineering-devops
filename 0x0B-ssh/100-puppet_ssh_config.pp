# set up your client SSH configuration file so that you can connect to a server without typing a password.
file { '/home/kira/.ssh/config':
  ensure => file,
  content => @("EOF"),
    Host myserver
      HostName 54.173.122.164  # Replace with your server's IP or hostname
      User ubuntu               # Replace with your server's username
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
    EOF,
  owner => 'kira',     # Replace with your username
  group => 'kira',     # Replace with your group if necessary
  mode => '0600',               # Ensure correct permissions on the file
}
