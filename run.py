from digitalframe.app import DigitalFrameApp
from strictyaml import load, Map, Str, Int, Seq, YAMLError

with open('config.yml', 'r') as file:
    config = file.read()

config = load(config)

digitalframe = DigitalFrameApp(config, True)
digitalframe.run()