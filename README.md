# j2t: Jinja2 Templating Utility

## Overview

`j2t` is a self contained Python 3 script that lets you invoke Jinja2 templates
via the command line.  It's designed to be a self contained file that has minimal
dependencies (Python3 and Jinja2 are required, PyYAML is optional).

## Usage

By default, `j2t` takes a Jinja2 template as input on `stdin` and spits out the
transformed result to `stdout`.  By itself, this isn't terribly useful, so you
can optionally inject `yaml`, `json`, or `key=value` pairs into the Jinja2 template.

The full j2t help is:

```
usage: j2t [-h] [-t path] [-o path] [-j path] [-y path] [-k key=value]

Jinja2 Template Transformer Utility

optional arguments:
  -h, --help            show this help message and exit
  -t path, --template path
                        jinja2 template path (default: stdin)
  -o path, --output path
                        output path (default: stdout)
  -j path, --add-json path
                        add json data
  -y path, --add-yaml path
                        add yaml data
  -k key=value, --add-kv key=value
                        add key=value pair
```
## Example

```
$ cat test1.yml
a: "hello"
b: "world"

$ cat test1.j2
{{a}} {{b}}!

$ cat test1.j2 | j2t --add-yaml test1.yml
hello world!

$ j2t --add-yaml test1.yml --template test1.j2
hello world!

$ j2t --add-yaml test1.yml --template test1.j2 --output -
hello world!

$ j2t --add-yaml test1.yml --template test1.j2 --output /tmp/output.txt ; cat /tmp/output.txt
hello world!

```

## Contact and Support

For questions or concerns, contact bmurphy@mediafly.com
