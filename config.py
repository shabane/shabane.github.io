"""config of the site goes here.

read the full doc to make True decisions; https://shabane.github.io/carbon/configs
"""

# [Theme]
DIR = "theme/carbon_default"
BASE = "base.html"
CLICK_TO_OPEN = "click_to_open.html"
REDIRECT_ON_OPEN = "redirect.html"
INDEX = "index.html"

# [Deployment]
BASE_URL = "https://shabane.github.io/"
PUBLISH_DIR = "docs"
MAX_URL_LENGTH = 4  # 36 ^ 4 = 1,679,616 possible addresses for each url
CHARS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
]  # contain 36 chars
