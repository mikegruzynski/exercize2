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
when satisfied with amount of data stremed from the twitter application hit ctrl + c to end the stream of data
