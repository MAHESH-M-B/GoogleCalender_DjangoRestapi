## Google Calendar API OAuth 2.0 for Web Server Applications Integration - Django Rest Framework

Problem: In this assignment you have to implement google calendar integration using django rest api. 
You need to use the OAuth2 mechanism to get users calendar access. Below are detail of API endpoint and corresponding views which you need to implement

For run this project on a local machine: 

```sh
pip install - r requriments.txt
```

- Endpoint:
```
/rest/v1/calendar/init/ -> GoogleCalendarInitView()
```
This view should start step 1 of the OAuth. Which will prompt user for his/her credentials

```
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
```
This view will do two things
1. Handle redirect request sent by google with code for token. You
need to implement mechanism to get access_token from given
code
2. Once got the access_token get list of events in users calendar

### Note: To run this assignment need google account credentials which need to save in the project directory and add a redirect URL in your google cloud. Please read below documents and references section.

## Documents and References

| Name | Sources |
| ------ | ------ |
| Google Identity: Using OAuth 2.0 for Web Server Applications | [/identity/protocols/oauth2/web-server][PlDb] |
| Google Calendar API | [/calendar/api/v3/referenc][PlGh] |
| Google Account Credentials| [/identity/protocols/oauth2/web-server#exchange-authorization-code][PlIa] |


[PlDb]: <https://developers.google.com/identity/protocols/oauth2/web-server>
[PlGh]: <https://developers.google.com/calendar/api/v3/reference>
[PlIa]: <https://developers.google.com/identity/protocols/oauth2/web-server#exchange-authorization-codee>
"# GoogleCalender_DjangoRestapi" 
