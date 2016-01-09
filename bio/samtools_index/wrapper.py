__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


prefix = os.path.splitext(snakemake.output.bam)[0]

shell("samtools index {snakemake.input.bam} {snakemake.output.bai}")
