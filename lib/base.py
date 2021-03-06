# Copyright (c) 2018 horizon robotics. All rights reserved.
# Created by yingxiang.hong@horizon.ai on 2018/10/18.
#
import tensorflow as tf


class Network(object):
    def __int__(self, inputs, network_creator, var_scope, name_scope=None, reuse=False):
        self._inputs = inputs
        self._var_scope = var_scope
        self._name_scope = name_scope
        self._network_creator = network_creator
        with tf.variable_scope(var_scope, reuse=reuse):
            if name_scope:
                with tf.name_scope(name_scope):
                    net = network_creator(inputs)
            else:
                net = network_creator(inputs)
        assert isinstance(net, dict)
        self._net = net

    def __getitem__(self, item):
        return self._net.get(item)

    def __call__(self, inputs):
        pass

    @property
    def inputs(self):
        return self._inputs

    @property
    def var_scope(self):
        return self._var_scope

    @property
    def name_scope(self):
        return self._name_scope


class NetworkUpdater(object):
    def __init__(self):
        super(NetworkUpdater, self).__init__()
        self.name = None

    def declare_update(self):
        raise NotImplementedError()

    def update(self, sess, *args, **kwargs):
        raise NotImplementedError()


class BaseDeepAgent(object):
    def __init__(self, *args, **kwargs):
        self._network = self.init_network(**kwargs)
        self._updater = self.init_updater(**kwargs)

    def init_network(self, *args, **kwargs):
        raise NotImplementedError()

    def init_updater(self, *args, **kwargs):
        raise NotImplementedError()

    def step(self, *args, **kwargs):
        raise NotImplementedError()

    def update(self, *args, **kwargs):
        raise NotImplementedError()

    @property
    def network(self):
        return self._network

    @property
    def updater(self):
        return self._updater
