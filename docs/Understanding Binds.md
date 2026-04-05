```
# Singleton-like model
class Universe(EventDispatcher):
    active_gameplay_view = StringProperty("overview")

# A widget that should mirror Universe.active_gameplay_view
class ViewLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Bind Universe property → this label's text
        Universe().bind(active_gameplay_view=self._update_text)

    def _update_text(self, inst, val):
        # inst is Universe(), val is the new active_gameplay_view
        self.text = f"Current view: {val}"
```

This is the best example of how to bind that I can come up with. 

I want widgets to use properties from the Universe() instance, and to react when it changes. 

**Step 1.** Make the source a Kivy Prperty (stringproperty, etc.)

**Step 2.** Put a bind to the source property in whatever widget or object I want to auto update:

    *REACT_TO*.bind(*THIS_PROPERTY*=self.*WITH_METHOD*)

In other words:

| Placeholder | Actual Component |
| --- | --- |
| REACT_TO | Universe() |
| THIS_PROPERTY | active_gameplay_view (from the REACT_TO object)
| WITH_METHOD | self._change_gameplay_view

This gives you:

    Universe().bind(active_gameplay_view=self._change_gameplay_view)

**Step 3.** Write the method that makes the change. Remember to use *inst* and *val* as the variables! inst is the object changing, and val is the changed property. 

    def _update_text(self, inst, val):
        # inst is Universe(), val is the new active_gameplay_view
        self.text = f"Current view: {val}"