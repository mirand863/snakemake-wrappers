# Wrapper for bcftools call.

## Example:

```
rule bcftools_call:
    input:
        fasta="genome.fasta",
        bams=expand("mapped/{sample}.sorted.bam", sample=config["samples"]),
        bais=expand("mapped/{sample}.sorted.bam.bai", sample=config["samples"])
    output:
        bam="called/{region}.bcf"  # region as expected by samtools mpileup (chr:start-stop)
    params:
        mpileup=""  # optional params for samtools mpileup
        call=""  # optional params for bcftools call
    script:
        "ce8c887/bio/bcftools_call"
```