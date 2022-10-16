# Instructions
[Install python 3+](https://www.python.org/) and [pip](https://pypi.org/project/pip/) into your device. 

Run:
```bash
pip install -r requirements.txt
```

After setup is complete, copy local to new .env:
```bash
cp .env.local .env
```

[Go to the security section of your google account settings and generate a new app password.](https://myaccount.google.com/u/1/security?hl=en) Fill EMAIL_U with the email associated with the password you generated and EMAIL_P with the password itself in .env and begin the server:
```bash
python app.py
```

## Test
Have your email open to test if everything works. Go to emails.REST and hit send request on the top. 

:octocat:

<!-- https://dvj70ijwahy8c.cloudfront.net/logger-microservice/icon | [{"description": "Request accepts JSON in any format. The service uses this as body to send to email designation.", "image": "https://dvj70ijwahy8c.cloudfront.net/logger-microservice/slides/image_0"}, {"description": "Before response and sent to email, it waits 20 seconds to accumilate more possible logs in order to send in one shot.", "image": "https://dvj70ijwahy8c.cloudfront.net/logger-microservice/slides/image_1"}] -->


