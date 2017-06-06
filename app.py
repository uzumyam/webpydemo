import web
import view, config
from view import render

urls = (
    '/', 'Index'
)

class Index:
    def GET(self):
        print render.base(view.listing())

if __name__ == '__main__':
    web.run(urls, globals(), *config.middleware)