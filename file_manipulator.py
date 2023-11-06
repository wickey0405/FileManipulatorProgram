from commandReverse import CommandReverse
from commandCopy import CommandCopy
from commandDuplicate import CommandDuplicate
from commandReplace import CommandReplace
from display import Display
import sys

reverse = CommandReverse('reverse')
copy = CommandCopy('copy')
duplicate_contents = CommandDuplicate('duplicate-contents')
replace_string = CommandReplace('replace-string')

display = Display()
display.addCommand(reverse)
display.addCommand(copy)
display.addCommand(duplicate_contents)
display.addCommand(replace_string)

args = sys.argv
display.parseInput(args)