import random
from musthe import Chord, Note, Interval
import ui

# Chord notation: https://en.m.wikipedia.org/wiki/Chord_notation

# https://en.m.wikipedia.org/wiki/List_of_chords


# --------------------------------
#    CLASSES FOR chord types
# --------------------------------
#             TRIADS
# --------------------------------
class Major():

	sym_short = 'M'
	sym = 'maj'
	sym_default = ''
	symbols = ['', 'maj', 'M']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Minor():

	sym_short = 'm'
	sym = 'min'
	sym_default = 'm'
	symbols = ['-', 'min', 'm']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Augmented():

	sym_short = '+'
	sym = 'aug'
	sym_default = 'aug'
	symbols = ['aug', 'M#5', 'M+5']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Diminished():

	sym_short = '°'
	sym = 'dim'
	sym_default = 'dim'
	symbols = ['dim', 'mb5', 'm°5']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


# --------------------------------
#             7th
# --------------------------------
class Major7():

	triangle = chr(9651)

	sym_short = 'M7'
	sym = 'maj7'
	sym_default = ''
	symbols = ['maj7', 'M7', triangle]

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Minor7():

	sym_short = 'm7'
	sym = 'min7'
	sym_default = 'm7'
	symbols = ['min7', 'm7', '-7']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Dominant7():

	sym_short = '7'
	sym = 'dom7'
	sym_default = '7'
	symbols = ['dom7', '7']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Augmented7():

	sym_short = '+'
	sym = 'aug7'
	sym_default = 'aug7'
	symbols = ['7M#5', '7M+5']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


class Diminished7():

	sym_short = '°'
	sym = 'm7dim5'
	sym_default = '7dim'
	symbols = ['m7b5', 'm7°5']

	def __init__(self):
		pass

	def replace(self, chord):
		random_sym = random.choice(self.symbols)
		return chord.replace(self.sym, random_sym)

	def replace_default(self, chord):
		return chord.replace(self.sym, self.sym_default)


obj = {
	'M': Major(),
	'm': Minor(),
	'+': Augmented(),
	'°': Diminished(),
	'M7': Major7(),
	'm7': Minor7(),
	'7': Dominant7(),
	'7#5': Augmented7(),
	'm7b5': Diminished7(),
}

# --------------------------------
#       USEFUL FUNCS
# --------------------------------


def circle(accidentals):

	note = Note('C5')
	interval = Interval('P4')

	for i in range(8):
		yield note

		if accidentals == 'Circle4th':
			note = note + interval
		elif accidentals == 'Circle5th':
			note = note - interval


def get_notes(accidentals):

	if accidentals in ('b', '#', 'all'):
		return Note('C').all()
	else:
		return circle(accidentals)


# --------------------------------
#       USER INTERFACE
# --------------------------------

screen_width = ui.get_screen_size().width
screen_height = ui.get_screen_size().height

tv_height = 125
tv_width = screen_width / 3
tv_x_pos = tv_width
tv_y_pos = 0

# Table view: Accidentals
tv_alter = ui.TableView()
tv_alter.border_width = 0
tv_alter.x = 0 * tv_x_pos
tv_alter.y = tv_y_pos
tv_alter.width = tv_width
tv_alter.height = tv_height

# Table view: Chord type
tv_type = ui.TableView()
tv_type.border_width = 0
tv_type.x = 1 * tv_x_pos
tv_type.y = tv_y_pos
tv_type.width = tv_width
tv_type.height = tv_height
tv_type.allows_multiple_selection = True

# Table view: Chord output
tv_view = ui.TableView()
tv_view.border_width = 0
tv_view.x = 2 * tv_x_pos
tv_view.y = 0
tv_view.width = tv_width
tv_view.height = tv_height

# Button: Generate chord
bt_height = 40
bt_width = screen_width
bt_x_pos = 0
bt_y_pos = tv_height

bt_generator = ui.Button()
bt_generator.border_width = 4
bt_generator.title = 'Generate'
bt_generator.x = bt_x_pos
bt_generator.y = bt_y_pos
bt_generator.width = bt_width
bt_generator.height = bt_height
bt_generator.font = ('verdana', 25)
bt_generator.corner_radius = 10

# TextView: List of chords
txtv_height = screen_height - tv_height - bt_height
txtv_width = screen_width - tv_width - bt_width

txtv_x_pos = 0
txtv_y_pos = bt_y_pos + bt_height

txtv_info = ui.TextView()
txtv_info.alignment = ui.ALIGN_CENTER
txtv_info.border_width = 0
txtv_info.x = txtv_x_pos
txtv_info.y = txtv_y_pos
txtv_info.width = screen_width
txtv_info.height = txtv_height
txtv_info.editable = False
txtv_info.font = ('verdana-bold', 30)


# ----------------------------------
# Delegate and DataSource for
# Chord types
# ----------------------------------
class tvDelegateType():
	def __init__(self, title, items):
		self.items = items
		self.currentNumLines = len(items)
		self.currentTitle = title
		self.currentRow = None
		self.selected_items = []

	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		self.selected_items.append(self.items[row])

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		self.selected_items.remove(self.items[row])

	def tableview_number_of_sections(self, tableview):
		# Return the number of sections (defaults to 1). Someone else can mess with
		# sections and section logic
		return 1

	def tableview_number_of_rows(self, tableview, section):
		# Return the number of rows in the section
		return self.currentNumLines  # needed to be in sync with displayed version

	def tableview_title_for_header(self, tableview, section):
		# Return a title for the given section.
		# If this is not implemented, no section headers will be shown.
		return self.currentTitle

	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row

		cell = ui.TableViewCell()
		cell.text_label.text = self.items[row]['title']
		return cell


