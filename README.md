# home-assistant-block-user-switch
Exposes the Home Assistant User API as a Custom Component Switch Entity, so you can Lock and Unlock Users via Automation Scripts

The point of this is that if you want to prevent people from yelling into your Window and give Alexa Home Assistant Commands, you can now use a separate Home Assistant User for linking with Alexa, and simply disable this user when you are not at Home, so any Alexa Requests during that time will experience an Authentication Failure, and Alexa will exclaim that she doesn't know what went wrong.

## Installation

Copy the `lockuser` folder into your `config/custom_components` directory.

## Configuration

Add the following to your configuration.yaml:
```
switch:
  - platform: lockuser
    devices:
      alexauser:
        name: Alexa User
        unique_id: 394578729384759384
```
You can find the Unique User ID at the Top of the User Administration settings for that user, where you would also manually disable the user.
