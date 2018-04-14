#!/bin/bash

file="accounts"

IFS=":"

mkdir /cmd
ln -s /bin/cat /cmd/cat
ln -s /usr/bin/find /cmd/find
ln -s /bin/ls /cmd/ls
ln -s /bin/passwd /cmd/passwd
ln -s /bin/pwd /cmd/pwd

while read user pass
do
        useradd -m ${user} -G GCTF -d /home/${user} -s /bin/rbash
        chpasswd <<< ${user}:${pass}
        echo 'alias cat="echo i have your cat"' > /home/${user}/.bashrc
        echo 'export PATH=/cmd' >> /home/${user}/.bashrc
        ln -s /GCTF/cat.flag /home/${user}/flag
        for i in {1..10}
        do
                for j in {1..10}
                do
                        for r in {1..10}
                        do
                                mkdir -p /home/$user/largedir/file$i/file$j/file$r/
                        done
                done
        done
        flagdir="/home/$user/largedir/file$(( (RANDOM % 10) + 1 ))/file$(( (RANDOM % 10) + 1 ))/file$(( (RANDOM % 10 ) + 1))/flag"
        sleep 5
        touch $flagdir
        echo GCTF{f1nd_is_m0r3_us3fu1_th4n_gr3p} > $flagdir
        chown -R ${user}:${user} /home/${user}

done < "${file}"

