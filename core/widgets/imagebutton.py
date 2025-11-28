from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

class ImageButton(ButtonBehavior, Image):
    def __init__(self, source, **kwargs):
        super().__init__(source=source, **kwargs)
        # You can set size hints or fixed size here if needed
        self.size_hint = (None, None)
        self.width = 100
        self.height = 100

# Example usage:
# img_btn = ImageButton(source="assets/images/logo.png")
# img_btn.bind(on_release=lambda instance: print("Image button clicked!"))