# gh-automate

A Python CLI tool to automate common GitHub tasks from the command line.

## Features

-  List repositories for any GitHub user
-  Create issues
-  List open issues (pull requests excluded)
-  Close issues
-  Auto-label issues based on keywords

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/areychana/gh-automate.git
   cd gh-automate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your GitHub token:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and replace `your_github_token_here` with a real token.
   Generate one at [github.com/settings/tokens](https://github.com/settings/tokens) with `repo` and `read:user` scopes.

## Usage

```bash
python src/cli.py [command]
```

### Commands

**List repositories for a user**
```bash
python src/cli.py list-repos <username>
# e.g.
python src/cli.py list-repos octocat
```

**Create an issue**
```bash
python src/cli.py create-issue <owner/repo> "<title>" --body "<description>"
# e.g.
python src/cli.py create-issue octocat/Hello-World "Bug: login fails" --body "Steps to reproduce..."
```

**List open issues**
```bash
python src/cli.py list-issues <owner/repo>
# e.g.
python src/cli.py list-issues octocat/Hello-World
```

**Close an issue**
```bash
python src/cli.py close-issue <owner/repo> <issue_number>
# e.g.
python src/cli.py close-issue octocat/Hello-World 42
```

**Auto-label an issue**

Automatically applies labels (`bug`, `enhancement`, `documentation`, `testing`) based on keywords found in the issue title and body.
```bash
python src/cli.py auto-label <owner/repo> <issue_number>
# e.g.
python src/cli.py auto-label octocat/Hello-World 42
```

## Running Tests

```bash
pytest
```

## Contributing

Pull requests are welcome! Please open an issue first to discuss what you'd like to change.

## License

MIT
