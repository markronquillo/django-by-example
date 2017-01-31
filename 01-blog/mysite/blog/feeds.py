from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post


class LatestPostsFeed(Feed):
	"""
	First we subclass the Feed class of the syndication framework.
	The title, link and description correspond to the <title>, <link> and <description>
	RSS elements respectively


	"""

	title = 'My blog'
	link = '/blog/'
	description = 'New posts of my blog.'

	def items(self):
		return Post.published.all()[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return truncatewords(item.body, 30)
