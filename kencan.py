import datetime
import subprocess
import xmltodict


class KenCan(object):
    """KenCan scanner."""
    def __init__(self):
        self.data = None
        self.err = None
        self.xml_dict = []
        self.refresh()

    def get_lan_hosts(self):
        host_dict = []
        for host in self.xml_dict['nmaprun']['host']:
            hostname = None
            if host['hostnames'] is not None:
                hostname = host['hostnames']['hostname']['@name']
            host_dict.append({
                'status': host['status']['@state'],
                'ip': host['address']['@addr'],
                'hostname': hostname,
            })
        return host_dict

    def get_search_exec_time(self):
        return self.xml_dict['nmaprun']['runstats']['finished']['@elapsed']

    def get_search_finished_time(self):
        data = self.xml_dict['nmaprun']['runstats']['finished']['@time']
        return datetime.datetime.fromtimestamp(int(data))

    def get_hosts_amount(self):
        return self.xml_dict['nmaprun']['runstats']['hosts']['@up']

    def get_nmap_version(self):
        return self.xml_dict['nmaprun']['@version']

    def refresh(self):
        self.data, self.err = subprocess.Popen(
            ['nmap', '-sP', '192.168.1.1/24', '-oX', '-'], stdout=subprocess.PIPE
        ).communicate()
        self.xml_dict = xmltodict.parse(self.data)

    def scan_ip_services(self, ip_addr):
        self.data, self.err = subprocess.Popen(
            ['nmap', ip_addr, '-oX', '-'], stdout=subprocess.PIPE
        ).communicate()
        data_dict = xmltodict.parse(self.data)
        result_dict = []
        for port in data_dict['nmaprun']['host']['ports']['port']:
            result_dict.append({
                'protocol': port['@protocol'],
                'port': port['@portid'],
                'state': port['state']['@state'],
                'service': port['service']['@name']
            })
        return result_dict

    def get_db_data(self):
        return {
            'time': self.get_search_finished_time(),
            'amount': self.get_hosts_amount(),
            'execution': self.get_search_exec_time(),
        }
