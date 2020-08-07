# -*- coding: utf-8 -*-
"""Sentinel Tools Constants

 Sentinel Tools - Constants
============================
 Class holding all package constants

 This file is a part of Sentinel Tools

 Copyright 2020 - MET Norway (Machine Ocean Project)

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from enum import Enum

class SQuery(Enum):

    # Search Terms
    # ============
    # Source: https://scihub.copernicus.eu/userguide/AdvancedSearch

    # Platform Name
    PlatformSentinel1  = 1
    PlatformSentinel2  = 2
    PlatformSentinel3  = 3
    PlatformSentinel5P = 5

    # Sort By
    SortByIngestionDate = 11
    SortBySensingDate   = 12
    SortByTileID        = 13

    # Order By
    OrderAscending  = 21
    OrderDescending = 22

    # Sentinel-1
    # ==========

    # Satellite Platform
    S1_Platform_S1_A = 101
    S1_Platform_S1_B = 102

    # Product Type
    S1_ProductType_SLC = 111
    S1_ProductType_GRD = 112
    S1_ProductType_OCN = 113

    # Polarisation
    S1_Polarisation_HH    = 121
    S1_Polarisation_VV    = 122
    S1_Polarisation_HV    = 123
    S1_Polarisation_VH    = 124
    S1_Polarisation_HH_HV = 125
    S1_Polarisation_VV_VH = 126

    # Sensor Mode
    S1_SensorMode_SM = 131
    S1_SensorMode_IW = 132
    S1_SensorMode_EW = 133
    S1_SensorMode_WV = 134

    # Sentinel-2
    # ==========

    # Satellite Platform
    S2_Platform_S2_A = 201
    S2_Platform_S2_B = 202

    # Product Type
    S2_ProductType_MSI1C  = 211
    S2_ProductType_MSI2A  = 212
    S2_ProductType_MSI2Ap = 213

    # Sentinel-3
    # ==========

    # Satellite Platform
    S3_Platform_S3_A = 301
    S3_Platform_S3_B = 302

    # Product Type
    S3_ProductType_SR1_SRA___  = 311
    S3_ProductType_SR1_SRA_A_  = 312
    S3_ProductType_SR1_SRA_BS  = 313
    S3_ProductType_SR2_LAN___  = 314
    S3_ProductType_OL_1_EFR___ = 315
    S3_ProductType_OL_1_ERR___ = 316
    S3_ProductType_OL_2_LFR___ = 317
    S3_ProductType_OL_2_LRR___ = 318
    S3_ProductType_SL_1_RBT___ = 319
    S3_ProductType_SL_2_LST___ = 320
    S3_ProductType_SY_2_SYN___ = 321
    S3_ProductType_SY_2_V10___ = 322
    S3_ProductType_SY_2_VG1___ = 323
    S3_ProductType_SY_2_VGP___ = 324

    # Timeliness
    S3_Timeliness_NTC = 331
    S3_Timeliness_STC = 332
    S3_Timeliness_NRT = 333

    # Instrument
    S3_Instrument_SRAL    = 341
    S3_Instrument_OLCI    = 342
    S3_Instrument_SLSTR   = 343
    S3_Instrument_SYNERGY = 344

    # Product Level
    S3_ProductLevel_L1 = 351
    S3_ProductLevel_L2 = 352

    # Sentinel-5P
    # ===========

    # Product Type
    S5P_ProductType_L1B_IR_SIR = 511
    S5P_ProductType_L1B_IR_UVN = 512
    S5P_ProductType_L1B_RA_BD1 = 513
    S5P_ProductType_L1B_RA_BD2 = 514
    S5P_ProductType_L1B_RA_BD3 = 515
    S5P_ProductType_L1B_RA_BD4 = 516
    S5P_ProductType_L1B_RA_BD5 = 517
    S5P_ProductType_L1B_RA_BD6 = 518
    S5P_ProductType_L1B_RA_BD7 = 519
    S5P_ProductType_L1B_RA_BD8 = 520
    S5P_ProductType_L2__AER_AI = 521
    S5P_ProductType_L2__AER_LH = 522
    S5P_ProductType_L2__CH4    = 523
    S5P_ProductType_L2__CLOUD_ = 524
    S5P_ProductType_L2__CO____ = 525
    S5P_ProductType_L2__HCHO__ = 526
    S5P_ProductType_L2__NO2___ = 527
    S5P_ProductType_L2__NP_BD3 = 528
    S5P_ProductType_L2__NP_BD6 = 529
    S5P_ProductType_L2__NP_BD7 = 530
    S5P_ProductType_L2__O3_TCL = 531
    S5P_ProductType_L2__O3____ = 532
    S5P_ProductType_L2__SO2___ = 533

    # Timeliness
    S5P_Timeliness_OFFL = 341
    S5P_Timeliness_NRT  = 342
    S5P_Timeliness_RPRO = 343

    # Processing Level
    S5P_ProcessingLevel_L1B = 351
    S5P_ProcessingLevel_L2  = 352

# END Class SQuery

class QueryLookup():

    QUERY_TERM = {
        # Platform Name
        SQuery.PlatformSentinel1  : "Sentinel-1",
        SQuery.PlatformSentinel2  : "Sentinel-2",
        SQuery.PlatformSentinel3  : "Sentinel-3",
        SQuery.PlatformSentinel5P : "Sentinel-5 Precursor",

        # Sort By
        SQuery.SortByIngestionDate : "",
        SQuery.SortBySensingDate   : "",
        SQuery.SortByTileID        : "",

        # Order By
        SQuery.OrderAscending  : "asc",
        SQuery.OrderDescending : "desc",

        # Sentinel-1
        # ==========

        # Satellite Platform
        SQuery.S1_Platform_S1_A : "S1_A",
        SQuery.S1_Platform_S1_B : "S1_B",

        # Product Type
        SQuery.S1_ProductType_SLC : "SLC",
        SQuery.S1_ProductType_GRD : "GRD",
        SQuery.S1_ProductType_OCN : "OCN",

        # Polarisation
        SQuery.S1_Polarisation_HH    : "",
        SQuery.S1_Polarisation_VV    : "",
        SQuery.S1_Polarisation_HV    : "",
        SQuery.S1_Polarisation_VH    : "",
        SQuery.S1_Polarisation_HH_HV : "",
        SQuery.S1_Polarisation_VV_VH : "",

        # Sensor Mode
        SQuery.S1_SensorMode_SM : "",
        SQuery.S1_SensorMode_IW : "",
        SQuery.S1_SensorMode_EW : "",
        SQuery.S1_SensorMode_WV : "",

        # Sentinel-2
        # ==========

        # Satellite Platform
        SQuery.S2_Platform_S2_A : "",
        SQuery.S2_Platform_S2_B : "",

        # Product Type
        SQuery.S2_ProductType_MSI1C  : "",
        SQuery.S2_ProductType_MSI2A  : "",
        SQuery.S2_ProductType_MSI2Ap : "",

        # Sentinel-3
        # ==========

        # Satellite Platform
        SQuery.S3_Platform_S3_A : "",
        SQuery.S3_Platform_S3_B : "",

        # Product Type
        SQuery.S3_ProductType_SR1_SRA___  : "",
        SQuery.S3_ProductType_SR1_SRA_A_  : "",
        SQuery.S3_ProductType_SR1_SRA_BS  : "",
        SQuery.S3_ProductType_SR2_LAN___  : "",
        SQuery.S3_ProductType_OL_1_EFR___ : "",
        SQuery.S3_ProductType_OL_1_ERR___ : "",
        SQuery.S3_ProductType_OL_2_LFR___ : "",
        SQuery.S3_ProductType_OL_2_LRR___ : "",
        SQuery.S3_ProductType_SL_1_RBT___ : "",
        SQuery.S3_ProductType_SL_2_LST___ : "",
        SQuery.S3_ProductType_SY_2_SYN___ : "",
        SQuery.S3_ProductType_SY_2_V10___ : "",
        SQuery.S3_ProductType_SY_2_VG1___ : "",
        SQuery.S3_ProductType_SY_2_VGP___ : "",

        # Timeliness
        SQuery.S3_Timeliness_NTC : "",
        SQuery.S3_Timeliness_STC : "",
        SQuery.S3_Timeliness_NRT : "",

        # Instrument
        SQuery.S3_Instrument_SRAL    : "",
        SQuery.S3_Instrument_OLCI    : "",
        SQuery.S3_Instrument_SLSTR   : "",
        SQuery.S3_Instrument_SYNERGY : "",

        # Product Level
        SQuery.S3_ProductLevel_L1 : "",
        SQuery.S3_ProductLevel_L2 : "",

        # Sentinel-5P
        # ===========

        # Product Type
        SQuery.S5P_ProductType_L1B_IR_SIR : "",
        SQuery.S5P_ProductType_L1B_IR_UVN : "",
        SQuery.S5P_ProductType_L1B_RA_BD1 : "",
        SQuery.S5P_ProductType_L1B_RA_BD2 : "",
        SQuery.S5P_ProductType_L1B_RA_BD3 : "",
        SQuery.S5P_ProductType_L1B_RA_BD4 : "",
        SQuery.S5P_ProductType_L1B_RA_BD5 : "",
        SQuery.S5P_ProductType_L1B_RA_BD6 : "",
        SQuery.S5P_ProductType_L1B_RA_BD7 : "",
        SQuery.S5P_ProductType_L1B_RA_BD8 : "",
        SQuery.S5P_ProductType_L2__AER_AI : "",
        SQuery.S5P_ProductType_L2__AER_LH : "",
        SQuery.S5P_ProductType_L2__CH4    : "",
        SQuery.S5P_ProductType_L2__CLOUD_ : "",
        SQuery.S5P_ProductType_L2__CO____ : "",
        SQuery.S5P_ProductType_L2__HCHO__ : "",
        SQuery.S5P_ProductType_L2__NO2___ : "",
        SQuery.S5P_ProductType_L2__NP_BD3 : "",
        SQuery.S5P_ProductType_L2__NP_BD6 : "",
        SQuery.S5P_ProductType_L2__NP_BD7 : "",
        SQuery.S5P_ProductType_L2__O3_TCL : "",
        SQuery.S5P_ProductType_L2__O3____ : "",
        SQuery.S5P_ProductType_L2__SO2___ : "",

        # Timeliness
        SQuery.S5P_Timeliness_OFFL : "",
        SQuery.S5P_Timeliness_NRT  : "",
        SQuery.S5P_Timeliness_RPRO : "",

        # Processing Level
        SQuery.S5P_ProcessingLevel_L1B : "",
        SQuery.S5P_ProcessingLevel_L2  : "",
    }

# END Class LookupMaps
