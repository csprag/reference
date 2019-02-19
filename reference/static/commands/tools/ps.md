ps
-------
`ps`, or Processes Status, is used to print information about currently running processes to the terminal. In the output below, PID is the Process ID, TTY is the terminal of the process, TIME is the CPU time for the process, and CMD is the name of the executable. With no commands, `ps` prints all the processes that are associated with the same user ID as the current user.

~~~ bash
$ ps
PID TTY          TIME CMD
2158 pts/17   00:00:00 bash
2198 pts/17   00:00:00 ps
~~~

---

### Useful Options

#### ps -C

##### The -C flag will show only the processes listed after it. This command is useful when you only care about the status of a few processes. Separate each process in your list with either spaces or commas. For example, the command `ps -C bash` will print only the following:

~~~ bash
$ ps -C bash
PID TTY          TIME CMD
2158 pts/17   00:00:00 bash
~~~

#### ps -e

##### The -e or -A flags will show all the processes running, not just those associated with the current user as in the default `ps` command. The output for this command will vary greatly based on what processes are running, but follow the same format as the above command outputs.

#### ps -U

##### The -U flag will show only the processes run by the users listed after it. This command is useful when you only care about the statuses of some processes being run by a specific user. Separate each user in your list with either spaces or commas. For example, the command `ps -U root` will print the following (output will vary greatly):

~~~ bash
ps -U root
PID TTY          TIME CMD
1 ?        00:00:01 systemd
2 ?        00:00:00 kthreadd
4 ?        00:00:00 kworker/0:0H
6 ?        00:00:00 mm_percpu_wq
7 ?        00:00:00 ksoftirqd/0
8 ?        00:00:00 rcu_sched
9 ?        00:00:00 rcu_bh
10 ?        00:00:00 migration/0
11 ?        00:00:00 watchdog/0
12 ?        00:00:00 cpuhp/0
13 ?        00:00:00 kdevtmpfs
14 ?        00:00:00 netns
15 ?        00:00:00 rcu_tasks_kthre
16 ?        00:00:00 kauditd
17 ?        00:00:00 khungtaskd
18 ?        00:00:00 oom_reaper
19 ?        00:00:00 writeback
20 ?        00:00:00 kcompactd0
21 ?        00:00:00 ksmd
22 ?        00:00:00 khugepaged
23 ?        00:00:00 crypto
24 ?        00:00:00 kintegrityd
25 ?        00:00:00 kblockd
26 ?        00:00:00 ata_sff
27 ?        00:00:00 md
28 ?        00:00:00 edac-poller
29 ?        00:00:00 devfreq_wq
30 ?        00:00:00 watchdogd
32 ?        00:00:00 kworker/0:1
34 ?        00:00:01 kswapd0
35 ?        00:00:00 ecryptfs-kthrea
77 ?        00:00:00 kthrotld
78 ?        00:00:00 acpi_thermal_pm
79 ?        00:00:00 scsi_eh_0
80 ?        00:00:00 scsi_tmf_0
81 ?        00:00:00 scsi_eh_1
82 ?        00:00:00 scsi_tmf_1
88 ?        00:00:00 ipv6_addrconf
97 ?        00:00:00 kstrp
114 ?        00:00:00 charger_manager
156 ?        00:00:00 scsi_eh_2
157 ?        00:00:00 scsi_tmf_2
158 ?        00:00:00 ttm_swap
159 ?        00:00:00 irq/18-vmwgfx
161 ?        00:00:00 kworker/0:1H
183 ?        00:00:00 jbd2/sda1-8
184 ?        00:00:00 ext4-rsv-conver
219 ?        00:00:00 systemd-journal
233 ?        00:00:00 systemd-udevd
422 ?        00:00:00 iprt-VBoxWQueue
660 ?        00:00:00 systemd-logind
661 ?        00:00:00 accounts-daemon
682 ?        00:00:00 NetworkManager
683 ?        00:00:00 cron
697 ?        00:00:00 snapd
711 ?        00:00:00 acpid
713 ?        00:00:00 cupsd
763 ?        00:00:00 cups-browsed
767 ?        00:00:00 polkitd
1038 ?        00:00:00 VBoxClient
1039 ?        00:00:00 VBoxClient
1050 ?        00:00:00 lightdm
1065 ?        00:00:00 VBoxService
1073 tty7     00:00:25 Xorg
1076 tty1     00:00:00 agetty
1151 ?        00:00:00 lightdm
1230 ?        00:00:00 upowerd
1982 ?        00:00:00 udisksd
2636 ?        00:00:00 dhclient
2686 ?        00:00:00 kworker/0:0
2761 ?        00:00:00 kworker/u2:1
2795 ?        00:00:00 kworker/u2:0
2812 ?        00:00:00 kworker/u2:2
~~~
