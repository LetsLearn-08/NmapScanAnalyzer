"""
Service Analyzer Module
Provides AI-powered explanations for discovered services using a local dictionary.
"""

from typing import Dict, List


class ServiceAnalyzer:
    """
    Analyzes services and provides AI-powered explanations.
    
    This class uses a curated dictionary of common services to provide
    beginner-friendly explanations about what each service does and
    potential security considerations.
    """
    
    # AI-powered service explanation dictionary
    # This is our "local AI" - a curated knowledge base of common services
    SERVICE_DICTIONARY = {
        'ssh': {
            'name': 'SSH (Secure Shell)',
            'purpose': 'Allows secure remote login and command execution on the server',
            'common_use': 'System administrators use this to remotely manage servers',
            'security_note': 'Should use strong passwords or key-based authentication',
            'risk_level': 'Low (if configured properly)'
        },
        'http': {
            'name': 'HTTP (Web Server)',
            'purpose': 'Serves websites and web applications over unencrypted connections',
            'common_use': 'Hosting websites, APIs, and web services',
            'security_note': 'Data is sent unencrypted - consider using HTTPS instead',
            'risk_level': 'Medium (unencrypted traffic)'
        },
        'https': {
            'name': 'HTTPS (Secure Web Server)',
            'purpose': 'Serves websites and web applications over encrypted SSL/TLS connections',
            'common_use': 'Secure hosting of websites, APIs, and web services',
            'security_note': 'Uses encryption to protect data in transit',
            'risk_level': 'Low (encrypted traffic)'
        },
        'ftp': {
            'name': 'FTP (File Transfer Protocol)',
            'purpose': 'Transfers files between computers over a network',
            'common_use': 'Uploading/downloading files to/from servers',
            'security_note': 'Transmits passwords in plain text - use SFTP or FTPS instead',
            'risk_level': 'High (insecure protocol)'
        },
        'smtp': {
            'name': 'SMTP (Email Server)',
            'purpose': 'Sends and routes email messages between mail servers',
            'common_use': 'Email delivery and relay',
            'security_note': 'Should be configured to prevent unauthorized relay',
            'risk_level': 'Medium (potential spam relay)'
        },
        'mysql': {
            'name': 'MySQL Database',
            'purpose': 'Manages and serves database queries for applications',
            'common_use': 'Backend database for websites and applications',
            'security_note': 'Should not be exposed to the internet - use firewall rules',
            'risk_level': 'High (if publicly accessible)'
        },
        'postgresql': {
            'name': 'PostgreSQL Database',
            'purpose': 'Advanced relational database management system',
            'common_use': 'Backend database for enterprise applications',
            'security_note': 'Should not be exposed to the internet - use firewall rules',
            'risk_level': 'High (if publicly accessible)'
        },
        'dns': {
            'name': 'DNS (Domain Name System)',
            'purpose': 'Translates domain names to IP addresses',
            'common_use': 'Name resolution for networks',
            'security_note': 'Should be configured to prevent DNS amplification attacks',
            'risk_level': 'Medium (potential for abuse)'
        },
        'telnet': {
            'name': 'Telnet',
            'purpose': 'Provides remote command-line access (unencrypted)',
            'common_use': 'Legacy remote access protocol',
            'security_note': 'Extremely insecure - transmits everything in plain text. Use SSH instead!',
            'risk_level': 'Critical (obsolete and insecure)'
        },
        'rdp': {
            'name': 'RDP (Remote Desktop Protocol)',
            'purpose': 'Allows remote graphical desktop access to Windows systems',
            'common_use': 'Remote administration of Windows servers and desktops',
            'security_note': 'Frequently targeted by attackers - use strong passwords and MFA',
            'risk_level': 'High (common attack target)'
        },
        'smb': {
            'name': 'SMB (File Sharing)',
            'purpose': 'Windows file and printer sharing protocol',
            'common_use': 'Network file shares in Windows environments',
            'security_note': 'Has been exploited by major ransomware - keep updated',
            'risk_level': 'High (vulnerable if outdated)'
        },
        'mongodb': {
            'name': 'MongoDB Database',
            'purpose': 'NoSQL document database for modern applications',
            'common_use': 'Backend database for web and mobile apps',
            'security_note': 'Many instances are found exposed without authentication',
            'risk_level': 'High (if publicly accessible)'
        },
        'redis': {
            'name': 'Redis Cache',
            'purpose': 'In-memory data structure store used as cache or message broker',
            'common_use': 'Application caching and session storage',
            'security_note': 'Should only be accessible from localhost or trusted networks',
            'risk_level': 'High (if publicly accessible)'
        },
        'elasticsearch': {
            'name': 'Elasticsearch',
            'purpose': 'Search and analytics engine for large datasets',
            'common_use': 'Log analysis, full-text search, and data analytics',
            'security_note': 'Often exposed without authentication - can leak sensitive data',
            'risk_level': 'High (if publicly accessible)'
        },
        'vnc': {
            'name': 'VNC (Virtual Network Computing)',
            'purpose': 'Remote desktop access protocol (cross-platform)',
            'common_use': 'Remote graphical access to Linux/Windows systems',
            'security_note': 'Weak encryption by default - tunnel through SSH or VPN',
            'risk_level': 'High (weak security)'
        }
    }
    
    def __init__(self):
        """Initialize the Service Analyzer."""
        pass
    
    def get_service_explanation(self, service_name: str) -> Dict[str, str]:
        """
        Get AI-powered explanation for a service.
        
        Args:
            service_name (str): Name of the service (e.g., 'ssh', 'http')
            
        Returns:
            Dict: Dictionary containing service explanation
        """
        # Normalize service name to lowercase
        service_name = service_name.lower()
        
        # Check if we have an explanation for this service
        if service_name in self.SERVICE_DICTIONARY:
            return self.SERVICE_DICTIONARY[service_name]
        else:
            # Return a generic explanation for unknown services
            return {
                'name': service_name.upper(),
                'purpose': 'Service details not in our knowledge base',
                'common_use': 'Check online documentation for this service',
                'security_note': 'Research security best practices for this service',
                'risk_level': 'Unknown'
            }
    
    def analyze_host(self, host_data: Dict) -> Dict:
        """
        Analyze all services on a host and add explanations.
        
        Args:
            host_data (Dict): Host information from the parser
            
        Returns:
            Dict: Enhanced host data with service explanations
        """
        # Add explanations to each port/service
        for port in host_data.get('ports', []):
            service_name = port.get('service', 'unknown')
            port['explanation'] = self.get_service_explanation(service_name)
        
        return host_data
    
    def get_security_summary(self, hosts: List[Dict]) -> Dict:
        """
        Generate a security summary for all scanned hosts.
        
        Args:
            hosts (List[Dict]): List of analyzed hosts
            
        Returns:
            Dict: Security summary with risk statistics
        """
        risk_counts = {
            'Critical': 0,
            'High': 0,
            'Medium': 0,
            'Low': 0,
            'Unknown': 0
        }
        
        total_open_ports = 0
        critical_services = []
        
        for host in hosts:
            for port in host.get('ports', []):
                total_open_ports += 1
                explanation = port.get('explanation', {})
                risk_level = explanation.get('risk_level', 'Unknown')
                
                # Extract risk level category
                if 'Critical' in risk_level:
                    risk_counts['Critical'] += 1
                    critical_services.append({
                        'host': host['ip'],
                        'port': port['port'],
                        'service': port['service']
                    })
                elif 'High' in risk_level:
                    risk_counts['High'] += 1
                elif 'Medium' in risk_level:
                    risk_counts['Medium'] += 1
                elif 'Low' in risk_level:
                    risk_counts['Low'] += 1
                else:
                    risk_counts['Unknown'] += 1
        
        return {
            'total_open_ports': total_open_ports,
            'risk_distribution': risk_counts,
            'critical_services': critical_services
        }
