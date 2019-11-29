git merge
-------
The this command lets you take the independent lines of development created by git branch and integrate them into a single branch.

~~~ bash
$ git checkout master
$ git merge otherBranch master
~~~

---

### Useful Options / Examples
git merge will automatically select a merge strategy unless explicitly specified, however, a desired merge strategy can be selected using the -s (strategy) option.

## Recursive
~~~ bash
$ git merge -s recursive branch1 branch2
Updating 676e434..c703d4e
Fast-forward
 2 | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 2
~~~

recursive is the default merge strategy when pulling or merging one branch, which operates on two heads.

## Resolve
~~~ bash
$ git merge -s resolve branch1 branch2
Updating 676e434..c703d4e
Fast-forward
 2 | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 2
~~~

revolve tries to carefully detect cris-cross merge ambiguities and is considered generally safe and fast.

## Octopus
~~~ bash
$ git merge -s octopus master branch1 branch2
Fast-forwarding to: branch1
Trying simple merge with branch2
Merge made by the 'octopus' strategy.
 4 | 0
 5 | 0
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 4
 create mode 100644 5
~~~

Octopus is default merge strategy for more than two heads.