# Auto generated from plasmo_tar_amp_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T14:26:12
# Schema: plasmo-tar-amp-schema
#
# id: https://plasmogenepi.github.io/plasmo-tar-amp-schema
# description: Schema for defining the results to a targeted amplicon analysis performed on plasmodium
# license: GNU GPL v3.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PLASMO_TAR_AMP_SCHEMA = CurieNamespace('plasmo_tar_amp_schema', 'https://plasmogenepi.github.io/plasmo-tar-amp-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = PLASMO_TAR_AMP_SCHEMA


# Types

# Class references



@dataclass
class TargetInfo(YAMLRoot):
    """
    Information about a specific target within a genome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.TargetInfo
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:TargetInfo"
    class_name: ClassVar[str] = "TargetInfo"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.TargetInfo

    target_id: str = None
    target_genome: Union[dict, "GenomeInfo"] = None
    gene_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.target_id):
            self.MissingRequiredField("target_id")
        if not isinstance(self.target_id, str):
            self.target_id = str(self.target_id)

        if self._is_empty(self.target_genome):
            self.MissingRequiredField("target_genome")
        if not isinstance(self.target_genome, GenomeInfo):
            self.target_genome = GenomeInfo(**as_dict(self.target_genome))

        if self.gene_id is not None and not isinstance(self.gene_id, str):
            self.gene_id = str(self.gene_id)

        super().__post_init__(**kwargs)


@dataclass
class GenomeInfo(YAMLRoot):
    """
    information on a genome
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.GenomeInfo
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:GenomeInfo"
    class_name: ClassVar[str] = "GenomeInfo"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.GenomeInfo

    name: str = None
    version: str = None
    taxon_id: str = None
    url: str = None
    gff_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.taxon_id):
            self.MissingRequiredField("taxon_id")
        if not isinstance(self.taxon_id, str):
            self.taxon_id = str(self.taxon_id)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self.gff_url is not None and not isinstance(self.gff_url, str):
            self.gff_url = str(self.gff_url)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.targetInfo__target_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.target_id, name="targetInfo__target_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('target_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.targetInfo__target_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.targetInfo__gene_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.gene_id, name="targetInfo__gene_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('gene_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.targetInfo__gene_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.targetInfo__target_genome = Slot(uri=PLASMO_TAR_AMP_SCHEMA.target_genome, name="targetInfo__target_genome", curie=PLASMO_TAR_AMP_SCHEMA.curie('target_genome'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.targetInfo__target_genome, domain=None, range=Union[dict, GenomeInfo])

slots.genomeInfo__name = Slot(uri=PLASMO_TAR_AMP_SCHEMA.name, name="genomeInfo__name", curie=PLASMO_TAR_AMP_SCHEMA.curie('name'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__name, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.genomeInfo__version = Slot(uri=PLASMO_TAR_AMP_SCHEMA.version, name="genomeInfo__version", curie=PLASMO_TAR_AMP_SCHEMA.curie('version'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__version, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.genomeInfo__taxon_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.taxon_id, name="genomeInfo__taxon_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('taxon_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__taxon_id, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]$'))

slots.genomeInfo__url = Slot(uri=PLASMO_TAR_AMP_SCHEMA.url, name="genomeInfo__url", curie=PLASMO_TAR_AMP_SCHEMA.curie('url'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__url, domain=None, range=str,
                   pattern=re.compile(r'r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"'))

slots.genomeInfo__gff_url = Slot(uri=PLASMO_TAR_AMP_SCHEMA.gff_url, name="genomeInfo__gff_url", curie=PLASMO_TAR_AMP_SCHEMA.curie('gff_url'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__gff_url, domain=None, range=Optional[str],
                   pattern=re.compile(r'r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"'))