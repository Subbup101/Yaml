import argparse
import yaml


def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def yaml_dump(filepath, data):
    with open(filepath, "a") as file_descriptor:
        yaml.dump(data, file_descriptor)


parser = argparse.ArgumentParser(description="An argparse example")
parser.add_argument('action', help='The action to take (e.g. Display, Display_All, Add.)')
parser.add_argument("n", type=str, help="the Nickname")

parser.add_argument("x", type=str, help="the Name")
parser.add_argument("y", type=int, help="the phone num")
parser.add_argument("z", type=str, help="the email")

args = parser.parse_args()

if args.action == "Display":
    filepath = "Contacts.yaml"
    '''f= open(filepath, "r")
    for x in f:
        print(x)'''
    with open('Contacts.yaml') as f:
        d = yaml.load(f.read())
        Nick_Name = d[args.n]
        print yaml.dump(Nick_Name)
elif args.action == "Display_All":
    filepath = "Contacts.yaml"
    f= open(filepath, "r")
    for x in f:
        print(x)
elif args.action == "Add":
    '''and args.x >0 and args.y != "" and args.z != "" and args.n != "":'''
    filepath = "Contacts.yaml"
    data = {
        args.n: dict(Name=args.x, Phone=args.y, email=args.z)
    }
    yaml_dump(filepath, data)
    print('Contact has been added')
else:
    print ('Incorrect option selected. Available options are Display, Display_All, Add')

