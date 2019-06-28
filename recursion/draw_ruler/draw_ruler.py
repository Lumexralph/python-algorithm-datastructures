def draw_line(tick_length, tick_label=''):
  """Draw one line with the given tick length (followed by optional label)"""
  line = "-" * tick_length

  if tick_label:
    line += ' ' + tick_label
  print(line)


def draw_interval(center_length):
  """Draw tick interval upon a central tick length"""
  if center_length > 0:                     # stops when length drops to zero
    draw_interval(center_length - 1)        # recursively draw top ticks
    draw_line(center_length)                # draw center tick
    draw_interval(center_length - 1)        # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
  """Draw English ruler with given number of inches, major tick length"""
  draw_line(major_length, '0')              # draw inch line 0
  for j in range(1, 1  + num_inches):
    draw_interval(major_length - 1)         # draw the interior inch
    draw_line(major_length, str(j))         # draw inch line j and the label


print(draw_ruler(1, 2))