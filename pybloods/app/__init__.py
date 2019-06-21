class PyBloodsApp(connexion.App):
    def __init__(self):
        self.add_api('openapi.yaml')
