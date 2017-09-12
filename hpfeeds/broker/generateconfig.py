import os.path
import sys

import argparse


def generate_config():
    if os.path.isfile('config.py'):
        print('config.py already exists')
        sys.exit()

    localconfig = {}

    is_unattended = False

    parser_description = 'This is a help script to generate a working config.py file from the config template.'
    parser = argparse.ArgumentParser(parser_description)

    subparsers = parser.add_subparsers(help='commands')

    parser_generate = subparsers.add_parser('generate',
                                            help='Generate a config.py and prompt for options')
    parser_generate.set_defaults(which='generate')
    parser_unatt = subparsers.add_parser('unattended', help='Unattended install')
    parser_unatt.set_defaults(which='unattended')
    parser_unatt.add_argument('--mongo_host', type=str, default="localhost",
                              help='MongoDB address')
    parser_unatt.add_argument('--mongo_port', type=int, default=27017,
                              help='MongoDB port')

    if len(sys.argv) < 2:
        args = parser.parse_args(['generate'])
    else:
        args = parser.parse_args(sys.argv[1:])

    # check for unattended install
    if args.which is 'unattended':
        is_unattended = True

    if is_unattended:
        mongo_host = args.mongo_host
        mongo_port = args.mongo_port
    else:
        mongo_host = raw_input('MongoDB hostname ["localhost"]: ')
        mongo_port = raw_input('MongoDB port [27017]: ')

    localconfig['MONGODB_HOST'] = mongo_host if mongo_host else "localhost"
    localconfig['MONGODB_PORT'] = mongo_port if mongo_port else 27017

    with open('config.py.template', 'r') as templfile,\
         open('config.py', 'w') as confile:
        templ = templfile.read()
        for key, setting in localconfig.iteritems():
            templ = templ.replace('{{' + key + '}}', str(setting))
        confile.write(templ)


if __name__ == '__main__':
    generate_config()
