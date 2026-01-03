# home-assistant-block-user-switch
Exposes the Home Assistant User API as a Custom Component Switch Entity, so you can Lock and Unlock Users via Automation Scripts

The point of this is that if you want to prevent people from yelling into your Window and execute Alexa Home Assistant Commands, you can now use a separate Home Assistant User for linking with Alexa, and simply disable this user when you are not at Home, so any Alexa Requests during that time will experience an Authentication Failure, and Alexa will exclaim that she doesn't know what went wrong.

### Logout Issues - Update

**If you're having issues with being logged out of devices after Locking a User since the latest HA release:** 
**Update this custom integration to the latest version to fix it.**

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
      wallpaneluser:
        name: Wall UI Panel User
        unique_id: x98zx978z6xz9z6x96
```
You can find the Unique User ID at the Top of the User Administration settings for that user, where you would also manually disable the user.

The Switch State represents the User is_active State, so to lock the User turn the Switch off.
