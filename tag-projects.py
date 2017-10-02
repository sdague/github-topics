#!/usr/bin/env python

import argparse
import os
import requests

PROJECTS = {}
ROOT = "topics"
TOKEN = ""

def parse_args():
    parser = argparse.ArgumentParser(
        description='Update topics for github projects')
    parser.add_argument('-t', '--token',
                        help='bearer token to operate under')
    return parser.parse_args()

def set_token(token):
    global TOKEN
    if token:
        TOKEN = token
    elif os.path.exists("token.txt"):
        with open("token.txt") as f:
            TOKEN = f.read().rstrip()

# Collect topics and add them to projects
def add_topic_to_project(topic, project):
    if project in PROJECTS:
        PROJECTS[project].add(topic)
    else:
        PROJECTS[project] = set()
        PROJECTS[project].add(topic)


def collect_tags():
    topic_files = os.listdir(ROOT)
    for fname in topic_files:
        topic = os.path.splitext(fname)[0]
        with open(os.path.join(ROOT, fname)) as f:
            for line in f.readlines():
                project = line.rstrip()
                add_topic_to_project(topic, project)


def update_topics(project, topics):
    # NOTE(sdague): the topics resource is only available in the
    # experimental version of the REST v3 API. It's available as a
    # mutation in graphql (i.e. v4 API), but that's kind of overkill
    # given how simple the code below is.
    headers = {
        "Accept": "application/vnd.github.mercy-preview+json",
        "Authorization": "Bearer " + TOKEN
    }
    data = {"names": list(topics)}
    url = "https://api.github.com/repos/%s/topics" % project

    resp = requests.put(url,
                        json=data,
                        headers=headers)
    if resp:
        print("Set topics for %s" % project)
    else:
        print("Error in PUT %s => %s" % (url, data))
        print(resp)
        print(resp.content)

def main():
    args = parse_args()
    set_token(args.token)
    collect_tags()
    for project, topics in PROJECTS.items():
        update_topics(project, topics)

if __name__ == "__main__":
    main()
