import subprocess

def allow_traffic(src_ip, src_port, dst_ip, dst_port, protocol):
    subprocess.run(["iptables", "-A", "INPUT", "-p", protocol, "--src", src_ip, "--sport", str(src_port), "--dst", dst_ip, "--dport", str(dst_port), "-j", "ACCEPT"])

def deny_traffic(src_ip, src_port, dst_ip, dst_port, protocol):
    subprocess.run(["iptables", "-A", "INPUT", "-p", protocol, "--src", src_ip, "--sport", str(src_port), "--dst", dst_ip, "--dport", str(dst_port), "-j", "DROP"])
