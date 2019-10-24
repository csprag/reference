cron
-------------

cron is a daemon or process which runs in the background.

Specifically, it allows the user to schedule predefined processes to run in the background at a regular interval of time.

cron repeatedly checks for when the scheduled time matches the current time, and then executes it's task once that condition is met.

cron [-f] [-l] [-n] [-L loglevel]

-f keeps the process in the foreground
-l enables LSB compliant names for cron.d files
-n adds the Fully Qualified Domain Name(FQDN) in the subject when sending email
-L loglevel tells cron what to log with the following modifications
-L 1 logs the start of all cron jobs
-L 2 logs the end of all cron jobs
-L 4 logs all the failed jobs. The exit status will be non-zero
-L 8 logs the process number of all the cron jobs
