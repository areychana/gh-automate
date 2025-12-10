import argparse
from rich import print
from rich.table import Table
import github_api as gh

def main():
    parser = argparse.ArgumentParser(
        description="🚀 GitHub Automation CLI Tool",
        prog="gh-automate"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # List repositories
    list_repos_parser = subparsers.add_parser("list-repos", help="List user repositories")
    list_repos_parser.add_argument("username", help="GitHub username")
    
    # Create issue
    create_issue_parser = subparsers.add_parser("create-issue", help="Create an issue")
    create_issue_parser.add_argument("repo", help="Repository (owner/repo)")
    create_issue_parser.add_argument("title", help="Issue title")
    create_issue_parser.add_argument("--body", default="", help="Issue description")
    
    # List issues
    list_issues_parser = subparsers.add_parser("list-issues", help="List repository issues")
    list_issues_parser.add_argument("repo", help="Repository (owner/repo)")
    
    # Close issue
    close_issue_parser = subparsers.add_parser("close-issue", help="Close an issue")
    close_issue_parser.add_argument("repo", help="Repository (owner/repo)")
    close_issue_parser.add_argument("issue_number", type=int, help="Issue number")

    # ⭐ NEW: Auto-label issue
    auto_label_parser = subparsers.add_parser("auto-label", help="Automatically label an issue based on keywords")
    auto_label_parser.add_argument("repo", help="Repository (owner/repo)")
    auto_label_parser.add_argument("issue_number", type=int, help="Issue number")
    auto_label_parser.add_argument("title", help="Issue title")
    auto_label_parser.add_argument("--body", default="", help="Issue description")

    args = parser.parse_args()
    
    try:
        if args.command == "list-repos":
            repos = gh.list_repositories(args.username)
            table = Table(title=f"Repositories for {args.username}")
            table.add_column("Name", style="cyan")
            table.add_column("Stars", style="yellow")
            table.add_column("URL", style="green")
            
            for repo in repos:
                table.add_row(
                    repo["name"],
                    str(repo["stargazers_count"]),
                    repo["html_url"]
                )
            print(table)
        
        elif args.command == "create-issue":
            issue = gh.create_issue(args.repo, args.title, args.body)
            print(f"[bold green]✅ Created Issue #{issue['number']}[/bold green]")
            print(f"URL: {issue['html_url']}")
        
        elif args.command == "list-issues":
            issues = gh.list_issues(args.repo)
            if not issues:
                print("[yellow]No issues found[/yellow]")
            else:
                table = Table(title=f"Issues in {args.repo}")
                table.add_column("#", style="cyan")
                table.add_column("Title", style="green")
                table.add_column("State", style="yellow")
                
                for issue in issues:
                    table.add_row(
                        str(issue["number"]),
                        issue["title"],
                        issue["state"]
                    )
                print(table)
        
        elif args.command == "close-issue":
            result = gh.close_issue(args.repo, args.issue_number)
            print(f"[bold red]✅ Closed Issue #{result['number']}[/bold red]")

        # ⭐ NEW: Auto-label issue handler
        elif args.command == "auto-label":
            result = gh.auto_label_issue(
                args.repo,
                args.issue_number,
                args.title,
                args.body
            )

            if "message" in result and result["message"] == "No labels matched":
                print("[yellow]⚠ No matching labels found[/yellow]")
            else:
                print("[bold green]🏷️ Labels applied successfully![/bold green]")
                print(result)

        else:
            parser.print_help()
    
    except Exception as e:
        print(f"[bold red]❌ Error: {str(e)}[/bold red]")

if __name__ == "__main__":
    main()
