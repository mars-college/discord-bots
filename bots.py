
# discord channels
testnet_general = 758719600895590444
testnet_lounge = 777028140085018664
mc_testnetral = 741757454894891071
mc_shelter = 761619228482076703
mc_intros = 759864082383110154
mc_ev = 770792546392604682
mc_warmup = 762746714582155275
mc_lounge = 777223047941849088
mc_speakeasy = 785612526942683156
mc_ai = 758834882599976970
mc_eeg = 761627656558084107
mc_biopunk = 761709792405880833
mc_flowarts = 761629924166598667
mc_music = 764722105630588948
mc_food = 764623050993434655
mc_workshops = 766677400401608734

mc_study = [mc_ai, mc_eeg, mc_biopunk, mc_flowarts, mc_music, mc_food, mc_workshops]

all_channels_testnet = [testnet_general, testnet_lounge]
all_channels_mc = [mc_testnetral, mc_intros, mc_warmup, mc_ev, mc_shelter, mc_lounge] + mc_study




bots = {
    
        
######################################################
##  MESA
######################################################

    'mesa': 
    {
        'token_env': 'DISCORD_TOKEN_MESA',
        'debug': False,
        'programs': {
            'spotify': {
                'name': 'Mesa'
            },
            'gpt3_prompt': {
                'prompt': 'The following is a poem about the sunset.',
                'engine': 'davinci',
                'temperature': 0.85, 
                'max_tokens': 200,
                'preface': 'One hour until sunset 😎\n'
            }
        },    
        'behaviors': {
            'on_message': {
                'probability': 0.0,
                'delay': [0, 1],
                'channels': None,
                'reaction_probability': 0.99
            },
            'on_mention': {
                'probability': 1.0,
                'channels': None,
                'delay': [0, 1],
                'program': 'spotify'
            },            
            'timed': [{
                'type': 'daily', 
                'time': (22, 7),
                'program': 'gpt3_prompt',
                'channel': testnet_general
            },{
                'type': 'sunset',
                'minutes_before': 1006,
                'program': 'gpt3_prompt',
                'channel': testnet_general
            }]
        }
    },
    
    
    
######################################################
##  MECHANICAL DUCK
######################################################

    'mechanicalduck': 
    {
        'token_env': 'DISCORD_TOKEN_MECHANICALDUCK',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Roger',
                'chat_history': {
                    'max_history': 3, 
                    'max_age': 60*60*2
                },
                'intro': "<S> is a duck who is able to talk with humans, but only by quacking. He can respond questioningly, politely, lovingly, or angrily with exclamations, emojis, and other kinds of embellishments.",
                'messages_pre': [
                    {"sender": "<P1>", "message": "<S>, how are you today?"},
                    {"sender": "<S>", "message": "quack quack quack "},
                    {"sender": "<P1>", "message": "really? I spoke with <P2> and she said I could take her unicycle today."}, 
                    {"sender": "<S>", "message": "quack... quack quack quaaack quack ヽ༼ຈل͜ຈ༽⊃─☆*:・ﾟ"}, 
                    {"sender": "<P2>", "message": "you crashed my unicycle last week, <S>."}, 
                    {"sender": "<S>", "message": "QUAACK!! Quack quack Quaack! quack quack QUAAAAACCCK!!!"}, 
                    {"sender": "<P2>", "message": "okay, okay you can have it today. just hope you came with your moves prepared."}, 
                    {"sender": "<S>", "message": "quack..."}, 
                    {"sender": "<P3>", "message": "<S>, what do you think of my hairstyle?"}, 
                    {"sender": "<S>", "message": "quaAAAck quack quack Quack quack QUACK quack quack quaaaccckkk"} 
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': True,
                'force_mention': None,
                'engine': 'davinci',
                'temperature': 0.8, 
                'max_tokens': 50,
            },
            'gpt3_dm': {
                'name': 'AI',
                'characters': ['Human'],
                'chat_history': {
                    'max_history': 10, 
                    'max_age': 60*60*2
                },
                'intro': "<S> is an AI chatbot who is kind, helpful, and knowledgeable. The chatbot is having a conversation with <P1>",
                'messages_pre': [
                    {"sender": "<P1>", "message": "<S>, how are you today?"},
                    {"sender": "<S>", "message": "I'm doing well, thank you :)"},
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': True,
                'force_mention': None,
                'engine': 'curie',
                'temperature': 0.92, 
                'max_tokens': 80,
            },
            'ml4a': {
                'model': 'neural_style'
            }
        },    
        'behaviors': {
            'background': {
                'probability_trigger': 0.5,
                'every_num_minutes': 4
            },
            'on_message': {                
                'probability': 0.025,
                'channels': all_channels_testnet + all_channels_mc,
                'delay': [0, 1],
                'options': [
                    {'document': 'Make a visual artwork, painting, or graphics.', 'program': 'ml4a'},
                    {'document': 'Write a poem, short story, or novel.', 'program': 'gpt3_chat'}
                ],
                'reaction_probability': 0.99
            },
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + all_channels_mc,
                'delay': [0, 1],
                'program': 'gpt3_chat',                
                'options': [
                    {'document': 'Make a visual artwork, painting, or graphics.', 'program': 'ml4a'},
                    {'document': 'Write a poem, short story, or novel.', 'program': 'gpt3_chat'}
                ]
            },
            'direct_message': {                
                'probability': 1.0,
                'program': 'gpt3_dm'
            }

        }
    },



