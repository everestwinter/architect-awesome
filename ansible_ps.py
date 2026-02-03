import logging
import shlex
import subprocess

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s - %(message)s"

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger("ansible_ps")

ansible_processes = {"ansible主机名": ["aaa.jar", "nginx"]}


def fetch_process_count(host: str, process_name: str) -> int:
    command = f"ansible {shlex.quote(host)} -m shell -a {shlex.quote(f'pgrep -fc {process_name}') }"
    result = subprocess.run(
        command,
        shell=True,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        logger.error("获取进程数量失败: %s %s", host, result.stderr.strip())
        return 0
    for line in result.stdout.splitlines():
        if line.strip().isdigit():
            return int(line.strip())
    logger.error("无法解析进程数量: %s %s", host, result.stdout.strip())
    return 0


host_count = len(ansible_processes)
logger.info("ansible主机数量: %s", host_count)

for host, processes in ansible_processes.items():
    for process_name in processes:
        process_count = fetch_process_count(host, process_name)
        logger.info("%s %s %s", host, process_name, process_count)
