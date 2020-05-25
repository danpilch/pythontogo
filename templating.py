import os
import yaml
from collections import defaultdict
from jinja2 import Environment, PackageLoader, select_autoescape

d = defaultdict(dict)

for dirpath, dirnames, filenames in os.walk("./code"):
    for filename in [f for f in filenames if f.endswith(".py")]:
        with open(os.path.join(dirpath, filename), 'r') as f:
            d[dirpath.split('/')[-1]]['python'] = f.read()
    for filename in [f for f in filenames if f.endswith(".go")]:
        with open(os.path.join(dirpath, filename), 'r') as f:
            d[dirpath.split('/')[-1]]['golang'] = f.read()
    for filename in [f for f in filenames if f.endswith(".yaml")]:
        with open(os.path.join(dirpath, filename), 'r') as f:
            d[dirpath.split('/')[-1]]['yaml'] = yaml.load(f.read(), Loader=yaml.FullLoader)

env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('index.html')

print(template.render(groups=d))
