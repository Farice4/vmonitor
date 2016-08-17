import ConfigParser


class VMonitorConfig(ConfigParser.RawConfigParser):

    def __init__(self):
        ConfigParser.RawConfigParser.__init__(self)
        self.defaults = {}

    def read_config(self, config_path):
        self.read(config_path)

    def register_opts(self, module, opts):
        if module not in self.defaults:
            self.defaults[module] = {}
        self.defaults[module].update(opts)

    def get(self, section, option):
        try:
            return ConfigParser.RawConfigParser.get(self, section, option)
        except ConfigParser.Error:
            return self.defaults[section][option]


CONF = VMonitorConfig()


