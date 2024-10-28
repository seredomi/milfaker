CLEARANCES = {
    "C": "Confidential",
    "S": "Secret",
    "TS": "Top Secret",
    "TS/SCI": "Top Secret / Sensitive Compartmented Information",
    "TS/SCI w/ CI Poly": "Top Secret / Sensitive Compartmented Information with Counterintelligence Polygraph",
    "TS/SCI w/ FS Poly": "Top Secret / Sensitive Compartmented Information with Full Scope Polygraph",
}

# source: https://www.defense.gov/Resources/Insignia/
ENLISTED_PAYGRADES = {
    "E-1": {
        "Army": ["Private"],
        "Marine Corps": ["Private"],
        "Navy": ["Seaman Recruit"],
        "Air Force": ["Airman Basic"],
        "Space Force": ["Specialist 1"],
    },
    "E-2": {
        "Army": ["Private"],
        "Marine Corps": ["Private First Class"],
        "Navy": ["Seaman Apprentice"],
        "Air Force": ["Airman"],
        "Space Force": ["Specialist 2"],
    },
    "E-3": {
        "Army": ["Private First Class"],
        "Marine Corps": ["Lance Corporal"],
        "Navy": ["Seaman"],
        "Air Force": ["Airman First Class"],
        "Space Force": ["Specialist 3"],
    },
    "E-4": {
        "Army": ["Corporal", "Specialist"],
        "Marine Corps": ["Corporal"],
        "Navy": ["Petty Officer Third Class"],
        "Air Force": ["Senior Airman"],
        "Space Force": ["Specialist 4"],
    },
    "E-5": {
        "Army": ["Sergeant"],
        "Marine Corps": ["Sergeant"],
        "Navy": ["Petty Officer Second Class"],
        "Air Force": ["Staff Sergeant"],
        "Space Force": ["Sergeant"],
    },
    "E-6": {
        "Army": ["Staff Sergeant"],
        "Marine Corps": ["Staff Sergeant"],
        "Navy": ["Petty Officer First Class"],
        "Air Force": ["Technical Sergeant"],
        "Space Force": ["Technical Sergeant"],
    },
    "E-7": {
        "Army": ["Sergeant First Class"],
        "Marine Corps": ["Gunnery Sergeant"],
        "Navy": ["Chief Petty Officer"],
        "Air Force": ["Master Sergeant", "First Sergeant"],
        "Space Force": ["Master Sergeant"],
    },
    "E-8": {
        "Army": ["Master Sergeant", "First Sergeant"],
        "Marine Corps": ["Master Sergeant", "First Sergeant"],
        "Navy": ["Senior Chief Petty Officer"],
        "Air Force": ["Senior Master Sergeant", "First Sergeant"],
        "Space Force": ["Senior Master Sergeant"],
    },
    "E-9": {
        "Army": ["Sergeant Major", "Command Sergeant Major"],
        "Marine Corps": ["Master Gunnery Sergeant", "Sergeant Major"],
        "Navy": ["Master Chief Petty Officer", "Fleet/Command Master Chief Petty Officer"],
        "Air Force": ["Chief Master Sergeant", "First Sergeant", "Command Chief Master Sergeant"],
        "Space Force": ["Chief Master Sergeant"],
    },
}
WARRANT_OFFICER_PAYGRADES = {
    "W-1": {
        "Army": ["Warrant Officer 1"],
        "Marine Corps": ["Warrant Officer 1"],
        "Navy": ["USN Warrant Officer 1"],
    },
    "W-2": {
        "Army": ["Chief Warrant Officer 2"],
        "Marine Corps": ["Chief Warrant Officer 2"],
        "Navy": ["USN Chief Warrant Officer 2"],
    },
    "W-3": {
        "Army": ["Chief Warrant Officer 3"],
        "Marine Corps": ["Chief Warrant Officer 3"],
        "Navy": ["USN Chief Warrant Officer 3"],
    },
    "W-4": {
        "Army": ["Chief Warrant Officer 4"],
        "Marine Corps": ["Chief Warrant Officer 4"],
        "Navy": ["USN Chief Warrant Officer 4"],
    },
    "W-5": {
        "Army": ["Chief Warrant Officer 5"],
        "Marine Corps": ["Chief Warrant Officer 5"],
        "Navy": ["USN Chief Warrant Officer 5"],
    },
}
OFFICER_PAYGRADES = {
    "O-1": {
        "Army": ["Second Lieutenant"],
        "Marine Corps": ["Second Lieutenant"],
        "Navy": ["Ensign"],
        "Air Force": ["Second Lieutenant"],
        "Space Force": ["Second Lieutenant"],
    },
    "O-2": {
        "Army": ["First Lieutenant"],
        "Marine Corps": ["First Lieutenant"],
        "Navy": ["Lieutenant Junior Grade"],
        "Air Force": ["First Lieutenant"],
        "Space Force": ["First Lieutenant"],
    },
    "O-3": {
        "Army": ["Captain"],
        "Marine Corps": ["Captain"],
        "Navy": ["Lieutenant"],
        "Air Force": ["Captain"],
        "Space Force": ["Captain"],
    },
    "O-4": {
        "Army": ["Major"],
        "Marine Corps": ["Major"],
        "Navy": ["Lieutenant Commander"],
        "Air Force": ["Major"],
        "Space Force": ["Major"],
    },
    "O-5": {
        "Army": ["Lieutenant Colonel"],
        "Marine Corps": ["Lieutenant Colonel"],
        "Navy": ["Commander"],
        "Air Force": ["Lieutenant Colonel"],
        "Space Force": ["Lieutenant Colonel"],
    },
    "O-6": {
        "Army": ["Colonel"],
        "Marine Corps": ["Colonel"],
        "Navy": ["Captain"],
        "Air Force": ["Colonel"],
        "Space Force": ["Colonel"],
    },
    "O-7": {
        "Army": ["Brigadier General"],
        "Marine Corps": ["Brigadier General"],
        "Navy": ["Rear Admiral Lower Half"],
        "Air Force": ["Brigadier General"],
        "Space Force": ["Brigadier General"],
    },
    "O-8": {
        "Army": ["Major General"],
        "Marine Corps": ["Major General"],
        "Navy": ["Rear Admiral Upper Half"],
        "Air Force": ["Major General"],
        "Space Force": ["Major General"],
    },
    "O-9": {
        "Army": ["Lieutenant General"],
        "Marine Corps": ["Lieutenant General"],
        "Navy": ["Vice Admiral"],
        "Air Force": ["Lieutenant General"],
        "Space Force": ["Lieutenant General"],
    },
    "O-10": {
        "Army": ["General"],
        "Marine Corps": ["General"],
        "Navy": ["Admiral"],
        "Air Force": ["General"],
        "Space Force": ["General"],
    },
}
PAYGRADES = {
    **ENLISTED_PAYGRADES,
    **WARRANT_OFFICER_PAYGRADES,
    **OFFICER_PAYGRADES,
}
