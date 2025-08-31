AUTHOR = 'David Lemus'
SITENAME = "Jesus Lemus"
SITETITLE = "Jesus Lemus - Platform Engineer"
SITEDESCRIPTION = "A blog about technology and more."
SITEURL = ""

PATH = "content"
THEME = "themes/simple-dev"

DEFAULT_LANG = "en"

# Feed generation is usually desired
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Navigation menu
MENUITEMS = (
    ('Blog', '/'),
    ('About', '/pages/about.html'),
    ('Projects', '/pages/projects.html'),
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/your-username'),
    ('LinkedIn', 'https://linkedin.com/in/your-username'),
    ('Email', 'mailto:jesus.lemus.leal@gmail.com'),
)

# URL settings for static pages
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
