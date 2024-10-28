from collections import OrderedDict

CLEARANCES = OrderedDict(
    [
        ("C", "Confidential"),
        ("S", "Secret"),
        ("TS", "Top Secret"),
        ("TS/SCI", "Top Secret / Sensitive Compartmented Information"),
        (
            "TS/SCI w/ CI Poly",
            "Top Secret / Sensitive Compartmented Information with Counterintelligence Polygraph",
        ),
        (
            "TS/SCI w/ FS Poly",
            "Top Secret / Sensitive Compartmented Information with Full Scope Polygraph",
        ),
    ]
)

# source: https,//www.defense.gov/Resources/Insignia/
ARMY_ENLISTED_PAYGRADES = [
    ("E-1", "PV2", "Private"),
    ("E-2", "PV2", "Private"),
    ("E-3", "PFC", "Private First Class"),
    ("E-4", "SPC", "Specialist", "CPL", "Corporal"),
    ("E-5", "SGT", "Sergeant"),
    ("E-6", "SSG", "Staff Sergeant"),
    ("E-7", "SFC", "Sergeant First Class"),
    ("E-8", "MSG", "Master Sergeant", "1SG", "First Sergeant"),
    ("E-9", "SGM", "Sergeant Major", "CSM", "Command Sergeant Major"),
]
ARMY_WARRANT_OFFICER_PAYGRADES = [
    ("W-1", "WO1", "Warrant Officer 1"),
    ("W-2", "CW2", "Chief Warrant Officer 2"),
    ("W-3", "CW3", "Chief Warrant Officer 3"),
    ("W-4", "CW4", "Chief Warrant Officer 4"),
    ("W-5", "CW5", "Chief Warrant Officer 5"),
]
ARMY_OFFICER_PAYGRADES = [
    ("O-1", "2LT", "Second Lieutenant"),
    ("O-2", "1LT", "First Lieutenant"),
    ("O-3", "CPT", "Captain"),
    ("O-4", "MAJ", "Major"),
    ("O-5", "LTC", "Lieutenant Colonel"),
    ("O-6", "COL", "Colonel"),
    ("O-7", "BG", "Brigadier General"),
    ("O-8", "MG", "Major General"),
    ("O-9", "LTG", "Lieutenant General"),
    ("O-10", "GEN", "General"),
]

MARINE_CORPS_ENLISTED_PAYGRADES = [
    ("E-1", "PVT", "Private"),
    ("E-2", "PFC", "Private First Class"),
    ("E-3", "LCpl", "Lance Corporal"),
    ("E-4", "Cpl", "Corporal"),
    ("E-5", "Sgt", "Sergeant"),
    ("E-6", "SSgt", "Staff Sergeant"),
    ("E-7", "GySgt", "Gunnery Sergeant"),
    ("E-8", "MSgt", "Master Sergeant", "1Sgt", "First Sergeant"),
    ("E-9", "MGySgt", "Master Gunnery Sergeant", "SGTMAJ", "Sergeant Major"),
]
MARINE_CORPS_WARRANT_OFFICER_PAYGRADES = ARMY_WARRANT_OFFICER_PAYGRADES
MARINE_CORPS_OFFICER_PAYGRADES = ARMY_OFFICER_PAYGRADES

NAVY_ENLISTED_POSITIONS = [
    ("E-1", "SR", "Seaman Recruit"),
    ("E-2", "SA", "Seaman Apprentice"),
    ("E-3", "SN", "Seaman"),
    ("E-4", "PO3", "Petty Officer Third Class"),
    ("E-5", "PO2", "Petty Officer Second Class"),
    ("E-6", "PO1", "Petty Officer First Class"),
    ("E-7", "CPO", "Chief Petty Officer"),
    ("E-8", "SCPO", "Senior Chief Petty Officer"),
    ("E-9", "MCPO", "Master Chief Petty Officer"),
]
NAVY_WARRANT_OFFICER_PAYGRADES = [
    ("W-1", "WO1", "USN Warrant Officer 1"),
    ("W-2", "CWO2", "USN Chief Warrant Officer 2"),
    ("W-3", "CWO3", "USN Chief Warrant Officer 3"),
    ("W-4", "CWO4", "USN Chief Warrant Officer 4"),
    ("W-5", "CWO5", "USN Chief Warrant Officer 5"),
]
NAVY_OFFICER_PAYGRADES = [
    ("O-1", "ENS", "Ensign"),
    ("O-2", "LTJG", "Lieutenant Junior Grade"),
    ("O-3", "LT", "Lieutenant"),
    ("O-4", "LCDR", "Lieutenant Commander"),
    ("O-5", "CDR", "Commander"),
    ("O-6", "CAPT", "Captain"),
    ("O-7", "RDML", "Rear Admiral Lower Half"),
    ("O-8", "RADM", "Rear Admiral"),
    ("O-9", "VADM", "Vice Admiral"),
    ("O-10", "ADM", "Admiral"),
]

