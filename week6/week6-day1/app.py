import json
import os
import sys


def read_digital_ocean_pat(fil_nm):
    with open(fil_nm, "r") as f:
        content = f.read()
    return content


def get_key_id(token):
    cmd = 'curl -X GET -H "Content-Type: application/json" ' \
        + '-H "Authorization: Bearer {0}" '.format(token) \
        + '"https://api.digitalocean.com/v2/account/keys" > ./curl_out.txt'

    # print(cmd)
    os.system(cmd)

    json_data = open('./curl_out.txt').read()
    values = json.loads(json_data)

    return values['ssh_keys'][0]['id']


def start_droplet(ssh_key_id, token, tag):
    props = {"name": "node",
             "region": "sfo2",    # nyc1
             "size": "1gb",
             "image": "ubuntu-16-04-x64",
             "ssh_keys": [ssh_key_id],
             "backups": False,
             "ipv6": False,
             # "user_data": null, \
             # "private_networking": null,
             "tags": [tag]}
    prop_str = json.dumps(props)

    cmd = 'curl -X POST' \
        + ' -H "Content-Type: application/json"' \
        + ' -H "Authorization: Bearer {0} "'.format(token) \
        + ' -d \'' + prop_str + '\'' \
        + ' "https://api.digitalocean.com/v2/droplets"'
    # print(cmd)
    stats = os.system(cmd)
    if stats != 0:
        print('Status:', stats)
        print('Command:', cmd)
    return stats


def delete_droplet(token, tag):
    cmd = 'curl -X DELETE -H "Content-Type: application/json" ' \
        + '-H "Authorization: Bearer {0}" '.format(token) \
        + '"https://api.digitalocean.com/v2/droplets?tag_name={0}" '.format(tag)

    # print(cmd)
    ret_sts = os.system(cmd)
    return ret_sts == 0


def get_regions(token):
    cmd = 'curl -X GET -H "Content-Type: application/json" -H' \
        + ' "Authorization: Bearer {0}"'.format(token) \
        + ' "https://api.digitalocean.com/v2/regions" > ./regions_out.txt'

    #print(cmd)
    os.system(cmd)

    with open('./regions_out.txt', 'r') as handle:
        parsed = json.load(handle)

    print(json.dumps(parsed, indent=4, sort_keys=True))
    regions = parsed['regions']

    return regions


def get_cmd_args():
    args = [0, 0]

    num_args = len(sys.argv )

    if num_args == 2:
        args[0] = 'regions'
        return True, args

    elif num_args == 3:
        actions = ['add', 'drop']
        for arg in sys.argv:
            if arg.lower() in actions:
                args[0] = arg.lower()
            else:
                args[1] = arg.lower()
        return True, args

    else:
        return False, args


def main():
    # get command line arguments
    ret_sts, args = get_cmd_args()
    if not ret_sts:
        msg = 'Command line arguments are:\n' \
              '   add <droplet_tag_name> or\n' \
              '   drop <droplet_tag_name>'
        print(msg)
    else:
        # read digital ocean personal access token from file
        #pat_from_file = read_digital_ocean_pat('/home/steve/.pat/do_key')
        pat_from_file = read_digital_ocean_pat('/dotfiles/do_key')

        # get ssh key id from digital ocean
        key_id = get_key_id(pat_from_file)
        print('SSH key id:', key_id)

        if args[0] == 'add':
            ret_sts = start_droplet(key_id, pat_from_file, args[1])
            msg = 'Added droplet {0}, start status {1}'.format(args[1], ret_sts)
            print(msg)
        elif args[0] == 'drop':
            ret_sts = delete_droplet(pat_from_file, args[1])
            msg = 'Dropped droplet {0}, drop status {1}'.format(args[1], ret_sts)
            print(msg)
        elif args[0] == 'regions':
            do_regions = get_regions(pat_from_file)

            regions = {}
            for r in do_regions:
                regions[r['slug']] = r['name']

            regions_sorted = sorted(regions.keys())
            for key in regions_sorted:
                print(key, regions[key])

            msg = 'Got regions, status {0}'.format(ret_sts)
            print(msg)


if __name__ == '__main__':
    try:
        main()
    except:
        info = sys.exc_info()
        print('Unexpected error')
        print('        type:', info[0])
        print('       value:', info[1])
        print('   traceback:', info[2])
