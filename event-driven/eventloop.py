import select


class Event:

    def fileno(self):
        raise NotImplemented("must implement")

    def receive_ready(self):
        return False

    def handle_receive(self):
        pass

    def send_ready(self):
        pass

    def handle_send(self):
        pass


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.receive_ready()]
        wants_send = [h for h in handlers if h.send_ready()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()
