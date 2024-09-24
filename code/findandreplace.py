from argparse import ArgumentParser, Namespace
from NormalizeText import *
import json

# parse the config argument
parser = ArgumentParser()
parser.add_argument('-c', '--config', required=True)
args = parser.parse_args()
config = None
with open(args.config) as fp:
    config = json.load(fp)

far_tool = NormalizeText(**config)

for document in config["config"]["documents"]:
    print(f"Normalizing {document}...")
    far_tool.find_and_replace(document, is_word_doc=config["config"]["is_word_doc"])
print("Done!")