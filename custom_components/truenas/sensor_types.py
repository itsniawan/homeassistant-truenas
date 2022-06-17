"""Definitions for TrueNAS sensor entities"""
from dataclasses import dataclass, field
from typing import List
from homeassistant.helpers.entity import EntityCategory
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
    SensorEntityDescription,
)
from homeassistant.const import PERCENTAGE, TEMP_CELSIUS, DATA_GIBIBYTES, DATA_KIBIBYTES
from .const import (
    SERVICE_CLOUDSYNC_RUN,
    SCHEMA_SERVICE_CLOUDSYNC_RUN,
    SERVICE_DATASET_SNAPSHOT,
    SCHEMA_SERVICE_DATASET_SNAPSHOT,
)

DEVICE_ATTRIBUTES_NETWORK = [
    "description",
    "mtu",
    "link_state",
    "active_media_type",
    "active_media_subtype",
    "link_address",
]

DEVICE_ATTRIBUTES_POOL = [
    "path",
    "status",
    "healthy",
    "is_decrypted",
    "autotrim",
    "scrub_state",
    "scrub_start",
    "scrub_end",
    "scrub_secs_left",
    "healthy",
]

DEVICE_ATTRIBUTES_DATASET = [
    "type",
    "pool",
    "mountpoint",
    "deduplication",
    "atime",
    "casesensitivity",
    "checksum",
    "exec",
    "sync",
    "compression",
    "compressratio",
    "quota",
    "copies",
    "readonly",
    "recordsize",
    "encryption_algorithm",
    "used",
    "available",
]

DEVICE_ATTRIBUTES_DISK = [
    "serial",
    "size",
    "hddstandby",
    "hddstandby_force",
    "advpowermgmt",
    "acousticlevel",
    "togglesmart",
    "model",
    "rotationrate",
    "type",
]

DEVICE_ATTRIBUTES_CPU = [
    "cpu_interrupt",
    "cpu_system",
    "cpu_user",
    "cpu_nice",
    "cpu_idle",
]

DEVICE_ATTRIBUTES_CLOUDSYNC = [
    "direction",
    "path",
    "enabled",
    "transfer_mode",
    "snapshot",
    "time_started",
    "time_finished",
    "job_percent",
    "job_description",
]

DEVICE_ATTRIBUTES_REPLICATION = [
    "source_datasets",
    "target_dataset",
    "recursive",
    "enabled",
    "direction",
    "transport",
    "auto",
    "retention_policy",
    "state",
    "time_started",
    "time_finished",
    "job_percent",
    "job_description",
]

DEVICE_ATTRIBUTES_SNAPSHOTTASK = [
    "recursive",
    "lifetime_value",
    "lifetime_unit",
    "enabled",
    "naming_schema",
    "allow_empty",
    "vmware_sync",
    "state",
    "datetime",
]


@dataclass
class TrueNASSensorEntityDescription(SensorEntityDescription):
    """Class describing mikrotik entities"""

    ha_group: str = ""
    ha_connection: str = ""
    ha_connection_value: str = ""
    data_path: str = ""
    data_attribute: str = ""
    data_name: str = ""
    data_uid: str = ""
    data_reference: str = ""
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "TrueNASSensor"


