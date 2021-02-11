import os
import smtplib
from email.message import EmailMessage

from flask_cors import CORS
from flask import Flask, request
app = Flask(__name__)
CORS(app)


@app.route("/api/v1/mail", methods=['post'])
def index():
	EMAIL_ADDRESS = os.environ.get('EMAIL_U');
	EMAIL_PASSWORD = os.environ.get('EMAIL_P');

	payload = request.get_json()
	
	msg = EmailMessage()
	msg['Subject'] = 'New message from my Portfolio'
	msg['From'] = payload['guestEmail']
	msg['To'] = EMAIL_ADDRESS
	msg.set_content("""\
		<html>
		  <head></head>
		  <body>
		    <p> <strong>Name:</strong> {sender_name} </p>
		    <p> <strong>Email:</strong> {sender_email} </p>
		   	<p> <strong>Message:</strong> {sender_body} </p>
		  </body>
		</html>
	""".format(
		sender_name=payload['guestName'],
		sender_email=payload['guestEmail'],
		sender_body=payload['guestInqury']
	), subtype='html')

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		smtp.send_message(msg)

	return "Ok"


if __name__ == '__main__':
	app.run(debug=False)