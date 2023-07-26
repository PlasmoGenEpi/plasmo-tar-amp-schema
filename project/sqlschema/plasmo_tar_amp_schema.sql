

CREATE TABLE "TargetInfo" (
	target_id TEXT NOT NULL, 
	gene_id TEXT, 
	PRIMARY KEY (target_id, gene_id)
);
