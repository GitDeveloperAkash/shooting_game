

class ConfigLoader:
    def __init__(self, config_file='configs/config.yaml'):
        import yaml
        try:
            with open(config_file,'r') as file:
                self.config = yaml.safe_load(file)

        except FileNotFoundError:
            print(f"Error: file '{config_file}' was not found.")
        except PermissionError:
            print(f"Permission denied when trying to open file '{config_file}'. ")
        except Exception as e:
            print(f"Unknown exception occured: '{e}'")

    def get_screanConfig(self):
        return self.config.get('Screan', {})
    
    def screen_height(self):
        return self.config.get('screen_height')
    def screen_width(self):
        return self.config.get('screen_width')
    def game_name(self):
        return self.config.get('game_name')
    def Player(self):
        return self.config.get('Player')
    def Background(self):
        return self.config.get('Background')
        
