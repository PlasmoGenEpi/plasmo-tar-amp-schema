# Auto generated from plasmo_tar_amp_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-09T20:08:00
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
from linkml_runtime.linkml_model.types import Double, Integer, String

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
    insert_location: Union[dict, "GenomicLocation"] = None
    forward_primers: Union[dict, "Primers"] = None
    reverse_primers: Union[dict, "Primers"] = None
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

        if self._is_empty(self.insert_location):
            self.MissingRequiredField("insert_location")
        if not isinstance(self.insert_location, GenomicLocation):
            self.insert_location = GenomicLocation(**as_dict(self.insert_location))

        if self._is_empty(self.forward_primers):
            self.MissingRequiredField("forward_primers")
        if not isinstance(self.forward_primers, Primers):
            self.forward_primers = Primers(**as_dict(self.forward_primers))

        if self._is_empty(self.reverse_primers):
            self.MissingRequiredField("reverse_primers")
        if not isinstance(self.reverse_primers, Primers):
            self.reverse_primers = Primers(**as_dict(self.reverse_primers))

        if self.gene_id is not None and not isinstance(self.gene_id, str):
            self.gene_id = str(self.gene_id)

        super().__post_init__(**kwargs)


@dataclass
class PanelInfo(YAMLRoot):
    """
    information on a panel of targeted amplicon primer pairs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.PanelInfo
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:PanelInfo"
    class_name: ClassVar[str] = "PanelInfo"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.PanelInfo

    panel_id: str = None
    targets: Union[Union[dict, TargetInfo], List[Union[dict, TargetInfo]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.panel_id):
            self.MissingRequiredField("panel_id")
        if not isinstance(self.panel_id, str):
            self.panel_id = str(self.panel_id)

        if self._is_empty(self.targets):
            self.MissingRequiredField("targets")
        self._normalize_inlined_as_dict(slot_name="targets", slot_type=TargetInfo, key_name="target_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class RepresentativeHaplotypeSequence(YAMLRoot):
    """
    the representative sequence for a haplotype, similar to a fast(a/q) format
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.RepresentativeHaplotypeSequence
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:RepresentativeHaplotypeSequence"
    class_name: ClassVar[str] = "RepresentativeHaplotypeSequence"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.RepresentativeHaplotypeSequence

    haplotype_id: str = None
    seq: str = None
    quality: Optional[str] = None
    alt_annotations: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.haplotype_id):
            self.MissingRequiredField("haplotype_id")
        if not isinstance(self.haplotype_id, str):
            self.haplotype_id = str(self.haplotype_id)

        if self._is_empty(self.seq):
            self.MissingRequiredField("seq")
        if not isinstance(self.seq, str):
            self.seq = str(self.seq)

        if self.quality is not None and not isinstance(self.quality, str):
            self.quality = str(self.quality)

        if not isinstance(self.alt_annotations, list):
            self.alt_annotations = [self.alt_annotations] if self.alt_annotations is not None else []
        self.alt_annotations = [v if isinstance(v, str) else str(v) for v in self.alt_annotations]

        super().__post_init__(**kwargs)


@dataclass
class RepresentativeHaplotypeSequences(YAMLRoot):
    """
    a list of the representative sequence for a haplotypes, similar to a fast(a/q) format
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.RepresentativeHaplotypeSequences
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:RepresentativeHaplotypeSequences"
    class_name: ClassVar[str] = "RepresentativeHaplotypeSequences"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.RepresentativeHaplotypeSequences

    target_id: str = None
    seqs: Union[Union[dict, RepresentativeHaplotypeSequence], List[Union[dict, RepresentativeHaplotypeSequence]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.target_id):
            self.MissingRequiredField("target_id")
        if not isinstance(self.target_id, str):
            self.target_id = str(self.target_id)

        if self._is_empty(self.seqs):
            self.MissingRequiredField("seqs")
        if not isinstance(self.seqs, list):
            self.seqs = [self.seqs] if self.seqs is not None else []
        self.seqs = [v if isinstance(v, RepresentativeHaplotypeSequence) else RepresentativeHaplotypeSequence(**as_dict(v)) for v in self.seqs]

        super().__post_init__(**kwargs)


@dataclass
class HaplotypesDetected(YAMLRoot):
    """
    the haplotypes detected in a targeted amplicon analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.HaplotypesDetected
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:HaplotypesDetected"
    class_name: ClassVar[str] = "HaplotypesDetected"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.HaplotypesDetected

    sequencing_id: str = None
    bioinformatics_id: str = None
    samples: Union[Union[dict, "HaplotypesForSample"], List[Union[dict, "HaplotypesForSample"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequencing_id):
            self.MissingRequiredField("sequencing_id")
        if not isinstance(self.sequencing_id, str):
            self.sequencing_id = str(self.sequencing_id)

        if self._is_empty(self.bioinformatics_id):
            self.MissingRequiredField("bioinformatics_id")
        if not isinstance(self.bioinformatics_id, str):
            self.bioinformatics_id = str(self.bioinformatics_id)

        if self._is_empty(self.samples):
            self.MissingRequiredField("samples")
        if not isinstance(self.samples, list):
            self.samples = [self.samples] if self.samples is not None else []
        self.samples = [v if isinstance(v, HaplotypesForSample) else HaplotypesForSample(**as_dict(v)) for v in self.samples]

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
    taxon_id: int = None
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
        if not isinstance(self.taxon_id, int):
            self.taxon_id = int(self.taxon_id)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self.gff_url is not None and not isinstance(self.gff_url, str):
            self.gff_url = str(self.gff_url)

        super().__post_init__(**kwargs)


@dataclass
class GenomicLocation(YAMLRoot):
    """
    information on the genomic location of specific sequence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.GenomicLocation
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:GenomicLocation"
    class_name: ClassVar[str] = "GenomicLocation"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.GenomicLocation

    chrom: str = None
    start: int = None
    end: int = None
    strand: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.chrom):
            self.MissingRequiredField("chrom")
        if not isinstance(self.chrom, str):
            self.chrom = str(self.chrom)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        if self.strand is not None and not isinstance(self.strand, str):
            self.strand = str(self.strand)

        super().__post_init__(**kwargs)


@dataclass
class PrimerInfo(YAMLRoot):
    """
    information on a primer sequence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.PrimerInfo
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:PrimerInfo"
    class_name: ClassVar[str] = "PrimerInfo"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.PrimerInfo

    seq: str = None
    location: Union[dict, GenomicLocation] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.seq):
            self.MissingRequiredField("seq")
        if not isinstance(self.seq, str):
            self.seq = str(self.seq)

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, GenomicLocation):
            self.location = GenomicLocation(**as_dict(self.location))

        super().__post_init__(**kwargs)


