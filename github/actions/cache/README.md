# Caching in Github Actions

Caching in Github Actions is a way to store and reuse dependencies and build outputs to speed up the workflow execution time. It can be particularly useful for large projects with many dependencies or for workflows that run frequently.

Can use the Github `cache` action.

| Parameter    | Description                                             | Required |
| ------------ | ------------------------------------------------------- | -------- |
| key          | The key identifier of the cache                         | yes      |
| path         | Refers to the paths of cacheable files                  | yes      |
| restore-keys | Alternative keys to caches if desired cache isn't found | no       |
