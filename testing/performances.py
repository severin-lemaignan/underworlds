#! /usr/bin/env python

import argparse
import time
import uuid

from multiprocessing import Pool
import threading
from concurrent.futures import ThreadPoolExecutor

import logging; logger = logging.getLogger("underworlds.testing.performances")

import underworlds
import underworlds.server
from underworlds.types import Node
from underworlds.helpers.profile import profileonce
import underworlds.underworlds_pb2 as gRPC

def ms(duration):
    return "%.1fms" % (duration * 1000)


def passthrough(world1, world2):
    """ Simple passthrough filter: wait for changes on a world world1 and
    propagate these changes to world world2.
    """

    client_id = str(uuid.uuid4())
    print("Hello, I'm client %s!" % client_id)
    with underworlds.Context("client_%s" % client_id) as ctx:

        world1 = ctx.worlds[world1]
        world2 = ctx.worlds[world2]

        try:
            print("Waiting for changes...")
            while True:
                change = world1.scene.waitforchanges(0.5)
                if change is not None:
                    id, op = change
                    print("%f -- Propagating from %s to %s" % (time.time(), world1, world2))
                    world2.scene.update_and_propagate(world1.scene.nodes[id])
        except Exception as e:
            import traceback
            traceback.print_exc()
        print("Stopping passthrough")


def wait_for_changes(world):

    print("Waiting for changes in world %s" % world)

    starttime = time.time()

    change = world.scene.waitforchanges(5)
    profileonce("waitforchanges triggered")
    return change, time.time()-starttime



    
def test_propagation_time(nb_worlds):

    executor = ThreadPoolExecutor(max_workers=nb_worlds)
    pool = Pool(nb_worlds)

    res = []
    for i in range(nb_worlds-1):
        print("Setting up passthrough between world %d and world %d" % (i, i+1))
        #f = executor.submit(passthrough, "world%d" % i, "world%d" % (i+1))
        res.append(pool.apply_async(passthrough, ["world%d" % i, "world%d" % (i+1)]))

    time.sleep(0.5)

    ctx = underworlds.Context("test_client")
    entry_world = ctx.worlds["world0"]
    exit_world = ctx.worlds["world%d" % (nb_worlds-1)]

    future = executor.submit(wait_for_changes, exit_world)

    n = Node()
    n.name = "test"

    print("\n\n\nPropagating a change from world %s..." % entry_world)
    profileonce("start test with %d worlds" % nb_worlds)

    starttime=time.time()

    entry_world.scene.append_and_propagate(n)

    change, duration = future.result()

    profileonce("end test")

    print("It took %s to be notified of the change in world %s" % (ms(duration), exit_world))

    if change is None:
        raise RuntimeError("The change has not been seen!")

    print("Total time: %.2f" % ((time.time() - starttime) * 1000))

    executor.shutdown(wait=True)
    pool.terminate()
    pool.join()
    ctx.close()

    return duration

if __name__ == '__main__':
    durations = []

    parser = argparse.ArgumentParser()
    parser.add_argument("maxworlds", default=5, type=int, nargs="?", help="Maximum number of Underworlds worlds to spawn")
    parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
    parser.add_argument("-dd", "--fulldebug", help="debug mode (verbose)", action="store_true")
    parser.add_argument("-i", "--incremental", action="store_true", help="test for every nb of worlds, from 2 to maxworlds")
    args = parser.parse_args()

    if args.debug or args.fulldebug:
        if args.fulldebug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)
    else:
        logger.setLevel(logging.WARN)

    minworlds = 2 if args.incremental else args.maxworlds

    for nb in range(minworlds, args.maxworlds+1):
        print("\n\n\n-- %d worlds --\n" % nb)

        server = underworlds.server.start()
        time.sleep(0.2) # leave some time to the server to start

        durations.append(test_propagation_time(nb))
        server.stop(0)
        time.sleep(0.2)

        for d in durations:
            print("%.1f" % (d * 1000))

