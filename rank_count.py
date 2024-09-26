a = [
     0, # 1   Junior Private
     2, # 2   Private
     4, # 3   Senior Private
     4, # 4   First Class Private
     4, # 5   Master Private
     
     0, # 6   Junior Corporal
     2, # 7   Corporal
     4, # 8   Senior Corporal
     4, # 9   First Class Corporal
     4, # 10  Master Corporal

     0, # 11  Junior Sergeant
     2, # 12  Sergeant
     4, # 13  Senior Sergeant
     4, # 14  First Class Sergeant
     4, # 15  Master Sergeant
     
     0, # 16  Junior Officer
     2, # 17  Officer
     4, # 18  Senior Officer
     4, # 19  First Class Officer
     4, # 20  Master Officer

     0, # 21  Junior Chief
     2, # 22  Chief
     4, # 23  Senior Chief
     4, # 24  First Class Chief
     4, # 25  Master Chief
     
     0, # 26  Junior Warrant Officer
     2, # 27  Warrant Officer
     4, # 28  Senior Warrant Officer
     4, # 29  First Class Warrant Officer
     4, # 30  Master Warrant Officer

     0, # 31  Junior Lieutenant
     2, # 32  Lieutenant
     4, # 33  Senior Lieutenant
     4, # 34  First Class Lieutenant
     4, # 35  Master Lieutenant
     
     0, # 36  Junior Captain
     2, # 37  Captain
     4, # 38  Senior Captain
     4, # 39  First Class Captain
     4, # 40  Master Captain

     1, # 41  Junior Major
     1, # 42  Major
     1, # 43  Senior Major
     1, # 44  First Class Major
     1, # 45  Master Major
     
     1, # 46  Junior Colonel
     1, # 47  Colonel
     1, # 48  Senior Colonel
     1, # 49  First Class Colonel
     1, # 50  Master Colonel

     1, # 51  Junior General
     1, # 52  General
     1, # 53  Senior General
     1, # 54  First Class General
     36, # 55  Master General
     
     36, # 56  Brigadier General
     6,  # 57  Lieutenant General
     6,  # 58  Major General
     6,  # 59  Colonel General
     6,  # 60  General
     1,  # 61  Army General
     
     36, # 62  General of Planetary Region
     36, # 63  General of Planetary Sector
     
     36, # 64  Planetary Marshal
     36, # 65  Star Marshal
     
     36, # 66  General of Star Sector Rank 4
     36, # 67  General of Star Sector Rank 3
     36, # 68  General of Star Sector Rank 2
     36, # 69  General of Star Sector Rank 1
     1,  # 70  Marshal of the Galaxy

     36, # 71  General of Galactic Group Rank 4
     36, # 72  General of Galactic Group Rank 3
     36, # 73  General of Galactic Group Rank 2
     36, # 74  General of Galactic Group Rank 1
     1,  # 75  Marshal of Galactic Group
     
     36, # 76  General of Galaxy Clusters Rank 4
     36, # 77  General of Galaxy Clusters Rank 3
     36, # 78  General of Galaxy Clusters Rank 2
     36, # 79  General of Galaxy Clusters Rank 1
     1,  # 80  Marshal of Galaxy Clusters

     36, # 81  General of Superclusters Rank 3
     36, # 82  General of Superclusters Rank 2
     36, # 83  General of Superclusters Rank 1
     1,  # 84  Marshal of Superclusters
     
     36, # 85  General of the Great Wall Rank 3
     36, # 86  General of the Great Wall Rank 2
     36, # 87  General of the Great Wall Rank 1
     1,  # 88  Marshal of the Great Wall
     
     36, # 89  General of the Cosmic Web Rank 3
     36, # 90  General of the Cosmic Web Rank 2
     36, # 91  General of the Cosmic Web Rank 1
     1,  # 92  Marshal of the Cosmic Web
     
     36, # 93  General of Universe Subsector Rank 3
     36, # 94  General of Universe Subsector Rank 2
     36, # 95  General of Universe Subsector Rank 1
     1,  # 96  Marshal of Universe Subsector
     
     36, # 97  Marshal of Universe Sector Rank 3
     36, # 98  Marshal of Universe Sector Rank 2
     6,  # 99  Marshal of Universe Sector Rank 1
     
     1, # 100 Marshal of the Universe
]

print(
    a[99]+
    
    a[99]*a[98]+
    a[99]*a[98]*a[97]+
    a[99]*a[98]*a[97]*a[96]+
    
    a[99]*a[98]*a[97]*a[96]*a[95]+
    a[99]*a[98]*a[97]*a[96]*a[95]*a[94]+
    a[99]*a[98]*a[97]*a[96]*a[95]*a[94]*a[93]
)
