

CREATE TABLE "BioMethod" (
	program TEXT NOT NULL, 
	purpose TEXT NOT NULL, 
	additional_argument TEXT, 
	PRIMARY KEY (program, purpose, additional_argument)
);

CREATE TABLE "GenomeInfo" (
	name TEXT NOT NULL, 
	version TEXT NOT NULL, 
	taxon_id INTEGER NOT NULL, 
	url TEXT NOT NULL, 
	gff_url TEXT, 
	PRIMARY KEY (name, version, taxon_id, url, gff_url)
);

CREATE TABLE "GenomicLocation" (
	chrom TEXT NOT NULL, 
	start INTEGER NOT NULL, 
	"end" INTEGER NOT NULL, 
	strand TEXT, 
	PRIMARY KEY (chrom, start, "end", strand)
);

CREATE TABLE "HaplotypeInfo" (
	haplotype_id TEXT NOT NULL, 
	target_id TEXT NOT NULL, 
	alt_annotations TEXT, 
	PRIMARY KEY (haplotype_id, target_id, alt_annotations)
);

CREATE TABLE "HaplotypesDetected" (
	sequencing_id TEXT NOT NULL, 
	bioinformatics_id TEXT NOT NULL, 
	samples TEXT NOT NULL, 
	PRIMARY KEY (sequencing_id, bioinformatics_id, samples)
);

CREATE TABLE "HaplotypesForSample" (
	sample_id TEXT NOT NULL, 
	target_results TEXT NOT NULL, 
	PRIMARY KEY (sample_id, target_results)
);

CREATE TABLE "HaplotypesForTarget" (
	target_id TEXT NOT NULL, 
	haplotype_ids TEXT NOT NULL, 
	read_counts FLOAT NOT NULL, 
	umi_counts FLOAT, 
	PRIMARY KEY (target_id, haplotype_ids, read_counts, umi_counts)
);

CREATE TABLE "PanelInfo" (
	panel_id TEXT NOT NULL, 
	targets TEXT NOT NULL, 
	PRIMARY KEY (panel_id, targets)
);

CREATE TABLE "PrimerInfo" (
	seq TEXT NOT NULL, 
	location TEXT NOT NULL, 
	PRIMARY KEY (seq, location)
);

CREATE TABLE "Primers" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "RepresentativeHaplotypeSequence" (
	haplotype_id TEXT NOT NULL, 
	seq TEXT NOT NULL, 
	quality TEXT, 
	PRIMARY KEY (haplotype_id, seq, quality)
);

CREATE TABLE "SequencingInfo" (
	seq_instrument TEXT NOT NULL, 
	seq_date TEXT NOT NULL, 
	nucl_acid_ext TEXT NOT NULL, 
	nucl_acid_amp TEXT NOT NULL, 
	nucl_acid_date TEXT NOT NULL, 
	pcr_cond TEXT NOT NULL, 
	lib_screen TEXT NOT NULL, 
	lib_layout TEXT NOT NULL, 
	lib_kit TEXT NOT NULL, 
	seq_center TEXT NOT NULL, 
	PRIMARY KEY (seq_instrument, seq_date, nucl_acid_ext, nucl_acid_amp, nucl_acid_date, pcr_cond, lib_screen, lib_layout, lib_kit, seq_center)
);

CREATE TABLE "TarAmpBioinformaticsInfo" (
	demultiplexing_method TEXT NOT NULL, 
	denoising_method TEXT NOT NULL, 
	population_clustering_method TEXT NOT NULL, 
	additional_methods TEXT, 
	PRIMARY KEY (demultiplexing_method, denoising_method, population_clustering_method, additional_methods)
);

CREATE TABLE "TargetInfo" (
	target_id TEXT NOT NULL, 
	gene_id TEXT, 
	target_genome TEXT NOT NULL, 
	insert_location TEXT NOT NULL, 
	forward_primers TEXT NOT NULL, 
	reverse_primers TEXT NOT NULL, 
	PRIMARY KEY (target_id, gene_id, target_genome, insert_location, forward_primers, reverse_primers)
);
