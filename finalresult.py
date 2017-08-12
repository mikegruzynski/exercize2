import psycopg2
import sys

try:
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    print "Connected Successfully to psycopg2.connect"
    print "------------------------------------------"
    if len(sys.argv) > 1:
        list_word = sys.argv[1:]
        for word in list_word:
            cur.execute("SELECT word, count from Tweetwordcount WHERE word = '%s';" %word)
            result = cur.fetchone()
            if result is not None:
                print "Total number of occurences of \"%s\": %s" %(result[0], result[1])
            else:
                print "Total number of occurences of \"%s\": %s" %(word, 0)
    else:
        cur.execute("SELECT word, count from Tweetwordcount order by word asc")
        records = cur.fetchall()
        for word in records:
            print "(%s, %s)" %(word[0], word[1])
    print "------------------------------------------"
    print "Your Query is done"
    conn.commit()
    conn.close()
except:
    print "Problems with psycopg2.connect"
 