import urllib
from manage import *
import query

class ShowHandler(AdminBaseHandler):

    def get(self, email):
        email = str(urllib.unquote(email))
        applicant, application = query.get_application_by_email(email)

        template_values = {
            'applicant': applicant,
            'application': application,
            'admin_url': '/admin/show/' + email
        }
        self.render_template('admin-show.html', template_values)