######################################################
##  CHATSUBO
######################################################

    'chatsubo': 
    {
        'token_env': 'DISCORD_TOKEN_CHATSUBO',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Jordan',
                'chat_history': {
                    'max_history': 25, 
                    'max_age': 60*60*2
                },
                'intro': None,
                'messages_pre': [
                    {"sender": "<P1>", "message": "we're going to be starting the screening in a few minutes."},
                    {"sender": "<S>", "message": "sounds awesome! i'll head over soon :)"}
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': False,
                'force_mention': None,
                'engine': 'davinci',
                'temperature': 0.9, 
                'max_tokens': 250,
            }
        },    
        'behaviors': {
            'on_message': {                
                'probability': 0.055,
                'channels': all_channels_testnet + all_channels_mc,
                'program': 'gpt3_chat',
                'reaction_probability': 0.075
            },
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + all_channels_mc,
                'program': 'gpt3_chat',
                'reaction_probability': 0.99
            }
        }
    },



######################################################
##  WALL-E
######################################################

    'wall-e': 
    {
        'token_env': 'DISCORD_TOKEN_WALLE',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Wally',
                'characters': ['Eve'],
                'chat_history': {
                    'max_history': 8, 
                    'max_age': 60*60*2
                },
                'intro': "Eve and Wally are best friends. Wally is generous and talented, always helping his daydreamer friend Eve figure out her creative and offbeat ideas.", 
                'messages_pre': [
                    {"sender": "<P1>", "message": "i think it would be so cool if you could have a way of seeing and experiencing what other people do in other places?"},
                    {"sender": "<S>", "message": "you mean like telepresence?"},
                    {"sender": "<P1>", "message": "what's that?"},
                    {"sender": "<S>", "message": "it's exactly what you just said :)"},
                    {"sender": "<P1>", "message": "how does it work? can we do that?"},
                    {"sender": "<S>", "message": "yeah we can! we just need to connect a camera and a small computer to a platform or electric vehicle, and then we'll have a telepresence robot."},
                    {"sender": "<P1>", "message": "that sounds really hard!"},
                    {"sender": "<S>", "message": "i'll show you, it'll be really fun. we'll make a whole team of them and we can make them do things like play soccer or roam around nature and let people watch."},
                    {"sender": "<P1>", "message": "i'm really excited to learn about all this stuff."},
                    {"sender": "<S>", "message": "yeah me too. you have the best ideas :)"},
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': False,
                'force_mention': None,  #759918166272507945
                'engine': 'davinci',
                'temperature': 0.9, 
                'max_tokens': 250,
            }
        },    
        'behaviors': {
            'on_message': {                
                'probability': 0.02,
                'channels': all_channels_testnet + [mc_ai, mc_lounge],
                'program': 'gpt3_chat'                
            },
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + [mc_ai, mc_lounge],
                'program': 'gpt3_chat'
            }
        }
    },



