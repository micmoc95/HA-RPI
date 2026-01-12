from __future__ import annotations

import aiohttp
from homeassistant.core import ServiceCall, callback

async def async_setup(hass, config):
    @callback
    async def dial(call: ServiceCall):
        async with aiohttp.ClientSession() as s:
            await s.post("http://127.0.0.1:8124/dial", json={"num": call.data ["num"]})
    hass.services.async_register("hadialer", "dial", dial)
    return True