# ----------------------------------
# General Delegate and DataSource for
# Accidentals and Output
# ----------------------------------
class tvDelegateGen():
	# also acts as the data_source. Can be separate, but this is easier.
	def __init__(self, title, items):
		self.items = items
		self.currentNumLines = len(items)
		self.currentTitle = title
		self.currentRow = None
		self.selected_item = ''

	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected
		self.selected_item = self.items[row]['value']

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_number_of_sections(self, tableview):
		# Return the number of sections (defaults to 1). Someone else can mess with
		# sections and section logic
		return 1

	def tableview_number_of_rows(self, tableview, section):
		# Return the number of rows in the section
		return self.currentNumLines  # needed to be in sync with displayed version

	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row

		cell = ui.TableViewCell()
		cell.text_label.text = self.items[row]['title']
		cell.accessory_type = self.items[row]['accessory_type']
		return cell

	def tableview_title_for_header(self, tableview, section):
		# Return a title for the given section.
		return self.currentTitle


# ----------------------------------
#     CHORD GENERATOR WINDOW
# ----------------------------------
class ChordGenerator(ui.View):

	chord_types = ' '

	# ACCIDENTALS -----------------
	titles = {
		'Flats': 'b',
		'Sharps': '#',
		'All': 'all',
		'Circle 4th': 'Circle4th',
		'Circle 5th': 'Circle5th'
	}

	itemlist = [{
		'title': x,
		'value': y,
		'accessory_type': 'none'
	} for x, y in titles.items()]

	tv_alter.data_source = tv_alter.delegate = tvDelegateGen(
		title='Notes', items=itemlist)

	# CHORD TYPES -----------------
	titles = {
		f'{item}': f'{key}'
		for key, item in Chord(Note('C')).aliases.items()
	}

	itemlist = [{
		'title': x,
		'value': y,
		'accessory_type': 'none'
	} for x, y in titles.items()]

	tv_type.data_source = tv_type.delegate = tvDelegateType(
		title='Chord type', items=itemlist)

	# CHORD OUTPUT -----------------

	titles = {
		'Random': 'Random',
		'Default': 'Default',
		'Musthe': 'Musthe',
	}

	itemlist = [{
		'title': x,
		'value': y,
		'accessory_type': 'none'
	} for x, y in titles.items()]

	tv_view.data_source = tv_view.delegate = tvDelegateGen(
		title='Notation', items=itemlist)

	# -------------------------

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.table1_selection = None
		self.bg_color = 'lightyellow'
		self.make_view()

	def make_view(self):
		self.add_subview(tv_alter)
		self.add_subview(tv_type)
		self.add_subview(tv_view)
		self.add_subview(bt_generator)
		self.add_subview(txtv_info)

		# Button: generate
		bt_generator.action = self.fn_generate

	def fn_generate(self, sender):

		notes = get_notes(tv_alter.delegate.selected_item)

		all_chords = []
		new_chord = ''

		txtv_info.text_color = 'red'

		if tv_alter.delegate.selected_item == '':
			txtv_info.text = 'Select Note type \n\n 1. Flats - notes with flats and notes without accidentals. Notes will be randomized \n 2. Sharps - notes with sharps and notes without accidentals. Notes will be randomized \n 3. All - all notes (with and without accidentals) \n 4. Circle of 4th - notes will be displayed in strict order of circle of 4th \n 5. Circle of 5th - notes will be displayed in strict order of circle of 5th'

			txtv_info.font = ('verdana-bold', 15)
		elif tv_type.delegate.selected_items == []:
			txtv_info.text = 'Select chord type \n\n Multiple choice is possible. \n - maj (M): major chord \n- min (m): minor chord \n- aug (+): augmented chord \n- dim (°): diminished chord \n- dom7 (7): dominant 7th chord \n- min7 (m7): minor 7th \n- maj7 (M7): major 7th \n- aug7 (7aug5): augmented 7 \n- m7dim5 (m7b5): diminished 7'

			txtv_info.font = ('verdana-bold', 15)
		elif tv_view.delegate.selected_item == '':
			txtv_info.text = 'Select notation  \n\n 1. Random: randomize chord notations display. For example: chord C major can be displayed as Cmaj, CM, C. C minor can be displayed as Cm, Cmin, C-  \n\n 2. Default: 1 most used notation is used. For example, C for C major, Cm for C minor. \n\n 3. MusThe: notations that are used in Musthe module.'

			txtv_info.font = ('verdana-bold', 15)
		else:
			txtv_info.font = ('verdana-bold', 30)
			txtv_info.text_color = 'black'

			# loop through notes and chord types
			for note in notes:
				for item_type in tv_type.delegate.selected_items:

					if tv_alter.delegate.selected_item in (
							'all', 'Circle4th', 'Circle5th'
					) or note.accidental == tv_alter.delegate.selected_item or note.accidental == '':

						new_chord = str(Chord(note, chord_type=item_type['value']))

						# substitue musthe chord types with custom: random or default
						if tv_view.delegate.selected_item == 'Random':

							t = obj[item_type['value']]

							new_chord = t.replace(new_chord)

						elif tv_view.delegate.selected_item == 'Default':

							t = obj[item_type['value']]
							new_chord = t.replace_default(new_chord)
						all_chords.append(new_chord)

			if tv_alter.delegate.selected_item in ('Circle4th', 'Circle5th'):
				# Circles of 4th or 5th
				txtv_info.text = ', '.join(all_chords)
			else:
				# random chords output
				txtv_info.text = ', '.join(random.sample(all_chords, len(all_chords)))


# --------------------------------
# MAIN
# -------------------------------
v = ChordGenerator(name='CHORD GENERATOR')
v.present('popover')

