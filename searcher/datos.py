from searcher import Searcher
import pandas as pd
#35.230.111.228
searcher = Searcher()

# cargar datos
"""
moons = {"name":['Io','Europa','Ganymede','Callisto',
                 'Titan','Enceladus','Iapetus','Rhea'],
         "planet":['Jupiter','Jupiter','Jupiter','Jupiter',
                   'Saturn','Saturn','Saturn','Saturn'],
         "planet_distance":['421.8','671.1','1,070.4','1,882.7',
                            '1,221,870','238,000','3,560,820','527,040'],
         "diameter":['3,642','3,122','5,268','4,820',
                     '5,150','504','1,470','1,528'],
         "orbit_days":['1.77','3.55','7.15','16.69',
                       '15.95','1.37','79.33','4.52'],
         "description":['Io is the innermost of Jupiter\'s four largest moons and is the most volcanically active body in our solar system, with over 400 active volcanoes. The intense tidal forces generated by Jupiter\'s gravity cause constant flexing and heating of Io\'s interior, leading to its fiery eruptions. In Greek mythology, Io was a priestess of Hera who was turned into a cow to hide her from Zeus.','Europa is the smallest of the four Galilean moons but is known for its smooth, icy surface with intriguing cracks and lines. It\'s believed to have a subsurface ocean beneath its icy crust, making it a prime target in the search for extraterrestrial life. In mythology, Europa was a Phoenician princess kidnapped by Zeus.','Ganymede is the largest moon in the solar system, even bigger than the planet Mercury. It has its own magnetic field and a diverse landscape with both heavily cratered regions and younger, grooved terrains. In Greek mythology, Ganymede was a Trojan prince who was taken by Zeus to be his cupbearer on Mount Olympus.','Callisto is one of the most heavily cratered objects in the solar system, indicating a lack of significant geological activity. It is believed to be one of the oldest objects in the solar system. In Greek mythology, Callisto was a nymph and companion of Artemis who was turned into a bear by Zeus.',
                        'Titan is the largest moon of Saturn and the second-largest moon in the solar system. It has a thick atmosphere primarily composed of nitrogen, with lakes and rivers of liquid methane and ethane on its surface, making it a target of astrobiological interest. Titan is named after the Titans of Greek mythology, the first divine beings.','Enceladus is known for its geysers that spew water and ice into space from cracks in its icy crust. These geysers have raised the possibility of a subsurface ocean beneath the moon\'s surface, making it a prime candidate for the search for extraterrestrial life. Enceladus is named after a giant in Greek mythology who was buried under Mount Etna.','Iapetus has a distinctive two-tone appearance, with one side being much darker than the other. This contrast is due to the presence of a dark material, possibly from external sources, covering one hemisphere. Iapetus is named after a Titan in Greek mythology, the son of Uranus and Gaia.','Rhea is the second-largest moon of Saturn and is heavily cratered, indicating a long history of impacts. It has a relatively bright surface and was discovered by Italian astronomer Giovanni Domenico Cassini in 1672. In Greek mythology, Rhea was a Titaness and the mother of the Olympian gods, including Zeus.']
         }

planets = {
    "sun_distance": ['57,90', '108,20', '149,60', '228', '778', '1400', '2870', '4.500', '5906,4'],
    "earth_distance": ['77', '38', '0', '225', '587', '1300', '2600', '4345,4', '5800'],
    "year_length": ['88', '225', '365', '687', '4328,9', '10585', '30660', '60225', '90520'],
    "day_length": ['1416', '5832', '24', '25,5', '11,33', '1018', '353', '16,25', '3672'],
    "diameter": ['4879,4', '12104', '12756', '6794', '139820', '116460', '51118', '49244', '2.376,60'],
    "mass": ['3,285E+23', '4,87E+24', '6E+24', '6,39E+23', '1,89813E+27', '5,683E+26', '8,6816E+25', '1,024E+26', '1,30 × 1022'],
    "density": ['54,3', '52,45', '55', '3,93', '1,33', '6,87', '19,05', '1,64', '1,88'],
    "known_satellites": ['0', '2', '1', '2', '95', '145', '27', '14', '3'],
    "avg_orbital": ['4.736.194', '35', '29,78', '24,13', '13,0697', '9,68', '6,81', '5,43', '4,74'],
    "avg_temperatures": ['167', '450', '15', '-62', '−121,15', '-176', '-195', '-218', '-229,1'],
    "description": ['Mercury, the cosmic speed demon of the solar system, is like the interstellar espresso shot you never knew you needed! Picture this: a scorching hot, pint sized planet that\'s closer to the Sun than a sunflower chasing sunshine. It\'s basically the solar system\'s hot potato, except it\'s so tiny that you could practically fit it in your cosmic pocket.But don\'t let its petite size fool you – Mercury\'s got some serious personality. With temperatures that swing from frying-pan hot enough to melt lead to ice-cold enough to freeze your cosmic popsicle, it\'s a real rollercoaster of climates. One moment, you\'re sizzling like a space bacon strip, and the next, you\'re cooler than a cosmic cucumber. Mercury\'s surface is a chaotic mixtape of craters, mountains, and valleys, like a DJ spinning space tunes on a rocky dance floor. Plus, it\'s got a day that\'s longer than its year, thanks to its wacky spin cycle – it\'s the ultimate planet with a serious case of <<Mercury Retrograde.>> <br/> And let\'s not forget the show-stealer: the sunsets on Mercury are a sight to behold, with the Sun appearing to do its very own cosmic limbo dance as it dips below the horizon. It\'s like Mother Nature decided to host the most dazzling light show in the universe. <br/> So, if you ever find yourself dreaming of a celestial adventure, hop on a spaceship and take a pit stop on Mercury. Just don\'t forget your SPF 1,000,000 sunscreen – you\'re gonna need it!', 'Venus, the solar system\'s sultry siren, is like the hottest date you\'ll never have – and I mean that quite literally! This planet is a scorching, sizzling, and sassy diva that\'ll make you break a sweat just thinking about it. <br/> Imagine a world where the weather report is just \"HOT\" every single day, and where rain isn\'t a refreshing shower but a torrential downpour of sulfuric acid. Venus is so fiery that it could make even the most seasoned sunbather retreat to the shade faster than you can say \"heatwave.\" <br/> But that\'s not all – Venus has a thick, mysterious veil of clouds that make it the ultimate enigma of the cosmos. These clouds are like the planet\'s cosmic fashion statement, perpetually draped in shades of yellow and orange, as if Venus is trying to outdo every sunset in the universe. <br/> And don\'t even get me started on Venus\'s signature move: the \"Retrograde Tango.\" While most planets spin clockwise, Venus decided to be the rebel of the solar system and spins counterclockwise. It\'s like the planet\'s own way of saying, \"I do what I want!\" <br/> Oh, and did I mention that Venus is the champion of the \"Greenhouse Gas Gala\"? Thanks to its thick atmosphere, it has a runaway greenhouse effect that could put even the trendiest eco-conscious celebs to shame. <br/> So, if you ever find yourself daydreaming of a fiery, acid-drenched, retrograde-spinning adventure, Venus is your go-to celestial hotspot. Just be sure to pack some serious heat-resistant gear, because this planet doesn\'t mess around when it comes to turning up the temperature!', 'Earth, the coolest hangout spot in the galaxy, is the ultimate cosmic rock star. It\'s like that trendy, bustling café where all the aliens secretly wish they had reservations! <br/> Picture a planet where you can have beach parties, ski trips, and jungle adventures all in one day – Earth\'s got it all. It\'s like a theme park with different zones for every type of thrill-seeker. You want icy mountains? Check. Sweltering deserts? Check. Lush rainforests? Double check. Earth is the ultimate vacation package, and it doesn\'t even require a spaceship ticket. <br/> And speaking of tickets, Earth\'s wildlife is like a never-ending parade of bizarre characters. From the quirky platypus to the majestic narwhal, it\'s a real-life carnival of creatures that could rival any intergalactic zoo. Plus, the humans – Earth\'s most dominant species – are like a chaotic blend of artists, scientists, and pizza enthusiasts. They\'ve even managed to send robots to other planets just to say, \"Hey, we\'re humans, and we\'re cool like that!\" <br/> Earth\'s got a built-in disco ball too – the Moon! Our trusty lunar sidekick keeps the night sky looking fab with its phases and lunar eclipses, making it the ultimate celestial dance partner. <br/> But Earth isn\'t all fun and games; it\'s also the planet of deep thoughts and philosophical pondering. It\'s where people gather around campfires to tell stories, gaze at the stars, and wonder about the meaning of life. It\'s like the universe\'s eternal coffee shop conversation that never gets old. <br/> So, if you ever get a chance to visit this cosmic hotspot, don\'t miss it. Earth is the place where adventure, wonder, and a little bit of chaos all come together in perfect harmony. Grab your passport (or spaceship) and join the interstellar party on this one-of-a-kind planet!', 'Earth, the coolest hangout spot in the galaxy, is the ultimate cosmic rock star. It\'s like that trendy, bustling café where all the aliens secretly wish they had reservations! <br/> Picture a planet where you can have beach parties, ski trips, and jungle adventures all in one day – Earth\'s got it all. It\'s like a theme park with different zones for every type of thrill-seeker. You want icy mountains? Check. Sweltering deserts? Check. Lush rainforests? Double check. Earth is the ultimate vacation package, and it doesn\'t even require a spaceship ticket. <br/> And speaking of tickets, Earth\'s wildlife is like a never-ending parade of bizarre characters. From the quirky platypus to the majestic narwhal, it\'s a real-life carnival of creatures that could rival any intergalactic zoo. Plus, the humans – Earth\'s most dominant species – are like a chaotic blend of artists, scientists, and pizza enthusiasts. They\'ve even managed to send robots to other planets just to say, \"Hey, we\'re humans, and we\'re cool like that!\" <br/> Earth\'s got a built-in disco ball too – the Moon! Our trusty lunar sidekick keeps the night sky looking fab with its phases and lunar eclipses, making it the ultimate celestial dance partner. <br/> But Earth isn\'t all fun and games; it\'s also the planet of deep thoughts and philosophical pondering. It\'s where people gather around campfires to tell stories, gaze at the stars, and wonder about the meaning of life. It\'s like the universe\'s eternal coffee shop conversation that never gets old. <br/> So, if you ever get a chance to visit this cosmic hotspot, don\'t miss it. Earth is the place where adventure, wonder, and a little bit of chaos all come together in perfect harmony. Grab your passport (or spaceship) and join the interstellar party on this one-of-a-kind planet!', 'Mars, the red-hot rascal of the solar system, is like the ultimate space adventurer\'s playground – a cosmic theme park with thrills, chills, and a whole lot of rusty charm! <br/> Imagine a world where the sky is a perpetual dusty tangerine hue, and where the idea of a \"red planet\" is taken quite literally. Mars is like the universe\'s very own fire-breathing dragon, a place where fiery sunsets last for hours and make you feel like you\'re in the front row of a celestial rock concert. <br/> Now, if you\'re looking for rugged landscapes that could put the Grand Canyon to shame, Mars is your go-to destination. It\'s got enormous canyons that stretch for miles and craters that look like they were plucked straight out of a sci-fi movie set. It\'s the kind of place where you could play hide-and-seek for eons and never run out of hiding spots. <br/>And let\'s not forget about the ice cream. Yes, you heard that right – Mars has polar ice caps made of water and dry ice, which is like Mother Nature\'s way of saying, \"Here, have some Martian sorbet to cool off after all that adventuring!\" <br/>Now, Mars does have a bit of a reputation for being a loner, with no neighbors to borrow a cup of sugar from, but that just means it\'s got plenty of room for you to make your mark. Plus, it\'s a hotbed of scientific intrigue, with NASA and other space agencies sending rovers to explore its mysteries and answer the age-old question: \"Is there life on Mars?\" <br/> So, if you\'re ready for a wild, dusty, and red-tinted adventure that\'s out of this world, Mars is the place to be. Just remember to pack your space sunscreen and a sense of interstellar curiosity – you\'re in for an extraterrestrial escapade like no other!', 'Jupiter, the cosmic heavyweight champion of the solar system, is like the oversized, gassy uncle at the family reunion who\'s always the life of the party! This planet is so big that if it were a celebrity, it would need its own zip code.<br/>Imagine a world where clouds come in more flavors than an intergalactic ice cream parlor – you\'ve got your vanilla, butterscotch, and even a swirl of raspberry-red storms that could put any rave\'s laser show to shame. Jupiter\'s iconic Great Red Spot is like the ultimate stormy disco ball, twirling in the vast dance floor of space.<br/>But Jupiter isn\'t just about looks – it\'s also got some serious bling. The planet\'s got an entourage of moons, and by \"entourage,\" I mean a whopping 79 of them! Some are like the quirky cousins who tag along for the ride, while others are the mysterious rebels that keep scientists scratching their heads.<br/>Speaking of head-scratchers, Jupiter is also the planet with a heart of gold – or rather, metallic hydrogen. Deep inside its ginormous belly, there\'s a core made of this exotic substance that\'s like the holy grail of high-pressure physics experiments.<br/>And let\'s not forget Jupiter\'s dramatic flair – it\'s a cosmic protector, using its massive gravitational pull to shield the inner planets from potential asteroid threats like a real-life superhero. Move over, Iron Man, it\'s Jupiter to the rescue!<br/>So, if you\'re ever in need of a planet-sized dose of awe, wonder, and interstellar pizzazz, Jupiter is your intergalactic destination. Just remember to pack your telescope, because this gas giant is like a never-ending cosmic fireworks show that\'s always ready to dazzle your stargazing soul!', 'Saturn, the celestial bling of the solar system, is like the Kardashian of planets – it\'s all about the glitz, glamour, and those fabulous rings! If Earth is a hip coffee shop, Saturn is the ultra-chic cocktail lounge where the universe\'s A-listers hang out.<br/>Picture a world with more style than a Parisian fashion runway – Saturn\'s got those iconic, shimmering rings that look like they\'re straight out of a cosmic jewelry store. They\'re like the planet\'s way of saying, \"I woke up like this, fabulous!\"<br/>But Saturn isn\'t just about its fashion-forward appearance. It\'s also a planet with serious personality. With crazy-fast winds that make Earth\'s hurricanes look like a gentle breeze, Saturn is like the intergalactic roller coaster ride you never knew you signed up for.<br/>And let\'s not forget the party animals – Saturn has a wild entourage of moons that are like the quirky characters at an extravagant soirée. Titan, for instance, is the one with the thick orange atmosphere, like the life of the party who insists on wearing sunglasses indoors.<br/>But Saturn\'s biggest secret weapon? It\'s got a magnetic field that could out-dance even the most electrifying pop stars. It generates enough electricity to power a whole fleet of interstellar spaceships.<br/>So, if you\'re ever in the mood for a cosmic fashion show, a wild ride, or just some good old-fashioned stargazing in style, Saturn is your planetary paradise. Just remember to pack your interstellar camera – you won\'t want to miss capturing the glitzy beauty of this celestial superstar!', 'Uranus, the solar system\'s cosmic oddball, is like that eccentric neighbor who throws the quirkiest backyard parties you\'ve ever seen. It\'s a planet that marches to the beat of its own interstellar drum, and it\'s a real breath of fresh air—well, maybe more like a whiff of space gas!<br/>Picture a world that spins on its side, like it\'s trying to do the limbo in the cosmic dance-off. Yes, Uranus decided to tilt itself almost perpendicular to its orbit, giving it a spin cycle that\'s more topsy-turvy than a rollercoaster ride. It\'s like the planet\'s own way of saying, \"I\'m different, and I\'m proud of it!\"<br/>And speaking of pride, Uranus is famous for its beautiful bluish-green complexion, thanks to the icy methane in its atmosphere. It\'s like the universe\'s own fashion-forward statement, with colors that would make any other planet jealous.<br/>But don\'t think Uranus is all about looks – it\'s also got a mystery to solve. The planet\'s core temperature is hotter than you\'d expect, like finding a cozy fireplace in the middle of a snowstorm. Scientists are scratching their heads trying to figure out why, making Uranus the ultimate cosmic enigma.<br/>Plus, Uranus has a funky ring system and a handful of quirky moons, each with its own personality. It\'s like a cosmic sitcom where the planets and moons are the cast, and every day is a new episode of interstellar drama.<br/>So, if you\'re ready for a journey to the outer reaches of our solar system and a visit to the wackiest neighbor in the cosmic cul-de-sac, Uranus is your ticket to an offbeat adventure like no other. Just remember to bring your sense of wonder and a penchant for the peculiar – you\'re in for a space odyssey that\'s out of this world!', 'Neptune, the cool cat of the cosmos, is a planet wrapped in mystery and painted in dazzling shades of blue and green. With its wild storms, supersonic winds, and peculiar weather phenomena like diamond rain, it\'s the ultimate rebel poet of our solar system. This enigmatic giant spins on its side, dancing to its own cosmic rhythm, proving that in the vast expanse of space, there\'s always room for a planet with a whole lot of charm and a splash of interstellar eccentricity.', 'Pluto, the cosmic underdog, dances on the fringes of our solar system like a mischievous sprite playing hide-and-seek with the stars. This pint-sized planet, once the ninth member of the planetary club, boasts a surface adorned with icy plains and mysterious, otherworldly terrains. It\'s the rebel with a frosty cause, wrapped in an enigmatic atmosphere that keeps its secrets well-guarded. Despite its demotion to \"dwarf planet\" status, Pluto shines brightly, reminding us that even the smallest celestial bodies can capture our imaginations and inspire awe in the vast, wondrous expanse of space.'],
    "images": [f"/images/planetas/{planeta.lower()}" for planeta in ['Mercurio', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']],
    "name": ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
}

#searcher.insert_moons_data(moons)

searcher.insert_planets_data(planets)
"""
#print(moons)
#moons_df.to_sql(con=conection,name='moons',if_exists='replace',index=False)

#moons = searcher.get_planets()

#for fila in moons:
#    print(fila)

result = searcher.get_moon("Jupiter")


#conection.close()


'''
planetas = {"name":['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'],
            "sun_distance":[57.9,108.2,149.60,228,778,1400,2870,4500,5906.4],
            "earth_distance":[77,38,0,225,587,1300,2600,4345.4,5800],
            "year_length":[88,225,365,687,4328.9,10585,30660,60225,90520],
            "day_length":[1416,5832,24,25.5,11.33,1018,353,16.25,49244,2376.6],
            "diameter":
            }

            '''