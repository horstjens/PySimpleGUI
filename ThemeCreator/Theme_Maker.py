import PySimpleGUI as sg
import color_themes

def rgb_to_hsl(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = ((high + low) / 2,)*3
    if high == low:
        h = s = 0.0
    else:
        d = high - low
        l = (high + low) / 2
        s = d / (2 - high - low) if l > 0.5 else d / (high + low)
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6
    return h, s, v

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple(int(hex[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


def sorted_tuple(tup, position):
    tup.sort(key=lambda x: x[position])
    return tup


sg.LOOK_AND_FEEL_TABLE = {}         # Entirely replace the look and feel table in PySimpleGUI
for key, colors in color_themes.themes.items():
    # Sort the colors from darkest to lightest

    color_lightness_pairs = []
    for color in colors:
        if type(color) in (tuple, list):
            continue
        r,g,b = hex_to_rgb(color)
        lightness = (rgb_to_hsl(r=r, g=g, b=b))[2]
        color_lightness_pairs.append((lightness, color))
    sorted_colors_tuples = sorted_tuple(color_lightness_pairs, 0)       # sort the pairs by the first item (lightness)
    scolors = [c for l, c in sorted_colors_tuples]          # Colors sorted from darkest to lightest
    # Create a "Dark" and a "Light" theme based on the sorted colors
    sg.LOOK_AND_FEEL_TABLE['Dark'+key] = {'BACKGROUND': scolors[0],
                                      'TEXT': scolors[3],
                                      'INPUT': scolors[2],
                                      'TEXT_INPUT': '#000000',
                                      'SCROLL': scolors[2],
                                      'BUTTON': ('#FFFFFF', scolors[1]),
                                      'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST':scolors,
                                      'DESCRIPTION':colors[4]}

    sg.LOOK_AND_FEEL_TABLE['Light'+key] = {'BACKGROUND': scolors[3],
                                      'TEXT': scolors[0],
                                      'INPUT': scolors[1],
                                      'TEXT_INPUT': '#FFFFFF',
                                      'SCROLL': scolors[0],
                                      'BUTTON': ('#FFFFFF', scolors[2]),
                                      'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': scolors,
                                      'DESCRIPTION':colors[4]}

    sg.LOOK_AND_FEEL_TABLE['Dark2'+key] = {'BACKGROUND': scolors[1],
                                      'TEXT': scolors[3],
                                      'INPUT': scolors[2],
                                      'TEXT_INPUT': '#000000',
                                      'SCROLL': scolors[2],
                                      'BUTTON': ('#FFFFFF', scolors[1]),
                                      'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST':scolors,
                                      'DESCRIPTION':colors[4]}


    sg.LOOK_AND_FEEL_TABLE['Light2'+key] = {'BACKGROUND': scolors[2],
                                      'TEXT': scolors[0],
                                      'INPUT': scolors[1],
                                      'TEXT_INPUT': '#FFFFFF',
                                      'SCROLL': scolors[0],
                                      'BUTTON': ('#FFFFFF', scolors[2]),
                                      'PROGRESS': sg.DEFAULT_PROGRESS_BAR_COLOR,
                                      'BORDER': 1,
                                      'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': scolors,
                                      'DESCRIPTION':colors[4]}


WINDOW_BACKGROUND = 'lightblue'

def sample_layout(theme_name, colors, description):
    name = 'Dark' if theme_name.startswith('D') else 'Light'
    name += "".join(description[:2])
    layout =  [[sg.Text('Text element', size=(12,1)), sg.InputText(' '.join(colors),text_color='#000000' ),sg.Radio('',theme+'1', key='-INPUT_RAD0-'+theme, default=True, metadata='#000000'),
                sg.Slider((0,10),size=(10,20), orientation='h')],
            [sg.T(size=(12,1)), sg.InputText(colors[0], text_color='#FFFFFF'),sg.Radio('',theme+'1', key='-INPUT_RAD1-'+theme, metadata='#FFFFFF')],
            [sg.T(size=(12,1)), sg.InputText(colors[0], text_color=colors[0]),sg.Radio('',theme+'1', key='-INPUT_RAD2-'+theme, metadata=colors[0])],
            [sg.T(size=(12,1)),sg.InputText(colors[3], text_color=colors[3]),sg.Radio('',theme+'1', key='-INPUT_RAD3-'+theme, metadata=colors[3])],
            [sg.T(', '.join(description)), sg.In(name, key='-NEW_THEME_NAME-'+theme)],
                [sg.Button('OK'), sg.Radio('',theme+'2',key='-BTN_RAD1-'+theme, default=True, metadata=sg.DEFAULT_BUTTON_COLOR),
                 sg.Button('OK', button_color=('white', colors[0])),sg.Radio('',theme+'2',key='-BTN_RAD2-'+theme, metadata=('white', colors[0])),
                 sg.Button('OK', button_color=('black', colors[0])),sg.Radio('',theme+'2',key='-BTN_RAD9-'+theme, metadata=('black', colors[0])),
                 sg.Button('OK', button_color=('white', colors[3])),sg.Radio('', theme+'2', key='-BTN_RAD10-' + theme, metadata=('white', colors[3])),
                 sg.Button('OK', button_color=('black', colors[3])),sg.Radio('', theme+'2', key='-BTN_RAD11-' + theme, metadata=('black', colors[3]))],
                [sg.Button('OK', button_color=(colors[0],colors[1])),sg.Radio('',theme+'2',key='-BTN_RAD3-'+theme, metadata=(colors[0], colors[1])),
                 sg.Button('OK', button_color=(colors[2],colors[1])),sg.Radio('',theme+'2',key='-BTN_RAD4-'+theme, metadata=(colors[2], colors[1])),
                 sg.Button('OK', button_color=(colors[3],colors[1])),sg.Radio('',theme+'2',key='-BTN_RAD5-'+theme, metadata=(colors[3], colors[1])),
                 sg.Button('OK', button_color=(colors[3],colors[0])),sg.Radio('',theme+'2',key='-BTN_RAD7-'+theme, metadata=(colors[3], colors[0])),
                 sg.Button('OK', button_color=(colors[0],colors[3])),sg.Radio('',theme+'2',key='-BTN_RAD8-'+theme, metadata=(colors[0], colors[3])),
                 sg.Button('Cancel', button_color=(colors[3], colors[2])),sg.Radio('',theme+'2',key='-BTN_RAD6-'+theme, metadata=(colors[3], colors[2])),
                 ] ]
    return layout
# layout =   [[sg.Text('Here is list of some themes', font='Default 18', background_color=WINDOW_BACKGROUND)]]
layout = []
row = []
layouts = []
for count, theme in enumerate(sg.ListOfLookAndFeelValues()):
    sg.change_look_and_feel(theme)
    if count and not(count % 4):
        layout += [row]
        row = []
    row += [sg.CB('',text_color='black', background_color=WINDOW_BACKGROUND, key='-CB-'+theme)]
    row += [sg.Frame(theme, sample_layout(theme, sg.LOOK_AND_FEEL_TABLE[theme]['COLOR_LIST'], sg.LOOK_AND_FEEL_TABLE[theme]['DESCRIPTION']))]
    if count and not (count % 20):
        if layout:
            layouts.append(layout)
        layout = []
if row:
    layout += [row]
if layout:
    layouts.append(layout)

for layout in layouts:
    window = sg.Window('PySimpleGUI Theme Maker', layout, background_color=WINDOW_BACKGROUND, default_element_size=(30,1))
    event, values = window.read()
    if event is not None and event.startswith('Cancel'):
        break
    for key, value in values.items():
        if type(key) is str and key.startswith('-CB-') and value:
            theme = key[4:]
            theme_entry = sg.LOOK_AND_FEEL_TABLE[theme]
            if values['-INPUT_RAD1-'+theme]:
                input_text_color = window['-INPUT_RAD1-'+theme].metadata
            elif values['-INPUT_RAD2-'+theme]:
                input_text_color = window['-INPUT_RAD2-'+theme].metadata
            elif values['-INPUT_RAD3-'+theme]:
                input_text_color = window['-INPUT_RAD3-'+theme].metadata
            elif values['-INPUT_RAD0-'+theme]:
                input_text_color = window['-INPUT_RAD0-'+theme].metadata
            else:
                print('** ERROR none of the radio buttons are true for input text **')
                continue

            if values['-BTN_RAD1-'+theme]:
                b_color = window['-BTN_RAD1-'+theme].metadata
            elif values['-BTN_RAD2-'+theme]:
                b_color = window['-BTN_RAD2-'+theme].metadata
            elif values['-BTN_RAD3-'+theme]:
                b_color = window['-BTN_RAD3-'+theme].metadata
            elif values['-BTN_RAD4-'+theme]:
                b_color = window['-BTN_RAD4-'+theme].metadata
            elif values['-BTN_RAD5-'+theme]:
                b_color = window['-BTN_RAD5-'+theme].metadata
            elif values['-BTN_RAD6-'+theme]:
                b_color = window['-BTN_RAD6-'+theme].metadata
            elif values['-BTN_RAD7-'+theme]:
                b_color = window['-BTN_RAD7-'+theme].metadata
            elif values['-BTN_RAD8-'+theme]:
                b_color = window['-BTN_RAD8-'+theme].metadata
            elif values['-BTN_RAD9-'+theme]:
                b_color = window['-BTN_RAD9-'+theme].metadata
            elif values['-BTN_RAD10-'+theme]:
                b_color = window['-BTN_RAD10-'+theme].metadata
            elif values['-BTN_RAD11-'+theme]:
                b_color = window['-BTN_RAD11-'+theme].metadata
            else:
                print('** ERROR none of the radio buttons are true for button color **')
                continue
            sg.LOOK_AND_FEEL_TABLE[theme]['TEXT_INPUT'] = input_text_color
            sg.LOOK_AND_FEEL_TABLE[theme]['BUTTON'] = b_color
            with open('new_theme_dict.py', 'a') as outfile:
                outfile.write(f"'{values['-NEW_THEME_NAME-'+theme]}' : {sg.LOOK_AND_FEEL_TABLE[theme]},\n")
            print(f"'{values['-NEW_THEME_NAME-'+theme]}' : {sg.LOOK_AND_FEEL_TABLE[theme]}")
    window.close()
    del window
