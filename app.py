import os
import json

import smtplib
import atexit
from threading import Timer

from email.message import EmailMessage
from flask_cors import CORS
from flask import Flask, request
app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = os.environ.get('EMAIL_U');
EMAIL_PASSWORD = os.environ.get('EMAIL_P');

state = []


@app.route("/api/v1/mail/message", methods=['post'])
def post_message():
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

@app.route("/api/v1/mail/complaints", methods=['post'])
def post_complains():
	payload = request.get_json()

	print(not len(state), len(state))
	def timeout_trigger_email(*ref_state):
		with open('complaints_payload.json', 'w') as f:
			json.dump(ref_state, f, indent=2)
			state.clear()
			print("New json file is created from data.json file", state)

	# push payload in state. if state is empty, set timer for 24 hours to send state as stringified notification
	if not len(state):
		print("trigger called")
		state.append(payload)

		s = Timer(2.0, timeout_trigger_email, (state))

		s.start()
	else:
		state.append(payload)

	return "Ok"
	


if __name__ == '__main__':
	app.run(host="{}".format(os.environ.get('DEV_HOST') or '0.0.0.0'), debug=True)