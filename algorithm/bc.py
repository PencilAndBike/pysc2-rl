# Copyright (c) 2018 horizon robotics. All rights reserved.
# Created by yingxiang.hong@horizon.ai on 2018/10/18.
#


from lib.base import BaseDeepAgent
from pysc2.agents.base_agent import BaseAgent as BaseSC2Agent


class BehaviorClone(BaseDeepAgent, BaseSC2Agent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._value = self._network['value']
        self._policies = self._network['policies']

    def init_network(self, *args, **kwargs):
        pass
