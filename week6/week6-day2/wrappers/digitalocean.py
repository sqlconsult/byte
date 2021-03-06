#!/usr/bin/env python3

import json
import os
import re
# import socket

# import requests


# TODO 1: Reduce the redundancy across variables `a_header`, `c_header`, and `headers`.
# TODO 2: Port the functionality of the `curl` command to the `requests.post()` function.

def builder(params):
    endpoint = 'https://api.digitalocean.com/v2/droplets'

    hostname = params['hostname']
    payload = {}

    a_header = 'Authorization: Bearer {pa_token}'.format(pa_token=params['pa_token'])  # TODO 1
    c_header = 'Content-Type: application/json'                             # TODO 1

    vm_count = int(params['num_vm'])
    if vm_count == 1:
        payload['name'] = '{0}-{1}'.format(hostname, 0)
    else:
        payload['names'] = ['{hostname}-{n}'.format(hostname=hostname, n=i)
                            for i in range(vm_count)]

    payload['region'] = params['region']
    payload['size']   = params['size']
    payload['image']  = 'ubuntu-16-04-x64'
    # headers = {
    #     'Authorization': 'Bearer {pa_token}'.format(pa_token=pa_token),
    #     'Content-Type': 'application/json'
    # }                                                             # TODO 1
    # headers['Authorization'] = 'Bearer {pa_token}'.format(pa_token=pa_token) # TODO 1
    # headers['Content-Type'] = 'application/json'                             # TODO 1
    # keys = json.loads(requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers).text)['ssh_keys']
    # payload['ssh_keys'] = [str(key['id']) for key in keys if key['name'] == socket.gethostname()]
    payload['ssh_keys'] = [get_key_id(params['pa_token'])]
    payload['tags'] = [params['tag']]
    endstate = 'curl -X POST "{endpoint}"            \
                -d \'{payload}\'                     \
                -H "{a_header}"                      \
                -H "{c_header}"'                     \
                .format(endpoint=endpoint,           \
                        payload=json.dumps(payload), \
                        a_header=a_header.strip(),   \
                        c_header=c_header) # TODO 2
    return re.sub(' +', ' ', endstate)     # TODO 2


def get_host(droplet_id, writeout_file, params):
    writeout_file_i = writeout_file.split('.')[0]     \
                        + writeout_file.split('.')[1] \
                        + '-'                         \
                        + str(droplet_id)             \
                        + '.json'
    os.system('curl -X GET "https://api.digitalocean.com/v2/droplets/{droplet_id}" \
                -H "Content-Type: application/json" \
                -H "Authorization: Bearer {pa_token}" > {writeout_file_i}'
              .format(droplet_id=droplet_id,
                      pa_token=params['pa_token'],
                      writeout_file_i=writeout_file_i))

    payload = json.load(open(writeout_file_i))
    ip_address = payload['droplet']['networks']['v4'][0]['ip_address']
    return ip_address


def get_key_id(token):
    cmd = 'curl -X GET -H "Content-Type: application/json" ' \
        + '-H "Authorization: Bearer {0}" '.format(token) \
        + '"https://api.digitalocean.com/v2/account/keys" > ./curl_out.txt'

    # print(cmd)
    os.system(cmd)

    json_data = open('./curl_out.txt').read()
    values = json.loads(json_data)

    return values['ssh_keys'][0]['id']
