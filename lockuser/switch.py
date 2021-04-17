"""
homeassistant.components.switch.lockuser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A switch that allows you to lock and unlock a Home Assistant User
"""

import threading
import time
import logging
import voluptuous as vol
from homeassistant.const import CONF_DEVICES, CONF_NAME, CONF_UNIQUE_ID
from homeassistant.components.switch import (
    SwitchEntity, PLATFORM_SCHEMA)
import homeassistant.helpers.config_validation as cv

from . import DOMAIN

DEVICE_SCHEMA = vol.Schema({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_UNIQUE_ID): cv.string
})

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_DEVICES, default={}): {cv.string: DEVICE_SCHEMA}
})

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """ Find and return objects """
    switches = []

    for device_id, device_config in config.get(CONF_DEVICES, {}).items():
        name = device_config[CONF_NAME]
        uid = device_config[CONF_UNIQUE_ID]
        user = await hass.auth.async_get_user(uid)
        switches.append(CustSwitch(name, device_id, hass, uid, user.is_active))
        _LOGGER.info("Added " + name)

    async_add_entities(switches)





class CustSwitch(SwitchEntity):
    """ Provides a Lock User Switch. """

    def __init__(self, name, device_id, hass, uid, state):
        self._name = name
        self._device_id = device_id
        self._state = state
        self.entity_id = "switch."+device_id
        self._hass = hass
        self._uid = uid

    @property
    def should_poll(self):
        """ No polling needed for this. """
        return False

    @property
    def unique_id(self):
        """ generate id. """
        return self._device_id

    @property
    def name(self):
        """ Returns the name of the object. """
        return self._name

    @property
    def is_on(self):
        """ True if the user is active. """
        return self._state

    async def async_turn_on(self, **kwargs):
        """ Enable the user. """
        self._state = True
        user = await self._hass.auth.async_get_user(self._uid)
        await self._hass.auth.async_update_user(user, is_active=True)
        self.async_schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        """ Disable the user. """
        self._state = False
        user = await self._hass.auth.async_get_user(self._uid)
        await self._hass.auth.async_update_user(user, is_active=False)
        self.async_schedule_update_ha_state()