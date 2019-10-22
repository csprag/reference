git checkout
---

`git checkout` is used to navigate between branches created by `git branch`

~~~ bash
$ git checkout <branch>
~~~

---

### Useful Options / Examples

#### `git checkout <branch>`
~~~ bash
$ git branch
master
feature1_branch
feature2_branch 
$ git checkout feature1_branch
~~~

##### Break it down
 
 * Shows available branches and switches to another branch, in this case we are switching to `feature1_branch`.
 * Updates the files in the working directory to match the version stored in branch and tells Git to record all
 new commits to that branch. 

#### `git checkout -b <newBranch>`

~~~ bash
$ git branch
master
feature1_branch
feature2_branch 
$ git checkout -b new_feature
$ git branch
master
feature1_branch
feature2_branch
new_feature
~~~

##### Break it down

 * Simulataneously creating a new branch off master and then checkout to the new branch.
 * git checkout -b 'newBranch' 'existingBranch' creates the new branch based off the stated 'existingBranch'.
