"""Example Load Platform integration."""
DOMAIN = 'lockuser'


def setup(hass, config):
    """Your controller/hub specific code."""

    hass.helpers.discovery.load_platform('switch', DOMAIN, {}, config)

    return True