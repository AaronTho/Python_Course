# Heredoc

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Blandit volutpat maecenas volutpat blandit aliquam etiam erat. Sagittis orci a scelerisque purus semper eget duis at tellus. Semper feugiat nibh sed pulvinar proin gravida hendrerit. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce. 

Orci dapibus ultrices in iaculis nunc sed augue lacus viverra. Maecenas ultricies mi eget mauris pharetra et ultrices neque ornare. Mattis pellentesque id nibh tortor id aliquet lectus proin nibh. Tellus elementum sagittis vitae et leo duis ut diam. Felis eget velit aliquet sagittis id consectetur purus ut. Sollicitudin aliquam ultrices sagittis orci. Mattis nunc sed blandit libero volutpat sed cras ornare arcu. Integer quis auctor elit sed.
"""

# repr displays the text as the language interprets it.
# \n represetns a new line.
print(repr(content))

long_string = '\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Blandit volutpat maecenas volutpat blandit aliquam etiam erat. Sagittis orci a scelerisque purus semper eget duis at tellus. Semper feugiat nibh sed pulvinar proin gravida hendrerit. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce. \n\nOrci dapibus ultrices in iaculis nunc sed augue lacus viverra. Maecenas ultricies mi eget mauris pharetra et ultrices neque ornare. Mattis pellentesque id nibh tortor id aliquet lectus proin nibh. Tellus elementum sagittis vitae et leo duis ut diam. Felis eget velit aliquet sagittis id consectetur purus ut. Sollicitudin aliquam ultrices sagittis orci. Mattis nunc sed blandit libero volutpat sed cras ornare arcu. Integer quis auctor elit sed.\n'

# Youn can write strings in the syntax repr displays and it will render correctly.

print(long_string)
