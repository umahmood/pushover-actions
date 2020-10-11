<p align="center">
    <img alt="Pushover Actions Logo" src="https://raw.githubusercontent.com/umahmood/pushover-actions/main/assets/images/logo.jpg" height="130" />
    <h3 align="center">Pushover Actions</h3>
    <p align="center">Pushover notifications for Github actions</p>
    <p align="center">
    <a href="https://github.com/Clivern/pushover-actions/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
    </p>
</p>

## Documentation
1 - Create a [pushover application](https://pushover.net/) and obtain a token and user key.

2 - Create a Github workflow by adding the following to your `.github/workflows/workflow.yml`.
```
name: pushover-actions
on: push
jobs:
  pushover-actions:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2 
      - name: pushover-actions
        uses: umahmood/pushover-actions@master
        env:
          PUSHOVER_TOKEN: ${{ secrets.PUSHOVER_TOKEN }}
          PUSHOVER_USER: ${{ secrets.PUSHOVER_USER }}
        with:
          status: ${{ job.status }}
          title: 'Repo. Activity Notification'
          message: 'Hello World!'
```
3 - In your repo go to github settings > secrets and add the secrets,  `PUSHOVER_TOKEN` and `PUSHOVER_USER`.

4 - Push a commit to your repo to test if you receive a notification. 

<p align="center">
<img alt="Notification" src="https://raw.githubusercontent.com/umahmood/pushover-actions/main/assets/images/notification.jpg" />
</p>

You can pass the following flags into the action:

| Flag | Description |
| ---- | ----------- |
| status | The current status of the job |
| message | Message text |
| title | Message title |
| url | Supplementary URL to show with your message |
| url_title | title for your supplementary URL |
| device | Device name to send the message directly to |

Example: 
```
...
      with:
        status: ${{ job.status }}
        title: 'Repo. Activity Notification'
        message: 'Activity in repo.'
        url: 'https://example.com'
        url_title: 'example'
        device: 'iphone' # or 'iphone,galaxy10'
```

## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Pushover Actions is maintained under the [Semantic Versioning guidelines](https://semver.org/) and the release process is predictable and business-friendly.

See the [Releases section of our GitHub project](https://github.com/umahmood/pushover-actions/releases) for change logs for each release version of Pushover Actions. It contains summaries of the most noteworthy changes made in each release.

## Bug tracker

If you have any suggestions, bug reports, or annoyances please report them to our issue tracker at https://github.com/umahmood/pushover-actions/issues

## License

Copyright (c) 2020 - Usman Mahmood

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
