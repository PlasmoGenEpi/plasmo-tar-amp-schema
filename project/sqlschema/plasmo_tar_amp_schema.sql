

CREATE TABLE "GenomeInfo" (
	name TEXT NOT NULL, 
	version TEXT NOT NULL, 
	taxon_id INTEGER NOT NULL, 
	url TEXT NOT NULL, 
	gff_url TEXT, 
	PRIMARY KEY (name, version, taxon_id, url, gff_url)
);

CREATE TABLE "TargetInfo" (
	target_id TEXT NOT NULL, 
	gene_id TEXT, 
	target_genome TEXT NOT NULL, 
	PRIMARY KEY (target_id, gene_id, target_genome)
);
