# W205 exercize 2 readme
# By Mike Gruzynski

## Step 1
Need to start postgres. And create a database and dataframe - inputs:

__START_INPUTS_IN_AWS_TERMINAL_BELOW__:

cd /data/
./start_postgres.sh
psql --username=postgres
CREATE DATABASE Tcount;
\connect tcount;
CREATE TABLE tweetwordcount (word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);

__END_INPUTS_IN_AWS_TERMINAL__

Now hit on keyboard : Ctrl - D (twice) to exit from postgres

## Step 2

