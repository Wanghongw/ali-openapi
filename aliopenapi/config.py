#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2020-03-21

import os
import json
import errno


class Config(dict):

    def __init__(self, defaults=None):
        dict.__init__(self, defaults or {})

    def from_json(self, filename, silent=False):
        """Updates the values in the config from a JSON file. This function
        behaves as if the JSON object was a dictionary and passed to the
        :meth:`from_mapping` function.

        :param filename: the filename of the JSON file.  This can either be an
                         absolute filename or a filename relative to the
                         root path.
        :param silent: set to ``True`` if you want silent failure for missing
                       files.

        """
        if not os.path.exists(filename):
            raise 'Unable to load configuration file path ({}) '.format(filename)

        try:
            with open(filename) as json_file:
                obj = json.loads(json_file.read())
        except IOError as e:
            if silent and e.errno in (errno.ENOENT, errno.EISDIR):
                return False
            e.strerror = 'Unable to load configuration file ({})'.format(e.strerror)
            raise
        return self.from_mapping(obj)

    def from_mapping(self, *mapping, **kwargs):
        """Updates the config like :meth:`update` ignoring items with non-upper
        keys.

        """
        mappings = []
        if len(mapping) == 1:
            if hasattr(mapping[0], "items"):
                mappings.append(mapping[0].items())
            else:
                mappings.append(mapping[0])
        elif len(mapping) > 1:
            raise TypeError(
                "expected at most 1 positional argument, got {}".format(len(mapping))
            )
        mappings.append(kwargs.items())
        for mapping in mappings:
            for (key, value) in mapping:
                if key.isupper():
                    self[key] = value
        return True

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, dict.__repr__(self))
