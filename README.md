# Budget Tracker CLI

Budget Tracker CLI is a simple command-line tool built with [Typer](https://typer.tiangolo.com/) and [SQLAlchemy](https://www.sqlalchemy.org/) to help you manage and track your monthly expenses. It allows you to add budget items with their associated prices and generate a summary of expenses for a specific month.

## Features

- **Add Budget Item**: Add an expense item by specifying its name and price.
- **Monthly Summary**: Calculate the total expense for a given month and year.
- **SQLite Database**: Uses SQLite to store your expense data locally.
- **Easy to Install and Use**: Packaged as a CLI tool with a simple command (`bt`) for quick access.

## Installation

You can install Budget Tracker CLI globally or for your user with pip.

### Global Installation

```bash
pip install .
```

### User-Level Installation

```bash
pip install --user .
```

> **Note**: After installation, make sure the scripts directory (typically `C:\Users\<YourUsername>\AppData\Roaming\Python\Python<version>\Scripts` on Windows or `~/.local/bin` on Linux/macOS) is in your PATH so that you can run the `bt` command directly.

## Usage

Once installed, you can use the CLI with the following commands:

### Add an Expense Item

```bash
bt add <item> <price>
```

For example, to add a "haircut" expense costing 500:

```bash
bt add Grocery 500
```

### Get a Monthly Summary

```bash
bt summary <month> <year>
```

For example, to get a summary for February 2025:

```bash
bt summary Feb 2025
```

The command will output the total expenses for that month, e.g.:

```
Feb-2025 -> Output : Rs. 2480.23
```

## Project Structure

```
budget_tracker/
├── budget_tracker/
│   ├── __init__.py
│   └── main.py       # Contains the Typer app code
├── setup.py          # Packaging configuration
├── pyproject.toml    # (Optional) Modern packaging config
└── README.md         # This file
```

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---