SENSOR_TYPES = {
    "system_uptime": TrueNASSensorEntityDescription(
        key="system_uptime",
        name="Uptime",
        icon="mdi:clock-outline",
        native_unit_of_measurement=None,
        device_class=SensorDeviceClass.TIMESTAMP,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="uptimeEpoch",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_cpu_temperature": TrueNASSensorEntityDescription(
        key="system_cpu_temperature",
        name="Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cpu_temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_load_shortterm": TrueNASSensorEntityDescription(
        key="system_load_shortterm",
        name="CPU Load Shortterm",
        icon="mdi:gauge",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="load_shortterm",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_load_midterm": TrueNASSensorEntityDescription(
        key="system_load_midterm",
        name="CPU Load Midterm",
        icon="mdi:gauge",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="load_midterm",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_load_longterm": TrueNASSensorEntityDescription(
        key="system_load_longterm",
        name="CPU Load Longterm",
        icon="mdi:gauge",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="load_longterm",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_cpu_usage": TrueNASSensorEntityDescription(
        key="system_cpu_usage",
        name="CPU Usage",
        icon="mdi:cpu-64-bit",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cpu_usage",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_CPU,
    ),
    "system_cache_size-arc_value": TrueNASSensorEntityDescription(
        key="system_cache_size-arc_value",
        name="ARC Size",
        icon="mdi:memory",
        native_unit_of_measurement=DATA_GIBIBYTES,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cache_size-arc_value",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_cache_size-L2_value": TrueNASSensorEntityDescription(
        key="system_cache_size-L2_value",
        name="L2ARC Size",
        icon="mdi:memory",
        native_unit_of_measurement=DATA_GIBIBYTES,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cache_size-L2_value",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_cache_ratio-arc_value": TrueNASSensorEntityDescription(
        key="system_cache_ratio-arc_value",
        name="ARC Ratio",
        icon="mdi:aspect-ratio",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cache_ratio-arc_value",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "system_cache_ratio-L2_value": TrueNASSensorEntityDescription(
        key="system_cache_ratio-L2_value",
        name="L2ARC Ratio",
        icon="mdi:aspect-ratio",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cache_ratio-L2_value",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    "dataset": TrueNASSensorEntityDescription(
        key="dataset",
        name="",
        icon="mdi:database",
        native_unit_of_measurement=DATA_GIBIBYTES,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="Datasets",
        data_path="dataset",
        data_attribute="used_gb",
        data_name="name",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_DATASET,
        func="TrueNASDatasetSensor",
    ),
    "disk": TrueNASSensorEntityDescription(
        key="disk",
        name="",
        icon="mdi:harddisk",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="Disks",
        data_path="disk",
        data_attribute="temperature",
        data_name="name",
        data_uid="",
        data_reference="devname",
        data_attributes_list=DEVICE_ATTRIBUTES_DISK,
    ),
    "pool_free": TrueNASSensorEntityDescription(
        key="pool_free",
        name="free",
        icon="mdi:database-settings",
        native_unit_of_measurement=DATA_GIBIBYTES,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="pool",
        data_attribute="available_gib",
        data_name="name",
        data_uid="",
        data_reference="guid",
        data_attributes_list=DEVICE_ATTRIBUTES_POOL,
    ),
    "cloudsync": TrueNASSensorEntityDescription(
        key="cloudsync",
        name="",
        icon="mdi:cloud-upload",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Cloudsync",
        data_path="cloudsync",
        data_attribute="state",
        data_name="description",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_CLOUDSYNC,
        func="TrueNASClousyncSensor",
    ),
    "replication": TrueNASSensorEntityDescription(
        key="replication",
        name="",
        icon="mdi:transfer",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Replication",
        data_path="replication",
        data_attribute="state",
        data_name="name",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_REPLICATION,
    ),
    "snapshottask": TrueNASSensorEntityDescription(
        key="snapshottask",
        name="",
        icon="mdi:checkbox-marked-circle-plus-outline",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Snapshot tasks",
        data_path="snapshottask",
        data_attribute="state",
        data_name="dataset",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_SNAPSHOTTASK,
    ),
    "traffic_rx": TrueNASSensorEntityDescription(
        key="traffic_rx",
        name="RX",
        icon="mdi:download-network-outline",
        native_unit_of_measurement=DATA_KIBIBYTES,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="interface",
        data_attribute="if_octets_rx",
        data_name="name",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_NETWORK,
    ),
    "traffic_tx": TrueNASSensorEntityDescription(
        key="traffic_tx",
        name="TX",
        icon="mdi:upload-network-outline",
        native_unit_of_measurement=DATA_KIBIBYTES,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="interface",
        data_attribute="if_octets_tx",
        data_name="name",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_NETWORK,
    ),
}

SENSOR_SERVICES = [
    [SERVICE_CLOUDSYNC_RUN, SCHEMA_SERVICE_CLOUDSYNC_RUN, "start"],
    [SERVICE_DATASET_SNAPSHOT, SCHEMA_SERVICE_DATASET_SNAPSHOT, "snapshot"],
]
