# Artifacts

Whenever a Action worfklow generates something other than logs, it's called an artifact. This can be used to increase the speed or make a cross-link between different actions (items aren't shared between), artifacts can be uploaded and redownloaded using [upload-artifact](https://github.com/actions/upload-artifact) and [download-artifact](https://github.com/actions/download-artifact).

Storing an artifact preserves it between jobs.

```yml
build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: npm install and build webpack
      run: |
        npm install
        npm run build
    - uses: actions/upload-artifact@main
      with:
        name: webpack artifacts
        path: public/
```

# Automated reviews labels

Can use https://github.com/abinoda/label-when-approved-action to automatically label PRs when they are approved. This is useful for automating the process of merging PRs.

```yml
steps:
  - name: Label when approved
    uses: pullreminders/label-when-approved-action@main
    env:
      APPROVALS: "1"
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      ADD_LABEL: "approved"
```
