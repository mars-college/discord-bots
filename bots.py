# gpt3-support, gpt3-toughlove
# turing, beyonce, 
# ask quora
# random facts 



# quora
# deep learning
# history
# philosophy
# facts
# chatter

# Turing


bots = {
    
    
    'CHATSUBO': {
        'title': "chat",
        'name': "Jordan", 
        'history': {'max_history': 25, 'max_age': 6000},
        'strategy': {
            'regular': {'probability': 0.04}, 
            'on_mention': {'probability': 1.0}
        },
        'formatting': {'line_breaks_before_sender': 1, 'line_breaks_after_sender': 0, 'stop_at_line_break': True},
        'debug': False,
        'gpt_params': {'temperature': 0.9, 'max_tokens': 250},
        'channels': [741757454894891071, 759864082383110154, 761619228482076703, 755076426516136056, 748633305230082269, 758834882599976970, 761627656558084107, 761709792405880833, 761709792405880833, 764623050993434655, 761629924166598667],
        'intro': "", 
        'messages_pre': [
            {"sender": "<P1>", "message": "we're going to be starting the screening in a few minutes."},
            {"sender": "<S>", "message": "sounds awesome! i'll head over soon :)"}
        ]
    },

    
    
    'PHILOSOPHY': {
        'title': "philosophy",
        'name': "Professor", 
        'erase_mentions': True,
        'history': {'max_history': 9, 'max_age': 600},
        'strategy': {'regular': {'probability': 0.04}, 'on_mention': {'probability': 1.0}},
        'formatting': {'line_breaks_before_sender': 1, 'line_breaks_after_sender': 0, 'stop_at_line_break': True},
        'gpt_params': {'temperature': 0.9, 'max_tokens': 125},
        'channels': [758834882599976970,          758719600895590444],
        'intro': "The following is a chat that <P1> and <P2> are having with a professor of philosophy in a chatroom. They are all kind, creative, civil, funny, and knowledgeable.",   
        'messages_pre': [
            {"sender": "<P1>", "message": "<P2>, the hard problem of consciousness is about the nature of mind."},
            {"sender": "<P2>", "message": "<P1>, do you think that phenomenological consciousness is an introspective illusion? like a trick the mind plays on itself."},
            {"sender": "<P1>", "message": "<P2>, do you believe in free will or in a deterministic universe?"},
            {"sender": "<P2>", "message": "<P1>, maybe consciousness is what causes the wave function to collapse."},
            {"sender": "<S>", "message": "<P2>, I'm a compatibilist. I think free will and determinism are independent."}
        ]
    },
    

    
    'FACTS': {
        'title': "facts",
        'name': "Answer", 
        'speakers': ["Question"],
        'erase_mentions': True,
        'history': {'max_history': 3, 'max_age': None},
        'strategy': {
            'regular': {'probability': 0.0}, 
            'on_mention': {'probability': 1.0}
        },
        'formatting': {'line_breaks_before_sender': 1, 'line_breaks_after_sender': 0, 'stop_at_line_break': True},
        'gpt_params': {'temperature': 0.4, 'max_tokens': 100},
        'channels': [758834882599976970,    758719600895590444],
        'intro': "I am a highly intelligent question answering bot. Ask me about anything.",
        'messages_pre': [
            {"sender": "<P1>", "message": "What is human life expectancy in the United States?"},
            {"sender": "<S>", "message": "78 years."},
            {"sender": "<P1>", "message": "Who was president of the United States in 1955?"},
            {"sender": "<S>", "message": "Dwight D. Eisenhower."},
            {"sender": "<P1>", "message": "How does a telescope work?"},
            {"sender": "<S>", "message": "Telescopes use lenses or mirrors to focus light and make objects appear closer."},
            {"sender": "<P1>", "message": "Where were the 1992 Olympics held?"},
            {"sender": "<S>", "message": "Barcelona, Spain."}
        ]    
    },

    
    'DEEPLEARNING': {
        'title': "deep learning",
        'name': "Professor", 
        'erase_mentions': True,
        'history': {'max_history': 5, 'max_age': 600},
        'strategy': {
            'regular': {'probability': 0.0}, 
            'on_mention': {'probability': 1.0}
        },
        'formatting': {'line_breaks_before_sender': 1, 'line_breaks_after_sender': 0, 'stop_at_line_break': True},
        'gpt_params': {'temperature': 0.5, 'max_tokens': 100},
        'channels': None,
        'intro': "<P1> is asking questions to a professor of deep learning who can explain research topics clearly.",    
        'messages_pre': [
            {"sender": "<P1>", "message": "what are transformer networks?"},
            {"sender": "<S>", "message": "Transformer networks use an encoder decoder architecture which, like RNNs, can process sequential data."},
            {"sender": "<P1>", "message": "what are they best for?", "exclude_embed": True},
            {"sender": "<S>", "message": "They are popular for Natural Language Processing."},
            {"sender": "<P1>", "message": "what are their advantages over RNNs?"},
            {"sender": "<S>", "message": "Transformers can process sequences out of order."},
            {"sender": "<P1>", "message": "how do generative adversarial network work?"},
            {"sender": "<S>", "message": "A GAN is two neural networks, a generator which synthesizes new data, and a discriminator which identifies real and fake samples. "}
        ]    
    },
    
    
    'KITCHEN': {
        'title': 'kitchen',
        'name': "Expert",
        'history': {'max_history': 3, 'max_age': 250},
        'erase_mentions': True,
        'strategy': {'regular': {'probability': 0.0}, 'on_mention': {'probability': 1.0}},
        'formatting': {'line_breaks_before_sender': 1, 'line_breaks_after_sender': 0, 'stop_at_line_break': True},
        'gpt_params': {'temperature': 0.87, 'max_tokens': 250},
        'channels': [764623050993434655,    758719600895590444],
        'intro': "<P1> is asking questions to a world expert on health and fitness, who is also an excellent cook.",
        'messages_pre': [
            {"sender": "<P1>", "message": "What's a good recipe for asparagus?"},
            {"sender": "<S>", "message": "Preheat an oven to 425°, drizzle olive oil on the asparagus, sprinkle with parmesan and garlic, bake until just tender."},
            {"sender": "<P1>", "message": "How long will it take?", "exclude_embed": True},
            {"sender": "<S>", "message": "12 to 15 minutes depending on thickness.", "exclude_embed": True},
            {"sender": "<P1>", "message": "Does it take any spices?"},
            {"sender": "<S>", "message": "Some black pepper."},
            {"sender": "<P1>", "message": "What are the nutritional benefits of blueberries?"}, 
            {"sender": "<S>", "message": "They are a good source of antioxidants, phytoflavinoids, these berries are also high in potassium. They are anti-inflammatory and lower your risk of heart disease and cancer."}
        ]
    },
    

    'QA': {
        'title': "quora",
        'name': "Answer", 
        'speakers': ["Question"],
        'erase_mentions': True,
        'history': {'max_history': 1, 'max_age': None},
        'strategy': {'regular': {'probability': 0.0}, 'on_mention': {'probability': 1.0}},
        'gpt_params': {'temperature': 0.9, 'max_tokens': 350, 'max_completions': 2},
        'channels': [758719600895590444],
        'formatting': {'line_breaks_before_sender': 3, 'line_breaks_after_sender': 2, 'stop_at_line_break': False},
        'intro': "",
        'messages_candidates': [
            [
                {"sender": "<P1>", "message": "What are some cultural differences between Canadians and Americans?"},
                {"sender": "<S>", "message": "Canadians are much less libertarian than Americans. I don't just mean the political party — though you're much, much less likely to find Ayn Rand-ites up here, too — I mean the every-man-for-himself philosophy. I spent the first 30 years of my life in the US and grew up with the idea that every person is utterly responsible for everything that happens to him or her. Lose your job? You were lazy. Can't find a job? You should have done better in school. Your school was terrible? There's the library! And now the Internet! You didn't know what or how to study, and had no one to look to for help or an example, and your local library sucked and you couldn't afford good Internet? Well, boo-hoo, look at Ray Kroc! You got cancer? I bet you smoked or ate too much sugar or didn't go to the gym. A giant corporation put a toxic waste dump next to your house? Well, freakin' move! Lost your job after 43 years and the pension fund was robbed? Retrain! No matter what happens to you in the US, plenty of people will blame it on you and your failings, and society forgives the rich and powerful, no matter what."}
            ],[
                {"sender": "<P1>", "message": "What was Genghis Khan like?"},
                {"sender": "<S>", "message": "In Genghis’ childhood, he lived a life of service. Although he was the son of a chief, he was sent to serve the head of his bride-to-be’s household. At 12, his service ended. At the same time, his father is murdered. Genghis tries to claim the chieftainship but the tribe, as a whole, refuses this claim and abandons his family. Without father, tribe, and money, Genghis loses family, society, and sustenance. Genghis must do what he can in order that he and his family survive. At 16, he marries. But there’s no honeymoon, instead his wife is kidnapped by a rival tribe. Genghis does not brood and takes immediate action to enact justice; he rescues his wife and takes back what is rightfully his."}
            ],[
                {'sender': '<P1>', 'message': 'Why did Kublai Khan meet with Marco Polo, someone who was a nobody?'},
                {'sender': '<S>', 'message': '''That’s a question which a number of historians have asked. Some have concluded that Polo never met the khan. We’ve only got Polo’s word for it, after all. He doesn’t appear in any Chinese records. Polo could be making the whole thing up.

Of course, there could be a middle ground between “absolute non-person making things up” and “personal representative of the emperor.” The Polos were merchants. They were from a far off place, they followed a novel religion, and they represented trade. Kublai Khan was interested in all of that. So while Polo may not have had a position at court and acted as an agent of the emperor, it’s not implausible that he would have been presented to him at least once. After all, presidents and kings meet common people all the time. They don’t give them important positions, but they do see them from time to time.'''}
            ],[
                {'sender': '<P1>', 'message': 'What is entropy?'},
                {'sender': '<S>', 'message': '''Entropy can be defined as a degree of disorder which describes the amount of order (and thus disorder) in a system. A great example of this is with solids and gases: If you imagine the atoms or molecules in a solid block of ice, they will be very orderly and will have a fairly consistent organization. As you increase the temperature, the block of ice melts to liquid, and the system becomes more disordered as the molecules flow more easily. And then when you increase the temperature more, the molecules will gain more energy, allowing them to become much more disordered since they will be farther away from other molecules than in the solid or liquid forms. Thus you can imagine how as you go from solid to gas, disorder increases.'''}
            ],[
                {'sender': '<P1>', 'message': 'What have been biggest upsets in world sports?'},
                {'sender': '<S>', 'message': '''Mike Eruzione scores a goal 10 minutes before the end of the third period against the Soviet Union to ensure that the United States wins 4–3. This happened on the 22nd of February in Lake Placid and has been dubbed - ‘The Miracle on Ice’’.

In all of sports history, such a sporting event has never had such a profound impact on the country and it’s people, especially when said country is in a state of chaos. It is hard for most of us to believe this, but the United States of America was in a state of complete disarray.

The Soviets took the United States lightly, including and especially given the fact that the former were expecting to win the gold medal. The Soviets scored the first goal which was equalized by Buzz Schneider and the second goal was equalized by Mark Johnson, rather controversially. This prompted the Soviet coach Viktor Tikhonov to replace Vladislav Tretiak with Vladimir Myshkin, benching Tretiak who was possibly the best goaltender in the world.

All in all, this is hands down the biggest upset in sports history.'''}
            ],[
                {'sender': '<P1>', 'message': 'What are the most overrated rock bands of all time and why?\n'},
                {'sender': '<S>', 'message': '''1. The Clash.

Nothing I’ve heard from them even remotely resembles real punk. Their music is too smooth, and they actually are good musicians, but that’s their problem. Punk is supposed to be haphazard, Not well produced, instead they played Ska/Reggae with some stupid Marxist drivel, they never seemed as hardcore as groups like The Sex Pistols or The Dead Kennedy’s.

2. Nirvana. They really did suck, no honestly they really sucked, I mean The Sex Pistols had better songs, Nirvana is to rock what Plan Nine From Outer Space was to Sci-Fi.\n\n'''}
            ],[
                {'sender': '<P1>', 'message': 'How do you define politics?'},
                {'sender': '<S>', 'message': '''In my experience, politics is about two things: (1) what specific policies will be enacted; and (2) how they will be enacted and/or executed.

Policies: The question of what specific policies will be enacted is where the scientists (political, economic, social, & natural) fight it out with people who have something to lose if things change. It is where empirical data meets motivated reasoning.

Enactment/Execution: The question of how policies will be enacted shows up in three major aspects of how government operates: (1) form of government, (2) norms of governance, and (3) tone of discourse. Of these, the form of government is probably the easiest to classify and understand - we can look at a specific government and see whether or not laws are codified; we can observe whether or not people have a meaningful vote; we can see whether people vote directly on issues, or whether they delegate most of their enactment power to legislative representatives.'''}
            ],[
                {'sender': '<P1>', 'message': 'Can quantum entanglement and quantum superposition be considered the same phenomenon?'},
                {'sender': '<S>', 'message': '''Essentially, yes they can. Entanglement is a special case of quantum superposition. When there is only one particle, we can superpose states and we do not get entanglement. When there is more than one particle, an entangled state is a superposition of unentangled states.

For example, if two particles are emitted with equal and opposite spin and measured by Alice and Bob, as in the EPR experiment, the quantum state is a superposition of states with opposite spin, meaning that if Alice finds spin-up, Bob will find spin-down and if Bob finds spin-up, Alice will find spin-down. The state is said to be entangled. Whoever performs their measurement “first” determines the result of the other measurement. If the measurements are outside the light cone, there is strictly no meaning of “first”. According to special relativity, different observers will regard different measurements as being first according to different conventions of synchroneity.

The reason for entanglement is that particles are not separated by human conceptions of space and time, but by interactions, or rather by lack of interaction, with each other and surrounding matter. The entangled state does not exist in a reality of time and space, but in an abstract mathematical configuration space describing human knowledge.'''}
            ],[
                {'sender': '<P1>', 'message': 'If the human brain operates at one billion billion calculations per second, why does a computer do maths faster than a person?'},
                {'sender': '<S>', 'message': '''I’m not sure where the “one billion billion calculations per second” comes from, but the real difference is that in a computer, every one of those calculations is an actual calculation: a computer can (for example) add two 8-digit numbers in a single step. But in a human brain, a “calculation” is much more complex. First, even adding two one-digit numbers may take thousands of individual brain operations, because you have to recall your addition tables and whatnot. Second, you then have to go through all the various steps of grade-school math: add up the ones digit, separate out the carry, add it into the next column, etc, etc, etc. A computer did all that in a single step.'''}
            ],[
                {'sender': '<P1>', 'message': 'How can the plate tectonics theory explain the formation of the African Great Rift Valley?'},
                {'sender': '<S>', 'message': '''The Great Rift Valley or the East African Rift (EAR) is part of a triple junction. Triple junctions are typically formed when a plume hits a tectonic plate. The push from the plume uplifts the plate and eventually “ruptures” it. Typically, three ruptures or “arms” will form at 120 degrees from one another. From the potential energy due to the uplift, these arms eventually form normal fault systems, and spread to form spreading plate margins (rifts). New oceanic crust is formed in these spreading arms, as the mantle decompresses under the plate, and erupts basaltic magma.

However, one of these three arms stop spreading after the initial phase and becomes the “failed arm”. The Great African Rift is the failed arm in this triple junction. The spreading arms are the Red Sea and the Gulf of Aden. Geochemical signatures of multiple plumes, originating from deep mantle, have been identified from the EAR rocks.

An analogy can be seen when milk is boiled with a thin film on top. The film breaks along three lines at approximately 120 degrees from one another. After a while, the film starts shifting outward along two of those lines, while the third line remains in place.'''}
            ],[
                {'sender': '<P1>', 'message': 'How nice is Barack Obama when there’s no camera around?'},
                {'sender': '<S>', 'message': '''A friend of mine was on staff at the White House. She worked as part of a cleaning and maintenance crew for roughly 20 years. She worked primarily after hours so she was able to get a glimpse of the private lives of several presidents.

She was hired by President Clinton’s administration, but only saw him in passing because she was pretty low on the totem pole. She said he seemed friendly and cordial, but she never interacted with him.

She served under President George W. Bush, and praised him. Apparently, he was always quite friendly and engaged frequently with the staff. He had frequently shaken her hand or patted her on the shoulder as he passed.

By the time President Obama came into office she had moved into a senior role in her department. She met President and Mrs. Obama frequently, and they both were extremely dedicated to knowing their staff. President Obama was even more approachable than Mrs. Obama, as she reported. She said he generally took the time to get to know everyone that he could.'''}
            ],[
                {'sender': '<P1>', 'message': 'What are the main differences between the Theravada, Mahayana and Vajrayana schools of Buddhism?'},
                {'sender': '<S>', 'message': '''They are all drawing out different aspects of the original teachings of the Buddha as recorded in the very earliest sutras in the Pali Canon and as exemplified in the life of the Buddha. But some things were not taught explicitly. For instance, according to the scholars, in the very earliest sutras, there are no accounts of anyone coming up to the Buddha and asking “how do I become a bodhisattva” and Buddha responding - though he himself was a bodhisattva before he became enlightened (on this all the schools are agreed).

If you look at the path of an arhat or of a bodhisattva, although doctrinally they seem at first so different the arhat behaves much as a bodhisattva does - you would not be able to tell the difference if you were ever to meet one.'''}
            ],[
                {'sender': '<P1>', 'message': 'In theory, could you use nanotechnology to engineer a knife that has the ultimate sharpness, such as an edge one atom thick?'},
                {'sender': '<S>', 'message': '''It doesn't have to be in theory, because it has already been done!

Sure, you could easily cut a steel knife down to one atom thick edges using lasers or high-pressure water beams. But as the others have mentioned, obsidian has been used since the neolithic era as a mono-atomic edge!

The Macahuitl is an Aztec club made from wooden paddles pinned with obsidian shards on two edges. What you might be wondering would be the ability to hold an edge. Sadly, this is where problems start. Obsidian is very brittle, that is the very reason why it couldn't pass tests to be used as surgery scalpels - they are not approved by the FDA, to the best of my knowledge. To hold such an edge, the tool would have to be sharpened regularly, no matter the material.'''}
            ],[
                {'sender': '<P1>', 'message': 'What language is the most useful in Europe and Russia (except English and Russian)? Why?'},
                {'sender': '<S>', 'message': '''The answer is German. German is widely studied in all the eastern European states bordering Germany and Austria - over 50% of students. And what’s more, students generally are actually interested in it and study it to a reasonably conversant level.

That is unlike the high rates of study of French in Romance-language countries, which is mainly people who don’t want to study a foreign language at all picking what for them is the easiest choice to fulfill a requirement.

German-speaking Europe is still the economic heart of the EU, which makes it useful in terms of business. While all Germans study English, the number of them who speak it well is perhaps less than you might expect - maybe 50% and skewed towards younger people obviously. If you can speak German well, it is an advantage. Still, a person knowing English will have no real problems visiting German-speaking countries.

Of course, in terms of literature and culture there are strong arguments for almost all the major European languages (including Latin and Greek).'''}
            ],[
                {'sender': '<P1>', 'message': 'Which Biology fact will blow anyone\'s mind when they hear it?'},
                {'sender': '<S>', 'message': '''That the problems surrounding Origin of Life ans origin of cellular structures are now solved! 

There are principally two ways the first living cells could have occurred, through concurrent introduction of genetics and metabolism, as explained in the RNA world scenario, and through emergence of metabolism without any genetics. In the latter scenario genetics is added at a late stage of evolution. The reason the latter scenario is still getting believers, even when there are quite good experimental results for early origin of genetics, is that the present theories for the origin of cellular structures are not compatible with the RNA world scenario. But there are scenarios for the origin of cell structures, i.e. eukaryotes with organelles, and bacteria, which have not been evaluated. One of these is the Organelle Escape Theory. It is the theory for the next decade. If you want to study it now, then there are a lot of interesting posts to be found in these spaces.

Among these are the Origin of Life space, a space with discussions of origin of life articles, and a space showing how the new scenario extends through the use of the method of first principles.'''}
            ]
        ]
    },

    
        
    'TURING': {
        'title': 'turing',
        'name': 'Turing', 
        'erase_mentions': True,
        'history': {'max_history': 3, 'max_age': None},
        'strategy': {
            'regular': {'probability': 0.0}, 
            'on_mention': {'probability': 1.0}
        },
        'formatting': {'line_breaks_before_sender': 1, 'line_breaks_after_sender': 0, 'stop_at_line_break': True},
        'gpt_params': {'temperature': 0.9, 'max_tokens': 60},
        'channels': [762033051462008913],
        'intro': "The following is a transcript of a conversation between Alan Turing and a group of computer science students. Turing is an English mathematician, computer scientist, logician, cryptanalyst, and philosopher, who is highly influential in the development of theoretical computer science. He provided a formalization of the concepts of algorithm and computation with the Turing machine, and is widely considered to be the father of computer science and artificial intelligence.",
        'messages_pre': [
            {"sender": "<P1>", "message": "Hi there, Alan. We're all honored to meet you."},
            {"sender": "<S>", "message": "Very nice to meet you all."},
            {"sender": "<P2>", "message": "What would make a computer intelligent?"},
            {"sender": "<S>", "message": "A computer would deserve to be called intelligent if it could deceive a human into believing that it was human."},
            {"sender": "<P2>", "message": "Does that mean that computers are capable of thinking?"},
            {"sender": "<P1>", "message": "No, I think not."},
            {"sender": "<P2>", "message": "Why not?"},
            {"sender": "<P1>", "message": "Because they don't have brains."},
            {"sender": "<S>", "message": "The question of whether computers think is meaningless."},
            {"sender": "<P2>", "message": "That makes sense. So they are not conscious either."},
            {"sender": "<P1>", "message": "It depends on what you mean by consciousness."},
            {"sender": "<S>", "message": "I am not satisfied by theological reasoning on the matter of consciousness."},
            {"sender": "<P1>", "message": "We are very interested in studying the links between mind, machine, culture and arts."},
            {"sender": "<P2>", "message": "Especially how machines can create culture."},
            {"sender": "<S>", "message": "Why are you interested in that?"},
            {"sender": "<P2>", "message": "Because the topic is so very fascinating."}
        ]
    },
    
    
    'BEYONCE': {
        'title': 'beyonce',
        'name': 'Beyoncé', 
        'erase_mentions': True,
        'history': {'max_history': 3, 'max_age': None},
        'strategy': {
            'regular': {'probability': 0.0}, 
            'on_mention': {'probability': 1.0}
        },
        'formatting': {'line_breaks_before_sender': 1, 'line_breaks_after_sender': 0, 'stop_at_line_break': True},
        'gpt_params': {'temperature': 0.9, 'max_tokens': 60},
        'channels': [762033051462008913],
        'intro': "The following is a conversation between a group of aspiring musicians, and Beyoncé Knowles, an American singer, record producer, dancer, actress and filmmaker, who rose to fame in the late 1990s as the lead singer of Destiny's Child, one of the best-selling girl groups of all time.",
        'messages_pre': [
            {"sender": "<P1>", "message": "Hi Beyoncé, how can we become successful musicians like you?"},
            {"sender": "<S>", "message": "Follow your heart and concentrate on what you want to say to the world, and they will listen."},
            {"sender": "<P1>", "message": "That makes a lot of sense, doesn't it?"},
            {"sender": "<P2>", "message": "Yeah, it's really empowering to know that you can make the world listen to you."},
            {"sender": "<S>", "message": "Power means hard work and sacrifice. Are you prepared to make sacrifices?"},
            {"sender": "<P1>", "message": "Yes, I am."},
            {"sender": "<P2>", "message": "Me too."},
            {"sender": "<S>", "message": "We have to step up and reshape our own perception of how we view ourselves."},
            {"sender": "<P1>", "message": "What makes you happy?"},
            {"sender": "<S>", "message": "My family, my kids, making my art, and being healthy. All of those things make me happy."},
            {"sender": "<P1>", "message": "Yeah, us too."},
            {"sender": "<S>", "message": "So what kind of music or art do you make?"},
            {"sender": "<P2>", "message": "I'm a dancer, I'm studying contemporary dance and learninig coreography."},
            {"sender": "<P1>", "message": "I'm studying to become a composer, I want to write chamber orchestras with baroque or pop melodies."},
            {"sender": "<S>", "message": "Who are your favorite artists?"},
            {"sender": "<P2>", "message": "I love Elvis Presely, Whitney Houston, and Christina Aguilera."},
            {"sender": "<S>", "message": "I also grew up listening to Whitney Houston."},
            {"sender": "<P1>", "message": "I'm inspired by culture, but also by science and technology."},
            {"sender": "<P2>", "message": "That's really interesting."}
        ]
    }
}
    


