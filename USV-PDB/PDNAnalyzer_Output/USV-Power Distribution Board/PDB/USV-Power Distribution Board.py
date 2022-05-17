designFile = "C:/USV-Power-Distribution-Board-PCB/USV-PDB/PDNAnalyzer_Output/USV-Power Distribution Board/odb.tgz"

powerNets = ["+12V_DIREC_1", "+12V_DIREC_2", "+12V_EXT_FCM", "+12V_EXT_MBF", "+7V4_EXT", "VBATT", "VCC", "+12V_INT", "MTR_PWR_1", "MTR_PWR_2", "NetC15_2", "NetC12_2", "NetF1_3", "NetF2_3", "NetC19_1", "NetC21_2", "+5V_INT", "+5V_EXT_MAP", "+5V_EXT_FLC", "+5V_EXT_CCB", "+5V_EXT_RPI", "+3V3_EXT", "+3V3_INT", "NetC32_1", "NetC34_1", "NetC47_1", "NetC45_1", "NetC41_1"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("U22", "6"), ("U22", "7"), ("U22", "8"), ("U22", "9"), ("U22", "10") ],
"ground_pins": [ ("U22", "1") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J8", "2") ],
"ground_pins": [ ("J8", "1") ],
"current": 0.5,
"Rpin": 0.2,
}
,
{
"id": "2",
"type": "source",
"power_pins": [ ("U24", "6"), ("U24", "7"), ("U24", "8"), ("U24", "9"), ("U24", "10") ],
"ground_pins": [ ("U24", "1") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("J13", "2") ],
"ground_pins": [ ("J13", "1") ],
"current": 0.5,
"Rpin": 0.2,
}
,
{
"id": "4",
"type": "source",
"power_pins": [ ("U20", "6"), ("U20", "7"), ("U20", "8"), ("U20", "9"), ("U20", "10") ],
"ground_pins": [ ("U20", "1") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("J16", "2") ],
"ground_pins": [ ("J16", "1") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "6",
"type": "source",
"power_pins": [ ("U18", "10"), ("U18", "9"), ("U18", "8"), ("U18", "7"), ("U18", "6") ],
"ground_pins": [ ("U18", "1") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("J20", "3") ],
"ground_pins": [ ("J20", "1") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "8",
"type": "source",
"power_pins": [ ("R33", "2") ],
"ground_pins": [ ("U11", "21"), ("U11", "10"), ("U11", "15"), ("U11", "13"), ("U11", "11") ],
"voltage": 7.4,
"Rpin": 0,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("J7", "2") ],
"ground_pins": [ ("J7", "1") ],
"current": 3,
"Rpin": 0.0333333333333333,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("J11", "2") ],
"ground_pins": [ ("J11", "1") ],
"current": 3,
"Rpin": 0.0333333333333333,
}
,
{
"id": "11",
"type": "source",
"power_pins": [ ("J1", "2") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 25.2,
"Rpin": 0,
}
,
{
"id": "12",
"type": "load",
"power_pins": [ ("Q1", "D") ],
"ground_pins": [ ("J1", "1") ],
"current": 130,
"Rpin": 0.000769230769230769,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("J17", "2") ],
"ground_pins": [ ("J17", "1") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("J18", "2") ],
"ground_pins": [ ("J18", "1") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "15",
"type": "source",
"power_pins": [ ("Q2", "D") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 25.2,
"Rpin": 0,
}
,
{
"id": "16",
"type": "load",
"power_pins": [ ("U8", "1"), ("U8", "2"), ("U8", "3") ],
"ground_pins": [ ("U8", "21"), ("U8", "10"), ("U8", "15"), ("U8", "13"), ("U8", "11") ],
"current": 3,
"Rpin": 0.125,
}
,
{
"id": "17",
"type": "load",
"power_pins": [ ("U6", "31"), ("U6", "27"), ("U6", "19"), ("U6", "18"), ("U6", "17"), ("U6", "16"), ("U6", "15"), ("U6", "14"), ("U6", "13"), ("U6", "31_3"), ("U6", "31_2"), ("U6", "31_1") ],
"ground_pins": [ ("U6", "29"), ("U6", "23"), ("U6", "21"), ("U6", "8"), ("U6", "7"), ("U6", "6"), ("U6", "5"), ("U6", "2"), ("U6", "29_8"), ("U6", "29_7"), ("U6", "29_6"), ("U6", "29_5"), ("U6", "29_4"), ("U6", "29_3"), ("U6", "29_2"), ("U6", "29_1") ],
"current": 8,
"Rpin": 0.171428571428571,
}
,
{
"id": "18",
"type": "load",
"power_pins": [ ("Q3", "D") ],
"ground_pins": [ ("J1", "1") ],
"current": 50,
"Rpin": 0.002,
}
,
{
"id": "19",
"type": "load",
"power_pins": [ ("Q4", "D") ],
"ground_pins": [ ("J1", "1") ],
"current": 50,
"Rpin": 0.002,
}
,
{
"id": "20",
"type": "load",
"power_pins": [ ("U11", "1"), ("U11", "2"), ("U11", "3") ],
"ground_pins": [ ("U11", "21"), ("U11", "10"), ("U11", "15"), ("U11", "13"), ("U11", "11") ],
"current": 6,
"Rpin": 0.0625,
}
,
{
"id": "21",
"type": "source",
"power_pins": [ ("R19", "2") ],
"ground_pins": [ ("U8", "21"), ("U8", "10"), ("U8", "15"), ("U8", "13"), ("U8", "11") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "22",
"type": "load",
"power_pins": [ ("U22", "11") ],
"ground_pins": [ ("U22", "1") ],
"current": 0.5,
"Rpin": 0.2,
}
,
{
"id": "23",
"type": "load",
"power_pins": [ ("U24", "11") ],
"ground_pins": [ ("U24", "1") ],
"current": 0.5,
"Rpin": 0.2,
}
,
{
"id": "24",
"type": "load",
"power_pins": [ ("U18", "11") ],
"ground_pins": [ ("U18", "1") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "25",
"type": "load",
"power_pins": [ ("U20", "11") ],
"ground_pins": [ ("U20", "1") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "26",
"type": "source",
"power_pins": [ ("R7", "2") ],
"ground_pins": [ ("J6", "1") ],
"voltage": 25.2,
"Rpin": 0,
}
,
{
"id": "27",
"type": "load",
"power_pins": [ ("J6", "2") ],
"ground_pins": [ ("J6", "1") ],
"current": 50,
"Rpin": 0.002,
}
,
{
"id": "28",
"type": "source",
"power_pins": [ ("R9", "2") ],
"ground_pins": [ ("J12", "1") ],
"voltage": 25.2,
"Rpin": 0,
}
,
{
"id": "29",
"type": "load",
"power_pins": [ ("J12", "2") ],
"ground_pins": [ ("J12", "1") ],
"current": 50,
"Rpin": 0.002,
}
,
{
"id": "30",
"type": "source",
"power_pins": [ ("F2", "2"), ("F2", "1") ],
"ground_pins": [ ("U5", "6"), ("U5", "7"), ("U5", "4") ],
"voltage": 25.2,
"Rpin": 0,
}
,
{
"id": "31",
"type": "load",
"power_pins": [ ("R9", "1") ],
"ground_pins": [ ("U5", "6"), ("U5", "7"), ("U5", "4") ],
"current": 50,
"Rpin": 0.003,
}
,
{
"id": "32",
"type": "source",
"power_pins": [ ("F1", "1"), ("F1", "2") ],
"ground_pins": [ ("U3", "6"), ("U3", "7"), ("U3", "4") ],
"voltage": 25.2,
"Rpin": 0,
}
,
{
"id": "33",
"type": "load",
"power_pins": [ ("R7", "1") ],
"ground_pins": [ ("U3", "6"), ("U3", "7"), ("U3", "4") ],
"current": 50,
"Rpin": 0.003,
}
,
{
"id": "34",
"type": "source",
"power_pins": [ ("Q3", "S") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 25.2,
"Rpin": 0,
}
,
{
"id": "35",
"type": "load",
"power_pins": [ ("F1", "4"), ("F1", "3") ],
"ground_pins": [ ("J1", "1") ],
"current": 50,
"Rpin": 0.00266666666666667,
}
,
{
"id": "36",
"type": "source",
"power_pins": [ ("Q4", "S") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 25.2,
"Rpin": 0,
}
,
{
"id": "37",
"type": "load",
"power_pins": [ ("F2", "3"), ("F2", "4") ],
"ground_pins": [ ("J1", "1") ],
"current": 50,
"Rpin": 0.00266666666666667,
}
,
{
"id": "38",
"type": "source",
"power_pins": [ ("U6", "30"), ("U6", "22"), ("U6", "12"), ("U6", "11"), ("U6", "10"), ("U6", "9"), ("U6", "4"), ("U6", "30_6"), ("U6", "30_5"), ("U6", "30_4"), ("U6", "30_3"), ("U6", "30_2"), ("U6", "30_1") ],
"ground_pins": [ ("U6", "29"), ("U6", "23"), ("U6", "21"), ("U6", "8"), ("U6", "7"), ("U6", "6"), ("U6", "5"), ("U6", "2"), ("U6", "29_8"), ("U6", "29_7"), ("U6", "29_6"), ("U6", "29_5"), ("U6", "29_4"), ("U6", "29_3"), ("U6", "29_2"), ("U6", "29_1") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "39",
"type": "load",
"power_pins": [ ("L1", "1") ],
"ground_pins": [ ("J1", "1") ],
"current": 10,
"Rpin": 0.01,
}
,
{
"id": "40",
"type": "source",
"power_pins": [ ("L1", "2") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "41",
"type": "load",
"power_pins": [ ("R12", "1") ],
"ground_pins": [ ("J1", "1") ],
"current": 10,
"Rpin": 0.01,
}
,
{
"id": "42",
"type": "source",
"power_pins": [ ("R12", "2") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "43",
"type": "load",
"power_pins": [ ("U23", "6") ],
"ground_pins": [ ("U23", "2") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "44",
"type": "load",
"power_pins": [ ("U26", "6") ],
"ground_pins": [ ("U26", "2") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "45",
"type": "load",
"power_pins": [ ("U25", "6") ],
"ground_pins": [ ("U25", "2") ],
"current": 3,
"Rpin": 0.0333333333333333,
}
,
{
"id": "46",
"type": "load",
"power_pins": [ ("U10", "2"), ("U10", "1") ],
"ground_pins": [ ("U10", "6"), ("U10", "3") ],
"current": 3,
"Rpin": 0.0666666666666667,
}
,
{
"id": "47",
"type": "load",
"power_pins": [ ("U27", "6") ],
"ground_pins": [ ("U27", "2") ],
"current": 1.5,
"Rpin": 0.0666666666666667,
}
,
{
"id": "48",
"type": "source",
"power_pins": [ ("U26", "1") ],
"ground_pins": [ ("U26", "2") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "49",
"type": "load",
"power_pins": [ ("J9", "2") ],
"ground_pins": [ ("J9", "1") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "50",
"type": "source",
"power_pins": [ ("U23", "1") ],
"ground_pins": [ ("U23", "2") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "51",
"type": "load",
"power_pins": [ ("J4", "2") ],
"ground_pins": [ ("J4", "1") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "52",
"type": "source",
"power_pins": [ ("U25", "1") ],
"ground_pins": [ ("U25", "2") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "53",
"type": "load",
"power_pins": [ ("J15", "2") ],
"ground_pins": [ ("J15", "1") ],
"current": 3,
"Rpin": 0.0333333333333333,
}
,
{
"id": "54",
"type": "source",
"power_pins": [ ("U27", "1") ],
"ground_pins": [ ("U27", "2") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "55",
"type": "load",
"power_pins": [ ("J14", "V") ],
"ground_pins": [ ("J14", "G"), ("J14", "G_B2"), ("J14", "G_A1"), ("J14", "G_A2"), ("J14", "G_B1"), ("J14", "S1"), ("J14", "S2") ],
"current": 3,
"Rpin": 0.0583333333333333,
}
,
{
"id": "56",
"type": "source",
"power_pins": [ ("U19", "1") ],
"ground_pins": [ ("U19", "2") ],
"voltage": 3.3,
"Rpin": 0,
}
,
{
"id": "57",
"type": "load",
"power_pins": [ ("J19", "2") ],
"ground_pins": [ ("J19", "1") ],
"current": 0.5,
"Rpin": 0.2,
}
,
{
"id": "58",
"type": "load",
"power_pins": [ ("J21", "2") ],
"ground_pins": [ ("J21", "1") ],
"current": 0.5,
"Rpin": 0.2,
}
,
{
"id": "59",
"type": "source",
"power_pins": [ ("U10", "4") ],
"ground_pins": [ ("U10", "6"), ("U10", "3") ],
"voltage": 3.3,
"Rpin": 0,
}
,
{
"id": "60",
"type": "load",
"power_pins": [ ("MD1", "2") ],
"ground_pins": [ ("MD1", "pdna_pin_39_1"), ("MD1", "pdna_pin_39_2"), ("MD1", "pdna_pin_39_3"), ("MD1", "pdna_pin_39_4"), ("MD1", "pdna_pin_39_5"), ("MD1", "pdna_pin_39_6"), ("MD1", "pdna_pin_39_7"), ("MD1", "pdna_pin_39_8"), ("MD1", "pdna_pin_39_9"), ("MD1", "15"), ("MD1", "38"), ("MD1", "1") ],
"current": 0.5,
"Rpin": 0.369230769230769,
}
,
{
"id": "61",
"type": "load",
"power_pins": [ ("U15", "14") ],
"ground_pins": [ ("U15", "1"), ("U15", "4"), ("U15", "7"), ("U15", "13"), ("U15", "10") ],
"current": 0.1,
"Rpin": 1.66666666666667,
}
,
{
"id": "62",
"type": "load",
"power_pins": [ ("U16", "14") ],
"ground_pins": [ ("U16", "1"), ("U16", "4"), ("U16", "7"), ("U16", "13"), ("U16", "10") ],
"current": 0.1,
"Rpin": 1.66666666666667,
}
,
{
"id": "63",
"type": "load",
"power_pins": [ ("U14", "16"), ("U14", "3"), ("U14", "2"), ("U14", "1") ],
"ground_pins": [ ("U14", "8") ],
"current": 0.1,
"Rpin": 1.6,
}
,
{
"id": "64",
"type": "load",
"power_pins": [ ("U13", "16") ],
"ground_pins": [ ("U13", "1") ],
"current": 0.1,
"Rpin": 1,
}
,
{
"id": "65",
"type": "load",
"power_pins": [ ("U19", "6") ],
"ground_pins": [ ("U19", "2") ],
"current": 1,
"Rpin": 0.1,
}
,
{
"id": "66",
"type": "source",
"power_pins": [ ("L2", "2") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "67",
"type": "load",
"power_pins": [ ("R19", "1") ],
"ground_pins": [ ("J1", "1") ],
"current": 3,
"Rpin": 0.0333333333333333,
}
,
{
"id": "68",
"type": "source",
"power_pins": [ ("U8", "20"), ("U8", "19"), ("U8", "18") ],
"ground_pins": [ ("U8", "21"), ("U8", "10"), ("U8", "15"), ("U8", "13"), ("U8", "11") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "69",
"type": "load",
"power_pins": [ ("L2", "1") ],
"ground_pins": [ ("J1", "1") ],
"current": 3,
"Rpin": 0.0333333333333333,
}
,
{
"id": "70",
"type": "source",
"power_pins": [ ("U11", "20"), ("U11", "19"), ("U11", "18") ],
"ground_pins": [ ("U11", "21"), ("U11", "10"), ("U11", "15"), ("U11", "13"), ("U11", "11") ],
"voltage": 7.4,
"Rpin": 0,
}
,
{
"id": "71",
"type": "load",
"power_pins": [ ("L3", "1") ],
"ground_pins": [ ("J1", "1") ],
"current": 3,
"Rpin": 0.0333333333333333,
}
,
{
"id": "72",
"type": "source",
"power_pins": [ ("L3", "2") ],
"ground_pins": [ ("J1", "1") ],
"voltage": 7.4,
"Rpin": 0,
}
,
{
"id": "73",
"type": "load",
"power_pins": [ ("R33", "1") ],
"ground_pins": [ ("J1", "1") ],
"current": 3,
"Rpin": 0.0333333333333333,
}
,
{
"id": "74",
"type": "source",
"power_pins": [ ("U10", "5") ],
"ground_pins": [ ("U10", "6"), ("U10", "3") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "75",
"type": "load",
"power_pins": [ ("C41", "1") ],
"ground_pins": [ ("U10", "6"), ("U10", "3") ],
"current": 0.1,
"Rpin": 1.33333333333333,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 7E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'INNER_1', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'INNER_2', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.1, 'Thickness': 7.112E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 7E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
