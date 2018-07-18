'''
This little scripts will generate a new Singularity recipe for updating the DB
'''

import argparse
import subprocess
import datetime
import logging
import os
import fileinput

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def get_args():
    '''
    Parse some arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", help="Which version of Abricate do you wish to update? (default: 0.8)", default='0.8')
    args = parser.parse_args()
    return args

def git(cmd, msg=None):
    '''
    Run different git commands
    '''
    cmd_str = ['git']
    if cmd == 'commit':
        if msg is None:
            log.critical("Can't commit without a message")
            raise SyntaxError
        else:
            cmd_str += ['commit', '-a', '-m', msg]
    else:
        cmd_str += [cmd]
    log.info(subprocess.list2cmdline(cmd_str))
    subprocess.run(cmd_str)

def get_today():
    '''
    datetime abstraction to get today's date in the right format
    '''
    return datetime.datetime.strftime(datetime.datetime.today(), '%Y%m%d')

def process_line(line, pattern, replacement):
    '''
    Process the template lines
    '''
    return line.replace(pattern, replacement)

def save_new_file(filename, lines):
    '''
    Save a new Singularity file.
     - filename: assumes absolute path to file
    '''
    fh = open(filename, 'wt')
    fh.writelines(lines)
    fh.close()
    log.info(f"Successfully created {filename}")

def update_db(version, today):
    '''
    The function that does it all
    '''
    new_dir = os.path.abspath(os.path.join(f'v{version}', f'DB{today}'))
    if os.path.exists(new_dir):
        log.critical('Version and date of DB already exist. Nothing to do.')
        return
    os.makedirs(new_dir)
    new_singularity=os.path.join(new_dir, f'Singularity.v{version}_DB{today}')
    recipe_lines = []
    with fileinput.FileInput('SingRecipeTemplate') as template:
        for line in template:
            recipe_lines.append(process_line(line, "{{VERSION}}", version))
    save_new_file(new_singularity, recipe_lines)
    git('commit', msg=f"DB update on {today} for version {version}")
    git('push')

def main():
    args = get_args()
    git('pull')
    today = get_today()
    update_db(args.version, today)

if __name__ == "__main__":
    main()