import subprocess

class KenCan():
    """KenCan scanner."""
    def __init__(self):
        self.devices_ips = []
        self.data, self.err = subprocess.Popen(['nmap', '-sP', '192.168.1.1/24'], stdout=subprocess.PIPE).communicate()

    def scan_network(self):
        for line in self.data.splitlines():
            if line.startswith(b'Nmap scan report for'):
                line_data = line.decode("utf-8").split()
                domain = ''
                if len(line_data) > 5:
                    domain = line_data[4]
                    ip = line_data[5].replace('(', '').replace(')', '')
                ip = line_data[4]
                self.devices_ips.append({
                    'ip': ip,
                    'domain': domain
                })
            if line.startswith(b'Nmap done: '):
                line_data = line.decode("utf-8").split()
                device_amount = line_data[5].replace('(', '')
                time = line_data[10]
        return {
            'devices': device_amount,
            'time': time
        }

    def get_devices_ips(self):
        return self.devices_ips