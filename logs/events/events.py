class Events(object):
    def __init__(self):
        self.events = {}
        '''
        events:
        {
            'event_name': {
                2: <func1>,
                0: <func2>,
                5: <func3>,
                'priorities': [5, 2, 0]   <-- sorted when subscribing, for faster access
            },
            'second_event_name': {
                ...
            }
        }
        
        functions get modified:
        
        func1.priorities = {
            'event_name': 2
        }
        '''
    
    def sortKeys(self, name):
        keys = list(self.events[name].keys())
        keys.remove('priorities')
        self.events[name]['priorities'] = sorted(keys, reverse=True)
    
    def _subscribe(self, name, priority, func):
        event = self.events.setdefault(name, {'priorities': []})
        while priority in event:
            # later subscribed --> higher prio
            priority += 1
        if not hasattr(func, 'priorities'):
            func.priorities = {}
        if name in func.priorities:
            return
        func.priorities[name] = priority
        event[priority] = func
        self.sortKeys(name)
    
    #def subscribe(self, func, priority = 0, name = None):
    def subscribe(self, *args):
        args = list(args)
        func = args.pop(0) if args and hasattr(args[0], '__call__') else None
        
        arg1 = args.pop(0) if args else None
        arg2 = args.pop(0) if args else None
        
        if isinstance(arg1, int):
            priority = arg1
            name = arg2
        else:
            name = arg1
            priority = arg2 if isinstance(arg2, int) else 0
        
        # for use as decorator
        # @subscribe('name', 0)
        def sub(func):
            name_ = (name or func.__name__).lower()
            self._subscribe(name_, priority, func)
            return func
        
        return sub(func) if func else sub
    
    def _unsubscribe(self, name, func):
        if name not in self.events:
            return
        event = self.events[name]
        priority = func.priorities[name]
        if event[priority] == func:
            del event[priority]
            del func.priorities[name]
            event['priorities'].remove(priority)
        if not len(event['priorities']):
            del self.events[name]
    
    def unsubscribe(self, func, name = None):
        name = (name or func.__name__).lower()
        self._unsubscribe(name, func)
    
    def invoke(self, name, *args, **kw):
        if name not in self.events:
            return None
        
        event = self.events[name]
        i = iter(event['priorities'])
        
        def parent(*args, **kw):
            try:
                priority = next(i)
            except StopIteration:
                return None
            try:
                return event[priority](parent, *args, **kw)
            except Exception as e:
                pass
        
        return parent(*args, **kw)
    
    def recorder(self):
        class Recorder(Events):
            '''Recorders track, what events they are subscribed'''
            def __init__(self, existing):
                # all properties are objects, so when they are copied
                # only references are made; so changes to one apply to all
                self.events = existing.events
                self.recorded = set()
            
            def _subscribe(self, name, priority, func):
                super()._subscribe(name, priority, func)
                self.recorded.add((name, func))
            
            def _unsubscribe(self, name, func):
                super()._unsubscribe(name, func)
                self.recorded.discard((name, func))
            
            def unsubscribe_all(self):
                for args in self.recorded.copy():
                    self._unsubscribe(*args)
        
        return Recorder(self)
