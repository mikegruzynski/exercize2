from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]        

        conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
        cur = conn.cursor()
        if self.counts[word] == 0:
            self.counts[word] += 1 #Increament the local count
            string = cur.mogrify("INSERT INTO Tweetwordcount VALUES (%s, %s)", (word, 1))
            cur.execute(string)
            conn.commit()
        else:
            self.counts[word] += 1 # Increment the local count
            string = cur.mogrify("UPDATE Tweetwordcount SET count=%s WHERE word=%s",(self.counts[word], word))
            cur.execute(string)
            conn.commit()

        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

