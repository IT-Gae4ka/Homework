import rss_storage
import parsers
import writers
import filters
from interface import args
import logging


class RssReader():
    """Reads news from RssStorage. Takes arguments
    source, limit, date, json from interface."""
    def __init__(self, source, limit, json):
        self._source = source
        self._limit = limit
        self._json = json

    def read_news(self):
        """Checks the arguments inputed by user
        Creates object storage from RssStorage.
        Depending on the arguments uses SourceFilter or DateFilter
        to add news into storage.
        If source, takes news from WebRssParser,
        if json, uses JsonWriter to print into console, else - ConsoleWriter.
        Takes into account limit argument while adding news into storage."""
        logging.info('Running read_news() function. Class RssReader().')
        storage = rss_storage.RssStorage(self._limit)
        got_from_cache = False

        if self._source:
            storage.add_filter(filters.SourceFilter(self._source))
        else:
            print('Must define source.')
            return

        parser = parsers.WebRssParser(self._source)
        for news in parser.read_news():
            if storage.add_news(news) and storage.limit_reached():
                break

        writer = writers.JsonWriter() if self._json else writers.ConsoleWriter()
        writer.write(storage.get_news())


def main():
    """Creates object of RssReader class.
    Calls method read_news."""
    logging.info('Running main() function. Class RssReader().')
    parser_1 = RssReader(args.source, args.limit, args.json)
    parser_1.read_news()


if __name__ == '__main__':
    main()
