"""
Display Module
Formats and displays scan results in a clean, readable format using Rich.
"""

from typing import List, Dict
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box


class ResultsDisplay:
    """
    Handles formatting and displaying scan results.
    
    This class uses the Rich library to create beautiful, color-coded
    console output that makes scan results easy to read and understand.
    """
    
    def __init__(self):
        """Initialize the display with a Rich console."""
        self.console = Console()
    
    def show_banner(self):
        """Display a welcome banner."""
        banner_text = """
   _   _                        
  | \\ | |_ __ ___   __ _ _ __  
  |  \\| | '_ ` _ \\ / _` | '_ \\ 
  | |\\  | | | | | | (_| | |_) |
  |_| \\_|_| |_| |_|\\__,_| .__/ 
                        |_|    
   ____                   
  / ___|  ___ __ _ _ __  
  \\___ \\ / __/ _` | '_ \\ 
   ___) | (_| (_| | | | |
  |____/ \\___\\__,_|_| |_|
                         
   _                _                     
  / \\   _ __   __ _| |_   _ _______ _ __ 
 / _ \\ | '_ \\ / _` | | | | |_  / _ \\ '__|
/ ___ \\| | | | (_| | | |_| |/ /  __/ |   
\\_/   \\_\\_| |_|\\__,_|_|\\__, /___\\___|_|   
                       |___/              
        """
        self.console.print(banner_text, style="bold cyan")
        self.console.print("=" * 60, style="cyan")
        self.console.print()
    
    def show_scan_info(self, scan_info: Dict):
        """
        Display general scan information.
        
        Args:
            scan_info (Dict): Scan metadata
        """
        self.console.print("\n[bold yellow]📋 Scan Information[/bold yellow]")
        self.console.print(f"  Scanner: {scan_info.get('scanner', 'N/A')}")
        self.console.print(f"  Version: {scan_info.get('version', 'N/A')}")
        self.console.print(f"  Start Time: {scan_info.get('start_time', 'N/A')}")
        self.console.print(f"  Command: {scan_info.get('command', 'N/A')}")
        self.console.print()
    
    def show_hosts_summary(self, hosts: List[Dict]):
        """
        Display a summary of scanned hosts.
        
        Args:
            hosts (List[Dict]): List of host data
        """
        up_hosts = sum(1 for h in hosts if h['status'] == 'up')
        down_hosts = len(hosts) - up_hosts
        
        self.console.print(f"[bold green]✓[/bold green] Total Hosts: {len(hosts)}")
        self.console.print(f"[bold green]✓[/bold green] Hosts Up: {up_hosts}")
        self.console.print(f"[bold red]✗[/bold red] Hosts Down: {down_hosts}")
        self.console.print()
    
    def show_host_details(self, host: Dict, host_number: int):
        """
        Display detailed information for a single host.
        
        Args:
            host (Dict): Host data
            host_number (int): Host number for display
        """
        # Create host header
        status_color = "green" if host['status'] == 'up' else "red"
        status_symbol = "✓" if host['status'] == 'up' else "✗"
        
        header = f"[bold]Host #{host_number}: {host['ip']}[/bold]"
        if host['hostname'] != 'N/A':
            header += f" ({host['hostname']})"
        
        self.console.print(f"\n{header}")
        self.console.print(f"[{status_color}]{status_symbol} Status: {host['status'].upper()}[/{status_color}]")
        
        # Show ports if host is up
        if host['status'] == 'up' and host['ports']:
            self.console.print(f"[bold cyan]Open Ports: {len(host['ports'])}[/bold cyan]")
            self._show_ports_table(host['ports'])
        elif host['status'] == 'up':
            self.console.print("[yellow]No open ports found[/yellow]")
        
        self.console.print("─" * 60)
    
    def _show_ports_table(self, ports: List[Dict]):
        """
        Display a table of open ports.
        
        Args:
            ports (List[Dict]): List of port data
        """
        # Create a table for ports
        table = Table(box=box.SIMPLE, show_header=True, header_style="bold magenta")
        table.add_column("Port", style="cyan", width=10)
        table.add_column("Service", style="green", width=15)
        table.add_column("Product", style="yellow", width=20)
        table.add_column("Version", style="blue", width=15)
        
        for port in ports:
            table.add_row(
                f"{port['port']}/{port['protocol']}",
                port['service'],
                port['product'],
                port['version']
            )
        
        self.console.print(table)
    
    def show_service_explanation(self, port: Dict):
        """
        Display AI-powered explanation for a service.
        
        Args:
            port (Dict): Port data with explanation
        """
        explanation = port.get('explanation', {})
        
        if not explanation:
            return
        
        # Determine color based on risk level
        risk_level = explanation.get('risk_level', 'Unknown')
        if 'Critical' in risk_level:
            risk_color = "bold red"
        elif 'High' in risk_level:
            risk_color = "red"
        elif 'Medium' in risk_level:
            risk_color = "yellow"
        elif 'Low' in risk_level:
            risk_color = "green"
        else:
            risk_color = "white"
        
        # Create explanation panel
        content = f"""[bold]{explanation.get('name', 'Unknown Service')}[/bold]

[cyan]Purpose:[/cyan] {explanation.get('purpose', 'N/A')}

[cyan]Common Use:[/cyan] {explanation.get('common_use', 'N/A')}

[yellow]⚠️  Security Note:[/yellow] {explanation.get('security_note', 'N/A')}

[{risk_color}]Risk Level: {risk_level}[/{risk_color}]
        """
        
        panel = Panel(
            content.strip(),
            title=f"[bold]🤖 AI Explanation - Port {port['port']} ({port['service']})[/bold]",
            border_style="blue",
            padding=(1, 2)
        )
        
        self.console.print(panel)
        self.console.print()
    
    def show_security_summary(self, summary: Dict):
        """
        Display security summary with risk analysis.
        
        Args:
            summary (Dict): Security summary data
        """
        self.console.print("\n[bold yellow]🔒 Security Summary[/bold yellow]")
        self.console.print("=" * 60)
        
        self.console.print(f"\n[bold]Total Open Ports:[/bold] {summary['total_open_ports']}")
        
        # Show risk distribution
        self.console.print("\n[bold]Risk Distribution:[/bold]")
        risk_dist = summary['risk_distribution']
        
        if risk_dist['Critical'] > 0:
            self.console.print(f"  [bold red]Critical:[/bold red] {risk_dist['Critical']}")
        if risk_dist['High'] > 0:
            self.console.print(f"  [red]High:[/red] {risk_dist['High']}")
        if risk_dist['Medium'] > 0:
            self.console.print(f"  [yellow]Medium:[/yellow] {risk_dist['Medium']}")
        if risk_dist['Low'] > 0:
            self.console.print(f"  [green]Low:[/green] {risk_dist['Low']}")
        if risk_dist['Unknown'] > 0:
            self.console.print(f"  [white]Unknown:[/white] {risk_dist['Unknown']}")
        
        # Show critical services if any
        if summary['critical_services']:
            self.console.print("\n[bold red]⚠️  Critical Services Found:[/bold red]")
            for service in summary['critical_services']:
                self.console.print(
                    f"  • {service['host']}:{service['port']} - {service['service']}"
                )
        
        self.console.print()
    
    def show_error(self, error_message: str):
        """
        Display an error message.
        
        Args:
            error_message (str): Error message to display
        """
        self.console.print(f"\n[bold red]❌ Error:[/bold red] {error_message}\n")
    
    def show_success(self, message: str):
        """
        Display a success message.
        
        Args:
            message (str): Success message to display
        """
        self.console.print(f"\n[bold green]✓ {message}[/bold green]\n")
