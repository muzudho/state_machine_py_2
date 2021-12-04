transition_dict = {
    "[Receipt]": {
        "----Login---->": {
            "====Ok====>": "[Match]",
            "====Incorrect====>": "[Receipt]",
        }
    },

    "[Match]": {
        "----Logout---->": {
            "====Completed====>": "[Receipt]",
        },
        "====GameSummary====>": "[Tell]",
    },

    "[Tell]": {
        "----Agree---->": {
            "====Start====>": "[Judgement]",
        },
        "----Reject---->": {
            "====Reject====>": "[Match]",
        },
    },

    "[Judgement]": {
        "----Move---->": "[Judgement]",
        "====Move====>": "[Judgement]",
        "====GameOver====>": {
            "====Floodgate====>": "[Receipt]",
            "====Wcsc====>": "[Match]",
        },
    },
}
