# DRD Pi
#
# Software for a Raspberry Pi based DRD robot, controlled via the Web of Things.
# Copyright Ben Francis 2001

#import robohat
import logging
from webthing import (Action, Event, Property, SingleThing, Thing, Value,
                      WebThingServer)

def make_thing():
    thing = Thing(
        'urn:dev:ops:drd-pi-1812',
        'DRD Pi',
        [],
        'Raspberry Pi based Diagnostic Repair Drone'
    )

    return thing

def run_server():
    thing = make_thing()

    server = WebThingServer(SingleThing(thing), port=8080)
    try:
        logging.info('starting the server')
        server.start()
    except KeyboardInterrupt:
        logging.info('stopping the server')
        server.stop()
        logging.info('done')


if __name__ == '__main__':
    logging.basicConfig(
        level=10,
        format="%(asctime)s %(filename)s:%(lineno)s %(levelname)s %(message)s"
    )
    run_server()