@dataclass
class Primers(YAMLRoot):
    """
    A holder of primer sequences
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.Primers
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:Primers"
    class_name: ClassVar[str] = "Primers"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.Primers

    entries: Optional[Union[Union[dict, PrimerInfo], List[Union[dict, PrimerInfo]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=PrimerInfo, key_name="seq", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class HaplotypesForSample(YAMLRoot):
    """
    Haplotypes detected for a sample for all targets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.HaplotypesForSample
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:HaplotypesForSample"
    class_name: ClassVar[str] = "HaplotypesForSample"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.HaplotypesForSample

    sample_id: str = None
    target_results: Union[Union[dict, "HaplotypesForTarget"], List[Union[dict, "HaplotypesForTarget"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self._is_empty(self.target_results):
            self.MissingRequiredField("target_results")
        if not isinstance(self.target_results, list):
            self.target_results = [self.target_results] if self.target_results is not None else []
        self.target_results = [v if isinstance(v, HaplotypesForTarget) else HaplotypesForTarget(**as_dict(v)) for v in self.target_results]

        super().__post_init__(**kwargs)


@dataclass
class HaplotypesForTarget(YAMLRoot):
    """
    Haplotypes detected for a specific target
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.HaplotypesForTarget
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:HaplotypesForTarget"
    class_name: ClassVar[str] = "HaplotypesForTarget"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.HaplotypesForTarget

    target_id: str = None
    haplotype_ids: Union[str, List[str]] = None
    read_counts: Union[float, List[float]] = None
    umi_counts: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.target_id):
            self.MissingRequiredField("target_id")
        if not isinstance(self.target_id, str):
            self.target_id = str(self.target_id)

        if self._is_empty(self.haplotype_ids):
            self.MissingRequiredField("haplotype_ids")
        if not isinstance(self.haplotype_ids, list):
            self.haplotype_ids = [self.haplotype_ids] if self.haplotype_ids is not None else []
        self.haplotype_ids = [v if isinstance(v, str) else str(v) for v in self.haplotype_ids]

        if self._is_empty(self.read_counts):
            self.MissingRequiredField("read_counts")
        if not isinstance(self.read_counts, list):
            self.read_counts = [self.read_counts] if self.read_counts is not None else []
        self.read_counts = [v if isinstance(v, float) else float(v) for v in self.read_counts]

        if not isinstance(self.umi_counts, list):
            self.umi_counts = [self.umi_counts] if self.umi_counts is not None else []
        self.umi_counts = [v if isinstance(v, float) else float(v) for v in self.umi_counts]

        super().__post_init__(**kwargs)


@dataclass
class BioMethod(YAMLRoot):
    """
    methodology description of a portion of a bioinformatics pipeline
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.BioMethod
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:BioMethod"
    class_name: ClassVar[str] = "BioMethod"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.BioMethod

    program: str = None
    purpose: str = None
    additional_argument: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.program):
            self.MissingRequiredField("program")
        if not isinstance(self.program, str):
            self.program = str(self.program)

        if self._is_empty(self.purpose):
            self.MissingRequiredField("purpose")
        if not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        if not isinstance(self.additional_argument, list):
            self.additional_argument = [self.additional_argument] if self.additional_argument is not None else []
        self.additional_argument = [v if isinstance(v, str) else str(v) for v in self.additional_argument]

        super().__post_init__(**kwargs)


@dataclass
class TarAmpBioinformaticsInfo(YAMLRoot):
    """
    the targeted amplicon bioinformatics pipeline
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.TarAmpBioinformaticsInfo
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:TarAmpBioinformaticsInfo"
    class_name: ClassVar[str] = "TarAmpBioinformaticsInfo"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.TarAmpBioinformaticsInfo

    tar_amp_bioinformatics_info_id: str = None
    demultiplexing_method: Union[dict, BioMethod] = None
    denoising_method: Union[dict, BioMethod] = None
    population_clustering_method: Union[dict, BioMethod] = None
    additional_methods: Optional[Union[Union[dict, BioMethod], List[Union[dict, BioMethod]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.tar_amp_bioinformatics_info_id):
            self.MissingRequiredField("tar_amp_bioinformatics_info_id")
        if not isinstance(self.tar_amp_bioinformatics_info_id, str):
            self.tar_amp_bioinformatics_info_id = str(self.tar_amp_bioinformatics_info_id)

        if self._is_empty(self.demultiplexing_method):
            self.MissingRequiredField("demultiplexing_method")
        if not isinstance(self.demultiplexing_method, BioMethod):
            self.demultiplexing_method = BioMethod(**as_dict(self.demultiplexing_method))

        if self._is_empty(self.denoising_method):
            self.MissingRequiredField("denoising_method")
        if not isinstance(self.denoising_method, BioMethod):
            self.denoising_method = BioMethod(**as_dict(self.denoising_method))

        if self._is_empty(self.population_clustering_method):
            self.MissingRequiredField("population_clustering_method")
        if not isinstance(self.population_clustering_method, BioMethod):
            self.population_clustering_method = BioMethod(**as_dict(self.population_clustering_method))

        if not isinstance(self.additional_methods, list):
            self.additional_methods = [self.additional_methods] if self.additional_methods is not None else []
        self.additional_methods = [v if isinstance(v, BioMethod) else BioMethod(**as_dict(v)) for v in self.additional_methods]

        super().__post_init__(**kwargs)


@dataclass
class SequencingInfo(YAMLRoot):
    """
    Information on sequencing info
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.SequencingInfo
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:SequencingInfo"
    class_name: ClassVar[str] = "SequencingInfo"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.SequencingInfo

    sequencing_info_id: str = None
    seq_instrument: str = None
    seq_date: str = None
    nucl_acid_ext: str = None
    nucl_acid_amp: str = None
    nucl_acid_date: str = None
    pcr_cond: str = None
    lib_screen: str = None
    lib_layout: str = None
    lib_kit: str = None
    seq_center: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sequencing_info_id):
            self.MissingRequiredField("sequencing_info_id")
        if not isinstance(self.sequencing_info_id, str):
            self.sequencing_info_id = str(self.sequencing_info_id)

        if self._is_empty(self.seq_instrument):
            self.MissingRequiredField("seq_instrument")
        if not isinstance(self.seq_instrument, str):
            self.seq_instrument = str(self.seq_instrument)

        if self._is_empty(self.seq_date):
            self.MissingRequiredField("seq_date")
        if not isinstance(self.seq_date, str):
            self.seq_date = str(self.seq_date)

        if self._is_empty(self.nucl_acid_ext):
            self.MissingRequiredField("nucl_acid_ext")
        if not isinstance(self.nucl_acid_ext, str):
            self.nucl_acid_ext = str(self.nucl_acid_ext)

        if self._is_empty(self.nucl_acid_amp):
            self.MissingRequiredField("nucl_acid_amp")
        if not isinstance(self.nucl_acid_amp, str):
            self.nucl_acid_amp = str(self.nucl_acid_amp)

        if self._is_empty(self.nucl_acid_date):
            self.MissingRequiredField("nucl_acid_date")
        if not isinstance(self.nucl_acid_date, str):
            self.nucl_acid_date = str(self.nucl_acid_date)

        if self._is_empty(self.pcr_cond):
            self.MissingRequiredField("pcr_cond")
        if not isinstance(self.pcr_cond, str):
            self.pcr_cond = str(self.pcr_cond)

        if self._is_empty(self.lib_screen):
            self.MissingRequiredField("lib_screen")
        if not isinstance(self.lib_screen, str):
            self.lib_screen = str(self.lib_screen)

        if self._is_empty(self.lib_layout):
            self.MissingRequiredField("lib_layout")
        if not isinstance(self.lib_layout, str):
            self.lib_layout = str(self.lib_layout)

        if self._is_empty(self.lib_kit):
            self.MissingRequiredField("lib_kit")
        if not isinstance(self.lib_kit, str):
            self.lib_kit = str(self.lib_kit)

        if self._is_empty(self.seq_center):
            self.MissingRequiredField("seq_center")
        if not isinstance(self.seq_center, str):
            self.seq_center = str(self.seq_center)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenInfo(YAMLRoot):
    """
    Information on specimen info
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.SpecimenInfo
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:SpecimenInfo"
    class_name: ClassVar[str] = "SpecimenInfo"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.SpecimenInfo

    sample_name: str = None
    samp_taxon_id: int = None
    collection_date: str = None
    lat_lon: str = None
    collector: str = None
    samp_store_loc: str = None
    samp_collect_device: str = None
    project_name: str = None
    host_taxon_id: Optional[int] = None
    alternate_identifiers: Optional[Union[str, List[str]]] = empty_list()
    parasite_density: Optional[int] = None
    accession: Optional[str] = None
    sample_comments: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample_name):
            self.MissingRequiredField("sample_name")
        if not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self._is_empty(self.samp_taxon_id):
            self.MissingRequiredField("samp_taxon_id")
        if not isinstance(self.samp_taxon_id, int):
            self.samp_taxon_id = int(self.samp_taxon_id)

        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self._is_empty(self.lat_lon):
            self.MissingRequiredField("lat_lon")
        if not isinstance(self.lat_lon, str):
            self.lat_lon = str(self.lat_lon)

        if self._is_empty(self.collector):
            self.MissingRequiredField("collector")
        if not isinstance(self.collector, str):
            self.collector = str(self.collector)

        if self._is_empty(self.samp_store_loc):
            self.MissingRequiredField("samp_store_loc")
        if not isinstance(self.samp_store_loc, str):
            self.samp_store_loc = str(self.samp_store_loc)

        if self._is_empty(self.samp_collect_device):
            self.MissingRequiredField("samp_collect_device")
        if not isinstance(self.samp_collect_device, str):
            self.samp_collect_device = str(self.samp_collect_device)

        if self._is_empty(self.project_name):
            self.MissingRequiredField("project_name")
        if not isinstance(self.project_name, str):
            self.project_name = str(self.project_name)

        if self.host_taxon_id is not None and not isinstance(self.host_taxon_id, int):
            self.host_taxon_id = int(self.host_taxon_id)

        if not isinstance(self.alternate_identifiers, list):
            self.alternate_identifiers = [self.alternate_identifiers] if self.alternate_identifiers is not None else []
        self.alternate_identifiers = [v if isinstance(v, str) else str(v) for v in self.alternate_identifiers]

        if self.parasite_density is not None and not isinstance(self.parasite_density, int):
            self.parasite_density = int(self.parasite_density)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.sample_comments is not None and not isinstance(self.sample_comments, str):
            self.sample_comments = str(self.sample_comments)

        super().__post_init__(**kwargs)


@dataclass
class PlasmoTarAmpResults(YAMLRoot):
    """
    Information on final results from a targeted amplicon analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.PlasmoTarAmpResults
    class_class_curie: ClassVar[str] = "plasmo_tar_amp_schema:PlasmoTarAmpResults"
    class_name: ClassVar[str] = "PlasmoTarAmpResults"
    class_model_uri: ClassVar[URIRef] = PLASMO_TAR_AMP_SCHEMA.PlasmoTarAmpResults

    specimen_infos: Union[Union[dict, SpecimenInfo], List[Union[dict, SpecimenInfo]]] = None
    sequencing_info: Union[dict, SequencingInfo] = None
    bioinformatics_info: Union[dict, TarAmpBioinformaticsInfo] = None
    panel_info: Union[dict, PanelInfo] = None
    representative_haplotype_sequences: Union[Union[dict, RepresentativeHaplotypeSequences], List[Union[dict, RepresentativeHaplotypeSequences]]] = None
    haplotypes_detected: Union[dict, HaplotypesDetected] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.specimen_infos):
            self.MissingRequiredField("specimen_infos")
        if not isinstance(self.specimen_infos, list):
            self.specimen_infos = [self.specimen_infos] if self.specimen_infos is not None else []
        self.specimen_infos = [v if isinstance(v, SpecimenInfo) else SpecimenInfo(**as_dict(v)) for v in self.specimen_infos]

        if self._is_empty(self.sequencing_info):
            self.MissingRequiredField("sequencing_info")
        if not isinstance(self.sequencing_info, SequencingInfo):
            self.sequencing_info = SequencingInfo(**as_dict(self.sequencing_info))

        if self._is_empty(self.bioinformatics_info):
            self.MissingRequiredField("bioinformatics_info")
        if not isinstance(self.bioinformatics_info, TarAmpBioinformaticsInfo):
            self.bioinformatics_info = TarAmpBioinformaticsInfo(**as_dict(self.bioinformatics_info))

        if self._is_empty(self.panel_info):
            self.MissingRequiredField("panel_info")
        if not isinstance(self.panel_info, PanelInfo):
            self.panel_info = PanelInfo(**as_dict(self.panel_info))

        if self._is_empty(self.representative_haplotype_sequences):
            self.MissingRequiredField("representative_haplotype_sequences")
        if not isinstance(self.representative_haplotype_sequences, list):
            self.representative_haplotype_sequences = [self.representative_haplotype_sequences] if self.representative_haplotype_sequences is not None else []
        self.representative_haplotype_sequences = [v if isinstance(v, RepresentativeHaplotypeSequences) else RepresentativeHaplotypeSequences(**as_dict(v)) for v in self.representative_haplotype_sequences]

        if self._is_empty(self.haplotypes_detected):
            self.MissingRequiredField("haplotypes_detected")
        if not isinstance(self.haplotypes_detected, HaplotypesDetected):
            self.haplotypes_detected = HaplotypesDetected(**as_dict(self.haplotypes_detected))

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

