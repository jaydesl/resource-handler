#
# Copyright (C) 2014 MTA SZTAKI
#
# Unit tests for the SZTAKI Cloud Orchestrator
#

import occo.util as util
import occo.util.config as config
import occo.util.factory as factory
from ..cloudhandler import CloudHandler
import logging
import time
import random
import uuid

PROTOCOL_ID='dummy'

__all__ = ['DummyCloudHandler']

log = logging.getLogger('occo.cloudhandler.backends.dummy')

@factory.register(CloudHandler, PROTOCOL_ID)
class DummyCloudHandler(CloudHandler):
    def __init__(self, kvstore, **config):
        self.kvstore = kvstore
    def create_node(self, node_description):
        log.debug("[CH] Creating node: %r", node)
        time.sleep(3 + max(-2, random.normalvariate(0, 0.5)))
        uid = 'dummy_vm_{0}'.format(uuid.uuid4())
        self.kvstore[uid] = True
        log.debug("[CH] Done")
        return uid
    def drop_node(self, node_id):
        log.debug("[CH] Dropping node '%s'", node_id)
        time.sleep(2 + max(-2, random.normalvariate(0, 0.5)))
        self.kvstore[node_id] = False
        log.debug("[CH] Done")

    def get_node_state(self, node_id):
        return self.kvstore[node_id]
