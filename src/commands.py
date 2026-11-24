import subprocess


def lookup_host(hostname: str) -> str:
    # Fixture: caller-controlled text is interpolated into a shell command.
    return subprocess.check_output(["nslookup", hostname], text=True)
