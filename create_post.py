import argparse, datetime

class ReadContentAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values[-3:] != ".md":
            print("File must be markdown format.\n")
            exit(1)
        setattr(namespace, self.dest, values)


def create_header(args):
    if args.title is not None:
        title = "title: " + args.title.replace('-', ' ')
    else: title = ""
    layout = "layout: " + args.layout
    
    header = "---\n" + layout + "\n" + title + "\n---\n"
    return header


parser = argparse.ArgumentParser(description="add a markdown file with headers for jekyll")
parser.add_argument("filename", action=ReadContentAction, help="A text file to read as a content of post")
parser.add_argument("--title", help="Specify title of post")
parser.add_argument("--layout", default="post", help="Specify the type of layout")
args = parser.parse_args()

posted_time = datetime.datetime.now().strftime('%Y-%m-%d-')
with open(args.filename, 'r') as f:
    content = f.read()
post_name = args.title if args.title is not None else args.filename.split('/')[1][:-3]

new_post = "_posts/" + posted_time + post_name + ".md"

print(args)
with open(new_post, 'a') as post:
    post.write(create_header(args))
    post.write(content)