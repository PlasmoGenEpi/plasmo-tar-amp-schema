

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

CREATE TABLE "TargetInfo" (
	target_id TEXT NOT NULL, 
	gene_id TEXT, 
	target_genome TEXT NOT NULL, 
	insert_location TEXT NOT NULL, 
	forward_primers TEXT NOT NULL, 
	reverse_primers TEXT NOT NULL, 
	PRIMARY KEY (target_id, gene_id, target_genome, insert_location, forward_primers, reverse_primers)
);
