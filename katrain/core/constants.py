HOMEPAGE = "https://github.com/sanderland/katrain"

PLAYER_HUMAN, PLAYER_AI = "player:human", "player:ai"
PLAYER_TYPES = [PLAYER_HUMAN, PLAYER_AI]

PLAYING_NORMAL, PLAYING_TEACHING = "game:normal", "game:teach"
GAME_TYPES = [PLAYING_NORMAL, PLAYING_TEACHING]

MODE_PLAY, MODE_ANALYZE = "play", "analyze"

AI_DEFAULT = "ai:default"
AI_SCORELOSS = "ai:scoreloss"
AI_WEIGHTED = "ai:p:weighted"
AI_JIGO = "ai:jigo"
AI_POLICY = "ai:policy"
AI_PICK = "ai:p:pick"
AI_LOCAL = "ai:p:local"
AI_TENUKI = "ai:p:tenuki"
AI_INFLUENCE = "ai:p:influence"
AI_TERRITORY = "ai:p:territory"

AI_CONFIG_DEFAULT = AI_SCORELOSS

AI_STRATEGIES_ENGINE = [AI_DEFAULT, AI_SCORELOSS, AI_JIGO]
AI_STRATEGIES_PICK = [AI_PICK, AI_LOCAL, AI_TENUKI, AI_INFLUENCE, AI_TERRITORY]
AI_STRATEGIES_POLICY = [AI_WEIGHTED, AI_POLICY] + AI_STRATEGIES_PICK
AI_STRATEGIES = AI_STRATEGIES_ENGINE + AI_STRATEGIES_POLICY
AI_STRATEGIES_RECOMMENDED_ORDER = [AI_DEFAULT, AI_SCORELOSS, AI_POLICY, AI_WEIGHTED, AI_PICK, AI_LOCAL, AI_TENUKI, AI_TERRITORY, AI_INFLUENCE, AI_JIGO]


AI_STRENGTH = {
    AI_DEFAULT: "9d",
    AI_POLICY: "4d",
    AI_JIGO: "?d",
    AI_SCORELOSS: "5k",
    AI_WEIGHTED: "5k",
    AI_PICK: "8k",
    AI_LOCAL: "5k",
    AI_TENUKI: "8k",
    AI_INFLUENCE: "8k",
    AI_TERRITORY: "5k",
}


OUTPUT_ERROR = -1
OUTPUT_KATAGO_STDERR = -0.5
OUTPUT_INFO = 0
OUTPUT_DEBUG = 1
OUTPUT_EXTRA_DEBUG = 2
