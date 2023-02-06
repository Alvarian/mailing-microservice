![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)
***
# Introduction
A bare minimal emailer service to one gmail account. I purposed it for backend logging from other applications like my portfolio.

## Getting Started
[Install python 3+](https://www.python.org/) and [pip](https://pypi.org/project/pip/) into your device. 

Run:
```
pip install -r requirements.txt
```

After setup is complete, copy local to new .env:
```
cp .env.local .env
```

[Go to the security section of your google account settings and generate a new app password.](https://myaccount.google.com/u/1/security?hl=en) Fill `EMAIL_U` with the email associated with the password you generated and `EMAIL_P` with the password itself in .env and begin the server:
```
python app.py
```

## Usage
When the app is running, make a post request to `/api/v1/mail/complaints` strictly in this shape:
```
{
  error: null or "STRING",
  warnings: [ANY]
}
```
As application/json in body. Check your gmail inbox.

## Troubleshoot
Have your email open to test if everything works. Go to emails.REST and hit send request on the top. 

# References
- Flask (https://flask.palletsprojects.com/en/2.2.x/)
- PyPi "email" (https://docs.python.org/3/library/email.html)
- Google Account (https://myaccount.google.com/u/1/security?hl=en)

:octocat:

<!-- https://dvj70ijwahy8c.cloudfront.net/logger-microservice/icon | [{"description": "Request accepts JSON in any format. The service uses this as body to send to email designation.", "image": "https://dvj70ijwahy8c.cloudfront.net/logger-microservice/slides/image_0"}, {"description": "Before response and sent to email, it waits 20 seconds to accumilate more possible logs in order to send in one shot.", "image": "https://dvj70ijwahy8c.cloudfront.net/logger-microservice/slides/image_1"}] -->