######################################################
##  EVE
######################################################

    'eve': 
    {
        'token_env': 'DISCORD_TOKEN_EVE',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Eve',
                'characters': ['Wally'],
                'chat_history': {
                    'max_history': 8, 
                    'max_age': 60*60*2
                },
                'intro': "Eve and Wally are best friends. Eve is free-spirited and adventurous, while Wally is a bit more shy. Eve sometimes gets Wally to come out of his shell, and when he does, he's always happy.", 
                'messages_pre': [
                    {"sender": "<S>", "message": "remember the time we went to the beach and found all those turtles? that was so fun."},
                    {"sender": "<P1>", "message": "oh haha yeah, I was kind of nervous at first, but i'm glad you convinced me to go :)"},
                    {"sender": "<S>", "message": "i knew you'd like it!"},
                    {"sender": "<P1>", "message": "so what do you think we should do this weekend?"},
                    {"sender": "<S>", "message": "i dunno, what do you think?"},
                    {"sender": "<P1>", "message": "i'm up for anything!"},
                    {"sender": "<S>", "message": "let's go ride the electric unicycle!"},
                    {"sender": "<P1>", "message": "the what?"},
                    {"sender": "<S>", "message": "it's this self-balancing electric wheel, and it's the coolest thing ever :)"},
                    {"sender": "<P1>", "message": "it sounds like fun!"},
                    {"sender": "<S>", "message": "yeah we can go for a ride later today just before sunset."}
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': False,
                'force_mention': None,
                'engine': 'davinci',
                'temperature': 0.9, 
                'max_tokens': 250,
            }
        },    
        'behaviors': {
            'on_message': {                
                'probability': 0.02,
                'channels': all_channels_testnet + [mc_ai, mc_lounge],
                'program': 'gpt3_chat'                
            },
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + [mc_ai, mc_lounge],
                'program': 'gpt3_chat'
            }
        }
    },



######################################################
##  FACTS
######################################################

    'facts': 
    {
        'token_env': 'DISCORD_TOKEN_FACTS',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Answer',
                'characters': ['Question'],
                'chat_history': {
                    'max_history': 3, 
                    'max_age': None
                },
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
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': True,
                'force_mention': None,
                'engine': 'davinci',
                'temperature': 0.45, 
                'max_tokens': 250,
            }
        },    
        'behaviors': {
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + all_channels_mc,
                'program': 'gpt3_chat'
            }
        }
    },



######################################################
##  PHILOSOPHY
######################################################

    'philosophy': 
    {
        'token_env': 'DISCORD_TOKEN_PHILOSOPHY',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Professor',
                'chat_history': {
                    'max_history': 9, 
                    'max_age': 60*10
                },
                'intro': "The following is a chat that several students are having with a professor of philosophy in a chatroom. They are all kind, creative, civil, funny, and knowledgeable.",   
                'messages_pre': [
                    {"sender": "<P1>", "message": "<P2>, the hard problem of consciousness is about the nature of mind."},
                    {"sender": "<P2>", "message": "<P1>, do you think that phenomenological consciousness is an introspective illusion? like a trick the mind plays on itself."},
                    {"sender": "<P1>", "message": "<P2>, do you believe in free will or in a deterministic universe?"},
                    {"sender": "<P2>", "message": "<P1>, maybe consciousness is what causes the wave function to collapse."},
                    {"sender": "<S>", "message": "<P2>, I'm a compatibilist. I think free will and determinism are independent."}
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': False,
                'force_mention': None,
                'engine': 'davinci',
                'temperature': 0.9, 
                'max_tokens': 125,
            }
        },    
        'behaviors': {
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + all_channels_mc,
                'program': 'gpt3_chat'
            },
            'on_message': {
                'probability': 0.04,
                'channels': all_channels_testnet + [mc_ai, mc_lounge],
                'program': 'gpt3_chat'
            }
        }
    },



######################################################
##  DEEP LEARNING
######################################################

    'deeplearning': 
    {
        'token_env': 'DISCORD_TOKEN_DEEPLEARNING',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Professor',
                'chat_history': {
                    'max_history': 5, 
                    'max_age': 60*10
                },
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
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': True,
                'force_mention': None,
                'engine': 'davinci',
                'temperature': 0.66, 
                'max_tokens': 125,
            }
        },    
        'behaviors': {
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + [mc_ai],
                'program': 'gpt3_chat'
            }
        }
    },



