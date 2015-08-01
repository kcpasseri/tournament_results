Udacity's FSND Project 2, Tournament Results
----------------------------------------------------------------------
Prerequisites:
-Ensure VirtualBox, Vagrant, and Git Shell are all installed.
-Ensure the 'vagrant' folder is stored locally on your machine.
 
Instructions:
-Navigate to the 'vagrant' folder using Git Shell (or other Git terminal)
-Run vagrant with command 'vagrant up'
-SSH into the virtual machine with command 'vagrant ssh'
-Navigate to the tournament directory with command 'cd /vagrant/tournament/'
-Run 'psql' to use the psql prompt
-Run '\i tournament.sql'
-Run '\q' to exit psql prompt
-Finally, run 'python tournament_test.py' to test the program.

***NOTE: Do not include the 'single quotes' around commands!