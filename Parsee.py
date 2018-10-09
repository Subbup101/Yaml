import argparse
import yaml


def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, "a") as file_descriptor:
        yaml.dump(data, file_descriptor)


parser = argparse.ArgumentParser(description="An argparse example")

parser.add_argument('action', help='The action to take (e.g. install, remove, etc.)')
parser.add_argument('foo-bar', help='Hyphens are cumbersome in positional arguments')

args = parser.parse_args()

if args.action == "Display":
    filepath = "test.yaml"
    '''f= open(filepath, "r")
    for x in f:
        print(x)'''
    with open('test.yaml') as f:
        d = yaml.load(f.read())
        print yaml.dump(d['Parr'])
elif args.action == "Display_All":
    filepath = "test.yaml"
    f= open(filepath, "r")
    for x in f:
        print(x)
elif args.action == "Add":
    filepath = "test.yaml"
    data = {
        'Parsu':{
            'Name': "Subbu23",
            'Phone': 143333,
            'email': "subbup10@gmail.com"
        }

    }
    yaml_dump(filepath, data)
    print('You asked for something other than installation')

# The following do not work:
# print(args.foo-bar)
# print(args.foo_bar)

# But this works:
'''print(getattr(args, 'foo-bar'))'''
