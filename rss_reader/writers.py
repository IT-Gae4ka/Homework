from .rss_item import RssItem
from .utils import Console, date_to_str, NewsEncoder, open_cache_file_for_write
from abc import ABCMeta, abstractmethod
import csv
import logging
import html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


class Writer(metaclass=ABCMeta):
    """Abstract class with write method. Takes news."""
    @abstractmethod
    def write(self, news):
        """Abstract method for writing."""
        pass


class CacheWriter(Writer):
    """Writes cache from RssStorage object."""
    def write(self, news):
        logging.info('Running write() function. Class CacheWriter(Writer).')
        with open_cache_file_for_write() as f:
            csv_writer = csv.writer(f, delimiter=',')

            for item in news:
                csv_writer.writerow([item.title, date_to_str(item.date),
                                    item.link])


class JsonWriter(Writer):
    """Writes news into console in json format"""
    def write(self, news):
        logging.info('Running write() function. Class JsonWriter(Writer).')
        encoder = NewsEncoder(indent=2, ensure_ascii=False)
        with Console() as console:
            console.write(encoder.encode(list(news)))


class ConsoleWriter(Writer):
    """Writes news into console."""
    def write(self, news):
        logging.info('Running write() function. Class ConsoleWriter(Writer).')
        with Console() as console:
            for item in news:
                title = item.title
                date = date_to_str(item.date)
                link = item.link
                console.write(f"Title: {title}\n\nDate: {date}\n\nLink: {link}\n\n\
                --------------\n\n")


class DocumentWriter(Writer):
	"""Abstract class, which 
	has abstract methods: start_doc, end_doc,
	start_element, end_element, add_title, add_link, add_italic, save.
	And method write which writes news item by item."""
	@abstractmethod
	def start_doc(self):
		"""Determines the type of the document"""
		pass

	@abstractmethod
	def end_doc(self):
		"""Ends the document."""
		pass
		
	@abstractmethod
	def start_element(self):
		"""Starts new element"""
		pass
		
	@abstractmethod
	def end_element(self):
		"""Ends the element"""
		pass
		
	@abstractmethod
	def add_title(self, title):
		"""Adds title"""
		pass

	@abstractmethod
	def add_link(self, link):
		"""Adds link"""
		pass

	@abstractmethod
	def add_italic(self, date):
		"""Adds text in italic"""
		pass

	@abstractmethod
	def save(self):
		"""Opens file and writes info there."""
		pass

	def write(self, news):
		self.start_doc()

		for item in news:
			self.start_element()
			self.add_title(item.title)
			self.add_link(item.link)
			self.add_italic(date_to_str(item.date))
			self.end_element()

		self.end_doc()
		self.save()

class HtmlWriter(DocumentWriter):
	"""Class for writing in html doc."""
	def __init__(self):
		self._html = ''

	def start_doc(self):
		logging.info('Running start_doc() function. Class HtmlWriter(DocumentWriter).')
		self._html += '<!DOCTYPE html><html><ul>'

	def end_doc(self):
		logging.info('Running end_doc() function. Class HtmlWriter(DocumentWriter).')
		self._html += '</ul></html>'
		
	def start_element(self):
		logging.info('Running start_element() function. Class HtmlWriter(DocumentWriter).')
		self._html += '<li>'
		
	def end_element(self):
		logging.info('Running end_element() function. Class HtmlWriter(DocumentWriter).')
		self._html += '</li>'
		
	def add_title(self, title):
		logging.info('Running add_title() function. Class HtmlWriter(DocumentWriter).')
		self._html += '<h1>{}</h1>'.format(html.escape(title))

	def add_link(self, link):
		logging.info('Running add_link() function. Class HtmlWriter(DocumentWriter).')
		self._html += '<a href="{0}">{0}</a><br>'.format(html.escape(link))

	def add_italic(self, s):
		logging.info('Running add_italic() function. Class HtmlWriter(DocumentWriter).')
		self._html += '<i>{}</i><br>'.format(html.escape(s))	

	def save(self):
		logging.info('Running save() function. Class HtmlWriter(DocumentWriter).')
		with open('articles.html', 'w', newline='', encoding='utf-8') as f:
			f.write(self._html)


class PdfWriter(DocumentWriter):	
	def __init__(self):
		self._doc = []
		self._styles = getSampleStyleSheet()

	def start_doc(self):
		pass

	def end_doc(self):
		pass
		
	def start_element(self):
		self._doc.append(Spacer(1, 12))
		
	def end_element(self):
		self._doc.append(Spacer(1, 12))
		
	def add_title(self, title):
		self._doc.append(Paragraph(title, self._styles['Title']))

	def add_link(self, link):
		address = '<link href={0}>{0}</link>'.format(link)
		self._doc.append(Paragraph(address, ParagraphStyle('body')))

	def add_italic(self, s):
		self._doc.append(Paragraph(s, self._styles['Italic']))

	def save(self):
		doc = SimpleDocTemplate("articles.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
		doc.build(self._doc)