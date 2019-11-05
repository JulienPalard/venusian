import venusian


class decorator(object):
    category = None
    call_count = 0

    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __call__(self, wrapped):
        view_config = self.__dict__.copy()

        def callback(context, name, ob):
            if hasattr(context, "test"):
                context.test(ob=ob, name=name, **view_config)
            self.__class__.call_count += 1

        info = venusian.attach(wrapped, callback, category=self.category)
        if info.scope == "class":
            # we're in the midst of a class statement
            if view_config.get("attr") is None:
                view_config["attr"] = wrapped.__name__
        return wrapped


class categorydecorator(decorator):
    category = "mycategory"


class categorydecorator2(decorator):
    category = "mycategory2"
