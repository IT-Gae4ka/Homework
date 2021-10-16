from bs4 import BeautifulSoup
import requests
from interface import args
import json
from interface import logger


url_input = args.source
url = requests.get(url_input)
soup = BeautifulSoup(url.content, 'xml')


class Parser():
    """ Parses info from url"""
    def __init__(self, soup, limit):
        """ Needs xml object and int for number of news to display"""
        logger.info('Running __init__ function')
        self.soup = soup
        self.limit = limit

    def check_limit(self):
        """Checks limit input"""
        logger.info('Running check_limit function')
        if self.limit == -1:
            self.limit = self.count_news_amount()
        if self.limit > self.count_news_amount():
            self.limit = self.count_news_amount()
        else:
            pass
        return self.limit 
            

    def count_news_amount(self):
        """Counts the amount of news"""
        logger.info('Running count_news_amount function')
        self.items = self.soup.find_all('item')
        self.news_amount = 0
        for self.item in self.items:
            self.news_amount += 1
        return self.news_amount

    def check_output_channel_cmd(self):
        """Checks json input and returns where to print news in bool type.
        if True in cmd, if Fals in json file"""
        logger.info('Running check_output_channel_cmd function')
        if args.json:
            self.output_channel_cmd = False 
        else:
            self.output_channel_cmd = True
        return self.output_channel_cmd


    
    def print_items_in_cmd_line(self):
        """Prints news in command line"""
        logger.info('Running print_items_in_cmd_line function')
        self.items = self.soup.find_all('item')
        self.check_limit()
        self.check_output_channel_cmd()
        if self.output_channel_cmd == True:
            counter = 0
            for self.item in self.items:
                if counter < self.limit:
                    self.title = self.item.title.text
                    self.date = self.item.pubDate.text
                    self.link = self.item.link.text
                    print(f"Title: {self.title}\n\nDate: {self.date}\n\nLink: {self.link}\n\n ---------------------\n\n")
                    counter += 1
                else:
                    break
        else:
            self.collect_items_for_json_file()
            self.write_items_in_json_file()

    def collect_items_for_json_file(self):
        """Collects news in list, number depends on limit"""
        logger.info('Running collect_items_for_json_file function')
        self.items = self.soup.find_all('item')
        self.check_limit()
        counter = 0
        self.items_list = []
        for self.item in self.items:
            if counter < self.limit:
                self.title = self.item.title.text
                self.date = self.item.pubDate.text
                self.link = self.item.link.text
                self.item_data = {'title': self.title, 'date': self.date, 'link': self.link}
                self.items_list.append(self.item_data)
                counter += 1
        return self.items_list

    def write_items_in_json_file(self):
        """Writes news in json file"""
        logger.debug('Running write_items_in_json_file function')
        self.collect_items_for_json_file()
        with open('json_news.json', 'w') as f:
            json.dump(self.items_list, f, indent = 2)

parser = Parser(soup, args.limit)
if args.source:
    parser.print_items_in_cmd_line()