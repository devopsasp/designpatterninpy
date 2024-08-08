# Handler interface
class Handler:
    def set_next(self, handler):
        self.next = handler

    def handle(self, request):
        if hasattr(self, 'next'):
            self.next.handle(request)


# Concrete handlers
class HandlerA(Handler):
    def handle(self, request):
        if request == 'A':
            print('Handler A handled the request')
        else:
            super().handle(request)


class HandlerB(Handler):
    def handle(self, request):
        if request == 'B':
            print('Handler B handled the request')
        else:
            super().handle(request)


class HandlerC(Handler):
    def handle(self, request):
        if request == 'C':
            print('Handler C handled the request')
        else:
            print('No handler found for the request')


# Client code
handler_a = HandlerA()
handler_b = HandlerB()
handler_c = HandlerC()

handler_a.set_next(handler_b)
handler_b.set_next(handler_c)

handler_a.handle('A')  # Handler A handled the request
handler_a.handle('B')  # Handler B handled the request
handler_a.handle('C')  # Handler C handled the request
handler_a.handle('D')  # No handler found for the request