import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import Optional
from models import Vendor, SearchFilters
from data import get_vendors, get_vendor_by_id, generate_requirement_template

app = typer.Typer(help="CLI tool to find and evaluate reliable outsourcing vendors for startups")
console = Console()

@app.command()
def search(
    skill: Optional[str] = typer.Option(None, help="Filter by skill (e.g., AI, Web, Mobile)"),
    min_rating: Optional[float] = typer.Option(None, help="Minimum rating (0-5)"),
    min_projects: Optional[int] = typer.Option(None, help="Minimum completed projects")
):
    """Search and filter outsourcing vendors"""
    filters = SearchFilters(skill=skill, min_rating=min_rating, min_projects=min_projects)
    vendors = get_vendors(filters)
    
    if not vendors:
        console.print("[yellow]No vendors found matching your criteria[/yellow]")
        return
    
    table = Table(title="Available Vendors")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Skills", style="blue")
    table.add_column("Rating", style="yellow")
    table.add_column("Projects", style="magenta")
    table.add_column("Price Range", style="white")
    
    for vendor in vendors:
        table.add_row(
            str(vendor.id),
            vendor.name,
            ", ".join(vendor.skills[:3]),
            f"{vendor.rating:.1f}/5.0",
            str(vendor.completed_projects),
            vendor.price_range
        )
    
    console.print(table)
    console.print(f"\n[green]Found {len(vendors)} vendors[/green]")
    console.print("[dim]Use 'vendor-scout detail <ID>' to see more information[/dim]")

@app.command()
def detail(vendor_id: int = typer.Argument(..., help="Vendor ID to view details")):
    """View detailed information about a specific vendor"""
    vendor = get_vendor_by_id(vendor_id)
    
    if not vendor:
        console.print(f"[red]Vendor with ID {vendor_id} not found[/red]")
        raise typer.Exit(1)
    
    console.print(Panel(f"[bold green]{vendor.name}[/bold green]", expand=False))
    console.print(f"\n[cyan]Rating:[/cyan] {vendor.rating}/5.0 ⭐")
    console.print(f"[cyan]Completed Projects:[/cyan] {vendor.completed_projects}")
    console.print(f"[cyan]Price Range:[/cyan] {vendor.price_range}")
    console.print(f"[cyan]Location:[/cyan] {vendor.location}")
    console.print(f"\n[cyan]Skills:[/cyan] {', '.join(vendor.skills)}")
    console.print(f"\n[cyan]Description:[/cyan]\n{vendor.description}")
    
    if vendor.reviews:
        console.print("\n[bold yellow]Recent Reviews:[/bold yellow]")
        for review in vendor.reviews[:3]:
            console.print(f"\n  [green]★ {review.rating}/5.0[/green] - {review.project_type}")
            console.print(f"  [dim]{review.comment}[/dim]")

@app.command()
def template(
    output: str = typer.Option("requirement.md", help="Output file name"),
    project_type: str = typer.Option("AI", help="Project type (AI, Web, Mobile, etc.)")
):
    """Generate a standardized project requirement document template"""
    content = generate_requirement_template(project_type)
    
    with open(output, "w") as f:
        f.write(content)
    
    console.print(f"[green]✓ Template generated: {output}[/green]")
    console.print(f"[dim]Edit this file and share it with potential vendors[/dim]")

if __name__ == "__main__":
    app()
