ITERATION-1 

To run rss-reader write in console:
python rss_reader.py https://news.yahoo.com/rss/

Utility provides the following interface:

  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided

ABOUT JSON:
The number of news in json format depends on the --limit.

Stdout json structure:
	title
	date
	link

As an example of a SOURCE you may write:
	https://news.yahoo.com/rss/
	https://www.livemint.com/rss/politics

ITERATION-3

Cached news are kept in article.csv file.
News are written by function write of class CacheWriter (writers.py).
Cache structure:
	title
	date
	link