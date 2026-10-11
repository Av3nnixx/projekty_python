import random
def los_postac():
    postacie = ['8-Bit', 'Amber', 'Angelo', 'Ash', 'Barley', 'Bea', 'Belle', 'Berry', 'Bibi', 'Bo', 'Bonnie', 'Brock', 'Bull', 'Buster', 'Buzz', 'Byron', 'Carl', 'Charlie', 'Chester', 'Chuck', 'Clancy', 'Colette', 'Colt', 'Cordelius', 'Crow', 'Darryl', 'Doug', 'Draco', 'Dynamike', 'Edgar', 'El Primo', 'Emz', 'Eve', 'Fang', 'Finx', 'Frank', 'Gale', 'Gene', 'Gigi', 'Gray', 'Griff', 'Grom', 'Gus', 'Hank', 'Jacky', 'Janet', 'Jessie', 'Juju', 'Jae-Yong', 'Kaze', 'Kenji', 'Kit', 'Larry & Lawrie', 'Leon', 'Lily', 'Lola', 'Lou', 'Lumi', 'Maisie', 'Mandy', 'Max', 'Meeple', 'Melodie', 'Mico', 'Mina', 'Moe', 'Mortis', 'Mr. P', 'Nani', 'Nita', 'Ollie', 'Otis', 'Pam', 'Pearl', 'Penny', 'Piper', 'Poco', 'R-T', 'Rico', 'Rosa', 'Ruffs', 'Sam', 'Sandy', 'Shade', 'Shelly', 'Spike', 'Sprout', 'Squeak', 'Stu', 'Surge', 'Tara', 'Tick', 'Trunk', 'Willow', 'Ziggy']
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]
    x = zip(liczby,postacie)
    x = dict(x)
    liczba = random.randint(1,96)
    postac = x[liczba]
    print(postac)
los_postac()