"""
Configuration constants for the assembler.
"""
a_command_pattern = r'^@(\d+|[\w\.\$:]+)$'
l_command_pattern = r'^\(([\w\.\$:]+)\)$'
c_command_pattern = r'^(?:(\w+)=)?([\w\+\-\&\|\!]+)(?:;(\w+))?$'