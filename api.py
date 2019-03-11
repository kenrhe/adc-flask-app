import sendgrid
import os
from sendgrid.helpers.mail import *

# If you are on OSX with Python3.6, run /Applications/Python\ 3.6/Install\ Certificates.command to bypass any SSL issues when running.

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("kaleo.sato@gmail.com")
to_email = Email("kaleo.sato@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
