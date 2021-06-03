import argparse, datetime

class ReadContentAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        with open(values, 'r') as f:
            content = f.read()
        setattr(namespace, self.dest, content)



def create_header(args):
    title = "title: " + args.title
    layout = "layout: " + args.layout
    header = "---\n" + layout + "\n" + title + "\n---\n"
    return header


parser = argparse.ArgumentParser(description="add a markdown file with headers for jekyll")
parser.add_argument("file", action=ReadContentAction, help="A text file to read as a content of post")
parser.add_argument("--title", help="Specify title of post")
parser.add_argument("--layout", default="post", help="Set layout")
args = parser.parse_args()

posted_time = datetime.datetime.now().strftime('%Y-%m-%d-')
new_post = "_posts/" + posted_time + args.title + ".md"

with open(new_post, 'a') as post:
    post.write(create_header(args))
    post.write(args.file)