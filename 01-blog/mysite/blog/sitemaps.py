from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
	"""
	We create a custom sitemap by inheriting the Sitemap class of the sitemaps module

	changefreq and priority attributes indicatehe change frequency of your post pages and 
		their relevance in your website

	https://docs.djangoproject.com/en/1.10/ref/contrib/sitemaps/
	"""
	changefreq = 'weekly'
	priority = 0.9

	def items(self):
		return Post.published.all()

	def lastmod(self, obj):
		"""
		The lastmod method receives each object returned by items()
		and returns the last time the object was modified
		"""
		return obj.publish
