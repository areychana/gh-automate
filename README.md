# GitHub Automation CLI Tool

## Overview
The `gh-automate` project is a command-line interface (CLI) tool designed to automate common tasks on GitHub. This tool allows users to easily manage their GitHub repositories and issues directly from the command line.

## Features
- List repositories
- Create issues
- List issues
- Close issues

## Installation
To get started with the `gh-automate` tool, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gh-automate.git
   cd gh-automate
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your GitHub personal access token:
   ```
   GITHUB_TOKEN=your_github_token_here
   ```

## Usage
After installation, you can use the CLI tool by running the following command:

```
python src/cli.py [command]
```

### Commands
- **List Repositories**
  ```
  python src/cli.py list-repos
  ```

- **Create an Issue**
  ```
  python src/cli.py create-issue "Issue Title" "Issue Body"
  ```

- **List Issues**
  ```
  python src/cli.py list-issues
  ```

- **Close an Issue**
  ```
  python src/cli.py close-issue issue_number
  ```

## Additional Information
For more details on how to use each command, refer to the help option:
```
python src/cli.py --help
```

Feel free to contribute to the project by submitting issues or pull requests. Happy automating!