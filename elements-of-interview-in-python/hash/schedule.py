import collections


Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    E = [Endpoint(e.start, True) for e in A]
    E += [Endpoint(e.finish, False) for e in A]

    E.sort(key=lambda e: (e.time, not e.is_start))

    max_events, num_events = 0, 0
    for e in E:
        if e.is_start:
            num_events += 1
            max_events = max(num_events, max_events)
        else:
            num_events -= 1
    return max_events
