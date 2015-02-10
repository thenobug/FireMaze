from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

import ConfigParser

configParser = ConfigParser.RawConfigParser()
configFilePath = r'wordpress.config'
configParser.read(configFilePath)

username = configParser.get('file', 'username')
password = configParser.get('file', 'password')

print username, password

wp = Client('https://thenobug.wordpress.com/xmlrpc.php', username, password)

post = WordPressPost()
post.title = 'RPC test'
post.content = 'Remote executed stuff'
post.terms_names = {
	'post_tag': ['test', 'testpost'],
	'category': ['automation', 'Tests']
}

post.post_status = 'publish'

wp.call(NewPost(post))


