"""Run MultiQC in a child Python."""
import subprocess
import sys


def run_multiqc(config, title, dirs, outdir):
    cmd = [sys.executable, "-I", "-m", "multiqc", "--force", "--no-ansi", "--outdir", outdir, "--filename", "multiqc_report.html"]
    if config:
        cmd += ["--config", config]
    if title:
        cmd += ["--title", title]
    try:
        r = subprocess.run(cmd + list(dirs), capture_output=True, text=True)
    except OSError as e:
        raise RuntimeError("multiqc: cannot run %s: %s" % (sys.executable, e))
    if r.returncode != 0:
        raise RuntimeError("multiqc failed (status %d):\n%s" % (r.returncode, r.stderr[-4000:]))
    return None
