#!/usr/bin/env python3

import datetime
import json
import os
# import sys
import time

from wrappers import digitalocean


# TODO 1: Write a module for AWS Lightsail.
# TODO 2: Write an error handler.

def spin_up(params):
    # timestamp_utc = time.time()

    now = datetime.datetime.now()
    timestamp_local = '{0}{1}{2}_{3}{4}{5}'.\
        format(now.year, now.month, now.day, now.hour, now.minute, now.second)

    writeout_file = 'logs/build-{timestamp_local}.json'.format(timestamp_local=timestamp_local)
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']

    for vendor_choice in params['platforms']:
        if vendor_choice in aws_lightsail:
            pass     # TODO 1
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > {writeout_file}'
                      .format(unix_command=digitalocean.builder(params),
                              writeout_file=writeout_file))
            time.sleep(60)
            return harden(writeout_file, params)
    else:
        pass     # TODO 2


def harden(writeout_file, params):
    response = json.load(open(writeout_file))
    payloads = []
    if 'droplets' in response:
        payloads = response['droplets']
    else:
        payloads = [response['droplet']]

    ip_addresses = []
    for payload in payloads:
        ip_addresses.append(digitalocean.get_host(payload['id'], writeout_file, params))

    for ip_address in ip_addresses:
        os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote0.sh'
                  .format(ip_address=ip_address))

        os.system('scp /home/steve/.ssh/id_rsa.pub root@{ip_address}:/etc/ssh/steve/authorized_keys'
                  .format(ip_address=ip_address))

        os.system('sh -c \'echo "steve:swordfish" > /home/steve/dotfiles/setup/.credentials\'')

        os.system('scp /home/steve/dotfiles/setup/.credentials root@{ip_address}:/home/steve/'
                  .format(ip_address=ip_address))

        os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote1.sh'
                  .format(ip_address=ip_address))

        os.system('rm /home/steve/dotfiles/setup/.credentials')
    return ip_addresses


def get_params():
    with open('./params.json', 'r') as handle:
        params = json.load(handle)

    # print(json.dumps(params, indent=4, sort_keys=True))
    pa_token = open('{pat_path}'.format(pat_path=params['pat_path'])).read().strip()
    params['pa_token'] = pa_token

    return params


def main():
    from pprint import pprint
    # params contains things like platforms, number of vm's and vm properties
    params = get_params()
    # print(json.dumps(params, indent=4, sort_keys=True))

    if params['num_vm'] == 0:
        print('Error: You cannot spin up less than one server.')
    else:
        pprint(spin_up(params))


if __name__ == '__main__':
    main()
