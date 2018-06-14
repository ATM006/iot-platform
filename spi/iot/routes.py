# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.spi_devices_hardwareId_events_UserCommands import SpiDevicesHardwareidEventsUsercommands
from .api.spi_devices_hardwareId_events_DevicesData import SpiDevicesHardwareidEventsDevicesdata
from .api.spi_tenants_tenantId import SpiTenantsTenantid
from .api.spi_users_username import SpiUsersUsername
from .api.spi_sites_token import SpiSitesToken
from .api.spi_sites import SpiSites
from .api.spi_devices_hardwareId import SpiDevicesHardwareid
from .api.spi_devices import SpiDevices
from .api.spi_tenants import SpiTenants
from .api.spi_users import SpiUsers


routes = [
    dict(resource=SpiDevicesHardwareidEventsUsercommands, urls=['/spi/devices/<hardwareId>/events/UserCommands'], endpoint='spi_devices_hardwareId_events_UserCommands'),
    dict(resource=SpiDevicesHardwareidEventsDevicesdata, urls=['/spi/devices/<hardwareId>/events/DevicesData'], endpoint='spi_devices_hardwareId_events_DevicesData'),
    dict(resource=SpiTenantsTenantid, urls=['/spi/tenants/<tenantId>'], endpoint='spi_tenants_tenantId'),
    dict(resource=SpiUsersUsername, urls=['/spi/users/<username>'], endpoint='spi_users_username'),
    dict(resource=SpiSitesToken, urls=['/spi/sites/<token>'], endpoint='spi_sites_token'),
    dict(resource=SpiSites, urls=['/spi/sites'], endpoint='spi_sites'),
    dict(resource=SpiDevicesHardwareid, urls=['/spi/devices/<hardwareId>'], endpoint='spi_devices_hardwareId'),
    dict(resource=SpiDevices, urls=['/spi/devices'], endpoint='spi_devices'),
    dict(resource=SpiTenants, urls=['/spi/tenants'], endpoint='spi_tenants'),
    dict(resource=SpiUsers, urls=['/spi/users'], endpoint='spi_users'),
]