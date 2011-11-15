# RequestHandler that handles all tasks
#

"""
RequestHandler that deals with tasks introduction, presentation, errors ans successes
"""

from google.appengine.ext import webapp

class TaskHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write('oi ')

