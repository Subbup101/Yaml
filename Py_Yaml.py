import argparse
import yaml

def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)
parser = argparse.ArgumentParser(description='Process Contact details .')
parser.add_argument('String', metavar='N', type=str, nargs='+',
                    help='String for the Name search')
parser.add_argument('--Show', dest='accumulate', action='Display_Details',
                    const=sum, default='No details found',
                    help='display contact details (default: No resluts found)')

if __name__ == "__main__":
    filepath = "test.yaml"
    data = yaml_loader(filepath)
    print data