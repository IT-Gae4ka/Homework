from . import rss_storage, parsers, writers, filters
from .interface import args
import logging


class RssReader():
    """Reads news from RssStorage. Takes arguments
    source, limit, date, json from interface."""
    def __init__(self, source, limit, date, output_format):
        self._source = source
        self._limit = limit
        self._date = date
        self._format = output_format

    def read_news(self):
        """Checks the arguments inputed by user.
        Creates object storage from RssStorage.
        Depending on the arguments uses SourceFilter or DateFilter
        to add news into storage.
        If source, takes news from WebRssParser,
        if date - from CacheRssParser.
        if json, uses JsonWriter to print into console, else - ConsoleWriter.
        Takes into account limit argument while adding news into storage."""
        logging.info('Running read_news() function. Class RssReader().')
        storage = rss_storage.RssStorage(self._limit)
        got_from_cache = False

        if self._source:
            storage.add_filter(filters.SourceFilter(self._source))
        elif not self._date:
            print('Must define source or date.')
            return

        if self._date:
            storage.add_filter(filters.DateFilter(self._date))
            cache_parser = parsers.CacheRssParser()

            for news in cache_parser.read_news():
                if storage.add_news(news):
                    got_from_cache = True
                    if storage.limit_reached():
                        break

        if not got_from_cache:
            if not self._source:
                return

            parser = parsers.WebRssParser(self._source)
            for news in parser.read_news():
                if storage.add_news(news) and storage.limit_reached():
                    break

            cache_writer = writers.CacheWriter()
            cache_writer.write(storage.get_news())

        writers_by_format = {'json': writers.JsonWriter, 'console': writers.ConsoleWriter,
            'html': writers.HtmlWriter, 'pdf': writers.PdfWriter}
        writer = writers_by_format[self._format]()
        writer.write(storage.get_news())


def main():
    """Creates object of RssReader class.
    Calls method read_news."""
    logging.info('Running main() function. Class RssReader().')
    if args.json:
        output_format = 'json'
    elif args.html:
        output_format = 'html'
    elif args.pdf:
        output_format = 'pdf'
    else:
        output_format = 'console'
        
    parser_4 = RssReader(args.source, args.limit, args.date, output_format)
    parser_4.read_news()


if __name__ == '__main__':
    main()