AIR_FORCE_ENLISTED_PAYGRADES = [
    ("E-1", "Amn", "Specialist 1"),
    ("E-2", "Amn", "Airman"),
    ("E-3", "A1C", "Airman First Class"),
    ("E-4", "SrA", "Senior Airman"),
    ("E-5", "SSgt", "Staff Sergeant"),
    ("E-6", "TSgt", "Technical Sergeant"),
    ("E-7", "MSgt", "Master Sergeant"),
    ("E-8", "SMSgt", "Senior Master Sergeant", "CMSgt", "Chief Master Sergeant"),
    ("E-9", "CMSgt", "Chief Master Sergeant of the Air Force"),
]
AIR_FORCE_OFFICER_PAYGRADES = ARMY_OFFICER_PAYGRADES

SPACE_FORCE_ENLISTED_PAYGRADES = [
    ("E-1", "Spc1", "Specialist 1"),
    ("E-2", "Spc2", "Specialist 2"),
    ("E-3", "Spc3", "Specialist 3"),
    ("E-4", "Spc4", "Specialist 4"),
    ("E-5", "Sgt", "Sergeant"),
    ("E-6", "TSgt", "Technical Sergeant"),
    ("E-7", "MSgt", "Master Sergeant"),
    ("E-8", "SMSgt", "Senior Master Sergeant"),
    ("E-9", "CMSgt", "Chief Master Sergeant"),
]
SPACE_FORCE_OFFICER_PAYGRADES = ARMY_OFFICER_PAYGRADES

PAYGRADES = OrderedDict(
    [
        (
            "Enlisted",
            OrderedDict(
                [
                    ("Army", ARMY_ENLISTED_PAYGRADES),
                    ("Marine Corps", MARINE_CORPS_ENLISTED_PAYGRADES),
                    ("Navy", NAVY_ENLISTED_POSITIONS),
                    ("Air Force", AIR_FORCE_ENLISTED_PAYGRADES),
                    ("Space Force", SPACE_FORCE_ENLISTED_PAYGRADES),
                ]
            ),
        ),
        (
            "Warrant Officer",
            OrderedDict(
                [
                    ("Army", ARMY_WARRANT_OFFICER_PAYGRADES),
                    ("Marine Corps", MARINE_CORPS_WARRANT_OFFICER_PAYGRADES),
                    ("Navy", NAVY_WARRANT_OFFICER_PAYGRADES),
                ]
            ),
        ),
        (
            "Officer",
            OrderedDict(
                [
                    ("Army", ARMY_OFFICER_PAYGRADES),
                    ("Marine Corps", MARINE_CORPS_OFFICER_PAYGRADES),
                    ("Navy", NAVY_OFFICER_PAYGRADES),
                    ("Air Force", AIR_FORCE_OFFICER_PAYGRADES),
                    ("Space Force", SPACE_FORCE_OFFICER_PAYGRADES),
                ]
            ),
        ),
    ]
)

BRANCHES = OrderedDict(
    [
        ("Army", ("Army Acitve Duty", "Army National Guard", "Army Reserve")),
        ("Marine Corps", ("Marine Corps Active Duty", "Marine Corps Reserve")),
        ("Navy", ("Navy Active Duty", "Navy Reserve")),
        ("Air Force", ("Air Force Active Duty", "Air Force Reserve")),
        ("Space Force", ("Space Force Active Duty", "Space Force Reserve")),
    ]
)

RANK_TIERS = ["Enlisted", "Warrant Officer", "Officer"]
