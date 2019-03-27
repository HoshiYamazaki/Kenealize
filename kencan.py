import subprocess


class KenCan(object):
    """KenCan scanner."""
    def __init__(self):
        self.devices_ips = []
        self.data, self.err = subprocess.Popen(
            ['nmap', '-sP', '192.168.1.1/24'], stdout=subprocess.PIPE
        ).communicate()

    def scan_network(self):
        for line in self.data.splitlines():
            if line.startswith(b'Nmap scan report for'):
                line_data = line.decode("utf-8").split()
                domain = ''
                ip = line_data[4]
                if len(line_data) > 5:
                    domain = line_data[4]
                    ip = line_data[5].replace('(', '').replace(')', '')
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

    def scan_device(self, ip):
        self.data, self.err = subprocess.Popen(['nmap', ip], stdout=subprocess.PIPE).communicate()
        scanned_ports = []
        for line in self.data.splitlines():
            if line.startswith(b'Host is up '):
                line_data = line.decode('utf-8').split()
                latency = line_data[3].replace('(', '')
            if b'/tcp' in line or b'/udp' in line:
                line_data = line.decode('utf-8').split()
                print(line_data)
                scanned_ports.append({
                    'port': line_data[0],
                    'state:': line_data[1],
                    'service': line_data[2]
                })
            if line.startswith(b'MAC Address: '):
                line_data = line.decode('utf-8').split()
                mac_addr = line_data[2]
            if line.startswith(b'Nmap done: '):
                line_data = line.decode('utf-8').split()
                time = line_data[10]
        return {
            'data': scanned_ports,
            'latency': latency,
            'mac': mac_addr,
            'time': time,
        }
