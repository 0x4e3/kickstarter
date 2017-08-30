# Kickstarter

Set of console commands for running services for Django project deploy.  
Also proxies django CLI commands and allows to upgrade database.

Repository contains demo project named "kickstarter".

Use ```kickstarter --help``` for full list of commands.

Allows to run services:  
* gunicorn
* celery
* celery-beat

#### run
```kickstarter run web``` - runs gunicorn  
Available options:
* ```--bind``` - Gunicorn bind address in "ip:port" format
* ```--workers``` - The number of worker processes for handling requests
* ```--upgrade``` - Upgrade before starting
* ```--noinput``` - Do not prompt the user for input of any kind

```kickstarter run worker``` - runs celery workers
Available options:
* ```--hostname``` - Set custom hostname, e.g. \'w1.%h\'
* ```--concurrency``` - Number of child processes processing the queue. The default is the number of CPUs available on your system
* ```--logfile``` - Path to log file. If no logfile is specified, stderr is used
* ```--autoreload``` - Enable auto reloading

```kickstarter run beat``` - runs celery task dispatcher
Available options:
* ```--pidfile``` - Optional file used to store the process pid. The program will not start if this file already exists and the pid is still alive.
* ```--logfile``` - Path to log file. If no logfile is specified, stderr is used
* ```--autoreload``` - Enable auto reloading

#### django
Simple proxy command for the default Django CLI.

#### upgrade
Performs any pending database migrations and upgrades.
Available options:
* ```--verbosity``` - Set verbosity level
* ```--traceback``` - Raise on exception
* ```--no-input``` - Do not prompt the user for input of any kind