import yaml
import sys
from translator.translator import translate

def read_yml(filename):
    with open(f'{filename}.yaml','r') as f:
        dic = yaml.safe_load(f)
        if not dic:
            return "Empty Yaml file passed!!"
    return(translate(dic))

if __name__ == "__main__":
    import sys
    read_yml(sys.argv[1])