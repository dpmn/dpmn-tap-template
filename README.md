# dpmn-tap-template

## Usage

The best way to demonstrate creating your tap structure is with an example.
Below I will initialize the "tap-foobar" project:

Start by installing cookiecutter:
```bash
$ pip install cookiecutter
```

The next command will ask for some input.  Enter the name of your tap:
```bash
$ cookiecutter https://github.com/singer-io/singer-tap-template.git
project_name [e.g. 'tap-facebook']: tap-foobar
```

For the package_name, I just hit enter since tap_foobar is what I wanted:
```bash
package_name [tap_foobar]:
```

Now that the project exists, make a virtual environment:
```bash
$ cd tap-foobar
$ python3 -m venv ~/.virtualenvs/tap-foobar
$ source ~/.virtualenvs/tap-foobar/bin/activate
```
Install the package:
```bash
$ pip install -e .
