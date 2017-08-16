import logging
from django import template

logger = logging.getLogger('django')
register = template.Library()

class UrlNode(template.Node):
    def __init__(self, appname, funcname, *args):
        self.appname = appname
        self.funcname = funcname
        self.args = args

    def render(self, context):
        try:
            return web.func_url(self.appname, self.funcname,
                *[template.Variable(var).resolve(context) for var in self.args])
            #if web.request_if_secure(url):
            #    return u"https://%s%s" % (get_host(request), url)
        except:
            logger.exception('urly failed with params: %s, %s, %s', self.appname, self.funcname, self.args)

@register.tag
def urly(parser, token):
    """ Generate a link to the given func in given app, plus add arguments
        {% url agency agency_list arg1 arg2 %} """
    parts = token.split_contents()
    return UrlNode(*parts[1:])

