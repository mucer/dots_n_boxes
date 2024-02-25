user=pi
pass=raspberry
host=192.168.254.36

sshpass $pass scp test.py $user@$host:/home/$user/pi