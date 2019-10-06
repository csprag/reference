# Computer Science Pragmatics Reference Page

This repository holds the reference page for the course homepage for Computer Science Pragmatics,
a course for early-career EECS students at the University of Michigan.

For more information, visit the course homepage: [https://cspragmatics.com](https://cspragmatics.com/)

## Contributing

The site itself uses [GitHub Pages][], [Flask][].

Before contributing, please check [open issues][] and create a [new issue][] if a one for your proposed contribution does not exist.

Content for the website is written in [Markdown][].
To contribute to the [reference page][], navigate to `reference/static/commands` and then to the specific section and edit an existing `.md` file or create a new one.
For example, to edit the `cd` reference, edit `reference/static/commands/basics/cd.md`.

In order to build the site locally on your computer, there are a number of dependencies to resolve first.
Make sure you're in a python 3.7 virtual environment, then run the following in your terminal:

```bash
export FLASK_APP=reference
export FLASK_ENV=development
python setup.py develop
flask run
```

Alternatively, just run the setup script provided.

```bash
chmod +x run.sh
run.sh
```

For more information on setting up, see [GitHub's guide][gh docs] or [Flask's documentation][flask docs].

After making a change and verifying that it works, please submit a [pull request][].

---------------------

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Computing for Computer Scientists</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://patpannuto.com" property="cc:attributionName" rel="cc:attributionURL">Pat Pannuto</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.


[GitHub Pages]: https://pages.github.com/
[Flask]: http://flask.pocoo.org/
[open issues]: https://github.com/csprag/reference/issues
[new issue]: https://github.com/csprag/reference/issues/new
[Markdown]: http://daringfireball.net/projects/markdown/
[reference page]: https://cspragmatics.com/reference
[gh docs]:https://help.github.com/articles/using-jekyll-with-pages/
[flask docs]: http://flask.pocoo.org/docs/1.0/
[pull request]: https://github.com/csprag/reference/pulls
