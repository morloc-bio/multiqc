# Reports for the multiqc suite.
import json
import os
import tempfile


def tmp_dir():
    return tempfile.mkdtemp(prefix="multiqc-test-")


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)
    return None


def check_report(outdir, sample):
    """'' when MultiQC wrote a report and its salmon table has `sample`."""
    if not os.path.exists(os.path.join(outdir, "multiqc_report.html")):
        return "no multiqc_report.html"
    data = os.path.join(outdir, "multiqc_report_data")
    p = os.path.join(data, "multiqc_salmon.txt")
    if not os.path.exists(p):
        return "no salmon table in %r" % sorted(os.listdir(data))
    with open(p) as f:
        rows = [l.split("\t")[0] for l in f][1:]
    if rows != [sample]:
        return "salmon samples: %r" % rows
    return ""
