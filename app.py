import os
import json

import smtplib
from threading import Timer

from email.message import EmailMessage
from flask_cors import CORS
import flask_cors
# flask_cors.cross_origin(["http://www.domain1.com"]) 

from flask import Flask, request
app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = os.environ.get('EMAIL_U')
EMAIL_PASSWORD = os.environ.get('EMAIL_P')

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
	msg = EmailMessage()

	def timeout_trigger_email(*ref_state):
		date = ref_state[0]['error'] and ''.join(e for e in ref_state[0]['error']['time'] if e.isalnum()) or len(ref_state[0]['warnings']) and ''.join(e for e in ref_state[0]['warnings'][0]['time'] if e.isalnum())
		filename = 'complaint_report_'+date+'.json'

		with open(filename, 'w') as f:
			json.dump(ref_state, f, indent=2)

		with open(filename, 'r') as readable_f:
			msg['Subject'] = 'NOTICE: Portfolio found '+str(len(ref_state))+' logs...'
			msg['From'] = 'norely_from_portfolio@gmail.com'
			msg['To'] = EMAIL_ADDRESS

			content = readable_f.read()
			
			msg.add_attachment(content, filename=filename)

		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
			smtp.send_message(msg)


		state.clear()
		print("New json file is created from data.json file", state)

	# push payload in state. if state is empty, set timer for 24 hours to send state as stringified notification
	if not len(state):
		state.append(payload)

		s = Timer(2.0, timeout_trigger_email, (state))

		s.start()
	else:
		state.append(payload)

	return "Ok"
	


if __name__ == '__main__':
	app.run(host="{}".format(os.environ.get('DEV_HOST') or '0.0.0.0'), debug=True)