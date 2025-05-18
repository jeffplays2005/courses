# Github Actions

- `matrix` - contex that contains all the values of properties defined in the `matrix` key of the workflow file. E.g. configure os and node keys.

```yml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [14, 16]
```

## Piping environment variables

Can pass environment variables between steps using the `env` context. This is useful for passing values between steps in a job.

```yml
steps:
  - name: Set the value
    id: step_one
    run: |
      echo "action_state=yellow" >> "$GITHUB_ENV"
  - name: Use the value
    id: step_two
    run: |
      printf '%s\n' "$action_state" # This will output 'yellow'
```
