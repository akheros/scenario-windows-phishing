#!/usr/bin/env python2
# -*- coding: UTF8 -*-
# Copyright (c) 2015, Nicolas VERDIER (contact@n1nj4.eu)
# Pupy is under the BSD 3-Clause license. see the LICENSE file at the root of the project for the detailed licence terms
import datetime
from pupylib.utils.decorators import threaded
import logging
import sys

# triggers and get executed at each client connection
@threaded
def on_connect(client):
    for action, command in client.pupsrv.config.items("on_connect"):
        if action=="run_module":
            for cmd in command.split('\n'):
                args=cmd.split()
                module_name=args.pop(0)
                for i in range(len(args)):
                    if args[i].startswith("'"):
                        args[i] = ' '.join(args[i:])
                        if i+1 < len(args):
                            del args[i+1:]
                        break
                job=client.run_module(module_name, args)
                job.wait()
                client.pupsrv.handler.display_srvinfo("on_connect: %s %s"%(module_name, ' '.join(args)))
        else:
            logging.warning("unknown action %s in pupy.conf [on_connect]"%action)



