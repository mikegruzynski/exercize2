import psycopg2
import sys

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

try:
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    print "Connected Successfully to psycopg2.connect"
    print "------------------------------------------"
    if len(sys.argv) == 2:
        input_list = sys.argv[1].split(",")

        if RepresentsInt(input_list[0]) == True & RepresentsInt(input_list[1]) == True:
            if int(input_list[0]) <= int(input_list[1]):
                cur.execute("SELECT word, count from Tweetwordcount WHERE count >= %s and count <= %s order by count desc;" %(input_list[0],input_list[1]))
                records = cur.fetchall()
                print "word : count"
                print "------------"
                for results in records:
                    print "%s : %s" %(results[0], results[1])
            else:
                print "first int needs to be equal or less to than the second int input, see below"
                print "python histogram.py 3,8"
        else:
            print "incorrect input types, this script requires to ints seperated by a comma, see below:"
            print "python histogram.py 3,8"

    else:
        print "Incorrect input: please refer to below:"
        print "python histogram.py 3,8"
    print "------------------------------------------"
    print "Your Query is done"
except:
    print "Problems with psycopg2.connect" 
