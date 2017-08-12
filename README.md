# W205 exercize 2 readme
# By Mike Gruzynski

## Step 1
Need to start postgres. And create a database and dataframe - inputs:

__START_INPUTS_IN_AWS_TERMINAL_BELOW__:

```
cd /data/
./start_postgres.sh
psql --username=postgres
CREATE DATABASE Tcount;
\connect tcount;
CREATE TABLE tweetwordcount (word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);
```
__END_INPUTS_IN_AWS_TERMINAL__

Now hit on keyboard : Ctrl - D (twice) to exit from postgres

## Step 2
Grab github repository and move it into AWS.

__START_INPUTS_IN_AWS_TERMINAL_BELOW__:
```
mkdir ex2_gruzynski
cd ex2_gruzynski/
git clone https://github.com/mikegruzynski/exercize2.git
cd exercize2/
chmod +x *.py
cd extweetwordcount/
sparse run
```
__END_INPUTS_IN_AWS_TERMINAL__

* NOTE after you input sparse run, you will need to hit enter to start the streaming app (SEE BELOW)
```
[root@ip-172-31-42-221 extweetwordcount]# sparse run
Running wordcount topology...
Routing Python logging to /root/ex2_gruzynski/exercize2/extweetwordcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/wordcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/ex2_gruzynski/exercize2/extweetwordcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

```

when satisfied with amount of data stremed from the twitter application hit ctrl + c to end the stream of data
