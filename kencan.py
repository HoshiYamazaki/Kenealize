import subprocess

data, err = subprocess.Popen(['nmap', '-sP', '192.168.1.1/24'], stdout=subprocess.PIPE).communicate()

devices_ips = []

for line in data.splitlines():
    if line.startswith(b'Nmap scan report for'):
        line_data = line.decode("utf-8").split()
        domain = ''
        if len(line_data) > 5:
            domain = line_data[4]
            ip = line_data[5].replace('(', '').replace(')', '')
        ip = line_data[4]
        devices_ips.append({
            'ip': ip,
            'domain': domain
        })
    if line.startswith(b'Nmap done: '):
        line_data = line.decode("utf-8").split()
        device_amount = line_data[5].replace('(', '')
        time = line_data[10]

print({
    'devices': device_amount,
    'time': time
})

print(devices_ips)