slots.targetInfo__insert_location = Slot(uri=PLASMO_TAR_AMP_SCHEMA.insert_location, name="targetInfo__insert_location", curie=PLASMO_TAR_AMP_SCHEMA.curie('insert_location'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.targetInfo__insert_location, domain=None, range=Union[dict, GenomicLocation])

slots.targetInfo__forward_primers = Slot(uri=PLASMO_TAR_AMP_SCHEMA.forward_primers, name="targetInfo__forward_primers", curie=PLASMO_TAR_AMP_SCHEMA.curie('forward_primers'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.targetInfo__forward_primers, domain=None, range=Union[dict, Primers])

slots.targetInfo__reverse_primers = Slot(uri=PLASMO_TAR_AMP_SCHEMA.reverse_primers, name="targetInfo__reverse_primers", curie=PLASMO_TAR_AMP_SCHEMA.curie('reverse_primers'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.targetInfo__reverse_primers, domain=None, range=Union[dict, Primers])

slots.panelInfo__panel_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.panel_id, name="panelInfo__panel_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('panel_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.panelInfo__panel_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.panelInfo__targets = Slot(uri=PLASMO_TAR_AMP_SCHEMA.targets, name="panelInfo__targets", curie=PLASMO_TAR_AMP_SCHEMA.curie('targets'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.panelInfo__targets, domain=None, range=Union[Union[dict, TargetInfo], List[Union[dict, TargetInfo]]])

slots.representativeHaplotypeSequence__haplotype_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.haplotype_id, name="representativeHaplotypeSequence__haplotype_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('haplotype_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.representativeHaplotypeSequence__haplotype_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.representativeHaplotypeSequence__seq = Slot(uri=PLASMO_TAR_AMP_SCHEMA.seq, name="representativeHaplotypeSequence__seq", curie=PLASMO_TAR_AMP_SCHEMA.curie('seq'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.representativeHaplotypeSequence__seq, domain=None, range=str,
                   pattern=re.compile(r'^[A-z]$'))

slots.representativeHaplotypeSequence__quality = Slot(uri=PLASMO_TAR_AMP_SCHEMA.quality, name="representativeHaplotypeSequence__quality", curie=PLASMO_TAR_AMP_SCHEMA.curie('quality'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.representativeHaplotypeSequence__quality, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.representativeHaplotypeSequence__alt_annotations = Slot(uri=PLASMO_TAR_AMP_SCHEMA.alt_annotations, name="representativeHaplotypeSequence__alt_annotations", curie=PLASMO_TAR_AMP_SCHEMA.curie('alt_annotations'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.representativeHaplotypeSequence__alt_annotations, domain=None, range=Optional[Union[str, List[str]]])

slots.representativeHaplotypeSequences__target_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.target_id, name="representativeHaplotypeSequences__target_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('target_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.representativeHaplotypeSequences__target_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.representativeHaplotypeSequences__seqs = Slot(uri=PLASMO_TAR_AMP_SCHEMA.seqs, name="representativeHaplotypeSequences__seqs", curie=PLASMO_TAR_AMP_SCHEMA.curie('seqs'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.representativeHaplotypeSequences__seqs, domain=None, range=Union[Union[dict, RepresentativeHaplotypeSequence], List[Union[dict, RepresentativeHaplotypeSequence]]])

slots.haplotypesDetected__sequencing_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.sequencing_id, name="haplotypesDetected__sequencing_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('sequencing_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesDetected__sequencing_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.haplotypesDetected__bioinformatics_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.bioinformatics_id, name="haplotypesDetected__bioinformatics_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('bioinformatics_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesDetected__bioinformatics_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.haplotypesDetected__samples = Slot(uri=PLASMO_TAR_AMP_SCHEMA.samples, name="haplotypesDetected__samples", curie=PLASMO_TAR_AMP_SCHEMA.curie('samples'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesDetected__samples, domain=None, range=Union[Union[dict, HaplotypesForSample], List[Union[dict, HaplotypesForSample]]])

slots.genomeInfo__name = Slot(uri=PLASMO_TAR_AMP_SCHEMA.name, name="genomeInfo__name", curie=PLASMO_TAR_AMP_SCHEMA.curie('name'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__name, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.genomeInfo__version = Slot(uri=PLASMO_TAR_AMP_SCHEMA.version, name="genomeInfo__version", curie=PLASMO_TAR_AMP_SCHEMA.curie('version'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__version, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.genomeInfo__taxon_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.taxon_id, name="genomeInfo__taxon_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('taxon_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__taxon_id, domain=None, range=int,
                   pattern=re.compile(r'^[0-9]$'))

slots.genomeInfo__url = Slot(uri=PLASMO_TAR_AMP_SCHEMA.url, name="genomeInfo__url", curie=PLASMO_TAR_AMP_SCHEMA.curie('url'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__url, domain=None, range=str,
                   pattern=re.compile(r'r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"'))

slots.genomeInfo__gff_url = Slot(uri=PLASMO_TAR_AMP_SCHEMA.gff_url, name="genomeInfo__gff_url", curie=PLASMO_TAR_AMP_SCHEMA.curie('gff_url'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomeInfo__gff_url, domain=None, range=Optional[str],
                   pattern=re.compile(r'r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"'))

slots.genomicLocation__chrom = Slot(uri=PLASMO_TAR_AMP_SCHEMA.chrom, name="genomicLocation__chrom", curie=PLASMO_TAR_AMP_SCHEMA.curie('chrom'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomicLocation__chrom, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.genomicLocation__start = Slot(uri=PLASMO_TAR_AMP_SCHEMA.start, name="genomicLocation__start", curie=PLASMO_TAR_AMP_SCHEMA.curie('start'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomicLocation__start, domain=None, range=int,
                   pattern=re.compile(r'^[0-9]$'))

slots.genomicLocation__end = Slot(uri=PLASMO_TAR_AMP_SCHEMA.end, name="genomicLocation__end", curie=PLASMO_TAR_AMP_SCHEMA.curie('end'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomicLocation__end, domain=None, range=int,
                   pattern=re.compile(r'^[0-9]$'))

slots.genomicLocation__strand = Slot(uri=PLASMO_TAR_AMP_SCHEMA.strand, name="genomicLocation__strand", curie=PLASMO_TAR_AMP_SCHEMA.curie('strand'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.genomicLocation__strand, domain=None, range=Optional[str],
                   pattern=re.compile(r'r'[+-]''))

slots.primerInfo__seq = Slot(uri=PLASMO_TAR_AMP_SCHEMA.seq, name="primerInfo__seq", curie=PLASMO_TAR_AMP_SCHEMA.curie('seq'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.primerInfo__seq, domain=None, range=str,
                   pattern=re.compile(r'^[A-z]$'))

slots.primerInfo__location = Slot(uri=PLASMO_TAR_AMP_SCHEMA.location, name="primerInfo__location", curie=PLASMO_TAR_AMP_SCHEMA.curie('location'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.primerInfo__location, domain=None, range=Union[dict, GenomicLocation])

slots.primers__entries = Slot(uri=PLASMO_TAR_AMP_SCHEMA.entries, name="primers__entries", curie=PLASMO_TAR_AMP_SCHEMA.curie('entries'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.primers__entries, domain=None, range=Optional[Union[Union[dict, PrimerInfo], List[Union[dict, PrimerInfo]]]])

slots.haplotypesForSample__sample_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.sample_id, name="haplotypesForSample__sample_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('sample_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesForSample__sample_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.haplotypesForSample__target_results = Slot(uri=PLASMO_TAR_AMP_SCHEMA.target_results, name="haplotypesForSample__target_results", curie=PLASMO_TAR_AMP_SCHEMA.curie('target_results'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesForSample__target_results, domain=None, range=Union[Union[dict, HaplotypesForTarget], List[Union[dict, HaplotypesForTarget]]])

slots.haplotypesForTarget__target_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.target_id, name="haplotypesForTarget__target_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('target_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesForTarget__target_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.haplotypesForTarget__haplotype_ids = Slot(uri=PLASMO_TAR_AMP_SCHEMA.haplotype_ids, name="haplotypesForTarget__haplotype_ids", curie=PLASMO_TAR_AMP_SCHEMA.curie('haplotype_ids'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesForTarget__haplotype_ids, domain=None, range=Union[str, List[str]])

slots.haplotypesForTarget__read_counts = Slot(uri=PLASMO_TAR_AMP_SCHEMA.read_counts, name="haplotypesForTarget__read_counts", curie=PLASMO_TAR_AMP_SCHEMA.curie('read_counts'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesForTarget__read_counts, domain=None, range=Union[float, List[float]])

slots.haplotypesForTarget__umi_counts = Slot(uri=PLASMO_TAR_AMP_SCHEMA.umi_counts, name="haplotypesForTarget__umi_counts", curie=PLASMO_TAR_AMP_SCHEMA.curie('umi_counts'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.haplotypesForTarget__umi_counts, domain=None, range=Optional[Union[float, List[float]]])

slots.bioMethod__program = Slot(uri=PLASMO_TAR_AMP_SCHEMA.program, name="bioMethod__program", curie=PLASMO_TAR_AMP_SCHEMA.curie('program'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.bioMethod__program, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.bioMethod__purpose = Slot(uri=PLASMO_TAR_AMP_SCHEMA.purpose, name="bioMethod__purpose", curie=PLASMO_TAR_AMP_SCHEMA.curie('purpose'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.bioMethod__purpose, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.bioMethod__additional_argument = Slot(uri=PLASMO_TAR_AMP_SCHEMA.additional_argument, name="bioMethod__additional_argument", curie=PLASMO_TAR_AMP_SCHEMA.curie('additional_argument'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.bioMethod__additional_argument, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.tarAmpBioinformaticsInfo__tar_amp_bioinformatics_info_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.tar_amp_bioinformatics_info_id, name="tarAmpBioinformaticsInfo__tar_amp_bioinformatics_info_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('tar_amp_bioinformatics_info_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.tarAmpBioinformaticsInfo__tar_amp_bioinformatics_info_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.tarAmpBioinformaticsInfo__demultiplexing_method = Slot(uri=PLASMO_TAR_AMP_SCHEMA.demultiplexing_method, name="tarAmpBioinformaticsInfo__demultiplexing_method", curie=PLASMO_TAR_AMP_SCHEMA.curie('demultiplexing_method'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.tarAmpBioinformaticsInfo__demultiplexing_method, domain=None, range=Union[dict, BioMethod])

slots.tarAmpBioinformaticsInfo__denoising_method = Slot(uri=PLASMO_TAR_AMP_SCHEMA.denoising_method, name="tarAmpBioinformaticsInfo__denoising_method", curie=PLASMO_TAR_AMP_SCHEMA.curie('denoising_method'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.tarAmpBioinformaticsInfo__denoising_method, domain=None, range=Union[dict, BioMethod])

slots.tarAmpBioinformaticsInfo__population_clustering_method = Slot(uri=PLASMO_TAR_AMP_SCHEMA.population_clustering_method, name="tarAmpBioinformaticsInfo__population_clustering_method", curie=PLASMO_TAR_AMP_SCHEMA.curie('population_clustering_method'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.tarAmpBioinformaticsInfo__population_clustering_method, domain=None, range=Union[dict, BioMethod])

slots.tarAmpBioinformaticsInfo__additional_methods = Slot(uri=PLASMO_TAR_AMP_SCHEMA.additional_methods, name="tarAmpBioinformaticsInfo__additional_methods", curie=PLASMO_TAR_AMP_SCHEMA.curie('additional_methods'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.tarAmpBioinformaticsInfo__additional_methods, domain=None, range=Optional[Union[Union[dict, BioMethod], List[Union[dict, BioMethod]]]])

slots.sequencingInfo__sequencing_info_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.sequencing_info_id, name="sequencingInfo__sequencing_info_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('sequencing_info_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__sequencing_info_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.sequencingInfo__seq_instrument = Slot(uri=PLASMO_TAR_AMP_SCHEMA.seq_instrument, name="sequencingInfo__seq_instrument", curie=PLASMO_TAR_AMP_SCHEMA.curie('seq_instrument'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__seq_instrument, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.sequencingInfo__seq_date = Slot(uri=PLASMO_TAR_AMP_SCHEMA.seq_date, name="sequencingInfo__seq_date", curie=PLASMO_TAR_AMP_SCHEMA.curie('seq_date'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__seq_date, domain=None, range=str,
                   pattern=re.compile(r'r"\d{4}-(?:0[1-9]|1[0-2])(?:-(?:0[1-9]|[12][0-9]|3[01]))?"'))

slots.sequencingInfo__nucl_acid_ext = Slot(uri=PLASMO_TAR_AMP_SCHEMA.nucl_acid_ext, name="sequencingInfo__nucl_acid_ext", curie=PLASMO_TAR_AMP_SCHEMA.curie('nucl_acid_ext'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__nucl_acid_ext, domain=None, range=str,
                   pattern=re.compile(r'r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"'))

slots.sequencingInfo__nucl_acid_amp = Slot(uri=PLASMO_TAR_AMP_SCHEMA.nucl_acid_amp, name="sequencingInfo__nucl_acid_amp", curie=PLASMO_TAR_AMP_SCHEMA.curie('nucl_acid_amp'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__nucl_acid_amp, domain=None, range=str,
                   pattern=re.compile(r'r"^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$"'))

slots.sequencingInfo__nucl_acid_date = Slot(uri=PLASMO_TAR_AMP_SCHEMA.nucl_acid_date, name="sequencingInfo__nucl_acid_date", curie=PLASMO_TAR_AMP_SCHEMA.curie('nucl_acid_date'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__nucl_acid_date, domain=None, range=str,
                   pattern=re.compile(r'r"\d{4}-(?:0[1-9]|1[0-2])(?:-(?:0[1-9]|[12][0-9]|3[01]))?"'))

slots.sequencingInfo__pcr_cond = Slot(uri=PLASMO_TAR_AMP_SCHEMA.pcr_cond, name="sequencingInfo__pcr_cond", curie=PLASMO_TAR_AMP_SCHEMA.curie('pcr_cond'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__pcr_cond, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.sequencingInfo__lib_screen = Slot(uri=PLASMO_TAR_AMP_SCHEMA.lib_screen, name="sequencingInfo__lib_screen", curie=PLASMO_TAR_AMP_SCHEMA.curie('lib_screen'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__lib_screen, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.sequencingInfo__lib_layout = Slot(uri=PLASMO_TAR_AMP_SCHEMA.lib_layout, name="sequencingInfo__lib_layout", curie=PLASMO_TAR_AMP_SCHEMA.curie('lib_layout'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__lib_layout, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.sequencingInfo__lib_kit = Slot(uri=PLASMO_TAR_AMP_SCHEMA.lib_kit, name="sequencingInfo__lib_kit", curie=PLASMO_TAR_AMP_SCHEMA.curie('lib_kit'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__lib_kit, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.sequencingInfo__seq_center = Slot(uri=PLASMO_TAR_AMP_SCHEMA.seq_center, name="sequencingInfo__seq_center", curie=PLASMO_TAR_AMP_SCHEMA.curie('seq_center'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.sequencingInfo__seq_center, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.specimenInfo__sample_name = Slot(uri=PLASMO_TAR_AMP_SCHEMA.sample_name, name="specimenInfo__sample_name", curie=PLASMO_TAR_AMP_SCHEMA.curie('sample_name'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__sample_name, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.specimenInfo__samp_taxon_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.samp_taxon_id, name="specimenInfo__samp_taxon_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('samp_taxon_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__samp_taxon_id, domain=None, range=int,
                   pattern=re.compile(r'^[0-9]$'))

slots.specimenInfo__host_taxon_id = Slot(uri=PLASMO_TAR_AMP_SCHEMA.host_taxon_id, name="specimenInfo__host_taxon_id", curie=PLASMO_TAR_AMP_SCHEMA.curie('host_taxon_id'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__host_taxon_id, domain=None, range=Optional[int],
                   pattern=re.compile(r'^[0-9]$'))

slots.specimenInfo__alternate_identifiers = Slot(uri=PLASMO_TAR_AMP_SCHEMA.alternate_identifiers, name="specimenInfo__alternate_identifiers", curie=PLASMO_TAR_AMP_SCHEMA.curie('alternate_identifiers'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__alternate_identifiers, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.specimenInfo__parasite_density = Slot(uri=PLASMO_TAR_AMP_SCHEMA.parasite_density, name="specimenInfo__parasite_density", curie=PLASMO_TAR_AMP_SCHEMA.curie('parasite_density'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__parasite_density, domain=None, range=Optional[int],
                   pattern=re.compile(r'r'^[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$''))

slots.specimenInfo__collection_date = Slot(uri=PLASMO_TAR_AMP_SCHEMA.collection_date, name="specimenInfo__collection_date", curie=PLASMO_TAR_AMP_SCHEMA.curie('collection_date'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__collection_date, domain=None, range=str,
                   pattern=re.compile(r'r"\d{4}-(?:0[1-9]|1[0-2])(?:-(?:0[1-9]|[12][0-9]|3[01]))?"'))

slots.specimenInfo__lat_lon = Slot(uri=PLASMO_TAR_AMP_SCHEMA.lat_lon, name="specimenInfo__lat_lon", curie=PLASMO_TAR_AMP_SCHEMA.curie('lat_lon'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__lat_lon, domain=None, range=str,
                   pattern=re.compile(r'r'^[-+]?\d{1,2}(?:\.\d+)?,[-+]?\d{1,3}(?:\.\d+)?$''))

slots.specimenInfo__collector = Slot(uri=PLASMO_TAR_AMP_SCHEMA.collector, name="specimenInfo__collector", curie=PLASMO_TAR_AMP_SCHEMA.curie('collector'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__collector, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.specimenInfo__samp_store_loc = Slot(uri=PLASMO_TAR_AMP_SCHEMA.samp_store_loc, name="specimenInfo__samp_store_loc", curie=PLASMO_TAR_AMP_SCHEMA.curie('samp_store_loc'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__samp_store_loc, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.specimenInfo__samp_collect_device = Slot(uri=PLASMO_TAR_AMP_SCHEMA.samp_collect_device, name="specimenInfo__samp_collect_device", curie=PLASMO_TAR_AMP_SCHEMA.curie('samp_collect_device'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__samp_collect_device, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.specimenInfo__project_name = Slot(uri=PLASMO_TAR_AMP_SCHEMA.project_name, name="specimenInfo__project_name", curie=PLASMO_TAR_AMP_SCHEMA.curie('project_name'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__project_name, domain=None, range=str,
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.specimenInfo__accession = Slot(uri=PLASMO_TAR_AMP_SCHEMA.accession, name="specimenInfo__accession", curie=PLASMO_TAR_AMP_SCHEMA.curie('accession'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__accession, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-z-._0-9]$'))

slots.specimenInfo__sample_comments = Slot(uri=PLASMO_TAR_AMP_SCHEMA.sample_comments, name="specimenInfo__sample_comments", curie=PLASMO_TAR_AMP_SCHEMA.curie('sample_comments'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.specimenInfo__sample_comments, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-z-._0-9 ]$'))

slots.plasmoTarAmpResults__specimen_infos = Slot(uri=PLASMO_TAR_AMP_SCHEMA.specimen_infos, name="plasmoTarAmpResults__specimen_infos", curie=PLASMO_TAR_AMP_SCHEMA.curie('specimen_infos'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.plasmoTarAmpResults__specimen_infos, domain=None, range=Union[Union[dict, SpecimenInfo], List[Union[dict, SpecimenInfo]]])

slots.plasmoTarAmpResults__sequencing_info = Slot(uri=PLASMO_TAR_AMP_SCHEMA.sequencing_info, name="plasmoTarAmpResults__sequencing_info", curie=PLASMO_TAR_AMP_SCHEMA.curie('sequencing_info'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.plasmoTarAmpResults__sequencing_info, domain=None, range=Union[dict, SequencingInfo])

slots.plasmoTarAmpResults__bioinformatics_info = Slot(uri=PLASMO_TAR_AMP_SCHEMA.bioinformatics_info, name="plasmoTarAmpResults__bioinformatics_info", curie=PLASMO_TAR_AMP_SCHEMA.curie('bioinformatics_info'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.plasmoTarAmpResults__bioinformatics_info, domain=None, range=Union[dict, TarAmpBioinformaticsInfo])

slots.plasmoTarAmpResults__panel_info = Slot(uri=PLASMO_TAR_AMP_SCHEMA.panel_info, name="plasmoTarAmpResults__panel_info", curie=PLASMO_TAR_AMP_SCHEMA.curie('panel_info'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.plasmoTarAmpResults__panel_info, domain=None, range=Union[dict, PanelInfo])

slots.plasmoTarAmpResults__representative_haplotype_sequences = Slot(uri=PLASMO_TAR_AMP_SCHEMA.representative_haplotype_sequences, name="plasmoTarAmpResults__representative_haplotype_sequences", curie=PLASMO_TAR_AMP_SCHEMA.curie('representative_haplotype_sequences'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.plasmoTarAmpResults__representative_haplotype_sequences, domain=None, range=Union[Union[dict, RepresentativeHaplotypeSequences], List[Union[dict, RepresentativeHaplotypeSequences]]])

slots.plasmoTarAmpResults__haplotypes_detected = Slot(uri=PLASMO_TAR_AMP_SCHEMA.haplotypes_detected, name="plasmoTarAmpResults__haplotypes_detected", curie=PLASMO_TAR_AMP_SCHEMA.curie('haplotypes_detected'),
                   model_uri=PLASMO_TAR_AMP_SCHEMA.plasmoTarAmpResults__haplotypes_detected, domain=None, range=Union[dict, HaplotypesDetected])