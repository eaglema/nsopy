class Observable(object):
    """ Make object observable. """
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


class Observer(object):
    def update(self):
        """
        This method is called whenever an Observable object calls notify_observers()
        (usually when the Observable object changes state).
        """
        raise NotImplementedError()
