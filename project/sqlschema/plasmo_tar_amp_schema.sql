

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TargetInfo" (
	target_id TEXT NOT NULL, 
	gene_id TEXT, 
	PRIMARY KEY (target_id, gene_id)
);
