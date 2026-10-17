# Repository Catalog

Record the repositories actually used by the target workspace. No required host, repository name, suffix, stack, or split: a monorepo and multiple repositories are both valid. Use the configured host's review-request mechanism (PR or merge request).

For each repository, record in the workspace setup or existing repository registry:

```text
Location (URL or approved local path):
Purpose / project / relevant component paths:
Human owner / permitted agent identities:
Default branch / protected branches / review and merge controls:
Build / test / lint instructions (link to repository-owned documentation):
Deployment / rollback documentation (link, if applicable):
```

Reference repository-owned instructions rather than duplicating commands or stack inventories here. Inspect existing manifests, conventions, and CI before making changes. Keep agent access least-privilege; never embed credentials in repository locations.

Branch isolation, approval, and commit requirements belong to `workspace/governance-rules.md`. Use repository-native branch names and hosting controls to enforce that policy; do not prescribe names or history strategy in this catalog.
