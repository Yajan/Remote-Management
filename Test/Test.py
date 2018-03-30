from prompt_toolkit import prompt
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token
from prompt_toolkit.shortcuts import print_tokens
example_style = style_from_dict({
    Token.RPrompt: 'bg:#ff0066 #ffffff',
    Token.Toolbar: '#ffffff bg:#333333',
})

tokens = [
    (Token.RPrompt, 'How about writing something long'),
    (Token.Toolbar, '  Working'),
]
def getValues():
    return "Something for Testing purpose"

def get_rprompt_tokens(cli):
    return [
        (Token.RPrompt, u'How about writing something long'),
    ]

def get_bottom_toolbar_tokens(cli):
    msg = getValues()
    return [(Token.Toolbar, msg.encode("UTF_8"))]
print_tokens(tokens,style=example_style)

"""answer = prompt( get_rprompt_tokens=get_rprompt_tokens,get_bottom_toolbar_tokens=get_bottom_toolbar_tokens,
                style=example_style)"""