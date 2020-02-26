"""Hi! This is a pattern for creating your own site parser Lets have a look at
it!

Remember!
		Our command will check every pull request.
		You can't add more than one file with one
		class of a parser. In this file you can
		store any amount of classes and functions
		but:
				1) You are forbidden to run anything inside your file.
				2) File should contain only 1 (one) class which parrent is
						Finder class in file finder.py.
				3) Your parser shoud have a function 'search'
						with params `self` and `name`
						name is a string. It is a name of a user
						whom we are going to find.
				4) If it will very hard to understand what each function does
						we will close pull request with some message.
						WRITE COMMENTS AND EVERYTHING WILL BE OK

				5) You are forbidden to change files of other users.
						We will check your pull request for this
"""

from finder import Finder


'''
Place here name of your parser
It is important as we do not know which
name you gave to your parser
'''
__all__ = ['YourSiteParserClassName']

'''
So this is a main parser
Please check name of your parser
to avoid rewriting of other parser
or having any Exception.

Your function 'search' should return a dict
{
	'url' : str: 
				site you are trying to check.
				it can not be an url but name
				of the site you are checking
	'nickname' : str name we gave you as a param
	'found'    : bool: Have you found a user?
	
	any other fields...
	
	if we will need other keys in this
	 dict we will notify you
}

Enjoy!

'''


class YourSiteParserClassName(Finder):
	def __init__(self):
		self.url = 'https://example.com/'

	def search(self, name):
		response, data = self.get_site_data(self.url + name)
		return {
			'url': self.url,
			'nickname': name,
			'found': response == 200
		}
