AUTHOR = 'David Lemus'
SITENAME = "Jesus Lemus"
SITETITLE = "Jesus Lemus - Platform Engineer"
SITESUBTITLE = "Platform Engineer"
SITEDESCRIPTION = "A blog about technology and more."
SITEURL = ""

PATH = "content"
THEME = "themes/simple-dev"

DEFAULT_LANG = "en"

# Feed generation is usually desired
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Navigation menu
MENUITEMS = (
    ('Blog', '/blog/'),
    ('About', '/pages/about.html'),
    ('Projects', '/pages/projects.html'),
)

# Social widget
GITHUB_USERNAME = 'your-username'
SOCIAL = (
    ('GitHub', f'https://github.com/{GITHUB_USERNAME}'),
    ('LinkedIn', 'https://linkedin.com/in/your-username'),
    ('Email', 'mailto:jesus.lemus.leal@gmail.com'),
)

# Tell Pelican to use a page for the homepage and move the article list
INDEX_SAVE_AS = 'blog.html' # /themes/simple-dev/templates/index.html

# URL settings for static pages
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = './{slug}.html'
