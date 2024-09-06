"""Example Load Platform integration."""
DOMAIN = 'lockuser'
from homeassistant.helpers.discovery import load_platform

def setup(hass, config):
    """Your controller/hub specific code."""

    load_platform(hass, 'switch', DOMAIN, {}, config)

    return True