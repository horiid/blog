import datetime, argparse

class TitleAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        pass
    def __call__(self, parser):
        pass


parser = argparse.ArgumentParser(description="add a markdown post with headers for jekyll")
parser.add_argument("file")
parser.add_argument("--title",)
parser.add_argument("--layout", default="post")
args = parser.parse_args()
tmp = "./tmp"
with open(tmp, "r") as tmp:
    created_time = datetime.datetime.now()
    tmp += "---" + created_time + "---"