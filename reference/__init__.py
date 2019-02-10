from flask import Flask, Markup
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

app = Flask(__name__)

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

mistune_markdown = mistune.Markdown(renderer=HighlightRenderer())

@app.template_filter('markdown')
def markdown(text, **options):
    return Markup(mistune_markdown(text, **options))

# All views must be imported after app creation
# TODO: Find a way to avoid circular imports
import reference.views
