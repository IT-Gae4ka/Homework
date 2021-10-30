from rss_item import RssItem
import logging


class RssStorage:
    """Stores news in items"""
    def __init__(self, limit=None):
        self._items = []
        self._filters = []
        self._limit = limit

    def add_filter(self, filter):
        """Adds filter to new items of news"""
        logging.info('Running add_filter() function. Class RssStorage().')
        self._filters.append(filter)

    def add_news(self, news):
        """Adds news into storage.
        Taking into account filters and limit"""
        logging.info('Running add_news() function. Class RssStorage().')
        assert(isinstance(news, RssItem))

        if self.limit_reached():
            return False

        for filter in self._filters:
            if not filter.check_news(news):
                return False

        self._items.append(news)
        return True

    def get_news(self):
        """Gets news item by item"""
        logging.info('Running get_news() function. Class RssStorage().')
        for item in self._items:
            yield item

    def limit_reached(self):
        """Checks limit.Returns bool."""
        logging.info('Running limit_reached() function. Class RssStorage().')
        return self._limit is not None and len(self._items) >= self._limit
