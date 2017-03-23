from google.appengine.api import urlfetch
import webapp2
import urllib
import os

class Sheduler(webapp2.RequestHandler):
    def get(self):
        appId = os.environ.get('GCLOUD_PROJECT', 'n-a')

        try:
            response = urlfetch.fetch(
                url='https://us-central1-' + appId + '.cloudfunctions.net/cronEndpoint',
                payload=urllib.urlencode({'key': os.environ.get('CRON_API_KEY')}),
                method=urlfetch.POST,
                headers={'Content-Type': 'application/x-www-form-urlencoded'})

            self.response.set_status(response.status_code, response.content)

        except urlfetch.Error:
            self.response.set_status(500, 'Caught exception while calling cloud functions')


app = webapp2.WSGIApplication([('/cron', Sheduler)], debug=True)
