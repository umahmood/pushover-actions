import os
import argparse

import requests

def main():
    parser = argparse.ArgumentParser(description="Pushover Notifications")
    parser.add_argument('--message',
                        type=str, 
                        help='Message text')
    parser.add_argument('--status',
                        type=str, 
                        help='The current status of the job')
    parser.add_argument('--title',
                        type=str, 
                        help='Message title')
    parser.add_argument('--url',
                        type=str, 
                        help='Supplementary URL to show with your message')
    parser.add_argument('--url_title',
                        type=str, 
                        help='title for your supplementary URL, otherwise just the URL is shown')
    parser.add_argument('--device',
                        type=str, 
                        help='Device name to send the message directly to')
    args = parser.parse_args()
    try:
        token   = os.environ['PUSHOVER_TOKEN']
        user    = os.environ['PUSHOVER_USER']
        repo    = 'Repo: '    + os.environ['GITHUB_REPOSITORY']
        sha     = 'Commit: '  + os.environ['GITHUB_SHA'][:8]
        ref     = 'Ref: '     + os.environ['GITHUB_REF'] if 'GITHUB_REF' in os.environ else ''
        status  = 'Status: '  + args.status if args.status else ''
        message = args.message if args.message else ''
        message = '\n'.join([m for m in [repo, sha, ref, status, message] if m])
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
            'token'     : token,
            'user'      : user,
            'message'   : message,
            'title'     : args.title,
            'url'       : args.url,
            'url_title' : args.url_title,
            'device'    : args.device,
        }
        response = requests.post('https://api.pushover.net/1/messages.json',
                                 headers=headers,
                                 data=payload,
                                 timeout=60)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == '__main__':
    main()
