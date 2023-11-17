from core.conf.database import session
from core.models import Post
from sqlalchemy import func
import utils
import html
import markdown


def transliterate_str(title):
    """
        Return new key if it is not exists 
        and {key-{keys.count()}} if it exists.
    """
    
    key = utils.transliterate_title(title)

    key_count = session.query(Post).filter(
        func.lower(Post.key)
        .ilike(f"%{key.lower()}%")
    ).count()
    if key_count > 0:
        key = '%s-%s' % (key, key_count + 1)

    return key


def markdown_to_html(text):
    """ 
        Convert markdownV2 to 
        HTML and Shielding. 
    """
    
    return utils.add_tag_to_title(
        markdown.markdown(html.escape(text))
        .replace('\n', '<br>')
    )
