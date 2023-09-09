from .libs.tool import Kit
from .libs.systemCommands import plug

def main():
    Kit.build().getCursor().run()

main()