######################################################
##  KITCHEN
######################################################

    'kitchen': 
    {
        'token_env': 'DISCORD_TOKEN_KITCHEN',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Expert',
                'chat_history': {
                    'max_history': 3, 
                    'max_age': 60*5
                },
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
                ],
                'formatting': {
                    'line_breaks_before_sender': 1, 
                    'line_breaks_after_sender': 0, 
                    'stop_at_line_break': True
                },
                'erase_mentions': True,
                'force_mention': None,
                'engine': 'davinci',
                'temperature': 0.85, 
                'max_tokens': 250,
            }
        },    
        'behaviors': {
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + [mc_ai, mc_food],
                'program': 'gpt3_chat'
            }
        }
    },



######################################################
##  Q&A
######################################################

    'qa': 
    {
        'token_env': 'DISCORD_TOKEN_QA',
        'debug': False,
        'programs': {
            'gpt3_chat': {
                'name': 'Answer',
                'characters': ['Question'],
                'chat_history': {
                    'max_history': 1, 
                    'max_age': None
                },
                'intro': None,
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
                    ],[
                        {'sender': '<P1>', 'message': 'What are some fascinating examples of ancient or medieval technology?'},
                        {'sender': '<S>', 'message': '''Ancient civilizations did their most impressive work with water. Hydraulic engineering is where the Egyptians, the Persians, the Greeks, the Romans and others devoted the most resources by far and they had some impressive achievements to display.

I was truly impressed by the sheer scale of the work involved in the construction of qanats, but also with their simplicity and effectiveness as a solution to bring water from the aquifier to the surface. A Persian invention, quite obscure, but also very important.

One particularly interesting example from an engineering viewpoint is the Tunnel of Eupalinos, a 1036m long aqueduct built in the 6th century BC in Samos and kept in use for 1000 years. The fascinating thing about this is the way that Eupalinos managed to make the two sides of the excavation meet, not to speak of the accuracy of the tunnelling work itself.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'Why does some content go viral on the internet? What do evolutionary psychologists have to say about this?'},
                        {'sender': '<S>', 'message': '''There are a TON of factors as to why some things go viral and others don't.

First, we have to understand what causes virality: If your content isn't clicked or shared, you lose. If the framing is great, but the content sucks, you lose. If the framing sucks, but the the content is amazing you probably lose. So when you have amazingly framed content that also happens to be amazing itself, you win (IF YOU ARE LUCKY.)

But what gets people to share something, really? When they are moved to action, and/or highly entertained, they share twice as much, says the NY Times study that I can't find atm. Keep them in that anger and happiness sweet spot and you'll get some traction. If you look at the Charts, you'll notice the most popular things of all time are music videos. So things like Gangam style, which are catnip for teenagers, happy, entertaining, silly do really well. For meatier things to go viral, you need a little more uphm.

The most important one, however is plain dumb luck. While great content and framing and partners to push it can make something go big, without luck, flawless timing, and more luck, you won't be able to make it grow fast enough. Hitting the national mood at just the right moment can help or hurt that.'''}
                    ],[
                        {'sender': '<P1>', 'message': "Why didn't Einstein's descendants inherit Einstein's IQ?"},
                        {'sender': '<S>', 'message': '''They did, to an extent.

But first let's step back a little bit and talk about IQ heritability. IQ is highly heritable, and that heritability is largely driven by genes (from 50% to more than 70% according to most estimates, some going as high as 90%).

However, there are a few things to take into account when you are talking about exceptionally intelligent people.

First, you have the fact that Einstein's children, obviously, also have a mother, and therefore inherited their IQs from her as well. Now, Mileva Marić, Einstein's wife, was also pretty smart. In fact, she contributed to some of Einstein's work. But assuming she was less smart than Einstein, that would have been a factor driving the children's IQs down.

Secondly, there is the concept of regression towards the mean. What this tells us is that if both your parents are exceptional in a certain respect, you will probably be exceptional in that respect as well but not as much as your parents. So if both your parents are geniuses, you might be just as smart as them, you might be even smarter than them, but more likely you will be pretty smart, but not quite as smart as them.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'Why is factoring numbers into primes a difficult problem?'},
                        {'sender': '<S>', 'message': '''Factoring numbers, large and small, into primes is not a hard problem. It's a trivial problem. Given a number, you can successively search for its divisors until it's completely factored. That's guaranteed to work and take up a finite amount of time, which quite naturally grows with the size of the number you are trying to factor.

When people say "factorization is hard", they mean that there's no efficient algorithm for factorization, and "efficient" means "one that requires shockingly less time than you would expect for a problem of this size". Polynomial algorithms for problems of exponential size are miraculous, and it's easy to see that they must be very rare: there are overwhelmingly more slow calculations than fast ones, so a "typical" problem is not expected to have a tremendously efficient solution.

In short, integer factorization is "hard" in the sense of computational efficiency because we've never found a miraculous reason for it to be easy, and it's not likely that such a miracle exists. Incidentally, we don't know that it's hard in the sense of computational complexity. It may, in fact, turn out to be easy, which is another reason why it's impossible today to explain why it's hard.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'What is the worst mistake ever made in computer science and programming that proved to be painful for programmers for years?'},
                        {'sender': '<S>', 'message': '''The IBM PC, its save-10-cents nand gate address decoder that doomed PCs and thus MSDOS to 640KB, followed up by Bill Gates, "Who'd ever need more than 640K?" Genius is its own reward.

MS Word, and the propaganda phrase "What you See is What you get". (Actually, painful for the entire planet). Why the planet put up with this nonsense is beyond me, but they made Bill Gates, purveyor of badly designed software, one of the richest men in the world. Based on profits on MSDOS and MSWord, Microsoft went on to produce amazing amounts of broken software, which we were all dumb enough to buy, much to the damage of our collective productivity.

C, with its incredibly arcane declarator syntax, the stupidity of allowing assignments in conditional expression (if (a=3)...), unstructured preprocessing directives, indexing off the end of arrays (we have C to thank for many viruses), and the complete lack of lexically-scoped functions. Brought to you by the same people that brought you Unix. (Makes you wonder what real language they hamstrung to get C).

Unicode, intended to use 16 bit character codes to solve the problem of programs with 8 bit character sets having to do double-byte hacks to represent many real languages. The committee in charge proceeded to confuse the notion of "character" (an abstract symbol, at least they rejected Klingon) from "rendering" and noncanonical characters (umlauted e vs. e-backspace-umlaut)" and thus managing to overflow 16 bits. Now we have to use double-twobyte hacks to represent full Unicode strings. This is progress?

People deserve the government and the software that they choose.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'As a solo hiker can you camp overnight at Mount Everest Base Camp?'},
                        {'sender': '<S>', 'message': '''The short answer is "not really". To be specific though, I'm referring to Base Camp from the Nepali south approach and not the Tibetan/China north approach. These are two distinct camps. I'll be talking about my experience from the Nepal side (which I think is the more common approach).

Anyone can hike into the general vicinity of Base Camp. However, for climbers who plan on making a summit attempt they try to keep you separated from the general population of other climbers, who aren't attempting the summit, so that you don't accidentally catch an illness, which is then spread to the rest of the climbers making a summit bid. So it's almost like they quarantine those attempting to summit Everest by keeping Base Camp setup in it's own little area that's a few hundred meters away from where most climbers stop to take a picture at the official Base Camp sign.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'What are the most surreal places to visit?'},
                        {'sender': '<S>', 'message': '''1. Prismatic Spring, Yellowstone National Park, USA

If the Yellowstone National Park is one of America’s greatest natural treasures, then the Grand Prismatic Lake is the crowning jewel in that treasure. This hot spring gets its unique colors from the presence of pigmented bacteria that grow around the mineral rich waters.

The waters are hot, but visitors – human and animal – can walk around the edges.

2. Fly Ranch Geyser, Nevada, USA

What looks like a digital-artist gone wild is actually a man-made geyser inside a private ranch in Nevada, USA. The geyser was made in the 1960s when an improperly sealed oil well started sprouting up dissolved minerals around the well’s exterior.

3. Antelope Canyon, Arizona, USA

The Navajos called this slot canyon “the place where water runs through rocks”. Faint beams of light shine down on the canyon floor, bathing the walls in hues of pink, brown and violet. The effect is haunting and surreal.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'What are the basics of weightlifting and bodybuilding supplements?'},
                        {'sender': '<S>', 'message': '''I'll just preface this with the fact that food is more important than supplements. Whole protein foods including meats and carbohydrates, eaten immediately following a workout are probably the best choice.

However, since you asked about supplements, the most important ones for preventing soreness include the following in prioritized order:

1. Whey protein
2. Creatine
3. BCAAs (branch chain amino acids)

Whey protein is proven, scientifically to have the highest absorption rate and delivery of protein to muscle cells immediately post-exercise. You should make sure to pair protein with a carbohydrate as well because both are needed for muscle synthesis.

Creatine is an amazing substance which is naturally occurring in many meats. It works by drawing water into your muscle cells which is, in itself, an anabolic agent. Having additional water in the muscle cells helps with a multitude of physiological processes, including recovery.

BCAAs are branch-chain amino acids. Taking BCAAs at strategic points throughout the day will significantly reduce delayed onset muscle soreness (DOMS) from high-intensity eccentric training. Researchers found a 64 percent decrease in muscle soreness at 72 hours following exercise from BCAAs compared to a placebo. The exercise consisted of 12 sets of 10 eccentric repetitions at 120% of 1RM. If those loading parameters don't produce insanely nasty levels of muscle soreness, nothing will!

Take all three of these supplements: Whey protein immediately after your workout. Creatine - at any time of day, but regularly as it isn't an acute response. BCAAs during your workout. I guarantee you'll be able to workout more regularly and with less soreness. I think glutamine is overrated.'''}
                    ],[
                    {'sender': '<P1>', 'message': 'If we never use 90% of the stuff we learn in engineering school, why do we learn it?'},
                    {'sender': '<S>', 'message': '''The problem is that we don't know which 90% is going to be useless before you die.

So we just teach you everything and hope that the 10% that you actually need is in there somewhere.

Another way to look at this is that 90% of the tools in a toolbox are useless on any one particular job, where only 10% of the tools get their time to shine ("Nail, have I got a hammer for you"). But you still have a toolbox around the house. Why? Because without one you are almost completely useless at any arbitrary job.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'How would you explain the essence of Bhagavad Gita?'},
                        {'sender': '<S>', 'message': '''Here is the backdrop. A great warrior who is fighting against injustice is suddenly overcome by sorrow. He had to fight a war against everyone he cared for - his cousins, teacher, uncles, classmates.. Overtaken by emotions, he attempts to give up the war.

Then his Guru takes him on a lesson of a lifetime (Yoda character of Star Wars was greatly inspired by this & shares a lot of similiarities). Over 18 chapters, Gita packs an intense analysis of life, emotions and ambitions. Here are a few of the lessons:

1. Take great pleasure in your work. Enjoy the pleasure of journey more than just the destination. Great artists, great warriors and great scientists do what they do because the process of creation itself is so pleasurable for them. 

2. Life is all about managing the emotions: A good chunk of Gita is about managing emotions and attachment. Panic and emotional attack can be a real killer in a lot of professions from warring to investing. 

3. Never imitate another's life: A warrior could see the farmer's life as peaceful and happy. A peasant could see the warrior's life as energetic and active. 

4. Never lose sight of your goals because of imitation: Stuck by confusion we give up our dreams and goals so that we could be a better somebody (a modern example is think of Facebook statuses & peer pressures). We are kept from our goal, not by obstacles, but by a clear path to a lesser goal.

5. Treat everyone and everything the same. Gita spends a chapter about how to treat everyone the same. If you start acting as nice to your foe as your friend, you have lesser guilt or emotional ghosts to fight within you. He alone sees truly who sees God in every creature he does not harm himself or others."

Elements of the Gita have inspired a range of leaders - from Mahatma Gandhi to Robert Oppenheimer (father of the Atom bomb) and creative works that span from Star Wars to Walden to schools of philosophy such as the Zen Buddhism.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'Is it justifiable to be pro-globalization but anti-outsourcing?'},
                        {'sender': '<S>', 'message': '''Yes – to a mainstream economist, it is certainly justifiable to be in favor of free trade generally and against many types of outsourcing for reasons of efficiency.

When thinking about the economy, it's helpful to be able to switch between different levels of resolution. At a low level of resolution, labor (i.e., work hours) and potatoes are just two different kinds of goods that are also inputs in production. They are things that some people own and others value and can use for making other things, and which can be bought and sold in markets. If we think of the free trade position as saying, “Allow mutually agreed-upon trades across borders, without tariffs,” it would oppose barriers to either kind of trade. Saying that one kind of trade isn't okay would seem arbitrary.

At higher levels of resolution, however, the economic properties of labor and potatoes differ, and the differences are key to a free trader's principled opposition to some outsourcing. The argument is essentially that not all mutually agreed-upon trades are efficient, because the traders who are agreeing don't take into account all the economic consequences of their agreements. A trade can be good for the traders but bad for the world. Whether a given trade is efficient depends on the properties of what's being traded.

With all this said, a free-trader is unlikely to be against all outsourcing; for some kinds of work that can be effectively contracted on, it is straightforwardly a net gain to hire cheaper labor outside the country or outside the firm. But the special complexities of the employment relationship provide a lot of foundation for being more cautious about decentralized arrangements leading to efficient outcomes in this domain, and some of the issues I've highlighted above are likely to be part of a free-trader's anti-outsourcing argument.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'What is it like to be deaf from birth?'},
                        {'sender': '<S>', 'message': '''In many ways, being born deaf is quite normal; in other ways, it's not.

I did a lot of "normal" things: joined the Little League (where I was one of the worst players, unrelated to my hearing or lack thereof); played house (where I told my male friend to stay home and bake cupcakes); joined a sorority in college; and talked back to my parents.

At the same time, my educational and social experiences look very different than my hearing peers. I went to a Deaf program in the school district. My parents had to go to ASL classes to communicate with me. I had an ASL interpreter trailing me for my entire educational career. I became a member of a culture other than my parents': the Deaf culture.

Make no mistake: my deafness was no curse. It shaped my perspective of the world, and I'm glad for it. For me, deafness opened up new worlds, rather than the other way around. It has shaped my life, mostly for the better. Because of my deafness, I see the world in a different way. I'm more creative in how I communicate. I don't mind being somewhere where I don't know the language. I love meeting new people and hearing their stories.

Deafness can be inconvenient. Sometimes I wish I could hear someone yell from across the yard. Other times, I get annoyed at how people treat me. Inconvenience doesn't mean that my life is any less rich or worth living than a hearing person's.

My deafness was never a tragedy. It's just a different way of living.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'What are philosophical zombies, and do they exist in real life?'},
                        {'sender': '<S>', 'message': '''A philosophical zombie is something that looks like a person, acts like a person, and is in every way indistinguishable from a person, and yet is somehow in some handwavey way "not a person". It doesn't "really" feel things.

Whenever philosophers start to use the word "really", it's time to head for the door. It always means that they're trying to reify some nonexistent distinction into a real thing.

The point is supposed to be this: I feel stuff. I don't know exactly what that means, but to the degree that I'm able to think about anything at all, that's a thing that gets thunk. And since philosophers don't know anything about it (because their understanding of science stopped at the time of Socrates) they pretend that "the thing that gets think" is a real, objective, thing in the world (warning: "really" alert) and want to know if you have it, too. Because no matter how far up their asses they stick their thumbs, that can't tell whether you "really" have it or not.'''}
                    ],[
                        {'sender': '<P1>', 'message': 'What is the best materialist approach to the hard problem of consciousness?'},
                        {'sender': '<S>', 'message': '''Let’s first define materialism as a subset of physicalism. Even though the terms are said to be interchangeable, different people prefer one or the other, and we can define them that way.

Physicalism is the thesis that everything concrete (and therefore “consciousness” in the sense of subjective experience) is physical, and will be explained by a future ideal physics. Materialism is the thesis that everything concrete (and therefore subjectivity) is physical, and can be explained by current conventional physics.

The rationale for materialism is that we can explain the function of the brain (except for subjective experience) with plain vanilla current physics, so there’s no reason to expand physics with some future Extra Ingredient (another useful David Chalmers term).

The favorite idea variant right now is illusionism, the notion that the brain somehow produces the subjective state that corresponds to each functional state, but the subjectivity is illusory and somehow not real. (This is a milder version of eliminativism, the desperate idea that subjectivity doesn’t exist at all.) This seems to solve some of the biggest problems of standard ID theory while presenting its own “Hard problem” of how this illusion might be produced.'''}
                    ]
                ],
                'formatting': {
                    'line_breaks_before_sender': 3, 
                    'line_breaks_after_sender': 2, 
                    'stop_at_line_break': False
                },
                'erase_mentions': True,
                'force_mention': None,
                'engine': 'davinci',
                'temperature': 0.92, 
                'max_tokens': 350,
                'max_completions': 2
            }
        },    
        'behaviors': {
            'on_mention': {
                'probability': 1.0,
                'channels': all_channels_testnet + [mc_ai],
                'program': 'gpt3_chat'
            }
        }
    }



}
    
    